# python3
import numpy

# Discrete Knapsack problem without repetition
def maxGold(W, n, items):
    """ Outputs the maximum weight of gold that fits in knapsack of capacity W
    (int, int, list) -> (int, 2D-array) """

    value = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            # if item i is not part of optimal knapsack
            value[i][j] = value[i][j-1]
            if items[j-1]<=i:
                # if item i is part of optimal knapsack
                temp = value[i-items[j-1]][j-1] + items[j-1]
                # max(i in knapsack, i not in knapsack)
                if temp > value[i][j]:
                    value[i][j] = temp

    return (int(value[W][n]), value)

def printItems(value, items, i, j, arr):
    """ Finds which items are present in optimal solution and returns a boolean array 
    (2D-array, list, int, int, list) -> (list) """

    if i == 0 and j == 0:
        arr.reverse()
        return arr
    if value[i][j] == value[i][j-1]:
        arr.append(0)
        return printItems(value, items, i, j-1, arr)
    else:
        arr.append(1)
        return printItems(value, items, i-items[j-1], j-1, arr)
        
if __name__ == '__main__':
    W, n               = [int(i) for i in input().split()]
    item_weights       = [int(i) for i in input().split()]
    max_weight, Matrix = maxGold(W, n, item_weights)
    bool_vector      = printItems(Matrix, item_weights, W, n, [])
    optimal = [str(j) for i, j in enumerate(item_weights) if bool_vector[i]]
    print(f"Weights in knapsack of capacity {W}: {' '.join(optimal)}")

    # print('\nMaximum weight of gold that fits into a knapsack of capacity', W,':', max_weight)
    # print(f"Weights: {' '.join([str(i) for i in item_weights])}\nVector : {' '.join([str(i) for i in bool_vector])}")
