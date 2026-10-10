from PyHJ import data, env, exploration, policy, trainer, utils

# Built-in reachability gym envs are optional. Importing them under Isaac Lab
# (gymnasium 1.x) used to fail; humanoid HJ uses LatentHumanoidEnv instead.
try:
    from PyHJ import reach_rl_gym_envs  # noqa: F401
except Exception as _reach_env_exc:  # pragma: no cover
    reach_rl_gym_envs = None  # type: ignore
    import warnings

    warnings.warn(
        f"PyHJ.reach_rl_gym_envs unavailable ({_reach_env_exc!r}); "
        "OK if you train with a custom env (e.g. LatentHumanoidEnv).",
        stacklevel=1,
    )

__version__ = "0.0.1" # we adapt this repo from Tianshou version 0.5.1

__all__ = [
    "env",
    "data",
    "utils",
    "policy",
    "trainer",
    "exploration",
    "reach_rl_gym_envs",
]
