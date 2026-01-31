class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression

    def evaluate(self):
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error: {e}"


class CalculatorApp:
    def run(self):
        expression = "(3 + 5) * 2"
        solver = ExpressionSolver(expression)
        result = solver.evaluate()

        print("Expression:", expression)
        print("Result:", result)


# Main execution
if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
