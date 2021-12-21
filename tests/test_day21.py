"""TEST MODULE TEMPLATE"""
from src.day21 import game, multiverseGame
import unittest

exampleInput = (4, 8)

class TestAOCDay21(unittest.TestCase):
    def test_solution_1(self):
        example_result = (745, 993)
        self.assertEqual(game(*exampleInput), example_result)

    def test_solution_2(self):
        example_result = (444356092776315,341960390180808)
        
        self.assertEqual(multiverseGame(*exampleInput, 0, 0, True),example_result)


if __name__ == "__main__":
    unittest.main()
