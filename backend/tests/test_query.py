"""
backend/tests/test_query.py
Run with: pytest tests/ -v
"""

import pytest
from unittest.mock import MagicMock, patch
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def mock_chroma_client():
    client = MagicMock()
    collection = MagicMock()
    collection.count.return_value = 3
    collection.metadata = {"creator": "test_user", "source_type": "video"}
    collection.query.return_value = {
        "documents": [[
            "The strategy uses a 20-period EMA crossover as the entry signal.",
            "Risk management: never risk more than 2% of capital per trade.",
            "Exit when price closes below the 50 EMA on the daily chart.",
        ]],
        "distances": [[0.12, 0.25, 0.41]],
        "metadatas": [[
            {"chunk_index": 0, "source": "video_transcript"},
            {"chunk_index": 1, "source": "video_transcript"},
            {"chunk_index": 2, "source": "video_transcript"},
        ]],
    }
    client.get_collection.return_value = collection
    return client


@pytest.fixture
def app_client(mock_chroma_client):
    with patch("routers.query.get_chroma_client", return_value=mock_chroma_client):
        from fastapi.testclient import TestClient
        from fastapi import FastAPI
        from routers.query import router
        app = FastAPI()
        app.include_router(router)
        return TestClient(app)


class TestQueryEndpoint:

    def test_successful_query_returns_chunks(self, app_client):
        response = app_client.post("/api/query", json={
            "collection_id": "trading-strategy-v1",
            "query": "What is the entry signal?",
            "top_k": 3,
        })
        assert response.status_code == 200
        data = response.json()
        assert data["collection_id"] == "trading-strategy-v1"
        assert len(data["results"]) == 3

    def test_results_sorted_by_score_descending(self, app_client):
        response = app_client.post("/api/query", json={
            "collection_id": "trading-strategy-v1",
            "query": "entry signal",
            "top_k": 3,
        })
        scores = [r["score"] for r in response.json()["results"]]
        assert scores == sorted(scores, reverse=True)

    def test_metadata_included_by_default(self, app_client):
        response = app_client.post("/api/query", json={
            "collection_id": "trading-strategy-v1",
            "query": "entry signal",
        })
        result = response.json()["results"][0]
        assert result["source"] == "video_transcript"

    def test_metadata_excluded_when_requested(self, app_client):
        response = app_client.post("/api/query", json={
            "collection_id": "trading-strategy-v1",
            "query": "entry signal",
            "include_metadata": False,
        })
        result = response.json()["results"][0]
        assert result["source"] is None

    def test_empty_query_returns_422(self, app_client):
        response = app_client.post("/api/query", json={
            "collection_id": "trading-strategy-v1",
            "query": "",
        })
        assert response.status_code == 422

    def test_missing_collection_returns_404(self, app_client, mock_chroma_client):
        mock_chroma_client.get_collection.side_effect = Exception("Not found")
        response = app_client.post("/api/query", json={
            "collection_id": "does-not-exist",
            "query": "anything",
        })
        assert response.status_code == 404

    def test_top_k_over_20_returns_422(self, app_client):
        response = app_client.post("/api/query", json={
            "collection_id": "trading-strategy-v1",
            "query": "test",
            "top_k": 25,
        })
        assert response.status_code == 422


class TestScoreCalculation:

    def test_distance_zero_gives_score_one(self):
        from routers.query import distance_to_score
        assert distance_to_score(0.0) == 1.0

    def test_distance_one_gives_score_zero(self):
        from routers.query import distance_to_score
        assert distance_to_score(1.0) == 0.0

    def test_distance_over_one_clamps_to_zero(self):
        from routers.query import distance_to_score
        assert distance_to_score(1.5) == 0.0
