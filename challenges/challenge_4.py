# https://www.geeksforgeeks.org/word-break-problem-dp-32/
def word_break(wordList, word):
    if word == '':
        return True
    else:
        wordLen = len(word)
        return any([(word[:i] in wordList) and word_break(wordList, word[i:]) for i in range(1, wordLen+1)])

words = ['hello', 'hell']
result = word_break(5)
print(result)

def knapSack(capacity, items, n):
    ''' A  method to determine the maximum value of the items included in the knapsack 
  without exceeding the capacity  
      Parameters: 
      C= 50
      items = (("boot", 10, 60),
           ("tent", 20, 100),
           ("water", 30, 120),
           ("first aid", 15, 70))
      Returns: max value
  '''
    # This is base Case
    if n == 0 or capacity == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # capacity, then this item cannot be included in the optimal solution
    item_weight = items[n-1][1]

    if (item_weight > capacity):
        return knapSack(capacity, items, n-1)

    else:
        return max(items[n-1][2] + knapSack(capacity - item_weight, items, n-1),
                   knapSack(capacity, items, n-1))


def print_knapsack_solution(items, capacity, result):
    '''prints the return value from our knapsack function'''
    print("For this input: {}, \n Capacity of knapsack: {}\n The value of the optimal solution to the knapsack problem is V={}".format(
        items, capacity, result))


items = (("boot", 10, 60),
         ("tent", 20, 100),
         ("water", 30, 120),
         ("first aid", 15, 70))
capacity = 50
result = knapSack(capacity, items, len(items))
print_knapsack_solution(items, capacity, result)