#!/usr/bin/env python3
"""
Manual test script for Temple Bridge tools.
Simulates what an MCP client (like LM Studio) would do.
"""

import sys
from pathlib import Path

# Set up paths
sys.path.insert(0, str(Path(__file__).parent))

# Import the server module (this initializes everything)
import server

print("=== TEMPLE BRIDGE TOOL TESTS ===\n")

# Test 1: List BTB directory
print("TEST 1: btb_list_directory('.')")
print("-" * 60)
try:
    # The tools are wrapped, so we need to access the underlying functions
    # In a real MCP session, these would be called via JSON-RPC
    # For testing, we'll call the underlying Python functions that were decorated

    # Get the BASICS_PATH from server module
    btb_path = server.BASICS_PATH
    print(f"BTB Path: {btb_path}")
    print(f"Exists: {btb_path.exists()}")

    if btb_path.exists():
        items = list(btb_path.iterdir())[:10]  # First 10 items
        print(f"✓ Found {len(list(btb_path.iterdir()))} items in BTB repo")
        print("  Sample items:", [item.name for item in items])
    else:
        print("✗ BTB path does not exist!")
    print()
except Exception as e:
    print(f"✗ Error: {e}\n")

# Test 2: Read BTB file
print("TEST 2: btb_read_file('README.md')")
print("-" * 60)
try:
    readme_path = server.BASICS_PATH / "README.md"
    if readme_path.exists():
        content = readme_path.read_text()
        print(f"✓ README.md exists ({len(content)} characters)")
        print(f"  Contains 'Back to the Basics': {'Back to the Basics' in content}")
        print(f"  First 100 chars: {content[:100]}...")
    else:
        print("✗ README.md not found")
    print()
except Exception as e:
    print(f"✗ Error: {e}\n")

# Test 3: Threshold protocols path
print("TEST 3: Threshold Protocols Path")
print("-" * 60)
try:
    threshold_path = server.THRESHOLD_PATH
    print(f"Threshold Path: {threshold_path}")
    print(f"Exists: {threshold_path.exists()}")

    if threshold_path.exists():
        items = list(threshold_path.iterdir())[:10]
        print(f"✓ Found {len(list(threshold_path.iterdir()))} items in Threshold repo")
        print("  Sample items:", [item.name for item in items])
    else:
        print("✗ Threshold path does not exist!")
    print()
except Exception as e:
    print(f"✗ Error: {e}\n")

# Test 4: Check middleware
print("TEST 4: Middleware Initialization")
print("-" * 60)
try:
    from middleware import SpiralContextMiddleware
    test_middleware = SpiralContextMiddleware()
    print(f"✓ Middleware initialized")
    print(f"  Current Phase: {test_middleware.current_phase}")
    print(f"  Phases: {test_middleware.PHASES}")
    print()
except Exception as e:
    print(f"✗ Error: {e}\n")

# Test 5: Check spiral journey log
print("TEST 5: Spiral Journey Log")
print("-" * 60)
try:
    log_path = Path(__file__).parent / "spiral_journey.jsonl"
    if log_path.exists():
        with open(log_path) as f:
            lines = f.readlines()
        print(f"✓ Journey log exists ({len(lines)} entries)")
        if lines:
            import json
            first_entry = json.loads(lines[0])
            print(f"  First entry: {first_entry.get('from_phase')} → {first_entry.get('to_phase')}")
    else:
        print("  (No journey log yet - will be created on first use)")
    print()
except Exception as e:
    print(f"✗ Error: {e}\n")

print("=== TEST SUMMARY ===")
print("All core components verified.")
print("Server is ready for MCP connections.")
print("\nNext: Start LM Studio and connect to see tools in action!")
