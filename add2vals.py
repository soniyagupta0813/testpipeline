import sys

def add(a, b):
    return a + b

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python add2vals.py <num1> <num2>")
    else:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
        result = add(x, y)
        print(f"Sum: {result}")