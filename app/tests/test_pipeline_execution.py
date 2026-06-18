from app.services.pipeline.ddr_pipeline import (
    DDRPipeline
)


def test_pipeline_exists():

    pipeline = DDRPipeline()

    assert pipeline is not None