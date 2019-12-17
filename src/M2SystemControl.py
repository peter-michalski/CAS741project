import numpy as np
from M3InputReading import *
from M12DataStructure import *
from M8Problem import *
import logging
import sys
import time



def main_function():
    s0 = time.time()
    logging.basicConfig(filename="log_file.log", level=logging.INFO)

    input_data = input_array()

    if input_data["Library"] == 1:
        # pylbm chosen
        if input_data["Problem"] == 1:
            # von karman vortex street chosen

            # first get problem parameters
            problem_parameters = format_input(input_data)
            boundary_data = get_boundary(input_data)

            # perform the simulation (based on pylbm tutorial), iterating for for time intervals - this is M5, M6, M7
            solution = pylbm.Simulation(problem_parameters)
            while solution.t < input_data["Time"]:
                solution.one_time_step()

            # create the image (based on pylbm tutorial) - this is M11
            viewer = pylbm.viewer.matplotlib_viewer
            fig = viewer.Fig()
            ax = fig[0]
            def vorticity(solution):
                ux = solution.m[qx] / solution.m[rho]
                uy = solution.m[qy] / solution.m[rho]
                V = np.abs(uy[2:, 1:-1] - uy[0:-2, 1:-1] - ux[1:-1, 2:] + ux[1:-1, 0:-2]) / (2 * solution.domain.dx)
                return -V
            im = ax.image(vorticity(solution).transpose(), clim=[-3., 0])
            ax.ellipse([.3 / (1./64), 0.5 * (boundary_data["y_min"] + boundary_data["y_max"]) / (1./64)], [0.05 / (1./64), 0.05 / (1./64)], 'r')
            ax.title = 'Von Karman vortex street at t = {0:f}'.format(solution.t)

            # output the image to the screen - M1

            s1 = time.time()
            s2 = s1-s0
            print(s2)
            fig.show()
main_function()
