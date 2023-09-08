
def dailyTemperature(temperatures):
    stack = []
    answer = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            j = stack.pop()
            answer[j] = i - j

        stack.append(i)

    return answer

temperatures = [73,74,75,71,69,72,76,73]
ans = dailyTemperature(temperatures)

print("The array with the number of days to get a warmer temperature is: ",ans)
