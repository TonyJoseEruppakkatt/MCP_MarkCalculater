
import asyncio
from fastmcp import Client

async def main():

    # Connect to our MCP server
    async with Client("server.py") as client:

        print("Connected to MCP Server")

        # Step 1: Discover available tools
        tools = await client.list_tools()

        print("\nAvailable Tools:")

        for tool in tools:
            print(tool.name)

        # Step 2: Call addition tool
        result1 = await client.call_tool(
            "add_numbers",
            {"a": 10, "b": 20}
        )

        print("\nAddition Result:")
        print(result1.content[0].text)

        # Step 3: Call average calculation tool
        result2 = await client.call_tool(
            "calculate_average",
            {
                "mark1": 80,
                "mark2": 70,
                "mark3": 90
            }
        )

        print("\nStudent Average:")
        print(result2.content[0].text)

        # Step 4: Check result
        result3 = await client.call_tool(
            "check_result",
            {"average": 80}
        )

        print("\nStudent Result:")
        print(result3.content[0].text)

        # Step 5: Read resource
        resource = await client.read_resource("student://about")

        print("\nApplication Information:")
        print(resource[0].text)

if __name__ == "__main__":
    asyncio.run(main())