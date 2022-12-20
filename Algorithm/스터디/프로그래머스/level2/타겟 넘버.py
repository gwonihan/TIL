def recursive(numbers, sum, target):
    if numbers == []:
        if sum == target:
            return 1
        else:
            return 0
    return recursive(numbers[1:], sum + numbers[0], target) + recursive(numbers[1:], sum - numbers[0], target)

def solution(numbers, target):
    return recursive(numbers, 0, target)