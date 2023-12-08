from sc2 import maps
from sc2.bot_ai import BotAI
from sc2.data import Difficulty, Race, AIBuild, Result

from sc2.ids.unit_typeid import UnitTypeId
from sc2.main import run_game
from sc2.player import Bot, Computer
from sc2.unit import Unit
from sc2.units import Units

from sc2.position import Point2, Point3
from sc2.ids.ability_id import AbilityId
from sc2.ids.buff_id import BuffId
from sc2.ids.upgrade_id import UpgradeId


class nani_bot(BotAI):

    async def on_step(self, iteration: int):

        target = self.game_info.map_center
        if self.enemy_start_locations:
            target = self.enemy_start_locations[0]
        elif self.enemy_structures:
            target = self.enemy_structures.first.position              
        for unit in self.units.idle:
            unit.attack(target)


def main():
    run_game(
        maps.get("BotMicroArena_"),
        [
            Bot(Race.Protoss, nani_bot(), name="Nani"),
            Computer(Race.Protoss, Difficulty.CheatInsane, ai_build=AIBuild.Rush),
        ],
        realtime=False,
        random_seed=0,
    )


if __name__ == "__main__":
    main()
