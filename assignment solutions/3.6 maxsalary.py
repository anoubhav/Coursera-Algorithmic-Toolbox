# python3
n = int(input())
lst = [int(i) for i in input().split()]


def IsGreaterOrEqual(digit, max_digit):
    return int(str(digit)+str(max_digit))>=int(str(max_digit)+str(digit))
    # a = len(str(digit))
    # b = len(str(max_digit))
    # if a==b:
    #     return digit>=max_digit
    # elif a<b:
    #     for i in range(a):
    #         if int(str(digit)[i])<int(str(max_digit)[i]):
    #             return False
    #     for i in range(a, b):
    #         if int(str(digit)[0]) < int(str(max_digit)[i]):
    #             return False
    #     return True
            
    # else:
    #     # print(digit, max_digit)
    #     # print('hi')
    #     a, b = b, a
    #     digit, max_digit = max_digit, digit
    #     for i in range(a):
    #         if int(str(digit)[i])<int(str(max_digit)[i]):
    #             return True
    #     for i in range(a, b):
    #         if int(str(digit)[0]) <= int(str(max_digit)[i]):
    #             return True
    #     return False


def largestnumber(lst):
    answer = []
    
    while lst!=[]:
        max_digit = 0
        for digit in lst:
            if IsGreaterOrEqual(digit, max_digit):
                max_digit = digit
        # print(max_digit)
        answer.append(max_digit)
        lst.remove(max_digit)

    return answer

print(''.join([str(i) for i in largestnumber(lst)]))
