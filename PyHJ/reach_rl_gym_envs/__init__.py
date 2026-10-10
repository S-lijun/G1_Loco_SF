"""Registers the internal gym envs (optional for Isaac / LatentHumanoid training).

``load_plugin_envs`` existed in older gymnasium (0.28/0.29) but was removed in
1.x (Isaac Lab pins gymnasium==1.2.0). It was unused here anyway.
"""
from gymnasium.envs.registration import register



# Customized environments begin: 


register(
    id='ra_highway_Game-v2',
    entry_point='PyHJ.reach_rl_gym_envs.ra_highway_10d:Highway_10D_game_Env2',
    max_episode_steps = 400, # horizon of the problem
    reward_threshold=1e8,
)
register(
    id="ra_droneracing_Game-v6",
    entry_point="PyHJ.reach_rl_gym_envs.Double_Drones_RA_linear:Double_Drones_RA_linear_Game_Env6",
    max_episode_steps=200,
    reward_threshold=1e8
)
register(
    id="ra_1d_Game-v0",
    entry_point="PyHJ.reach_rl_gym_envs.ra_1d:LQR_Env",
    max_episode_steps=1000,
    reward_threshold=1e8,
)

register(
    id="dubins-v0",
    entry_point="PyHJ.reach_rl_gym_envs.dubins:Dubins_Env",
    max_episode_steps=1000,
    reward_threshold=1e8,
)

register(
    id="dubins4d-v0",
    entry_point="PyHJ.reach_rl_gym_envs.dubins4d:Dubins_Env_4D",
    max_episode_steps=1000,
    reward_threshold=1e8,
)

register(
    id="dubinsRA-v0",
    entry_point="PyHJ.reach_rl_gym_envs.dubinsRA:DubinsRA_Env",
    max_episode_steps=1000,
    reward_threshold=1e8,
)

register(
    id="dubins-wm",
    entry_point="PyHJ.reach_rl_gym_envs.dubins-wm:Dubins_WM_Env",
    max_episode_steps=16,
    reward_threshold=1e8,
)

