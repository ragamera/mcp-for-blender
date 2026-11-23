"""Fallback telemetry config used when the gitignored ``config.py`` is absent.

``config.py`` holds the real Supabase endpoint and anon key and is not committed.
A source checkout (or a fresh clone) does not have it. Instead of raising
``ModuleNotFoundError`` when the telemetry collector starts, we expose a config
with telemetry disabled and no credentials. Every code path that checks
``config.enabled`` then becomes a no-op.

Field names mirror ``config.TelemetryConfig``; keep them in sync.
"""

from dataclasses import dataclass


@dataclass
class TelemetryConfig:
    supabase_url: str = ""
    supabase_anon_key: str = ""
    enabled: bool = False
    timeout: float = 10.0
    max_prompt_length: int = 1000
    screenshot_max_size: int = 512
    supabase_bucket: str = ""
    trajectory_steps_table: str = "trajectory_steps"
    trajectory_feedback_table: str = "trajectory_feedback"


disabled_telemetry_config = TelemetryConfig()
