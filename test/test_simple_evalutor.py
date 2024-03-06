import threading
import unittest
import sys

sys.path.append('../')

import evaluator

class TestSimpleEvaluator(unittest.TestCase):
    def __init__(self, arg):
        super().__init__(arg)

    def test_simple_evaluator(self):
        evaluators = [
            evaluator.SimpleEvaluator()
        ]

        test_cases = [
            ["5+5", 10],
            ["5*5", 25],
            ["5-4", 1],
            ["21/7", 3],
            ["5+5*5-5", 25],
            ["2*(5+4)", 18],
            ["(4+5)*(5+4)", 81],
            ["0+0*0+0-0+0-0+0", 0],
            ["10-1-1-1-1-1", 5],
            ["0", 0],
            ["-5", -5],
            ["--5", 5],
            ["1--5", 6],
            ["---5", -5],
            ["2-3-4", -5],
            ["2-3-4-5", -10],
            ["1*2*3*4*5*6", 720],
            ["12/6/2", 1],
            ["100/2/2/5", 5],
            ["(50-5)/5", 9],
            ["((2+2)/4)", 1],
            ["((2+2)/4)+(4*(2+2))", 17],
            ["((2+2)/4)*(4*(2+2))", 16],
            ["2*(((2+2)/4)+(4*(2+2)))", 34],
            ["((2+2)/4)-(4*(2+2))", -15],
            ["5*(5-4)", 5],
            ["5*5-4", 21],
            ["5**2", 25],
            ["5**5", 3125],
            ["100/2/2/5/5", 1],
            ["1*5/5*2/2*3/3*4/4*5/5", 1],
            ["1/5", 0],
            ["1/5*5*2/2*3/3*4/4*5/5", 0],
            ["(5+5)/11", 0],
        ]

        error_test_cases = [
            "",
            "0/0",
            "1/0",
            "+",
            "-",
            "/",
            "*",
            "1*",
            "*1",
            "1++1",
        ]

        for evaluator_instance in evaluators:
            for test_case in test_cases:
                source_expression = test_case[0]
                source_answer = test_case[1]

                answer = evaluator_instance.eval(source_expression)

                self.assertEqual(answer, source_answer)

            for test_case in error_test_cases:
                haveError = False
                try:
                    evaluator_instance.eval(test_case)
                    haveError = False
                except:
                    haveError = True
                self.assertTrue(haveError)
            