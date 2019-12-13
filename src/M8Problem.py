import pylbm
from M9Lattice import *
from M10Boundary import *
from M12DataStructure import *

def format_input(input_data):
    lattice = get_weights(input_data)
    boundary = get_boundary(input_data)

    if input_data["Library"] == 1:
        if input_data["Problem"] == 1:

            def bc_in(f, m, x, y):
                m[qx] = input_data["Density"] * (input_data["Velocity"]/20)

            dummy = 3.0/(input_data["Velocity"]*input_data["Density"]*(1./64))
            s_mu = 1.0/(0.5+input_data["BulkViscosity"]*dummy)
            eta = input_data["Density"]*(1./20)*2*0.05/input_data["ReynoldsNumber"]
            s_q = 1.0/(0.5+eta*dummy)
            s = [0., 0., 0., s_mu, s_mu, s_q, s_q, s_q, s_q]
            dummy2 = 1./(LA**2*input_data["Density"])
            qx2 = dummy2 * qx ** 2
            qy2 = dummy2 * qy ** 2
            q2 = qx2 + qy2
            qxy = dummy2 * qx * qy

            problem_parameters = {
                'box': {'x': [boundary["x_min"], boundary["x_max"]],
                        'y': [boundary["y_min"], boundary["y_max"]],
                        'label': [0, 2, 0, 0]
                        },
                'elements': [pylbm.Circle([.3, 0.5 * (boundary["y_min"] + boundary["y_max"]) + 1./64], 0.05, label=1)],
                'space_step': 1./64,
                'scheme_velocity': input_data["Velocity"],
                'parameters': {LA: input_data["Velocity"]},
                'schemes': [
                    {
                        'velocities': list(range(9)),
                        'conserved_moments': [rho, qx, qy],
                        'polynomials': [
                            1, LA * X, LA * Y,
                               3 * (X ** 2 + Y ** 2) - 4,
                               (9 * (X ** 2 + Y ** 2) ** 2 - 21 * (X ** 2 + Y ** 2) + 8) / 2,
                               3 * X * (X ** 2 + Y ** 2) - 5 * X, 3 * Y * (X ** 2 + Y ** 2) - 5 * Y,
                               X ** 2 - Y ** 2, X * Y
                        ],
                        'relaxation_parameters': s,
                        'equilibrium': [
                            rho, qx, qy,
                            -2 * rho + 3 * q2,
                            rho - 3 * q2,
                            -qx / LA, -qy / LA,
                            qx2 - qy2, qxy
                        ],
                    },
                ],
                'init': {rho: input_data["Density"],
                         qx: 0.,
                         qy: 0.
                         },
                'boundary_conditions': {
                    0: {'method': {0: pylbm.bc.BouzidiBounceBack}, 'value': bc_in},
                    1: {'method': {0: pylbm.bc.BouzidiBounceBack}},
                    2: {'method': {0: pylbm.bc.NeumannX}},
                },
                'generator': 'cython',
            }

            return problem_parameters
