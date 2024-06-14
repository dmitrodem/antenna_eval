#!/usr/bin/env python3

import click
import subprocess
import sys, os
import h5py
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

@click.group()
def main():
    pass

@main.command()
def build():
    base, _ = os.path.splitext(os.path.basename(sys.argv[0]))
    with h5py.File(f"{base}.hdf5", "a") as hdf:
        try:
            grp = hdf["sweep"]
        except KeyError:
            grp = hdf.create_group("sweep")

        values = np.linspace(5, 55, num = 201)
        with click.progressbar(values) as progressbar:
            for ustrip_stub in progressbar:
                # click.echo(f"Running {ustrip_stub}")
                dset_name = f"{ustrip_stub:.4f}"
                if dset_name in grp:
                    continue
                subprocess.run(["cadfeko_batch", base, "-#", f"ustrip_stub={ustrip_stub}"], stdout=subprocess.DEVNULL)
                subprocess.run(["runfeko", base, "-np", "all"], stdout=subprocess.DEVNULL)
                r = subprocess.run(["postfeko", "--non-interactive", "--run-script", f"{base}.lua", base], capture_output=True, text = True)

                content = []
                started = False
                for line in r.stdout.split("\n"):
                    if not started:
                        if line.startswith("--START--"):
                            started = True
                    else:
                        if line.startswith("--END--"):
                            break
                        else:
                            content.append(list(map(float, line.split(","))))

                content = np.asarray(content)

                grp.create_dataset(dset_name, data = content)


@main.command()
def postprocess():
    base, _ = os.path.splitext(os.path.basename(sys.argv[0]))
    with h5py.File(f"{base}.hdf5", "r") as hdf:
        keys = sorted(hdf["sweep"].keys(), key = lambda a: float(a))
        Z = np.zeros(len(keys), dtype = complex)
        for i, k in enumerate(keys):
            try:
                line = hdf["sweep"][k][0]
                Z[i] = line[1] + 1j*line[2]
            except IndexError:
                Z[i] = np.NaN
        parameter = np.asarray([float(x) for x in keys])
        # plt.plot(parameter, Z.real)
        # plt.plot(parameter, Z.imag)
        # plt.show()
        wavelength = 43.8994
        l1 = 2*np.pi/wavelength * 50.0
        l2 = 2*np.pi/wavelength * parameter
        z = Z/50.0
        z_deembed = 50*(z - 1j*np.tan(l2))/(1-1j*z*np.tan(l2))
        plt.plot(parameter, z_deembed.real)
        plt.plot(parameter, z_deembed.imag)
        plt.show()
if __name__ == "__main__":
    main()
