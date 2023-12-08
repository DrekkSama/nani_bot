import sys

from __init__ import run_ladder_game

# Load bot
from nani_bot import nani_bot

from sc2 import maps
from sc2.data import Difficulty, Race
from sc2.main import run_game
from sc2.player import Bot, Computer

from sc2.bot_ai import BotAI
from sc2.data import Difficulty, Race
from sc2.ids.ability_id import AbilityId
from sc2.ids.unit_typeid import UnitTypeId
from sc2.position import Point2, Point3
from sc2.unit import Unit
from sc2.units import Units

from sc2.ids.buff_id import BuffId
from sc2.ids.upgrade_id import UpgradeId

import numpy as np


bot = Bot(Race.Protoss, nani_bot())

# Start game
if __name__ == "__main__":
    if "--LadderServer" in sys.argv:
        # Ladder game started by LadderManager
        print("Starting ladder game...")
        result, opponentid = run_ladder_game(bot)
        print(result, " against opponent ", opponentid)
    else:
        # Local game
        print("Starting local game...")
        run_game(maps.get("BotMicroArena_3"), [bot, Computer(Race.Protoss, Difficulty.VeryHard)], realtime=True)
