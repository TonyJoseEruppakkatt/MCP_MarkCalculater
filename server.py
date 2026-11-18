
from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("MCP Mark Calculator")

# Tool 1: Add two numbers
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""

    return a + b

# Tool 2: Calculate student average
@mcp.tool()
def calculate_average(mark1: float, mark2: float, mark3: float) -> float:
    """Calculate the average of three subject marks."""

    average = (mark1 + mark2 + mark3) / 3

    return round(average, 2)

# Tool 3: Check student result
@mcp.tool()
def check_result(average: float) -> str:
    """Check whether the student passed or failed. Passing mark is 40."""

    if average >= 40:
        return "Pass"

    return "Fail"

# Resource: Information about our application
@mcp.resource("student://about")
def student_info() -> str:
    """Get information about the Student Assistant application."""

    return "Student Assistant MCP provides addition, average calculation and result checking."

# Start the MCP server
if __name__ == "__main__":
    mcp.run()