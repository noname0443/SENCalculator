import simple_eval

class Evaluator():
    def eval(self, expression):
        pass

class SimpleEvaluator(Evaluator):
    def eval(self, expression):
        return simple_eval.eval_expr(expression)