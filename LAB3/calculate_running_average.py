def calculate_running_average(numbers):
    running_sum = 0
    result = []

    for i, num in enumerate(numbers, 1):
        running_sum += num
        result.append(running_sum / i)

    return result
input_numbers = [2, 4, 6, 8, 10]
running_averages = calculate_running_average(input_numbers)
print(running_averages)
