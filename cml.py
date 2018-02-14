import argparse
import math

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number", help="number")
    parser.add_argument("--operation", help="operation", \
                        choices=["add2", "subtract2", "multiply2", "divide2", "square",
                                 "square_root", "absolute_value", "logof2"])

    args = parser.parse_args()

    n = int(args.number)
    result = None
    if args.operation == "add2":
        result = n+2
    elif args.operation == "subtract2":
        result = n-2
    elif args.operation == "multiply2":
        result = n*2
    elif args.operation == "divide2":
        result = n/2
    elif args.operation == "square":
        result = n*n
    elif args.operation == "square_root":
        result = math.sqrt(n)
    elif args.operation == "absolute_value":
        result = math.fabs(n)
    elif args.operation == "logof2":
        result = math.log2(n)

    print("Result:", result)