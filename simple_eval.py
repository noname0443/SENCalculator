import ast
import operator as op

operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.floordiv, ast.USub: op.neg}

def eval_expr(expr):
    return eval_(ast.parse(expr, mode='eval').body)

def eval_(node):
    match node:
        case ast.Constant(value) if isinstance(value, int):
            return value
        case ast.BinOp(left, op, right):
            return operators[type(op)](eval_(left), eval_(right))
        case ast.UnaryOp(op, operand):
            return operators[type(op)](eval_(operand))
        case _:
            raise TypeError(node)