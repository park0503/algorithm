import itertools
import math

def isPrime(number):
    if number < 2:
        return 0
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return 0
    print(number)
    return 1
        
def solution(numbers):
    answer = 0
    numbers = list(numbers)
    possible = []
    for i in range(1,len(numbers)+1):
        temp = list(itertools.permutations(numbers, i))
        temp = list(map(lambda x:int(''.join(x)), temp))
        possible += temp
    possible = list(set(possible))

    for num in possible:
        answer += isPrime(num)
                   
    
    return answer