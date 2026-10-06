#!/usr/bin/env python3
"""
Capstone Numerical Verification Script
Reconstructs Chirp Mass, component masses, and Schwarzschild radius from GW150914 data.
"""

import math

# Fundamental physical constants
G = 6.67430e-11        # m^3 kg^-1 s^-2
c = 299792458.0        # m s^-1
M_sun = 1.98847e30     # kg

def run_capstone_verification():
    # Observational inputs (GW150914)
    f = 75.0               # Hz
    f_dot = 1350.0         # Hz / s

    # 1. Calculate Chirp Mass
    coeff = 5.0 / (96.0 * (math.pi ** (8.0 / 3.0)))
    bracket = coeff * (f ** (-11.0 / 3.0)) * f_dot
    M_chirp_kg = (c**3 / G) * (bracket ** (3.0 / 5.0))
    M_chirp_solar = M_chirp_kg / M_sun

    # 2. Equal mass components: M_chirp = M_0 * 2^(-1/5) => M_0 = M_chirp * 2^(1/5)
    M_0_solar = M_chirp_solar * (2.0 ** (0.2))

    # 3. Final black hole Schwarzschild radius (M_f = 62 M_sun)
    M_final_kg = 62.0 * M_sun
    r_s_final = (2 * G * M_final_kg) / (c**2)

    print(f"Masa chirpowa: {M_chirp_solar:.2f} M_sun")
    print(f"Masy poczatkowe czarnych dziur: m1 = m2 = {M_0_solar:.2f} M_sun")
    print(f"Promien Schwarzschilda po polaczeniu: {r_s_final / 1000.0:.2f} km")

    # Assertions
    assert 28.0 <= M_chirp_solar <= 32.0, f"Niepoprawna masa chirpowa: {M_chirp_solar}"
    assert 33.0 <= M_0_solar <= 37.0, f"Niepoprawna masa skladowa: {M_0_solar}"
    assert 170.0 <= (r_s_final / 1000.0) <= 195.0, f"Niepoprawny promien horyzontu: {r_s_final}"
    print("[SUCCESS] Capstone numerical verification passed!")

if __name__ == "__main__":
    run_capstone_verification()
