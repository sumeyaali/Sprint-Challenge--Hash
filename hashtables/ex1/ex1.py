def get_indices_of_item_weights(weights, length, limit):
   

    """
    YOUR CODE HERE
    
    weight limit = limit
    weights = [item weights]
    """
    out_put = {}
     

    for i in range(length):
        out_put[weights[i]] = i
    print(out_put)
    return None

weights = [ 4, 6, 10, 15, 16 ]
get_indices_of_item_weights(weights, 5, 21)


    
