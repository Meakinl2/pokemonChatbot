from math import sqrt
import random
from dictonaries import *

# Stats are based on this formula and I think it is redone every levelup, based on experience
# Level: 1-100; IV: 0 - 31 per Stat; EV: 0 - 255 per stat, 510 across all stats cumulatively (Wild Pokemon have none)
# Nature Modifier for health should always be just one and will be either 0.9,1 or 1.1 for all other stats
def calculateStat(base,level,IV,EV,isHP,natureModifier,stage = 1):
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
    print(move.damageClass)
    if move.damageClass == "Physical":
        damage = (((2 * attacker.level)//5 + 2) * move.power * attacker.actualStats[2]//defender.actualStats[1])//20 + 2
    elif move.damageClass == "Special":
        damage = (((2 * attacker.level)//5 + 2) * move.power * attacker.actualStats[4]//defender.actualStats[5])//20 + 2
    elif move.damageClass == "Status":
        damage = 0

    damageMultipliers = []
    appliedMultipliers = []

    # Typing related damage multipliers
    for i in range(2):

        if defender.types[i] in type_matching[move.typing][0]:
            damageMultipliers.append(2)
            appliedMultipliers.append("Supereffective")
        elif defender.types[i] in type_matching[move.typing][1]:
            damageMultipliers.append(0.5)
            appliedMultipliers.append("Ineffective")
        elif defender.types[i] in type_matching[move.typing][5]:
            damageMultipliers.append(0)
            appliedMultipliers.append("Nullified")

    # Randomly applies critical hits
    if random.randint(1,16) == 1:
        damageMultipliers.append(2)
        appliedMultipliers.append("Critical")
    else:
        print("Not Critical")

    for multiplier in damageMultipliers:
        damage *= multiplier

    print(appliedMultipliers)
    print(damage)

    return int(damage // 1),appliedMultipliers

