# utils.py

import ast

def create_rule(rule_definition):
    try:
        rule_ast = ast.parse(rule_definition, mode='eval').body

        def rule_function(user_data):
            return eval(compile(ast.Expression(body=rule_ast), filename="<ast>", mode="eval"), {}, user_data)

        return rule_function
    except Exception as e:
        raise ValueError(f"Failed to create rule from definition: {e}")

def evaluate_rule(rule, user_data):
    try:
        return rule(user_data)
    except Exception as e:
        raise ValueError(f"Failed to evaluate rule with user data: {e}")
