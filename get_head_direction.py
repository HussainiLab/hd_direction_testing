def get_head_direction(pos_x, pos_y): 
    
    """
            
            Will compute the head direction.
            Parameters: 
                pos_x, pos_y: 1D arrays of x and y coordinates and time array.
                
                
            Returns: 
                angles: Array of angles in degrees.
    """
    
    last_point = [0,0]  # Keep track of the last x,y point
    last_angle = 0      # Keep track of the most previous computed angle
    angles = []         # Will accumulate angles as they are computed
    
    # Iterate over the pos_x and pos_y points
    for i in range(len(pos_x)): 
        
        # Grab the current point
        current_point = [float(pos_x[i]), float(pos_y[i])]  
        
        # If the last point is the same as the current point
        if (last_point[0] == current_point[0]) and (last_point[1] == current_point[1]): 
            # Retain the same angle 
            angle = last_angle
            
        else: 
            # Compute the arctan (i.e the angle formed by the line defined by both points
            # and the horizontal axis [range -180 to +180])
            # Uses the formula arctan( (y2-y1) / (x2-x1))
            Y = current_point[1] - last_point[1]
            X = current_point[0] - last_point[0]
            angle = math.atan2(Y,X) * (180/np.pi) # Convert to degrees
        
        # Append angle value to list
        angles.append(angle)
        
        # Update new angle and last_point values 
        last_point[0] = current_point[0]
        last_point[1] = current_point[1]
        last_angle = angle
        
    # Angle smoothing. Currently it does NOT smooth at all 
    # Can increase smoothing by increasing number. 
    angles = smooth(angles, 1)
    # Adding 180 to scale between 0 and 360 rather than -180 to 180
    angles = np.array(angles) + 180
    
    return angles
