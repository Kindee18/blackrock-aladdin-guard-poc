# 🛡️ Aladdin Guard: AI-Driven Reliability & FinOps

## Project Overview
Aladdin Guard is a Proof of Concept (PoC) demonstrating an **AI-Augmented SRE workflow** designed for the scale and complexity of BlackRock's Aladdin platform.

This tool uses a Python-based "Reliability Agent" to bridge the gap between market volatility and infrastructure cost, automatically adjusting resource capacity while providing human-readable "Reasoning Reports."

## 💎 The Edge: Why This Matters for BlackRock
*   **AI-Augmented Engineering:** Directly implements the "AI-assisted development" goal mentioned in recent Aladdin Engineering roles.
*   **Cost-Aware Reliability:** Optimizes multi-cloud infrastructure based on market hours and utilization trends.
*   **Operational Intelligence:** Replaces static threshold alerts with a reasoning-based remediation engine.

## 🏗️ Technical Stack
*   **Infrastructure:** Terraform (AWS/Multi-Cloud simulation)
*   **Automation:** GitHub Actions
*   **Logic Engine:** Python (Aladdin Guard Agent)
*   **Observability:** CloudWatch Metrics

## 🚀 How It Works
1.  **Monitor:** The agent ingest real-time performance metrics (CPU, Memory, Cost).
2.  **Reason:** The "Aladdin Guard Agent" determines the operational context (e.g., "Is the market open?", "Is this a peak volatility period?").
3.  **Act:** The agent triggers auto-scaling actions (up or down) to ensure 100% availability during market hours and maximum efficiency during off-hours.
4.  **Report:** The agent generates an automated audit trail of its reasoning for the SRE team.

## 🛠️ Local Demo
You can build and simulate the agent reasoning locally:
```bash
# Run the AI-driven reasoning simulation
make agent
```

---
**Built for the Aladdin Engineering Team by Aegis Agent.**
