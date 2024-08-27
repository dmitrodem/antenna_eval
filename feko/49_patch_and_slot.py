#!/usr/bin/env python3

import click
import subprocess
import sys, os
import h5py
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.interpolate
import glob

@click.group()
def main():
    pass

@main.command()
def test():
    variations = [
        ("slot_length", np.linspace(2, 12, num = 21)),
        ("slot_width", np.linspace(0.1, 2.0, num = 20))
    ]
    vars = np.meshgrid(*tuple([x[1] for x in variations]))


@main.command()
def build():
    base, _ = os.path.splitext(os.path.basename(sys.argv[0]))
    with h5py.File(f"{base}.hdf5", "a") as hdf:
        try:
            grp = hdf["sweep"]
        except KeyError:
            grp = hdf.create_group("sweep")

        #variation = ("slot_length", np.linspace(2, 12, num = 21))
        variation = ("patch_width", np.linspace(30, 40, num = 21))
        with click.progressbar(variation[1]) as progressbar:
            for value in progressbar:
                #click.echo(f"Running {value}")
                dset_name = f"{value:.4f}"
                if dset_name in grp:
                    continue
                subprocess.run(["cadfeko_batch", base, "-#", f"{variation[0]}={value}"], stdout=subprocess.DEVNULL)
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

                dset = grp.create_dataset(dset_name, data = content)
                dset.attrs[variation[0]] = value


@main.command()
def postprocess():
    base, _ = os.path.splitext(os.path.basename(sys.argv[0]))
    plot_data = []
    with h5py.File(f"{base}.hdf5", "r") as hdf:
        keys = sorted(hdf["sweep"].keys(), key = lambda a: float(a))
        for k in keys:
            data = hdf["sweep"][k]
            f = scipy.interpolate.interp1d(data[:,0], data[:,1], kind = 'cubic')
            freq = np.linspace(data[0,0], data[-1, 0], num = 1001)
            index = np.argmax(f(freq))
            plot_data.append((float(k), freq[index]))
            #plt.plot(data[:,0], data[:,1])
    plt.plot(np.asarray([x[0] for x in plot_data]), np.asarray([x[1] for x in plot_data])*1e-9)
    plt.show()

@main.command()
def combine():
    base, _ = os.path.splitext(os.path.basename(sys.argv[0]))

    for hdf_file in glob.glob(f"{base}.hdf5.slot_length__*"):
        with h5py.File(hdf_file, "r") as hdf:
            plot_data = []
            keys = sorted(hdf["sweep"].keys(), key = lambda a: float(a))
            for k in keys:
                data = hdf["sweep"][k]
                f = scipy.interpolate.interp1d(data[:,0], data[:,1], kind = 'cubic')
                freq = np.linspace(data[0,0], data[-1, 0], num = 1001)
                index = np.argmax(f(freq))
                plot_data.append((float(k), freq[index]))
                #plt.plot(data[:,0], data[:,1])
            plt.plot(np.asarray([x[0] for x in plot_data]), np.asarray([x[1] for x in plot_data])*1e-9, label = f"{hdf_file}")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
