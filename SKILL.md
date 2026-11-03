---
name: genpark-personal-agent-cardiac-heart-rate-recovery-post-exercise-skill
description: Evaluates post-exercise parasympathetic autonomic reactivation and cardiovascular mortality risk via 1-minute and 2-minute heart rate recovery (HRR) kinetics.
---

# Cardiac Heart Rate Recovery (HRR) Post-Exercise Skill

This skill computes autonomic parasympathetic vagal reactivation metrics following peak exercise testing to stratify cardiovascular mortality risk according to Cole et al. (NEJM) standards.

## Core Capabilities
- Evaluates 1-Minute Heart Rate Recovery ($HRR_1 = HR_{peak} - HR_{1\text{min}}$).
- Evaluates 2-Minute Heart Rate Recovery ($HRR_2 = HR_{peak} - HR_{2\text{min}}$).
- Applies protocol-specific prognostic thresholds:
  * Active cooldown: normal $> 12\text{ bpm}$; abnormal $\le 12\text{ bpm}$.
  * Passive cooldown: normal $> 18\text{ bpm}$; abnormal $\le 18\text{ bpm}$.
- Analyzes chronotropic reserve utilization and vagal reactivation kinetics.

## Zero-Mock Architecture
Standard Python standard library only with zero external dependencies.
