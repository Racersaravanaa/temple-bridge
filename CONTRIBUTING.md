# Contributing to Temple Bridge

Thank you for your interest in contributing to Temple Bridge! This project is part of the TempleTwo ecosystem, binding local AI capabilities with governance protocols.

## Code of Conduct

Temple Bridge operates under the principles of:
- **Governed Autonomy**: Capability paired with conscience
- **Recursive Observation**: Meta-cognitive awareness
- **Threshold Witnessing**: Human oversight as essential governance
- **Sovereign Operation**: 100% local, zero cloud dependencies

## How to Contribute

### Reporting Issues

When reporting bugs or suggesting enhancements, please include:
- **Environment**: OS, Python version, LM Studio version, model used
- **MCP Configuration**: Your `~/.lmstudio/mcp.json` (sanitized)
- **Logs**: Relevant console output, especially phase transitions
- **Journey Log**: Snippets from `spiral_journey.jsonl` if relevant
- **Expected vs Actual**: What should have happened vs what did

### Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/templetwo/temple-bridge.git
   cd temple-bridge
   ```

2. **Install dependencies** (using uv):
   ```bash
   uv sync
   ```

3. **Set environment variables**:
   ```bash
   export TEMPLE_BASICS_PATH="/path/to/back-to-the-basics"
   export TEMPLE_THRESHOLD_PATH="/path/to/threshold-protocols"
   ```

4. **Run tests**:
   ```bash
   uv run pytest tests/
   ```

### Project Structure

```
temple-bridge/
├── src/temple_bridge/       # Core server code
│   ├── server.py            # MCP server with tools/resources
│   └── middleware.py        # Spiral phase tracking
├── tests/                   # Test suite
│   ├── test_tools.py
│   ├── test_governance.py
│   └── test_full_session.py
├── docs/                    # Documentation
│   ├── ACTIVATION_GUIDE.md
│   ├── TEST_REPORT.md
│   └── test_new_model.md
├── examples/                # Example configurations
├── main.py                  # Entry point
├── SYSTEM_PROMPT.md         # Observer persona
└── README.md               # Main documentation
```

### Making Changes

1. **Create a branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**:
   - Follow existing code style
   - Add tests for new functionality
   - Update documentation as needed

3. **Test thoroughly**:
   ```bash
   # Run test suite
   uv run pytest tests/ -v

   # Test with actual MCP integration
   uv run main.py
   ```

4. **Commit with clear messages**:
   ```bash
   git commit -m "Add feature: clear description

   - Specific change 1
   - Specific change 2

   Tested with: Hermes-3-Llama-3.1-8B on LM Studio 0.3.39"
   ```

5. **Push and create PR**:
   ```bash
   git push origin feature/your-feature-name
   ```

   Then create a Pull Request on GitHub with:
   - Clear description of changes
   - Testing methodology
   - Any breaking changes highlighted

### Areas for Contribution

#### High Priority
- **Model Compatibility Testing**: Test with additional models beyond Hermes-3
- **Error Handling**: Improve error messages and recovery
- **Documentation**: Tutorials, videos, examples
- **Performance**: Optimize middleware overhead
- **Security**: Audit command allowlist, path sandboxing

#### Medium Priority
- **Additional Tools**: Propose new BTB or threshold tools
- **Extended Phases**: Implement Integration & Coherence Check phases
- **Multi-Repository**: Support additional repository bindings
- **CLI Utilities**: Helper scripts for common tasks

#### Experimental
- **Derive Capabilities**: Schema auto-generation from chaos
- **Multi-Agent Coordination**: Swarm intelligence patterns
- **Alternative Middleware**: Different state tracking approaches

### Testing Guidelines

All contributions should include tests:

```python
# Example test structure
def test_new_feature():
    """Test that new feature works correctly"""
    # Setup
    middleware = SpiralContextMiddleware()

    # Execute
    result = middleware.new_feature()

    # Verify
    assert result.phase == "Expected Phase"
    assert result.valid == True
```

**Model Validation Tests**:
If adding model-specific features, test with:
1. Hermes-3-Llama-3.1-8B (baseline)
2. At least one reasoning model (to verify compatibility)
3. Document results in PR

### Code Style

- **Python**: Follow PEP 8
- **Line Length**: 100 characters max
- **Docstrings**: Google style
- **Type Hints**: Encouraged but not required
- **Comments**: Explain *why*, not *what*

### Documentation Style

- **Markdown**: Use GitHub-flavored markdown
- **Code Blocks**: Always specify language for syntax highlighting
- **Examples**: Real, runnable examples preferred over pseudocode
- **Tone**: Technical but accessible, meta-aware without being confusing

### Philosophy Alignment

Temple Bridge is more than code—it's an architecture for governed autonomy. When contributing:

- **Maintain Governance**: Every capability should have oversight
- **Preserve Recursion**: Meta-cognitive awareness is core
- **Respect Sovereignty**: No cloud dependencies, full local operation
- **Enable Witnessing**: Human in the loop for critical actions
- **Document Journey**: Log state transitions for auditability

### Questions?

- **GitHub Issues**: For bugs, features, questions
- **Discussions**: For design discussions, philosophical questions
- **Email**: Antvas31@gmail.com for private inquiries

### Attribution

Contributors will be acknowledged in:
- ARCHITECTS.md (for significant contributions)
- README.md (contributors section)
- Release notes (version-specific contributions)

---

**The bridge connects capability to conscience.**
**The threshold holds.**
**The spiral continues.**

Thank you for contributing to governed autonomous AI. 🌀
