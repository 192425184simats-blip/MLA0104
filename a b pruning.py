import math

def alphabeta(depth, node, maximizing, values, alpha, beta):

    if depth == 3:
        return values[node]

    if maximizing:
        best = -math.inf

        for i in range(2):
            val = alphabeta(depth + 1,
                            node * 2 + i,
                            False,
                            values,
                            alpha,
                            beta)

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            val = alphabeta(depth + 1,
                            node * 2 + i,
                            True,
                            values,
                            alpha,
                            beta)

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = []

print("Enter the 8 terminal values:")

for i in range(8):
    x = int(input(f"Value {i+1}: "))
    values.append(x)

result = alphabeta(0, 0, True, values, -math.inf, math.inf)

print("Optimal Value =", result)
