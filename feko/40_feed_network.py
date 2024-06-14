#!/usr/bin/env python3

import click
import subprocess
import sys, os
import h5py
import numpy as np
from pathlib import Path

BASE = "39_stacked_patch_from_ieee_paper_s_band"

@click.command()
def main():
    base, _ = os.path.splitext(os.path.basename(sys.argv[0]))
    with h5py.File(f"{base}.hdf5", "a") as hdf:
        try:
            grp = hdf["sweep"]
        except KeyError:
            grp = hdf.create_group("sweep")

        for l1, l2 in zip(*tuple([x.reshape(-1) for x in np.meshgrid(np.linspace(5, 10, num = 21), np.linspace(5, 10, num = 21))])):
            click.echo(f"Running length = {l1}, {l2}")
            dset_name = f"{l1}:{l2}"
            if dset_name in grp:
                continue
            subprocess.run(["cadfeko_batch", base, "-#", f"ltest_1={l1}", "-#", f"ltest_2={l2}"], stdout=subprocess.DEVNULL)
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
            # if not "frequency" in grp:
            #     grp.create_dataset("frequency", data = content[:, 0])

            grp.create_dataset(dset_name, data = content)


if __name__ == "__main__":
    main()
