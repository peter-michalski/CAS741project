import numpy as np
from M3InputReading import *
from M12DataStructure import *
from M8Problem import *
import logging
np.set_printoptions(threshold=sys.maxsize)
import sys



def main_function():

    logging.basicConfig(filename="log_file.log", level=logging.INFO)

    input_data = input_array()

    if input_data["Library"] == 1:
        # pylbm chosen
        if input_data["Problem"] == 1:
            # von karman vortex street chosen

            # first get problem parameters
            problem_parameters = format_input(input_data)
            boundary_data = get_boundary(input_data)

            # This is M5, M6, M7; perform the simulation (based on pylbm tutorial - https://pylbm.readthedocs.io/en/latest/notebooks/07_Von_Karman_vortex_street.html), iterating for for time intervals
            solution = pylbm.Simulation(problem_parameters)
            while solution.t < input_data["Time"]:
                solution.one_time_step()

            # This is M11 - create the image (also based on pylbm tutorial)
            viewer = pylbm.viewer.matplotlib_viewer
            fig = viewer.Fig()
            image = fig[0]

            def vorticity(solution):
                ux = solution.m[qx] / solution.m[rho]
                uy = solution.m[qy] / solution.m[rho]
                vortvector = np.abs(uy[2:, 1:-1] - uy[0:-2, 1:-1] - ux[1:-1, 2:] + ux[1:-1, 0:-2]) / (2 * solution.domain.dx)
                return -vortvector
            im = image.image(vorticity(solution).transpose(), clim=[-3., 0])
            image.ellipse([.3 / (1./64), 0.5 * (boundary_data["y_min"] + boundary_data["y_max"]) / (1./64)], [0.05 / (1./64), 0.05 / (1./64)], 'r')
            image.title = 'Von Karman Vortex Street at time = {0:f}'.format(solution.t)

            # output the image to the screen - M1
            fig.show()


main_function()
