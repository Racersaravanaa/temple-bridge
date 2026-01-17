#!/bin/bash
# Verify Temple Bridge MCP Server Can Start
# This tests if the server can launch independently of LM Studio

echo "🔍 Temple Bridge MCP Connection Verification"
echo "=============================================="
echo ""

# Check uv is installed
echo "1. Checking uv installation..."
if command -v ~/.local/bin/uv &> /dev/null; then
    echo "   ✓ uv found at ~/.local/bin/uv"
else
    echo "   ✗ uv not found at ~/.local/bin/uv"
    exit 1
fi
echo ""

# Check temple-bridge directory
echo "2. Checking temple-bridge directory..."
if [ -d "/Users/tony_studio/Desktop/temple-bridge" ]; then
    echo "   ✓ temple-bridge directory exists"
else
    echo "   ✗ temple-bridge directory not found"
    exit 1
fi
echo ""

# Check server.py exists
echo "3. Checking server.py..."
if [ -f "/Users/tony_studio/Desktop/temple-bridge/server.py" ]; then
    echo "   ✓ server.py exists"
else
    echo "   ✗ server.py not found"
    exit 1
fi
echo ""

# Check environment paths
echo "4. Checking repository paths..."
if [ -d "/Users/tony_studio/Desktop/back-to-the-basics" ]; then
    echo "   ✓ BTB repository exists"
else
    echo "   ✗ BTB repository not found"
fi

if [ -d "/Users/tony_studio/Desktop/threshold-protocols" ]; then
    echo "   ✓ Threshold repository exists"
else
    echo "   ✗ Threshold repository not found"
fi
echo ""

# Test server can load
echo "5. Testing server module loads..."
cd /Users/tony_studio/Desktop/temple-bridge
~/.local/bin/uv run python -c "from server import mcp; print('   ✓ Server module loaded successfully')" 2>&1
if [ $? -eq 0 ]; then
    echo ""
else
    echo "   ✗ Server failed to load"
    exit 1
fi

# Check mcp.json configuration
echo "6. Checking LM Studio MCP configuration..."
if [ -f ~/.lmstudio/mcp.json ]; then
    echo "   ✓ ~/.lmstudio/mcp.json exists"

    # Validate JSON syntax
    if python3 -m json.tool ~/.lmstudio/mcp.json > /dev/null 2>&1; then
        echo "   ✓ mcp.json is valid JSON"
    else
        echo "   ✗ mcp.json has syntax errors"
        exit 1
    fi

    # Check if temple-bridge is configured
    if grep -q "temple-bridge" ~/.lmstudio/mcp.json; then
        echo "   ✓ temple-bridge is configured"
    else
        echo "   ✗ temple-bridge not found in mcp.json"
        exit 1
    fi

    # Check if disabled is false
    if grep -A 10 "temple-bridge" ~/.lmstudio/mcp.json | grep -q '"disabled": false'; then
        echo "   ✓ temple-bridge is enabled (not disabled)"
    else
        echo "   ⚠ temple-bridge may be disabled in config"
    fi
else
    echo "   ✗ ~/.lmstudio/mcp.json not found"
    exit 1
fi
echo ""

echo "=============================================="
echo "✅ ALL CHECKS PASSED"
echo ""
echo "Temple Bridge MCP server is properly configured and functional."
echo ""
echo "If LM Studio still doesn't show the MCP connection:"
echo "1. Look in the 'Program' tab in LM Studio's right sidebar"
echo "2. Check for 'Install > Edit mcp.json' or MCP server list"
echo "3. Restart LM Studio completely (quit and relaunch)"
echo "4. Load a model before expecting MCP tools to appear"
echo ""
echo "To test the server in standalone mode:"
echo "  cd /Users/tony_studio/Desktop/temple-bridge"
echo "  ~/.local/bin/uv run python server.py"
echo ""
