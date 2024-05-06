#!/usr/bin/env python3

import click
import subprocess
import sys
import h5py
import numpy as np

BASE = "39_stacked_patch_from_ieee_paper_s_band"

@click.command()
def main():
    with h5py.File("data.hdf5", "a") as hdf:
        try:
            grp = hdf["sweep"]
        except KeyError:
            grp = hdf.create_group("sweep")

        for length in np.linspace(1, 20, num = 20):
            click.echo(f"Running length = {length}")
            dset_name = f"{length}"
            if dset_name in grp:
                continue
            subprocess.run(["cadfeko_batch", BASE, "-#", f"ustrip_l2={length}"], stdout=subprocess.DEVNULL)
            subprocess.run(["runfeko", BASE, "-np", "all"], stdout=subprocess.DEVNULL)
            r = subprocess.run(["postfeko", "--non-interactive", "--run-script", "my_pf.lua", BASE], capture_output=True, text = True)

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

            # if not "frequency" in grp:
            #     grp.create_dataset("frequency", data = content[:, 0])

            grp.create_dataset(dset_name, data = content)


if __name__ == "__main__":
    main()
