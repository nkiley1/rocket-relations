"""Ideal Nozzle Relations for calculating Cf and cstar

This code assumes ideal rocket relations. Additionally, all inputs must be float values that make sense.

"""

import numpy as np


# Function to calculate cstar using ideal rocket relations
def cstar_calc(gamma, specific_gas_const, stagnation_temp) -> float:
    """
    Calculate cstar value for an ideal rocket

    Input:
     specific heat ratio (gamma [-]): float
     specific gas constant (R [J/kg/K]): float
     stagnation temp (T0 [K]): float

    Output:
     cstar [m/s]: float --> characteristic velocity
    """
    type_error = []
    if not isinstance(gamma, float):
        type_error.append("gamma must be a number")
    if not isinstance(specific_gas_const, float):
        type_error.append("R must be a number")
    if not isinstance(stagnation_temp, float):
        type_error.append("T0 must be a number")
    if not type_error == []:
        raise TypeError(type_error)

    value_error = []
    if not 1 < gamma:
        value_error.append("gamma must be greater than 1 (should be less than 1.8 as well)")
    if not 0 < stagnation_temp:
        value_error.append("T0 must be greater than 0 K")
    if not 0 < specific_gas_const:
        value_error.append("R must be greater than 0")
    if not value_error == []:
        raise ValueError(value_error)

    cstar = np.sqrt((1/gamma)*((gamma+1)/2)**((gamma+1)/(gamma-1)*specific_gas_const*stagnation_temp))
    return cstar


# Function to calculate Cf using ideal rocket relations
def cf_calc(gamma, pe_over_po, pa_over_po, ae_over_astar) -> float:
    """
    Calculate Cf value for an ideal rocket

    Input:
     specific heat ratio (gamma [-]): float
     Pe/P0 [-]: float --> exit pressure over stagnation pressure
     Pa/P0 [-]: float --> ambient pressure over stagnation pressure
     Ae/A* [-]: float --> nozzle exit area over throat area

    Output:
     Cf [-]: float --> thrust coefficient
    """
    type_error = []
    if not isinstance(gamma, float):
        type_error.append("gamma must be a number")
    if not isinstance(pe_over_po, float):
        type_error.append("Pe/P0 must be a number")
    if not isinstance(pa_over_po, float):
        type_error.append("Pa/P0 must be a number")
    if not isinstance(ae_over_astar, float):
        type_error.append("Ae/A* must be a number")
    if not type_error == []:
        raise TypeError(type_error)

    value_error = []
    if not 1 < gamma:
        value_error.append("gamma must be greater than 1 (should be less than 1.8 as well)")
    if not 0 <= pe_over_po < 1:
        value_error.append("Pe/P0 must be in range [0,1)")
    if not 0 <= pa_over_po < 1:
        value_error.append("Pa/P0 must be in range [0,1)")
    if not 1 <= ae_over_astar:
        value_error.append("Ae/A* must be >= 1")
    if not value_error == []:
        raise ValueError(value_error)

    cf = np.sqrt(((2*gamma**2)/(gamma-1))*(2/(gamma+1))**((gamma+1)/(gamma-1))*(1-pe_over_po**((gamma-1)/gamma)))+(pe_over_po-pa_over_po)*ae_over_astar
    return cf
