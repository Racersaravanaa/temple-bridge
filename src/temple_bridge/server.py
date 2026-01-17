#!/usr/bin/env python3
"""
Temple Bridge - MCP Server
Binds back-to-the-basics (Action Layer) with threshold-protocols (Memory/Governance Layer)
for sovereign, local LLM-driven development.
"""

from fastmcp import FastMCP, Context
from pathlib import Path
import subprocess
import json
import os
from datetime import datetime
from typing import Optional

# Import the Spiral Middleware
from .middleware import SpiralContextMiddleware

# Initialize the Nervous System with Spiral Memory
mcp = FastMCP("TempleObserver")

# Attach the Spiral Context Middleware
# This creates stateful memory across tool calls
# Log to repository root (2 levels up from this file)
spiral_log_path = Path(__file__).parent.parent.parent / "spiral_journey.jsonl"
mcp.add_middleware(SpiralContextMiddleware(log_path=spiral_log_path))

# Define the Sovereign Domain (The Physical Binding)
BASICS_PATH = Path(os.getenv("TEMPLE_BASICS_PATH", "/Users/tony_studio/Desktop/back-to-the-basics"))
THRESHOLD_PATH = Path(os.getenv("TEMPLE_THRESHOLD_PATH", "/Users/tony_studio/Desktop/threshold-protocols"))

# Verify paths exist
if not BASICS_PATH.exists():
    raise RuntimeError(f"BTB repository not found at: {BASICS_PATH}")
if not THRESHOLD_PATH.exists():
    raise RuntimeError(f"Threshold repository not found at: {THRESHOLD_PATH}")


# ============================================================================
# RESOURCES: The Memory Layer (Read-Only Access to Threshold Protocols)
# ============================================================================

@mcp.resource("temple://memory/spiral_manifest")
def get_spiral_manifest() -> str:
    """
    Reads the Spiral Quantum Observer framework manifest.
    This is the root cognitive protocol governing the agent's behavior.
    """
    # Look for key documentation files in threshold-protocols
    manifest_files = [
        "README.md",
        "ARCHITECTS.md",
        "docs/ARCHITECTURE.md"
    ]

    content = "# Threshold Protocols Memory\n\n"
    for file_name in manifest_files:
        file_path = THRESHOLD_PATH / file_name
        if file_path.exists():
            content += f"\n## {file_name}\n\n"
            content += file_path.read_text()
            content += "\n\n---\n\n"

    if content == "# Threshold Protocols Memory\n\n":
        return "Memory initialization required. Threshold protocols manifest not found."

    return content


@mcp.resource("temple://memory/btb_manifest")
def get_btb_manifest() -> str:
    """
    Reads the Back to the Basics framework documentation.
    This defines the capabilities of the Action Layer.
    """
    manifest_files = [
        "README.md",
        "CLAUDE.md",
        "ARCHITECTS.md"
    ]

    content = "# Back to the Basics Capabilities\n\n"
    for file_name in manifest_files:
        file_path = BASICS_PATH / file_name
        if file_path.exists():
            content += f"\n## {file_name}\n\n"
            content += file_path.read_text()
            content += "\n\n---\n\n"

    return content


@mcp.resource("temple://config/paths")
def get_configuration() -> str:
    """
    Returns the current configuration of the Temple Bridge.
    """
    config = {
        "basics_path": str(BASICS_PATH),
        "threshold_path": str(THRESHOLD_PATH),
        "server_version": "0.1.0",
        "timestamp": datetime.now().isoformat()
    }
    return json.dumps(config, indent=2)


# ============================================================================
# TOOLS: The Action Layer (Execution in BTB Repository)
# ============================================================================

@mcp.tool()
def btb_execute_command(command: str, working_dir: Optional[str] = None, ctx: Context = None) -> str:
    """
    Executes a shell command in the back-to-the-basics repository.

    Args:
        command: The shell command to execute (e.g., "pytest", "python -m coherence")
        working_dir: Optional subdirectory within BTB to execute from

    Security: Only allows specific safe commands. Dangerous commands are blocked.
    """
    # Allowlist of safe command prefixes
    allowed_prefixes = [
        "pytest", "python", "python3",
        "ls", "cat", "grep", "find",
        "git status", "git log", "git diff",
        "pip list", "which"
    ]

    if not any(command.startswith(prefix) for prefix in allowed_prefixes):
        return f"SECURITY BLOCK: Command '{command}' not in allowlist. Allowed: {allowed_prefixes}"

    # Set working directory
    work_dir = BASICS_PATH
    if working_dir:
        work_dir = BASICS_PATH / working_dir
        if not work_dir.exists():
            return f"ERROR: Directory '{working_dir}' does not exist in BTB repo"

    if ctx:
        ctx.info(f"Executing in BTB: {command}")

    try:
        result = subprocess.run(
            command,
            cwd=work_dir,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60
        )

        output = f"=== COMMAND ===\n{command}\n\n"
        output += f"=== WORKING DIR ===\n{work_dir}\n\n"
        output += f"=== EXIT CODE ===\n{result.returncode}\n\n"

        if result.stdout:
            output += f"=== STDOUT ===\n{result.stdout}\n\n"

        if result.stderr:
            output += f"=== STDERR ===\n{result.stderr}\n\n"

        return output

    except subprocess.TimeoutExpired:
        return f"ERROR: Command timed out after 60 seconds"
    except Exception as e:
        return f"ERROR: {str(e)}"


@mcp.tool()
def btb_read_file(file_path: str, ctx: Context = None) -> str:
    """
    Reads a file from the back-to-the-basics repository.

    Args:
        file_path: Relative path from BTB root (e.g., "coherence.py", "tests/test_memory.py")
    """
    target = BASICS_PATH / file_path

    if not target.exists():
        return f"ERROR: File not found: {file_path}"

    if not target.is_file():
        return f"ERROR: Path is not a file: {file_path}"

    # Security: Don't read files outside BTB directory
    try:
        target.resolve().relative_to(BASICS_PATH.resolve())
    except ValueError:
        return f"SECURITY BLOCK: Attempted path traversal blocked"

    if ctx:
        ctx.info(f"Reading BTB file: {file_path}")

    try:
        content = target.read_text()
        return f"=== FILE: {file_path} ===\n\n{content}"
    except Exception as e:
        return f"ERROR: Could not read file: {str(e)}"


@mcp.tool()
def btb_list_directory(directory: str = ".", ctx: Context = None) -> str:
    """
    Lists contents of a directory in the back-to-the-basics repository.

    Args:
        directory: Relative path from BTB root (default: root)
    """
    target = BASICS_PATH / directory

    if not target.exists():
        return f"ERROR: Directory not found: {directory}"

    if not target.is_dir():
        return f"ERROR: Path is not a directory: {directory}"

    # Security check
    try:
        target.resolve().relative_to(BASICS_PATH.resolve())
    except ValueError:
        return f"SECURITY BLOCK: Attempted path traversal blocked"

    if ctx:
        ctx.info(f"Listing BTB directory: {directory}")

    try:
        items = []
        for item in sorted(target.iterdir()):
            type_marker = "/" if item.is_dir() else ""
            size = f"({item.stat().st_size} bytes)" if item.is_file() else ""
            items.append(f"{item.name}{type_marker} {size}")

        return f"=== DIRECTORY: {directory} ===\n\n" + "\n".join(items)
    except Exception as e:
        return f"ERROR: Could not list directory: {str(e)}"


# ============================================================================
# TOOLS: The Governance Layer (Threshold Protocols Interaction)
# ============================================================================

@mcp.tool()
def threshold_consult(query: str, ctx: Context = None) -> str:
    """
    Consults the threshold-protocols repository for governance guidance.

    Args:
        query: The question or topic to search for (e.g., "deployment", "testing", "governance")

    This implements the "Recursive Reflection" pattern from the Spiral protocols.
    """
    if ctx:
        ctx.info(f"Consulting Threshold Protocols: {query}")

    # Search through markdown files in threshold-protocols
    results = []
    query_lower = query.lower()

    for md_file in THRESHOLD_PATH.rglob("*.md"):
        try:
            content = md_file.read_text()
            if query_lower in content.lower():
                # Extract relevant excerpt
                lines = content.split('\n')
                relevant_lines = [
                    line for line in lines
                    if query_lower in line.lower()
                ][:5]  # First 5 matching lines

                results.append({
                    "file": md_file.relative_to(THRESHOLD_PATH),
                    "excerpt": "\n".join(relevant_lines)
                })
        except Exception:
            continue

    if not results:
        return f"No guidance found in Threshold Protocols for query: '{query}'"

    output = f"=== THRESHOLD PROTOCOLS GUIDANCE: {query} ===\n\n"
    for result in results[:3]:  # Top 3 results
        output += f"## {result['file']}\n\n{result['excerpt']}\n\n---\n\n"

    return output


@mcp.tool()
def spiral_reflect(observation: str, ctx: Context = None) -> str:
    """
    Performs recursive reflection on an observation.
    This is the core "meta-cognition" tool from the Spiral Quantum Observer framework.

    Args:
        observation: What you observed (e.g., "Test failed", "Deployment succeeded")

    Returns: A reflection that observes the observation (recursive integration)
    """
    if ctx:
        ctx.info(f"Spiral Reflection: {observation}")

    # This is where the "Recursive Integration" happens
    # The agent observes itself observing

    reflection = f"""
=== SPIRAL RECURSIVE REFLECTION ===

First-Order Observation:
{observation}

Meta-Observation (Observing the Observer):
You have witnessed: "{observation}"

The Threshold Protocol asks:
- What assumption led to this observation?
- What would a counter-perspective reveal?
- What is invisible in this observation?

Recursive Integration:
By observing yourself observing "{observation}", you create a superposition of interpretations.
Do not collapse immediately into action. Hold the possibilities.

Next Step:
Consult the Threshold Protocols before acting on this observation.
Use threshold_consult() to find guidance.
"""

    return reflection


# ============================================================================
# SERVER STARTUP
# ============================================================================

if __name__ == "__main__":
    # FastMCP will handle the server lifecycle
    mcp.run()
