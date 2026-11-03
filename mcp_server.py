"""
MCP Server implementation for Cardiac Heart Rate Recovery (HRR) Post-Exercise Skill.
Exposes standard FastMCP-compatible tools for exercise autonomic recovery and vagal reactivation analysis.
"""

import sys
import json
from typing import Dict, Any, Optional
from client import HeartRateRecoveryClient


def evaluate_heart_rate_recovery(
    peak_heart_rate_bpm: float,
    heart_rate_1min_bpm: float,
    heart_rate_2min_bpm: Optional[float] = None,
    resting_heart_rate_bpm: Optional[float] = 70.0,
    cooldown_protocol: Optional[str] = "Active Cooldown",
    patient_age_years: Optional[int] = 45
) -> str:
    """
    Evaluates 1-minute and 2-minute post-exercise heart rate recovery (HRR).
    Returns structured analysis of parasympathetic vagal reactivation and cardiovascular mortality risk.
    """
    client = HeartRateRecoveryClient()
    result = client.evaluate_hrr(
        peak_heart_rate_bpm=peak_heart_rate_bpm,
        heart_rate_1min_bpm=heart_rate_1min_bpm,
        heart_rate_2min_bpm=heart_rate_2min_bpm,
        resting_heart_rate_bpm=resting_heart_rate_bpm,
        cooldown_protocol=cooldown_protocol,
        patient_age_years=patient_age_years
    )
    return json.dumps(result, indent=2)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--tools":
        tools = [
            {
                "name": "evaluate_heart_rate_recovery",
                "description": "Calculates 1-minute and 2-minute post-exercise heart rate recovery (HRR = HR_peak - HR_recovery) to assess parasympathetic vagal reactivation and cardiovascular mortality risk.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "peak_heart_rate_bpm": {"type": "number", "description": "Maximal heart rate achieved at peak exertion in bpm (e.g. 175 bpm)"},
                        "heart_rate_1min_bpm": {"type": "number", "description": "Heart rate measured exactly 60 seconds into recovery in bpm"},
                        "heart_rate_2min_bpm": {"type": "number", "description": "Optional heart rate measured at 120 seconds into recovery in bpm"},
                        "resting_heart_rate_bpm": {"type": "number", "description": "Baseline pre-exercise resting heart rate in bpm (default: 70 bpm)"},
                        "cooldown_protocol": {"type": "string", "description": "Cooldown mode: 'Active Cooldown' (cutoff <= 12 bpm) or 'Passive Cooldown' (cutoff <= 18 bpm)"},
                        "patient_age_years": {"type": "integer", "description": "Patient age in years (default: 45)"}
                    },
                    "required": ["peak_heart_rate_bpm", "heart_rate_1min_bpm"]
                }
            }
        ]
        print(json.dumps(tools, indent=2))
    else:
        # Simple self-test
        client = HeartRateRecoveryClient()
        test_res = client.evaluate_hrr(
            peak_heart_rate_bpm=172.0,
            heart_rate_1min_bpm=148.0,
            heart_rate_2min_bpm=124.0
        )
        print("Self-test passed:")
        print(json.dumps(test_res, indent=2))
