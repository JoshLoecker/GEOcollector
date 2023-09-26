import pytest
import aiohttp
import pandas as pd
from unittest.mock import Mock
from geocollector.api import NCBI

ncbi_key = "test_key"


# Define a fixture for the NCBI class
@pytest.fixture
async def ncbi_instance():
    async with aiohttp.ClientSession() as eutils_session, aiohttp.ClientSession() as sra_session:
        input_df = pd.DataFrame({'GSE': [], 'GSM': [], 'SRR': []})
        logger = Mock()
        ncbi = NCBI(input_df, logger)
        ncbi.eutils_session = eutils_session
        ncbi.sra_session = sra_session
        yield ncbi


@pytest.fixture
async def ncbi_api_instance():
    async with aiohttp.ClientSession() as eutils_session, aiohttp.ClientSession() as sra_session:
        input_df = pd.DataFrame({'GSE': [], 'GSM': [], 'SRR': []})
        logger = Mock()
        ncbi = NCBI(input_df, logger, key=ncbi_key)
        ncbi.eutils_session = eutils_session
        ncbi.sra_session = sra_session
        yield ncbi


# Test the initialization of NCBI class
@pytest.mark.asyncio
async def test_ncbi_init(ncbi_instance):
    async for instance in ncbi_instance:
        assert instance._ncbi_key == ""
        assert instance.request_per_second == 3
        assert instance.delay == 0.37


# Test the initialization of NCBI class with an API key
@pytest.mark.asyncio
async def test_ncbi_init_with_key(ncbi_api_instance):
    async for instance in ncbi_api_instance:
        assert instance.ncbi_key == ncbi_key
        assert instance.request_per_second == 10
        assert instance.delay == 0.12


# Test adding columns to input dataframe
@pytest.mark.asyncio
async def test_add_columns_to_dataframe(ncbi_instance):
    async for instance in ncbi_instance:
        main_columns = ["GSE", "GSM", "SRR", "Rename", "Strand", "Prep Method"]
        internal_columns = ["search_id", "cell_type", "srx"]
        
        assert all(col in instance.input_df.columns for col in main_columns)
        assert all(col in instance.input_df.columns for col in internal_columns)
