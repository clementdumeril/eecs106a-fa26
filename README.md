# EECS C106A Fall 2026 Homework Skeletons

This public repository is the staff-managed source for homework skeletons. Students keep one private repository for the semester and pull new assignments from this repository as they are released.

## One-time setup

1. On GitHub, create an **empty private repository** named `eecs106a-fa26`. Do not initialize it with a README, license, or `.gitignore`.
2. Clone this staff repository once:

   ```bash
   git clone https://github.com/ucb-ee106/fa26-hw-skeleton.git eecs106a-fa26
   cd eecs106a-fa26
   ```

3. Keep the public course repository as the `staff` remote and add your private repository as `origin`:

   ```bash
   git remote rename origin staff
   git remote set-url --push staff DISABLED
   git remote add origin https://github.com/YOUR_GITHUB_USERNAME/eecs106a-fa26.git
   git push -u origin main
   ```

4. Confirm the remotes before doing coursework:

   ```bash
   git remote -v
   ```

`origin` must be your private repository. `staff` must fetch from this public repository and show `DISABLED` as its push target; students should never push to the staff repository.

## Getting a newly released assignment

Commit your current work first, then run:

```bash
git pull staff main
git push origin main
```

Staff normally add new assignment directories without changing previously released notebooks, so these pulls should merge cleanly.

## Submitting to Gradescope

After completing an assignment:

```bash
git status
git add hw0/HW0.ipynb
git commit -m "Complete HW0"
git push origin main
```

Open Gradescope directly, choose the GitHub submission method, select your private `eecs106a-fa26` repository and the `main` branch, and verify that the intended notebook is present. Saving locally is not enough: the notebook must be committed and pushed before submission.

Never add solutions, credentials, access tokens, or unrelated private material to this repository or to a submission.
