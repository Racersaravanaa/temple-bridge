# Auto-Loading System Prompt (Advanced Option)

## The Challenge

LM Studio requires manually pasting the system prompt each time, or saving it as a preset. This document explores ways to automate this.

## Current Best Practice: LM Studio Presets

**Recommended:** Create a saved preset in LM Studio (see `quick_start.md`)

This is the most reliable method and works today.

---

## Future Enhancement: MCP-Injected System Prompt

### Concept

The MCP server could provide the system prompt as an initial context message or resource that LM Studio automatically loads when connecting.

### Implementation Ideas

#### Option A: System Prompt as MCP Resource

Add to `server.py`:

```python
@mcp.resource("temple://config/system_prompt")
def get_system_prompt() -> str:
    """Return the complete Spiral Observer system prompt"""
    prompt_path = Path(__file__).parent.parent.parent / "SYSTEM_PROMPT.md"
    return prompt_path.read_text()
```

**Issue:** LM Studio would need to explicitly request this resource and inject it. Not automatic.

#### Option B: Prompt in Server Description

```python
mcp = FastMCP(
    "TempleObserver",
    instructions=Path("SYSTEM_PROMPT.md").read_text()
)
```

**Issue:** MCP spec's `instructions` field is meant for tool usage, not full persona prompts. Some clients ignore it.

#### Option C: Pre-Chat Message Hook

If LM Studio supported a "pre-chat hook" that MCP servers could populate, we could inject the prompt there.

**Issue:** Not part of current MCP spec.

---

## Workarounds That Work Today

### 1. LM Studio Preset (Recommended)

- One-time setup
- Reliable
- Built-in feature
- See `quick_start.md`

### 2. Shell Alias (For Terminal Users)

Add to `~/.zshrc` or `~/.bashrc`:

```bash
alias spiral="cat ~/Desktop/temple-bridge/SYSTEM_PROMPT.md | pbcopy && echo 'System prompt copied to clipboard. Paste into LM Studio.'"
```

Then just run: `spiral`

### 3. AppleScript Launcher (macOS)

```applescript
-- Save as SpiralObserver.app
tell application "LM Studio"
    activate
    -- This would require LM Studio to support AppleScript
    -- Currently it doesn't, but could in future
end tell
```

---

## Feature Request to LM Studio

We could request LM Studio add:

1. **MCP-aware system prompts**: Auto-load prompt from MCP server metadata
2. **Startup scripts**: Run script when MCP server connects
3. **Persistent presets**: Auto-select preset based on MCP server name

This would make Temple Bridge truly one-click.

---

## Current Recommendation

**Use LM Studio Presets** (Option 1 above)

1. Create preset once with full SYSTEM_PROMPT.md
2. Name it "Spiral Observer"
3. Every future session: Just select that preset

This is the most reliable solution with current LM Studio capabilities.

---

## Contributing

If you discover a better way to auto-inject system prompts via MCP, please:

1. Document it here
2. Submit a PR to temple-bridge
3. Share with the MCP community

---

**For now: Presets are your friend.** 🌀
