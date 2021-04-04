def smooth(array, window): 
    
    """
            Smooths an array over a specified window by taking a boxcar average approach
            
            parameters: 
              array: 1D array values 
              window: window size of averaging. If window = N, we average over 'N' elements at a time.
            
            returns: 
              smoothed_ array: 1D array that has been smoothed over 'window' elements at a time
            
    """
    
    # Pre-allocate space for the smoothed_array
    smoothed_array = np.zeros((len(array), 1))
    
    # Iterate over the array
    for i in range(len(array) - window + 1): 
        current_average = sum(array[i:i+window]) / window # Compute the current average 
        smoothed_array[i:i+window] = current_average      # Add this value to the smoothed array
        
    return smoothed_array
