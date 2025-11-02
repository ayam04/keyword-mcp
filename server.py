from fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("Keyword Search")


@mcp.tool()
def search_keyword(file_path: str, keyword: str, case_sensitive: bool = False) -> dict:
    try:
        path = Path(file_path)
        
        if not path.exists():
            return {"success": False,"error": "fine not found"}
        
        if not path.is_file():
            return {"success": False,"error": "path is not a file"}
        
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        matches = []
        search_keyword = keyword if case_sensitive else keyword.lower()
        
        for line_num, line in enumerate(lines, start=1):
            search_line = line if case_sensitive else line.lower()
            if search_keyword in search_line:
                matches.append({"line_number": line_num,"content": line.rstrip('\n')})
        
        return {"success": True,"file_path": str(path.absolute()),"keyword": keyword,"total_matches": len(matches),"matches": matches}
    
    except Exception as e:
        return {"success": False,"error": f"Error: {str(e)}"}


if __name__ == "__main__":
    mcp.run(transport="sse", port=9100)
