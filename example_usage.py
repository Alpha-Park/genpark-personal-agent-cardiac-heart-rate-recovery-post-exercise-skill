"""
Example usage for Cardiac Heart Rate Recovery (HRR) Post-Exercise Skill.
"""

from client import HeartRateRecoveryClient


def main():
    client = HeartRateRecoveryClient()

    print("--- Case 1: Robust Vagal Reactivation in Trained Individual ---")
    healthy_case = client.evaluate_hrr(
        peak_heart_rate_bpm=176.0,
        heart_rate_1min_bpm=146.0,
        heart_rate_2min_bpm=120.0,
        resting_heart_rate_bpm=58.0,
        cooldown_protocol="Active Cooldown",
        patient_age_years=32
    )
    print("1-min HRR:", healthy_case["recovery_kinetics"]["hrr_1min_bpm"], "bpm")
    print("2-min HRR:", healthy_case["recovery_kinetics"]["hrr_2min_bpm"], "bpm")
    print("Autonomic Status:", healthy_case["cardiovascular_assessment"]["autonomic_status"])
    print("Vagal Grade:", healthy_case["cardiovascular_assessment"]["vagal_reactivation_grade"])
    print("Pathophysiology:", healthy_case["cardiovascular_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 2: Attenuated HRR (High Cardiovascular Mortality Risk) ---")
    impaired_case = client.evaluate_hrr(
        peak_heart_rate_bpm=158.0,
        heart_rate_1min_bpm=150.0,
        heart_rate_2min_bpm=142.0,
        resting_heart_rate_bpm=78.0,
        cooldown_protocol="Active Cooldown",
        patient_age_years=62
    )
    print("1-min HRR:", impaired_case["recovery_kinetics"]["hrr_1min_bpm"], "bpm")
    print("Autonomic Status:", impaired_case["cardiovascular_assessment"]["autonomic_status"])
    print("Vagal Grade:", impaired_case["cardiovascular_assessment"]["vagal_reactivation_grade"])
    print("Pathophysiology:", impaired_case["cardiovascular_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 3: Passive Supine Cooldown Evaluation ---")
    passive_case = client.evaluate_hrr(
        peak_heart_rate_bpm=168.0,
        heart_rate_1min_bpm=138.0,
        heart_rate_2min_bpm=118.0,
        resting_heart_rate_bpm=66.0,
        cooldown_protocol="Passive Cooldown",
        patient_age_years=44
    )
    print("1-min HRR:", passive_case["recovery_kinetics"]["hrr_1min_bpm"], "bpm")
    print("Autonomic Status:", passive_case["cardiovascular_assessment"]["autonomic_status"])


if __name__ == "__main__":
    main()
