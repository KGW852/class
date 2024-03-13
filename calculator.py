class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

# 객체 생성 및 메소드 생성
calculator = Calculator(10, 5)
sum_result = calculator.add()
mul_result = calculator.multiply()

# 계산 결과 출력
print(f"덧셈 결과: {sum_result}")
print(f"곱셈 결과: {mul_result}")