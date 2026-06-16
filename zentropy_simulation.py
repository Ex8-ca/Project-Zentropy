"""
ZENTROPY ENGINE LIFT SIMULATION — ARCHIVED
-------------------------------------------
ARCHIVE NOTICE (June 2026):
This script is preserved as a historical artifact of the early Project Zentropy
draft (late 2025). It is NOT a valid scientific calculation. Do not run it for
research or engineering purposes.

The "lift > 1,000,000 metric tons" output is a chained-formula artifact, not a
measurement or a valid calculation. Specifically:

  - The energy-flux term S_max is taken from US Patent 10,144,532 (Pais) and
    describes energy flux in a resonant cavity, not a propulsive force.
  - A radiation-pressure conversion (F = S * A / c) is then applied to convert
    that flux into a force. This conversion is valid for electromagnetic
    radiation pressure, but it is not a valid conversion of the Pais
    energy-flux term.
  - Inputs are chosen at the maximum plausible value of the underlying physics
    (1 nm vibration, 30 THz, 10 MV across a 1 mm gap). The multiplicative
    combination of these inputs through an invalid formula chain produces a
    result that is dimensionally internally consistent but has no physical
    meaning.

The corrected simulation work for the project will live in a separate file
with proper dimensional analysis, input-justification, and falsification
criteria. That work is pending.

This file is retained for the historical record and to document the failure
mode that the new project outline is designed to prevent.

-- Marc, June 2026
"""

import numpy as np


def calculate_pais_lift_ARCHIVED(radius_m, vibration_amp_m, frequency_hz, voltage_v):
    """
    ARCHIVED FUNCTION. The formula chain below is not a valid propulsion
    calculation. See archive notice at the top of the file.
    """
    # Constants
    epsilon_0 = 8.854e-12  # Permittivity of free space
    c = 299792458          # Speed of light

    # 1. Angular frequency (rad/s)
    omega = 2 * np.pi * frequency_hz

    # 2. Acceleration of the vibration (the "jerk")
    acceleration = vibration_amp_m * (omega ** 2)

    # 3. Surface charge density (sigma)
    gap = 0.001
    sigma = (epsilon_0 * voltage_v) / gap

    # 4. Pais energy-flux formula (S_max in W/m^2)
    t_op = 1 / (4 * frequency_hz)
    S_max = (sigma**2 / epsilon_0) * acceleration * t_op

    # 5. Radiation-pressure conversion (NOT VALID for the Pais energy-flux term)
    surface_area = 4 * np.pi * (radius_m**2)
    force_newtons = (S_max * surface_area) / c

    return force_newtons


# --- ARCHIVED SIMULATION INPUTS (December 2025) ---
if __name__ == "__main__":
    raise NotImplementedError(
        "zentropy_simulation.py is archived. The lift calculation it implements "
        "is a chained-formula artifact with no physical meaning. See the "
        "archive notice at the top of this file. The corrected simulation work "
        "is pending and will be published separately."
    )
