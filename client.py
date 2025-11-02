from mcp import ClientSession
from mcp.client.sse import sse_client
import asyncio


async def test_search():
    async with sse_client("http://localhost:9100/sse") as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            result = await session.call_tool(
                "search_keyword",
                arguments={
                    "file_path": "test.py",
                    "keyword": "def",
                    "case_sensitive": False
                }
            )
            print(f"Result: {result.content[0].text}")


if __name__ == "__main__":
    asyncio.run(test_search())