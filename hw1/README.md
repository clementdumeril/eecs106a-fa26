# HW1: Vehicle Coordinate Transformations

Implement `get_corners` in `hw1.py`. It transforms four vehicle-frame corner
positions into world-frame positions using the vehicle's position and heading.
The function signature and array shapes are documented in the starter file.
Follow the assignment handout for the full problem statement.

## Files and setup

- `hw1.py`: implement `get_corners` here.
- `car_vis.py`: plot the supplied path and your transformed car corners.
- `parking_path.mat`: the supplied `x`, `y`, and `theta` samples; do not edit it.
- `check_hw1.py`: four public correctness checks.
- `requirements.txt`: NumPy for arrays, SciPy to load the MATLAB data file, and
  Matplotlib for plotting.

Generated `__pycache__/` folders and `.OTTER_LOG` files are ignored by Git.
They are not assignment deliverables. Keep saved preview images out of your
submission unless the handout requests them.

Activate the [course Python environment](../README.md#python-environment)
(tested with Python 3.13.5). From the semester repository root, run:

```bash
python -m pip install -r hw1/requirements.txt
```

## Visualize and understand the problem

Before implementing the function, you can inspect the supplied path:

```bash
python hw1/car_vis.py --path-only
```

At each sample, `xy` is the world-frame location of the car's coordinate-frame
origin. It is a reference point on the car, not its geometric center. `theta`
is its heading in radians: zero points along world +x, and positive angles turn
counterclockwise. Use the supplied heading, not the direction of travel along
the path (a parking car may be reversing).

The four corner inputs describe fixed points in the car's own frame, in this
order: front right, front left, rear left, rear right. Your function returns
those same points in the world frame, in the same order, each as a `(2, 1)`
column vector. The visualizer calls your function without supplying a solution.

Once you have implemented it, draw the car snapshots:

```bash
python hw1/car_vis.py
python hw1/car_vis.py --step 25
```

The dashed line is the car-frame origin's path; black dots mark the sampled
origins. Blue outlines show your car corners, and the orange edge marks the
front of the car. The axes use equal scale so a correct car keeps its dimensions
as it rotates and translates. Smaller `--step` values draw more snapshots.
This is an overlay of poses, not an animation.

If a plot window is unavailable, save an image instead:

```bash
python hw1/car_vis.py --save parking.png
```

You can combine `--save` with `--path-only`. The dataset is located relative to
`car_vis.py`, so running from either the repository root or inside `hw1/` works.

## Local checks

```bash
python hw1/check_hw1.py
```

The untouched starter deliberately fails the checks. A completed implementation
should pass all four public cases. Passing these cases does not guarantee full
credit on the additional Gradescope tests. A plausible-looking plot is useful
feedback, but is not a substitute for the numerical checks.

## Submission

Run the checker, then commit and push your implementation from the repository root:

```bash
git add hw1/hw1.py
git commit -m "Complete HW1"
git push origin main
```

Select your private semester repository and its `main` branch in the HW1
Gradescope assignment. Verify that the latest commit is included and review
the grading results. After changes, commit, push, and resubmit.

Do not move `hw1.py` to the repository root. See the
[repository README](../README.md) for the Git setup and submission workflow,
and follow the handout for any additional deliverables.
