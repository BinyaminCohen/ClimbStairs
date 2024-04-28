def climbStairs(n):
    try:
        # Ensure that n is an integer and is greater than zero
        if not isinstance(n, int):
            raise ValueError("Input must be an integer")

        if n <= 1:
            return 1

        a, b = 1, 1
        for i in range(2, n + 1):
            a, b = b, a + b  # `b` becomes the current step, `a` is the previous step
            print(a, b)
        return b

    except (ValueError, TypeError) as e:
        # Handle the error by printing an error message
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    print(climbStairs(5))
