#!/usr/bin/env python3
"""Plot the parking trajectory and the corners returned by your HW1 code.

Adapted from HW1 Problem 4, EECS C106A Fall 2022.
Original: Valmik Prabhu (2019); modified by Jay Monga (2021).
"""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat

import hw1


def plot_car_path(step=50, path_only=False):
    """Draw snapshots every `step` samples, or just the supplied trajectory."""
    path = loadmat(Path(__file__).with_name("parking_path.mat"))
    x, y, theta = (path[name].ravel() for name in ("x", "y", "theta"))

    length = 2.54
    bumper = 0.725
    half_width = 0.865
    corners = (
        np.array([[length + bumper], [-half_width]]),  # front right
        np.array([[length + bumper], [half_width]]),   # front left
        np.array([[-bumper], [half_width]]),           # rear left
        np.array([[-bumper], [-half_width]]),          # rear right
    )

    figure, axes = plt.subplots(figsize=(10, 6))
    axes.plot(x, y, "--", color="0.5", label="Reference-point path")
    if not path_only:
        for index in range(0, len(x), step):
            xy = np.array([[x[index]], [y[index]]])
            world_corners = hw1.get_corners(xy, theta[index], *corners)
            # Close the outline by connecting the last corner to the first.
            outline = np.hstack((*world_corners, world_corners[0]))
            axes.plot(
                outline[0], outline[1], color="tab:blue",
                label="Car outline" if index == 0 else None,
            )
            axes.plot(
                outline[0, :2], outline[1, :2], color="tab:orange", linewidth=3,
                label="Front edge" if index == 0 else None,
            )
            axes.plot(
                x[index], y[index], "o", color="black", markersize=4,
                label="Car-frame origin" if index == 0 else None,
            )

    axes.set_title("HW1 parking trajectory" if path_only else "HW1 car poses along the parking path")
    axes.set_xlabel("World x (m)")
    axes.set_ylabel("World y (m)")
    axes.set_aspect("equal", adjustable="box")
    axes.grid(alpha=0.25)
    axes.legend()
    figure.tight_layout()
    return figure


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--step", type=int, default=50, help="samples between car outlines (default: 50)")
    parser.add_argument("--path-only", action="store_true", help="show the supplied path before implementing get_corners")
    parser.add_argument("--save", type=Path, help="save the plot to a file instead of opening a window")
    args = parser.parse_args()
    if args.step < 1:
        parser.error("--step must be a positive integer")

    try:
        figure = plot_car_path(args.step, args.path_only)
    except NotImplementedError:
        parser.exit(1, "Implement get_corners to draw the car, or use --path-only to view the trajectory first.\n")
    if args.save:
        figure.savefig(args.save, dpi=150)
        plt.close(figure)
    else:
        plt.show()


if __name__ == "__main__":
    main()
