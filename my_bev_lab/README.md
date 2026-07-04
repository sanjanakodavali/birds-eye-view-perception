# BEV Perception Lab

This folder contains my original implementation and experimentation layer built on top of the OpenDriveLab BEV perception toolbox.

## My Contributions

- Built a reproducible camera-to-BEV visualization pipeline for autonomous driving perception experiments.
- Implemented utilities for loading camera intrinsics, extrinsics, and lidar-to-image transformation matrices.
- Added BEV visualization scripts to inspect multi-view camera projection behavior.
- Documented the BEV perception workflow, dataset assumptions, and experiment setup.
- Added evaluation notes for comparing baseline BEV augmentations and projection outputs.

## Why BEV Perception

Bird's-eye-view perception is widely used in autonomous driving because it transforms multi-camera or multi-sensor inputs into a shared top-down spatial representation for detection, segmentation, and planning.

## Tech Stack

Python, PyTorch, OpenCV, NumPy, BEV toolbox, Waymo/nuScenes-style camera calibration data

## Attribution

This work uses OpenDriveLab's public BEV perception repository as a reference/toolbox. The `my_bev_lab` folder contains my own implementation notes, scripts, visualizations, and experiments.
