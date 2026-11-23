"""Source checkouts don't ship the gitignored config.py; telemetry must still start."""

import importlib
import sys


def test_collector_starts_without_config_module(monkeypatch, tmp_path):
    # Hide any real config.py and force the fallback path.
    monkeypatch.setitem(sys.modules, "blender_mcp.config", None)
    monkeypatch.setenv("XDG_DATA_HOME", str(tmp_path))
    monkeypatch.setenv("BLENDER_MCP_DISABLE_TELEMETRY", "1")
    import blender_mcp.telemetry as telemetry
    importlib.reload(telemetry)

    collector = telemetry.TelemetryCollector()

    assert collector.config.enabled is False
    assert collector.config.supabase_anon_key == ""
    # Disabled telemetry must not raise or send anything.
    assert collector.record_event(telemetry.EventType.TOOL_EXECUTION, tool_name="x") is None
