import pytest
import aiohttp
from unittest.mock import AsyncMock
from fetcher import fetcher  # Import your fetcher class

@pytest.mark.asyncio
async def test_fetch_text():
    async with aiohttp.ClientSession() as session:
        mock_response = AsyncMock()
        mock_response.text.return_value = "mocked text response"
        session.get = AsyncMock(return_value=mock_response)

        response = await fetcher.fetch(session, "http://example.com", "text")
        assert response == "mocked text response"