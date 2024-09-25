import aiohttp
import asyncio
import json

# Function to fetch data from a URL, handling retries, timeouts, and return types.
async def fetch(session, url, return_type, retries=5, timeout=15):
    for attempt in range(retries):
        try:
            # Try making an HTTP request
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=timeout)) as response:
                if return_type == 'text':
                    return await response.text()  # Return text response if requested
                elif return_type == 'json':
                    try:
                        body = await response.text()  # Read the response body as text
                        json_start = body.find('[')  # Look for the start of JSON data
                        if json_start != -1:
                            json_data = body[json_start:]  # Extract JSON data from the response
                            return json.loads(json_data)   # Parse and return JSON data
                        else:
                            print("No JSON data found in response")
                            raise ValueError("No JSON data found")
                    except json.JSONDecodeError as e:
                        print(f"Failed to parse JSON response: {e}")
                        raise
                else:
                    return None
        except (aiohttp.ClientError, asyncio.TimeoutError, ValueError) as e:
            if attempt + 1 == retries:  # If maximum retries are reached
                return None
            await asyncio.sleep(1)  # Wait for a second before retrying