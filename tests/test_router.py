import unittest
import sys
import os

# Add examples and tools directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "examples"))
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "tools"))

import skill_router
import capability_architect

class TestSkillRouter(unittest.TestCase):
    def test_tokens(self):
        tokens = skill_router._tokens("A farmer needs to plan spraying without GPS")
        # should exclude stop words and lower/split correctly
        self.assertIn("farmer", tokens)
        self.assertIn("spraying", tokens)
        self.assertIn("gps", tokens)
        self.assertNotIn("without", tokens)
        self.assertNotIn("need", tokens)

    def test_rank(self):
        idx = [
            {"name": "spraying-drone", "desc": "agricultural drone for spraying crop fields", "rel": "05-food/autonomous/spraying-drone"},
            {"name": "finance-analyst", "desc": "financial risk analysis and modeling", "rel": "16-finance/roles/analyst"},
        ]
        results = skill_router.rank("spraying crops", idx)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][1]["rel"], "05-food/autonomous/spraying-drone")

class TestCapabilityArchitect(unittest.TestCase):
    def test_parse_flags(self):
        argv = ["--safety", "high", "--latency", "hrt", "--task", "control"]
        s = capability_architect.parse_flags(argv)
        self.assertEqual(s["safety"], "high")
        self.assertEqual(s["latency"], "hrt")
        self.assertEqual(s["task"], "control")
        self.assertEqual(s["compute"], "edge") # should fall back to default

    def test_recommend_deterministic(self):
        s = {
            "safety": "high",
            "latency": "hrt",
            "verify": "req",
            "task": "control",
            "data": "sim",
            "compute": "edge",
            "conn": "reliable"
        }
        tier, methods, fallback, why = capability_architect.recommend(s)
        self.assertIn("Deterministic controller", tier)
        self.assertIn("formal verification", tier)
        self.assertIn("Sim-to-real (domain randomization)", methods)
        self.assertIn("minimal-risk maneuver", fallback)

if __name__ == "__main__":
    unittest.main()
