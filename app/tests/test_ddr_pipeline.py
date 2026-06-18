from app.services.pipeline.ddr_pipeline import (
    DDRPipeline
)


def test_pipeline_creation():

    pipeline = DDRPipeline()

    assert pipeline is not None