# This file contains all of the default pokemon formula for calcultaing various values.
from math import sqrt
from dictonaries import *

# Stats are based on this formula and I think it is redone every levelup, based on experience
# Level: 1-100; IV: 0 - 31 per Stat; EV: 0 - 255 per stat, 510 across all stats cumulatively (Wild Pokemon have none)
# Nature Modifier for health should always be just one and will be either 0.9,1 or 1.1 for all other stats
def calculateStat(base,level,IV,EV,isHP,natureModifier,stage = [1,1,1,1,1,1]):
    stat = ((2 * base + IV + (EV//4)) * level) // 100
    if isHP:
        stat += (level + 5)
    stat += 5
    stat *= statStageMultiplers[stage]
    stat *= natureModifier
    stat = int(stat // 1)
    return stat


# The base damage of an attack is determined by a constant formula based on the intrinsic attributes of both pokemon and the move used
# Several external factors are then applied, there are quite a few of them
def calculateDamage(attacker,defender,move):
    if move.damageClass == "Physical":
        baseDamage = (((2 * attacker.level)//5 + 2) * move.power * attacker.actualStats[2]//defender.actualStats[1])//20 + 2
        finalDamage = baseDamage
    if move.damageClass == "Special":
        baseDamage = (((2 * attacker.level)//5 + 2) * move.power * attacker.actualStats[4]//defender.actualStats[5])//20 + 2
        finalDamage = baseDamage
    return finalDamage

