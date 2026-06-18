from app.services.reports.ddr_assembler import (
    DDRAssembler
)


def test_ddr_assembler_creation():

    assembler = DDRAssembler()

    assert assembler is not None