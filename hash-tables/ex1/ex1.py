#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)


    diff = []
    answers = []
    for i in range(len(weights)):
        hash_table_insert(ht, weights[i], i)
        diff.append(limit-weights[i])

    for i in diff:
        if hash_table_retrieve(ht, i) != None:
            answers.append(i)
        
    if len(answers)==2:
        x = hash_table_retrieve(ht, answers[0])
        y = hash_table_retrieve(ht, answers[1])
        if x == y:
            indices = [i for i, x in enumerate(weights) if x == answers[0]]
            return (indices[1], indices[0])
        if x > y:
            return (x, y)
        else:
            return (y, x)
    else:
        return None
    

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)