import boto3
import os
import json
from datetime import datetime

class AladdinGuardAgent:
    def __init__(self, asg_name):
        self.asg_name = asg_name
        self.client = boto3.client('autoscaling')

    def analyze_and_act(self, cpu_utilization, is_market_open=True):
        print(f"[AI] Aladdin Guard Agent: Analyzing system metrics at {datetime.now()}")
        print(f"DEBUG: CPU Utilization: {cpu_utilization}%, Market Open: {is_market_open}")

        #  Operational Reasoning Engine
        recommendation = ""
        action_taken = False

        if is_market_open and cpu_utilization > 80:
            recommendation = "High volatility detected during market hours. Scaling up for reliability."
            # self.client.set_desired_capacity(AutoScalingGroupName=self.asg_name, DesiredCapacity=5)
            action_taken = True
        elif not is_market_open and cpu_utilization < 20:
            recommendation = "Market closed. Efficiency potential (FinOps) detected. Scaling down to base capacity."
            # self.client.set_desired_capacity(AutoScalingGroupName=self.asg_name, DesiredCapacity=2)
            action_taken = True
        else:
            recommendation = "System within healthy parameters. No action required."

        print(f"[AI] AGENT REASONING: {recommendation}")
        return {
            "timestamp": datetime.now().isoformat(),
            "action_taken": action_taken,
            "reasoning": recommendation
        }

if __name__ == "__main__":
    agent = AladdinGuardAgent("aladdin-core-asg")
    # Simulate a FinOps optimization opportunity
    report = agent.analyze_and_act(cpu_utilization=15, is_market_open=False)
    print(f"[SUCCESS] Final Agent Report: {json.dumps(report, indent=2)}")
