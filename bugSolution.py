def my_function(x):
    fib_sequence = [0, 1]
    if x <= 1:
        return fib_sequence[x]
    else:
        for i in range(2, x + 1):
            next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_fib)
        return fib_sequence[x]