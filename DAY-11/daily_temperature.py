def dailyTemperatures(temps):
    stack = []
    res = [0] * len(temps)

    for i, temp in enumerate(temps):
        while stack and temp > temps[stack[-1]]:
            idx = stack.pop()
            res[idx] = i - idx
        stack.append(i)

    return res


print(dailyTemperatures([73,74,75,71,69,72,76,73]))