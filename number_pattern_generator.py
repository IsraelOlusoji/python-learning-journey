def number_pattern(n: int) -> str:
    if not isinstance(n, int):
        raise TypeError("Argument must be an integer value")

    if n <= 0:
        raise ValueError("Argument must be an integer greater than 0")
        
    return " ".join(str(i) for i in range(1, n + 1))

if __name__ == "__main__":
    try:
        print(number_pattern(8))
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")