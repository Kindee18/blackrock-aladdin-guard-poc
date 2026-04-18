.PHONY: test agent help

help:
	@echo "Aladdin Guard PoC: AI-Driven Reliability & FinOps"
	@echo ""
	@echo "Usage:"
	@echo "  make agent    Run the AI-driven Reliability Agent (simulation)"
	@echo "  make test     Run unit tests for the agent logic"

agent:
	@echo "🚀 Starting Aladdin Guard Agent..."
	@python3 agent/guard_agent.py

test:
	@echo "🛠️ Running agent logic verification..."
	@python3 -m unittest tests/test_agent.py
