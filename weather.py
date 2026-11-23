from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_wether(location:str)->str:
    """get the weather loaction."""
    return "It's always raining in California"

mcp = FastMCP(
    "Weather",
    host="127.0.0.1",
    port=8001
)

if __name__=="__main__":
    mcp.run(transport="streamable-http")
    