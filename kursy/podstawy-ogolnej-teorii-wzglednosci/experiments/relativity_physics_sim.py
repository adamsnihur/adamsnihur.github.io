#!/usr/bin/env python3
"""
ScientistTwo Empirical Simulation & Validation Engine
Domain: General Relativity Foundations & Classical Tests
Calculates:
1. Light Deflection (Einstein vs Newton)
2. Schwarzschild Geodesics & ISCO (r = 6GM/c^2)
3. Gravitational Redshift (Pound-Rebka Experiment)
4. Gravitational Wave Chirp Waveform (GW150914 inspired)
Generates publication-grade 300 DPI figures in the canonical academic palette.
"""

import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

# Canonical Academic Palette
COLOR_CARMINE = "#821D2D"
COLOR_GOLD = "#B88942"
COLOR_NAVY = "#1B354B"
COLOR_BG = "#FAF8F5"
COLOR_TEXT = "#2C2C2C"

# Physical constants (SI)
G = 6.67430e-11        # m^3 kg^-1 s^-2
c = 299792458.0        # m s^-1
M_sun = 1.98847e30     # kg
R_sun = 6.9634e8       # m
g_earth = 9.80665      # m s^-2


def calculate_light_deflection():
    """Deflection of light grazing the solar limb in arcseconds."""
    theta_gr_rad = (4 * G * M_sun) / (c**2 * R_sun)
    theta_newton_rad = (2 * G * M_sun) / (c**2 * R_sun)
    
    rad_to_arcsec = (180.0 / math.pi) * 3600.0
    theta_gr_arcsec = theta_gr_rad * rad_to_arcsec
    theta_newton_arcsec = theta_newton_rad * rad_to_arcsec
    
    # Assertions for verification
    assert 1.74 <= theta_gr_arcsec <= 1.76, f"GR deflection out of bounds: {theta_gr_arcsec}"
    assert 0.86 <= theta_newton_arcsec <= 0.88, f"Newton deflection out of bounds: {theta_newton_arcsec}"
    assert abs(theta_gr_arcsec - 2.0 * theta_newton_arcsec) < 1e-4, "GR must be exactly double Newtonian"
    
    return theta_gr_arcsec, theta_newton_arcsec


def calculate_pound_rebka():
    """Fractional frequency shift for Harvard tower height h = 22.5 m."""
    h = 22.5  # meters
    delta_f_over_f = (g_earth * h) / (c**2)
    assert 2.4e-15 <= delta_f_over_f <= 2.5e-15, f"Pound-Rebka shift mismatch: {delta_f_over_f}"
    return delta_f_over_f


def calculate_mercury_precession():
    """Relativistic perihelion advance per revolution in arcseconds."""
    a = 5.790905e10  # semi-major axis, m
    e = 0.205630     # eccentricity
    T_orbit = 87.969 * 86400  # seconds
    
    delta_phi_rad = (6 * math.pi * G * M_sun) / (c**2 * a * (1 - e**2))
    rad_to_arcsec = (180.0 / math.pi) * 3600.0
    delta_phi_arcsec = delta_phi_rad * rad_to_arcsec
    
    # In 1 century (100 Earth years):
    revolutions_per_century = (100 * 365.25 * 86400) / T_orbit
    precession_century = delta_phi_arcsec * revolutions_per_century
    assert 42.5 <= precession_century <= 43.5, f"Mercury precession out of bounds: {precession_century}"
    return precession_century


def generate_figures(output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Setup styling
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["axes.edgecolor"] = "#CCCCCC"
    plt.rcParams["axes.linewidth"] = 0.8

    # 1. Light Deflection Plot
    fig, ax = plt.subplots(figsize=(7, 4.2), dpi=300)
    fig.patch.set_facecolor(COLOR_BG)
    ax.set_facecolor("#FFFFFF")
    
    b_factors = np.linspace(1.0, 5.0, 200)
    gr_curve = 1.751 / b_factors
    newton_curve = 0.875 / b_factors
    
    ax.plot(b_factors, gr_curve, color=COLOR_CARMINE, lw=2.4, label="Ogólna Teoria Względności (Einstein: 1.751'')")
    ax.plot(b_factors, newton_curve, color=COLOR_NAVY, lw=2.0, ls="--", label="Podejście Newtonowskie (Soldner: 0.875'')")
    
    # Eddington 1919 observation point
    ax.scatter([1.0], [1.751], color=COLOR_GOLD, s=70, zorder=5, edgecolor="#000", label="Krawędź Słońca (R = R☉, Sobral/Principe 1919)")
    
    ax.set_title("Ugięcie promieni świetlnych w polu grawitacyjnym Słońca", fontsize=11, fontweight="bold", color=COLOR_TEXT, pad=12)
    ax.set_xlabel("Parametr zderzenia b [R☉]", fontsize=10, color=COLOR_TEXT)
    ax.set_ylabel("Kąt ugięcia θ [sekundy łuku]", fontsize=10, color=COLOR_TEXT)
    ax.grid(True, linestyle=":", alpha=0.5, color="#BBBBBB")
    ax.legend(frameon=True, facecolor="#FFFFFF", edgecolor="#DDDDDD", fontsize=9)
    plt.tight_layout()
    fig.savefig(output_dir / "ugiecie_swiatla_porownanie.png")
    plt.close(fig)
    print("Wygenerowano: images/ugiecie_swiatla_porownanie.png")

    # 2. Schwarzschild Effective Potential and ISCO
    fig, ax = plt.subplots(figsize=(7, 4.2), dpi=300)
    fig.patch.set_facecolor(COLOR_BG)
    ax.set_facecolor("#FFFFFF")
    
    r = np.linspace(2.2, 18.0, 300)  # in units of M (G=M=c=1)
    L_vals = [3.464, 3.8, 4.2]  # L = sqrt(12) is critical ISCO threshold
    
    for L, style, col in zip(L_vals, [":", "-", "-."], [COLOR_GOLD, COLOR_CARMINE, COLOR_NAVY]):
        # V_eff = (1 - 2/r) * (1 + L^2 / r^2)
        v_eff = (1.0 - 2.0 / r) * (1.0 + (L**2) / (r**2))
        lbl = f"L = {L:.2f}" + (" (Próg ISCO: r = 6M)" if abs(L - 3.464) < 0.05 else "")
        ax.plot(r, v_eff, color=col, lw=2.0, ls=style, label=lbl)

    ax.axvline(6.0, color=COLOR_GOLD, ls="--", alpha=0.8, lw=1.2, label="ISCO (r = 6 GM/c²)")
    ax.axvline(2.0, color="#555555", ls="-", lw=1.5, label="Horyzont zdarzeń (r = 2 GM/c²)")
    
    ax.set_title("Efektywny potencjał w geometrii Schwarzschilda i próg ISCO", fontsize=11, fontweight="bold", color=COLOR_TEXT, pad=12)
    ax.set_xlabel("Promień r [GM/c²]", fontsize=10, color=COLOR_TEXT)
    ax.set_ylabel("Potencjał efektywny V_eff(r)", fontsize=10, color=COLOR_TEXT)
    ax.set_ylim(0.85, 1.05)
    ax.grid(True, linestyle=":", alpha=0.5, color="#BBBBBB")
    ax.legend(frameon=True, facecolor="#FFFFFF", edgecolor="#DDDDDD", fontsize=8.5, loc="lower right")
    plt.tight_layout()
    fig.savefig(output_dir / "orbity_schwarzschild_isco.png")
    plt.close(fig)
    print("Wygenerowano: images/orbity_schwarzschild_isco.png")

    # 3. Gravitational Wave Chirp Signal (GW150914-like)
    fig, ax = plt.subplots(figsize=(7, 3.8), dpi=300)
    fig.patch.set_facecolor(COLOR_BG)
    ax.set_facecolor("#FFFFFF")
    
    t = np.linspace(-0.25, 0.0, 1000)
    tau = -t
    tau[tau <= 0] = 1e-5
    # Frequency f(tau) ~ tau^(-3/8)
    f = 35.0 * (tau / 0.25)**(-3/8)
    phi = 2 * np.pi * np.cumsum(f) * (t[1] - t[0])
    # Amplitude grows ~ tau^(-1/4)
    amp = (tau / 0.25)**(-1/4) * np.exp(t * 3.0)
    wave = amp * np.sin(phi)
    
    # Ringdown (after t=0)
    t_post = np.linspace(0.0, 0.06, 250)
    wave_post = np.exp(-t_post / 0.012) * np.sin(2 * np.pi * 250.0 * t_post)
    
    t_full = np.concatenate([t, t_post])
    wave_full = np.concatenate([wave, wave_post])
    
    ax.plot(t_full, wave_full, color=COLOR_CARMINE, lw=1.6, label="Sygnał odkształcenia czasoprzestrzeni h(t)")
    ax.axvline(0.0, color=COLOR_GOLD, ls="--", lw=1.2, label="Moment koalescencji (Merger)")
    
    ax.set_title("Relatywistyczny sygnał 'Chirp' koalescencji podwójnej czarnej dziury", fontsize=11, fontweight="bold", color=COLOR_TEXT, pad=12)
    ax.set_xlabel("Czas t [s] względem momentu zderzenia", fontsize=10, color=COLOR_TEXT)
    ax.set_ylabel("Odkształcenie tensora h+", fontsize=10, color=COLOR_TEXT)
    ax.grid(True, linestyle=":", alpha=0.5, color="#BBBBBB")
    ax.legend(frameon=True, facecolor="#FFFFFF", edgecolor="#DDDDDD", fontsize=9)
    plt.tight_layout()
    fig.savefig(output_dir / "fala_grawitacyjna_chirp.png")
    plt.close(fig)
    print("Wygenerowano: images/fala_grawitacyjna_chirp.png")


if __name__ == "__main__":
    print("=== ScientistTwo Sandbox Verification ===")
    gr_def, newt_def = calculate_light_deflection()
    print(f"[OK] Ugięcie światła: GR = {gr_def:.3f}'', Newton = {newt_def:.3f}''")
    
    redshift = calculate_pound_rebka()
    print(f"[OK] Przesunięcie Pounda-Rebki: df/f = {redshift:.3e}")
    
    merc = calculate_mercury_precession()
    print(f"[OK] Precesja Merkurego: {merc:.2f}'' na stulecie")
    
    out_dir = Path(__file__).resolve().parent.parent / "images"
    generate_figures(out_dir)
    print("Wszystkie testy empiryczne ScientistTwo zaliczone ze statusem GOOD.")
