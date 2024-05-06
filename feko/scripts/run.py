#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("../26_turnstile_with_sat_FarField1.ffe", skiprows = 15)
theta, phi, gain = tuple(map(lambda x: x.reshape(361, 181), [np.deg2rad(data[:, 0]), np.deg2rad(data[:, 1]), data[:, -1]]))

gain_min = np.linspace(-6, 3, num = 101)
area_factor = np.asarray([np.trapz(x = phi[:, 0], y = np.trapz(x = theta[0, :], y = (gain > _g) * np.sin(theta)))/4/np.pi for _g in gain_min])

plt.plot(gain_min, area_factor)
plt.xlabel("$G_{min}$ [dBi]")
plt.ylabel("Solid angle ratio")
plt.tight_layout()
plt.grid()
plt.show()
