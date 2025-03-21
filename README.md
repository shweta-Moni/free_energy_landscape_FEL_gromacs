# free_energy_landscape_FEL_gromacs
Calculate and visualize the Free Energy Landscape (FEL) against Root Mean Square Deviation (RMSD) and Radius of Gyration (Rg) from molecular dynamics trajectories from GROMACS

# Free Energy Landscape (FEL) Analysis

This repository contains a workflow for calculating and visualizing the Free Energy Landscape (FEL) against Root Mean Square Deviation (RMSD) and Radius of Gyration (Rg) from molecular dynamics trajectories. The workflow uses GROMACS tools and custom Python scripts for data processing and visualization.

## Workflow Overview

1. Calculate RMSD and Rg from Trajectory
2. Merge RMSD and Rg Data
3. Calculate Free Energy Landscape using `gmx sham`
4. Convert XPM File to TXT
5. Generate 2D Contour Plot
6. Generate 3D Surface Plot
7. Find Closest Matching Timestamp

## Prerequisites

- GROMACS installed and properly configured.
- Python 3.x with the following libraries:
  - `numpy`
  - `matplotlib`
  - `scipy`
- Perl (for `sham.pl` script).

