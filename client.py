"""
Cardiac Heart Rate Recovery (HRR) Post-Exercise & Parasympathetic Reactivation Client.
Zero-mock pure Python standard library implementation.
Calculates 1-minute HRR (HRR1), 2-minute HRR (HRR2), chronotropic reserve utilization,
and autonomic vagal reactivation / cardiovascular mortality risk stratification (Cole NEJM standards).
"""

import math
from typing import Dict, Any, Optional


class HeartRateRecoveryClient:
    """
    Evaluates autonomic parasympathetic reactivation following graded exercise testing:
    - HRR1 (bpm): HR_peak - HR_1min
        * Active cooldown: normal > 12 bpm (abnormal <= 12 bpm)
        * Passive cooldown: normal > 18 bpm (abnormal <= 18 bpm)
    - HRR2 (bpm): HR_peak - HR_2min (normal > 22 bpm active, > 42 bpm passive)
    - Chronotropic Reserve: (HR_peak - HR_rest) / (HR_max_pred - HR_rest) * 100
    - Key prognostic biomarker for all-cause mortality, autonomic neuropathy, and physical conditioning.
    """

    def __init__(self):
        pass

    def evaluate_hrr(
        self,
        peak_heart_rate_bpm: float,
        heart_rate_1min_bpm: float,
        heart_rate_2min_bpm: Optional[float] = None,
        resting_heart_rate_bpm: Optional[float] = 70.0,
        cooldown_protocol: Optional[str] = "Active Cooldown",
        patient_age_years: Optional[int] = 45
    ) -> Dict[str, Any]:
        """
        Calculates post-exercise Heart Rate Recovery metrics.
        peak_heart_rate_bpm: maximal HR achieved at peak exertion (e.g. 172.0 bpm).
        heart_rate_1min_bpm: HR measured exactly 60 seconds into recovery (e.g. 148.0 bpm).
        heart_rate_2min_bpm: optional HR measured at 120 seconds into recovery (e.g. 126.0 bpm).
        cooldown_protocol: 'Active Cooldown' (standard walking) or 'Passive Cooldown' (supine/seated rest).
        """
        if peak_heart_rate_bpm <= 0 or heart_rate_1min_bpm <= 0:
            raise ValueError("Heart rates must be strictly positive.")
        if heart_rate_1min_bpm > peak_heart_rate_bpm:
            raise ValueError("1-minute recovery heart rate cannot exceed peak heart rate.")

        hrr_1min = round(peak_heart_rate_bpm - heart_rate_1min_bpm, 1)

        hrr_2min = None
        if heart_rate_2min_bpm is not None:
            if heart_rate_2min_bpm > peak_heart_rate_bpm:
                raise ValueError("2-minute recovery heart rate cannot exceed peak heart rate.")
            hrr_2min = round(peak_heart_rate_bpm - heart_rate_2min_bpm, 1)

        # Tanaka age-predicted max HR: 208 - 0.7 * age
        age = patient_age_years if patient_age_years is not None else 45
        tanaka_max_hr = round(208.0 - (0.7 * age), 1)

        chronotropic_index = None
        if resting_heart_rate_bpm and (tanaka_max_hr > resting_heart_rate_bpm):
            chronotropic_index = round(
                ((peak_heart_rate_bpm - resting_heart_rate_bpm) / (tanaka_max_hr - resting_heart_rate_bpm)) * 100.0, 1
            )

        # Clinical Classification based on Cole et al. (NEJM) standards:
        is_active = (cooldown_protocol.lower().startswith("active"))
        abnormal_threshold_1min = 12.0 if is_active else 18.0

        if hrr_1min <= abnormal_threshold_1min:
            autonomic_status = f"Attenuated / Delayed Heart Rate Recovery (<= {abnormal_threshold_1min} bpm)"
            clinical_risk = (
                f"Blunted post-exercise HR recovery ({hrr_1min} bpm <= {abnormal_threshold_1min} bpm cutoff); "
                "indicates severely impaired parasympathetic vagal reactivation and represents an established independent predictor of cardiovascular mortality."
            )
            vagal_reactivation_grade = "Impaired / Suppressed Vagal Reactivation"
        elif hrr_1min < (abnormal_threshold_1min + 6.0):
            autonomic_status = "Borderline / Low-Normal Heart Rate Recovery"
            clinical_risk = "Marginal vagal tone restoration; associated with deconditioning or subclinical autonomic dysregulation."
            vagal_reactivation_grade = "Borderline Vagal Tone Recovery"
        else:
            autonomic_status = "Robust / Preserved Heart Rate Recovery"
            clinical_risk = "Rapid post-exercise parasympathetic deceleration; reflects high cardiorespiratory fitness and favorable cardiovascular autonomic profile."
            vagal_reactivation_grade = "Vigorous Parasympathetic Reactivation"

        return {
            "status": "success",
            "recovery_kinetics": {
                "hrr_1min_bpm": hrr_1min,
                "hrr_2min_bpm": hrr_2min,
                "peak_heart_rate_bpm": round(peak_heart_rate_bpm, 1),
                "heart_rate_1min_bpm": round(heart_rate_1min_bpm, 1),
                "heart_rate_2min_bpm": round(heart_rate_2min_bpm, 1) if heart_rate_2min_bpm is not None else None,
                "cooldown_protocol": cooldown_protocol,
                "abnormal_cutoff_1min_bpm": abnormal_threshold_1min
            },
            "chronotropic_parameters": {
                "patient_age_years": age,
                "age_predicted_max_hr_bpm": tanaka_max_hr,
                "chronotropic_reserve_utilization_pct": chronotropic_index
            },
            "cardiovascular_assessment": {
                "autonomic_status": autonomic_status,
                "vagal_reactivation_grade": vagal_reactivation_grade,
                "pathophysiology_summary": clinical_risk
            }
        }
