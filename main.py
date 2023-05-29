def fibonacci(n):
    if n < 0:
        raise ValueError("Não existe fibonacci com n negativo!")
    if type(n) != int:
        raise ValueError("so serve com numeros inteiros") 
    fib = [0, 1]
    if n == 0:
        return fib[0]
    for i in range(2, n + 1): 
        fib.append(fib[-1]+ fib[-2])
    return fib.pop()
