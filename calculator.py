def add(a, b):
    """Функция сложения"""
    return a + b

def multiply(a, b):
    """Функция умножения"""
    return a * b

def divide(a, b):
    """Функция деления с обработкой деления на ноль"""
    if b == 0:
        raise ValueError("Деление на ноль запрещено!")
    return a / b

if __name__ == "__main__":
    print(f"Add: 2 + 3 = {add(2, 3)}")
    print(f"Multiply: 2 * 3 = {multiply(2, 3)}")
    print(f"Divide: 6 / 3 = {divide(6, 3)}")
