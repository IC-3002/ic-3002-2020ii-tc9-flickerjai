def maximizar(As, D):
    As.sort(key=lambda x: x[1])
    total = 0
    secuencia = []

    i = 0

    while total < D and i < len(As):
        if total + As[i][1] <= D:
            total =  total + As[i][1]
            secuencia.append(As[i])
        else:
            return secuencia

        i = i + 1
