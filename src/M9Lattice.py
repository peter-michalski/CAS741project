def get_weights(input_data):
    if input_data["Library"] == 1:
        # pylbm chosen
        # this library sets the model wights automatically
        return 0
    if input_data["Dimensions"] == 2:
        if input_data["VelocityDirections"] == 9:
            weights = [4/9, 1/9, 1/9, 1/9, 1/9, 1/36, 1/36, 1/36, 1/36]
            #return weights

    # other libraries may require dynamic setting of weights, and will include an exception handler and log file entry
