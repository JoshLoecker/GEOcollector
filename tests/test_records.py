from dataclasses import dataclass
import pytest

from geocollector.records import Record

EXAMPLE_DATA = {
    "TITLE": "Sample Title",
    "ORGANISM": "Example Organism",
    "SOURCE": "Example Source",
    "PLATFORM_ID": "Platform123",
    "PLATFORM_NAME": "PlatformName",
    "SRX_LINK": "https://example.com/srx=SRX12345",
    "CELL_TYPE": "Cell Type",
    "GSE": "GSE123",
    "GSM": "GSM456",
    "SEARCH_ID": "Search123",
}

EXPECTED_ORGANISM = "example organism"
EXPECTED_SRX_ACCESSION = "SRX12345"


@pytest.fixture
def record_instance():
    return Record(**EXAMPLE_DATA)


def test_post_init_lowercase_organism(record_instance):
    assert record_instance.ORGANISM == EXPECTED_ORGANISM


def test_set_srx_accession(record_instance):
    assert record_instance.SRX_ACCESSION == EXPECTED_SRX_ACCESSION


def test_default_srx_accession():
    NEW_DATA = EXAMPLE_DATA.copy()
    NEW_DATA.pop("SRX_LINK")
    record = Record(**NEW_DATA, SRX_LINK="https://example.com/some_other_link")
    assert record.SRX_ACCESSION == ""
