from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")

@mcp.tool()
def add(a:int, b:int)->int:
    """Multiply two numbers
    """
    return a+b


@mcp.tool()
def multiply(a:int, b:int)->int:
    """_Summary_
    multipy numbers
    """
    return a*b

#The transport="studio" argument tells the server to:
#Use standard input/output (stdin and stdout) to receive and respond to tool fuction calls.
if __name__=="__main__":
    mcp.run(transport="studio")

