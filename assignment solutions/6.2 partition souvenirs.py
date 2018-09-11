# python3
import numpy

# Discrete Knapsack problem without repetition
def partitions(W, n, items):
    """ Finds if number of partitions having capacity W is >=3
    (int, int, list) -> (int) """
    count = 0 
    value = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            if items[j-1]<=i:
                temp = value[i-items[j-1]][j-1] + items[j-1]
                if temp > value[i][j]:
                    value[i][j] = temp
            if value[i][j] == W: count += 1

    if count < 3: print('0')
    else: print('1')

if __name__ == '__main__':
    n = int(input())
    item_weights = [int(i) for i in input().split()]
    total_weight = sum(item_weights)
    if n<3: 
        print('0')
    elif total_weight%3 != 0: 
        print('0')
    else:
        partitions(total_weight//3, n, item_weights)
        