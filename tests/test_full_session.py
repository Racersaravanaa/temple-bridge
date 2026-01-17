#!/usr/bin/env python3
"""
Simulate a Full Spiral Observer Session
This mimics what would happen when Llama-4-Scout uses the tools via LM Studio.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from middleware import SpiralContextMiddleware

print("=== SIMULATED SPIRAL OBSERVER SESSION ===\n")

# Create a middleware instance (this is what the MCP server does)
middleware = SpiralContextMiddleware(log_path=Path("test_session_journey.jsonl"))

print(f"Starting Phase: {middleware.current_phase}\n")

# Simulate a sequence of tool calls that an agent would make
print("SCENARIO: Agent asked to 'Run the BTB test suite'\n")

# Phase 1: Read BTB directory (First-Order Observation)
print("STEP 1: Agent calls btb_list_directory('.')")
middleware._update_phase_based_on_tool("btb_list_directory")
print(f"  → Phase: {middleware.current_phase}")
print(f"  → Tool calls: {middleware.tool_call_count}")
print()

# Phase 2: Read a file (Still First-Order Observation)
print("STEP 2: Agent calls btb_read_file('README.md')")
middleware._update_phase_based_on_tool("btb_read_file")
print(f"  → Phase: {middleware.current_phase}")
print(f"  → Tool calls: {middleware.tool_call_count}")
print()

# Phase 3: Consult threshold (Recursive Integration)
print("STEP 3: Agent calls threshold_consult('testing')")
middleware._update_phase_based_on_tool("threshold_consult")
print(f"  → Phase: {middleware.current_phase}")
print(f"  → Tool calls: {middleware.tool_call_count}")
print()

# Phase 4: Reflect on the observation (Counter-Perspectives)
print("STEP 4: Agent calls spiral_reflect('I found tests/ directory')")
middleware._update_phase_based_on_tool("spiral_reflect")
print(f"  → Phase: {middleware.current_phase}")
print(f"  → Reflection depth: {middleware.reflection_depth}")
print()

# Phase 5: Execute the command (Execution)
print("STEP 5: Agent calls btb_execute_command('pytest tests/')")
middleware._update_phase_based_on_tool("btb_execute_command")
print(f"  → Phase: {middleware.current_phase}")
print(f"  → Tool calls: {middleware.tool_call_count}")
print()

# Post-execution update
middleware._post_execution_phase_update("btb_execute_command", "All tests passed")
print("STEP 6: Post-execution reflection")
print(f"  → Phase: {middleware.current_phase}")
print()

# Get journey summary
print("=" * 60)
print(middleware.get_journey_summary())

# Check the log file
print("\n=== SESSION LOG ===")
log_file = Path("test_session_journey.jsonl")
if log_file.exists():
    with open(log_file) as f:
        lines = f.readlines()
    print(f"✓ Logged {len(lines)} phase transitions")
    print("\nPhase History:")
    import json
    for line in lines[:5]:
        entry = json.loads(line)
        print(f"  {entry['from_phase']} → {entry['to_phase']}")
else:
    print("✗ No log file created")

print("\n=== TEST COMPLETE ===")
print("This is what the middleware does during a real LM Studio session.")
print("Every tool call advances the Spiral phase automatically.")
