"""

Couldn't get the import to work for some reason
"""

from rocket_relations.ideal import cstar_calc, cf_calc

# Define the given parameters
T0 = 3500.0  # Combustion chamber temperature in Kelvin
gamma = 1.2  # Specific heat ratio
R = 350.0  # Specific gas constant in J/(kg*K)
pe_p0 = 0.0125  # Nozzle exit to chamber pressure ratio
pa_p0 = 0.02  # Ambient to chamber pressure ratio
Ae_Astar = 10.0  # Nozzle area ratio

# Calculate c* using the cstar_calc function
c_star = cstar_calc(gamma, R, T0)

# Calculate CF using the cf_calc function
cf = cf_calc(gamma, pe_p0, pa_p0, Ae_Astar)

# Display results
print(f"Characteristic Velocity (c*): {c_star:.7f} m/s")  # Rounded to 7 decimal places
print(f"Thrust Coefficient (CF): {cf:.7f}")  # Rounded to 7 decimal places

# Expected results
expected_c_star = 1706.6214
expected_cf = 1.5423079

# Validate results with expected values
print("\nValidation:")
print(f"c* matches expected: {abs(c_star - expected_c_star) < 1e-4}")
print(f"CF matches expected: {abs(cf - expected_cf) < 1e-4}")