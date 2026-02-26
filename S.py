# Before applying the S principle:
# The add method is doing the calculation and also the display of the result

class Calculator:
    def add(self, a, b):
        result = a + b
        print(f"Result is: {result}")


# After applying the S principle:
# There is a dedicated class and its method to display results in general,
# So now the add method can focus solely on calculating results

class MathEngine:
    def add(self, a, b):
        return a + b # Job 1: Just math

class DisplayManager:
    def show(self, value):
        print(f"--- [ {value} ] ---")


# Testing

if __name__ == "__main__":
    engine = MathEngine()
    display = DisplayManager()
    
    result = engine.add(5, 10)
    display.show(result)
