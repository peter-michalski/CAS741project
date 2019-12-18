import datetime
import sys
import logging
from M13InputTypes import *


def verify_input(input_data):

    input_bounds = {
        "LIBRARY": 1,
        "PROBLEM": 1,
        "DIMENSIONS": 2,
        "VEL_DIRS": 9,
        "SIZE": 1,
        "REYNOLDS_MIN": 0.0001,
        "REYNOLDS_MAX": 50000,
        "DENSITY_MIN": 0.0708,
        "DENSITY_MAX": 13.6,
        "BULK_VIS_MIN": 0.0001,
        "BULK_VIS_MAX": 20000,
        "SHEAR_VIS_MIN": 0.001,
        "SHEAR_VIS_MAX": 20000,
        "TIME": 1
    }

    # first check if the input file keys are acceptable
    verification_issues = False
    for key in input_data:
        is_parameter_known = False
        for x in inputTypes:
            if key == x:
                is_parameter_known = True
        if not is_parameter_known:
            error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), " - The parameter ", key,
                  " is not known to the system. Please see the User Guide.")
            logging.error(str(error_message))
            verification_issues = True

    # now check if the input file values are acceptable
    if 'Library' in input_data:
        if input_data["Library"] != input_bounds["LIBRARY"]:
            error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                  " - The input.txt file parameter Library is out of bounds. Please see the User Guide.")
            logging.error(str(error_message))
            verification_issues = True
    else:
        error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
              " - The input.txt file parameter Library is out of bounds. Please see the User Guide.")
        logging.error(str(error_message))
        verification_issues = True

    if 'Problem' in input_data:
        if input_data["Problem"] != input_bounds["PROBLEM"]:
            error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                  " - The input.txt file parameter Problem is out of bounds. Please see the User Guide.")
            logging.error(str(error_message))
            verification_issues = True
    else:
        error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
              " - The input.txt file parameter Problem is out of bounds. Please see the User Guide.")
        logging.error(str(error_message))
        verification_issues = True

    if 'Dimensions' in input_data:
        if input_data["Dimensions"] != input_bounds["DIMENSIONS"]:
            error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                  " - The input.txt file parameter Dimensions is out of bounds. Please see the User Guide.")
            logging.error(str(error_message))
            verification_issues = True

    if 'Size' in input_data:
        if input_data["Size"] != input_bounds["SIZE"]:
            error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                  " - The input.txt file parameter Size is out of bounds. Please see the User Guide.")
            logging.error(str(error_message))
            verification_issues = True

    if 'VelocityDirections' in input_data:
        if input_data["VelocityDirections"] != input_bounds["VEL_DIRS"]:
            error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                  " - The input.txt file parameter VelocityDirections is out of bounds. Please see the User Guide.")
            logging.error(str(error_message))
            verification_issues = True

    if 'ReynoldsNumber' in input_data:
        if input_data["ReynoldsNumber"] < input_bounds["REYNOLDS_MIN"]:
            error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                  " - The input.txt file parameter ReynoldsNumber is out of bounds. Please see the User Guide.")
            logging.error(str(error_message))
            verification_issues = True
        if input_data["ReynoldsNumber"] > input_bounds["REYNOLDS_MAX"]:
            error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                  " - The input.txt file parameter ReynoldsNumber is out of bounds. Please see the User Guide.")
            logging.error(str(error_message))
            verification_issues = True

    if 'Density' in input_data:
        if input_data["Density"] < input_bounds["DENSITY_MIN"]:
            error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                  " - The input.txt file parameter Density is out of bounds. Please see the User Guide.")
            logging.error(str(error_message))
            verification_issues = True
        if input_data["Density"] > input_bounds["DENSITY_MAX"]:
            error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                  " - The input.txt file parameter Density is out of bounds. Please see the User Guide.")
            logging.error(str(error_message))
            verification_issues = True

    if 'BulkViscosity' in input_data:
        if input_data["BulkViscosity"] < input_bounds["BULK_VIS_MIN"]:
            error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                  " - The input.txt file parameter BulkViscosity is out of bounds. Please see the User Guide.")
            logging.error(str(error_message))
            verification_issues = True
        if input_data["BulkViscosity"] > input_bounds["BULK_VIS_MAX"]:
            error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                  " - The input.txt file parameter BulkViscosity is out of bounds. Please see the User Guide.")
            logging.error(str(error_message))
            verification_issues = True

    if 'ShearViscosity' in input_data:
        if input_data["ShearViscosity"] < input_bounds["SHEAR_VIS_MIN"]:
            error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                  " - The input.txt file parameter ShearViscosity is out of bounds. Please see the User Guide.")
            logging.error(str(error_message))
            verification_issues = True
        if input_data["ShearViscosity"] > input_bounds["SHEAR_VIS_MAX"]:
            error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                  " - The input.txt file parameter ShearViscosity is out of bounds. Please see the User Guide.")
            logging.error(str(error_message))
            verification_issues = True

    if 'Time' in input_data:
        if input_data["Time"] < input_bounds["TIME"]:
            error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                  " - The input.txt file parameter Time is out of bounds. Please see the User Guide.")
            logging.error(str(error_message))
            verification_issues = True

    # finally check if all necessary inputs are provided
    dimensions = False
    velocity_directions = False
    reynolds_number = False
    density = False
    bulk_viscosity = False
    time = False
    size = False

    if input_data["Library"] == input_bounds["LIBRARY"]:
        if input_data["Problem"] == input_bounds["PROBLEM"]:
            for key in input_data:
                if key == "Dimensions":
                    dimensions = True
                if key == "VelocityDirections":
                    velocity_directions = True
                if key == "ReynoldsNumber":
                    reynolds_number = True
                if key == "Density":
                    density = True
                if key == "BulkViscosity":
                    bulk_viscosity = True
                if key == "Time":
                    time = True
                if key == "Size":
                    size = True

    if not dimensions or not velocity_directions or not reynolds_number or not density or not bulk_viscosity or not time or not size:
        verification_issues = True
        error_message = (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
              " - The input.txt file is missing (or has incorrect) required parameters for the designated problem. Please see the User Guide.")
        logging.error(str(error_message))

    if verification_issues:
        sys.exit()

    return True
