#import statistics

def solution(numbers):
    #answer = statistics.mean(numbers)
    answer = sum(numbers) / len(numbers)
    return answer