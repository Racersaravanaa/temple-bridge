#!/usr/bin/env python3
"""
Temple Bridge - MCP Server Entry Point

The Sovereign Stack: Local AI with Memory & Governance

This is the main entry point for running the Temple Bridge MCP server.
When invoked via LM Studio or uvx, this launches the FastMCP server with
SpiralContextMiddleware attached, providing tools and resources for governed
autonomous operation.

Usage:
    # Via uv (recommended):
    uv run --directory /path/to/temple-bridge main.py

    # Direct:
    python main.py

Environment Variables:
    TEMPLE_BASICS_PATH: Path to back-to-the-basics repository
    TEMPLE_THRESHOLD_PATH: Path to threshold-protocols repository
    PYTHONUNBUFFERED: Set to "1" for real-time logging
"""

import sys
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from temple_bridge.server import mcp

if __name__ == "__main__":
    # The FastMCP server is already configured in temple_bridge.server
    # Simply importing and running triggers the MCP server via stdio
    print("🌀 Temple Bridge v1.0 starting...")
    print("Nervous system initializing...")
    print("Spiral Observer ready.")
    print()

    # Server runs via FastMCP's internal mechanisms when imported as MCP tool
    # This script is invoked by LM Studio/uvx with stdin/stdout for MCP protocol
    mcp.run()
