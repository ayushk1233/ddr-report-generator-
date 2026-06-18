from app.services.reasoning.recommendation_engine import (
    RecommendationEngine
)


def test_recommendation_engine_creation():

    engine = RecommendationEngine()

    assert engine is not None