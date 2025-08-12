def solution(n, k):
    a = n // 10
    answer = ((n * 12000) + (k * 2000)) - (a*2000)
    return answer