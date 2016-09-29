import gym
from gym import spaces
from gym import utils
from gym.utils import seeding
import numpy as np

import logging
logger = logging.getLogger(__name__)


class StakingEnv(gym.Env, utils.EzPickle):
    """Staking environment

    TO BE EDITED

    This environment corresponds to the version of the gambling
    problem described in Example 1.2 in Algorithms for
    Reinforcement Learning by Csaba Szepesvari (2010).
    https://sites.ualberta.ca/~szepesva/RLBook.html
    """

    def __init__(self):
        pass
