import unittest
from unittest.mock import MagicMock, patch
import os
import sys

# Add the agent directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../agent'))
import guard_agent

class TestAladdinGuard(unittest.TestCase):
    @patch('boto3.client')
    def test_high_volatility_scaling(self, mock_boto):
        agent = guard_agent.AladdinGuardAgent("test-asg")
        # Scenario: Market Open, 90% CPU
        report = agent.analyze_and_act(cpu_utilization=90, is_market_open=True)
        
        self.assertTrue(report['action_taken'])
        self.assertIn("High volatility", report['reasoning'])

    @patch('boto3.client')
    def test_off_hours_optimization(self, mock_boto):
        agent = guard_agent.AladdinGuardAgent("test-asg")
        # Scenario: Market Closed, 10% CPU
        report = agent.analyze_and_act(cpu_utilization=10, is_market_open=False)
        
        self.assertTrue(report['action_taken'])
        self.assertIn("Efficiency potential", report['reasoning'])

if __name__ == '__main__':
    unittest.main()
