def get_indices_of_item_weights(weights, length, limit):
   

    """
    YOUR CODE HERE
    
    weight limit = limit
    weights = [item weights]
    """
    out_put = {}
     
    #iterate through the list
    for i in range(length):
        #if limit - out_put[i] should return a num in array
        if limit - weights[i] in out_put:
            key = limit - weights[i]
            index = out_put[key]
            return [i, index]
        out_put[weights[i]] = i


    print(out_put)
    return None

weights = [ 4, 6, 10, 15, 16 ]
get_indices_of_item_weights(weights, 5, 21)


    
