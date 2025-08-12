def solution(array):
    answer = array
    answer.sort()
    return answer[len(answer) // 2]