def solution(numbers):
    li = []
    for n in numbers:
        std = n
        summ = 0
        for m in numbers:
            summ += abs(std-m)
        li.append([std, summ])
    
    li.sort(key=lambda x:x[1])
    answer = li[0][0]
    return answer

numbers = [1, 5, 7, 9]
answer = solution(numbers)
print(answer)
