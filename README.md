# Humanoid Locomotion SF

Safety-filter training for the Unitree G1 in Isaac Sim. PyHJ and the Isaac Lab source used by the training scripts are already in this repo.

## Install

Use a new conda environment. Do not reuse an older Isaac Sim environment. Open a fresh terminal so `PYTHONPATH`, `ISAACSIM_PATH`, and `ISAACLAB_PATH` are unset.

Works on Windows 11 and Ubuntu 22.04 / 24.04 (x86_64). The NVIDIA driver must support CUDA 12.8. `git` must be on `PATH`. The Isaac Sim download is several GB.

From the repository root:

```bash
conda create -n env_isaaclab python=3.11.14 pip -y
conda activate env_isaaclab
pip install -r requirements.txt
```

`requirements.txt` installs:

- Isaac Sim 5.1.0.0 and PyTorch 2.7.0+cu128
- Isaac Lab from `IsaacLab/source` inside this repo
- `pywin32` on Windows only

PyHJ is the `PyHJ/` directory in this repo. Do not clone PytorchReachability and do not `pip install` PyHJ.

## Weights not stored in git

These paths are gitignored. Copy them onto the machine after clone:

- `wm_ckpt_18-27-17/` (`hydra.yaml` and `checkpoints/model_latest.pth`)
- `.pretrained_checkpoints/rsl_rl/Isaac-Velocity-Flat-G1-v0/checkpoint.pt`

Training reads the world model with `--dino_ckpt_dir <repo root> --dino_encoder wm_ckpt_18-27-17`.
