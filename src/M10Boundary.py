def get_boundary(input_data):
    if input_data["Library"] == 1 and input_data["Problem"] == 1 and input_data["Size"] == 1:
        # pylbm, von karman vortex street and size of 1 chosen
        boundary_data = {"x_min": 0., "x_max": 3., "y_min": 0., "y_max": 1.}
        return boundary_data

