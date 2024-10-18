import ast

def create_rule(rule_definition):
    """
    Create a rule by parsing the rule definition and converting it into an executable Python expression.

    Args:
        rule_definition (str): The rule as a string (e.g., "age > 18 and income > 50000").

    Returns:
        function: A function that evaluates the rule with the provided user data.
    """
    try:
        # Parse the rule into an Abstract Syntax Tree (AST)
        rule_ast = ast.parse(rule_definition, mode='eval').body

        # Define a function that takes user data as input and evaluates the rule
        def rule_function(user_data):
            # Ensure the user_data dictionary is used within the eval function
            return eval(compile(ast.Expression(body=rule_ast), filename="<ast>", mode="eval"), user_data)

        return rule_function
    except Exception as e:
        raise ValueError(f"Failed to create rule from definition: {e}")

def evaluate_rule(rule, user_data):
    """
    Evaluate a given rule function with user data.

    Args:
        rule (function): A function created by `create_rule`.
        user_data (dict): The data to evaluate the rule against.

    Returns:
        bool: The result of the rule evaluation.
    """
    try:
        # Call the rule function with the user_data
        return rule(user_data)
    except Exception as e:
        raise ValueError(f"Failed to evaluate rule with user data: {e}")
