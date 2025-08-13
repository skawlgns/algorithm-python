# 정수가 담긴 리스트 num_list가 주어질 때, 
# num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(num_list):
    answer = num_list
    even_num = 0
    old_num = 0

    for i in answer:
        if i % 2 == 0:
            even_num += 1
        else:
            old_num += 1
    
    print([even_num, old_num])

solution([1, 2, 3, 4, 5]) 