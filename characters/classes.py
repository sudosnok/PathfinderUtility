from typing import Optional

from utils import Alignment, Dice
from skills import *

ProgressionTH   = dict[int, tuple[tuple[int], int, int, int]]
ClassSkillsTH   = list[type[_BaseSkill]]
SpellsTH        = dict[int, tuple[int, ...]]

class _BaseClass:
    LVL: int                        = 0
    BAB: tuple[int]                 = 1
    FORT: int                       = 0
    REF: int                        = 0
    WILL: int                       = 0
    HitDie: Dice                    = Dice.d4()

    alignment_range: Alignment      = Alignment('TN')
    class_skills: ClassSkillsTH     = []
    _skills: list[_BaseSkill]       = ALL
    skill_ranks: int                = 1
    progression: ProgressionTH      = {}

    spellcaster_type: Optional[str] = None
    _spells_known: SpellsTH         = {}
    spells_known: dict[int, int]    = {}
    _spells_perday: SpellsTH        = {}
    spells_perday: dict[int, int]   = {}
    _spell_list: list               = []

    def resolve_stats(self, level: int = 1):
        self.LVL = level
        self.BAB, self.FORT, self.REF, self.WILL = self.progression[level]
        self.skills = [inst() for inst in self._skills]
        if self.spellcaster_type is not None:
            self.spells_perday  = self._spells_perday[level]
            self.spells_known   = self._spells_known[level]

class Barbarian(_BaseClass):
    progression: ProgressionTH = {
        1:  ((1,), 2, 0, 0,),
        2:  ((2,), 3, 0, 0,),
        3:  ((3,), 3, 1, 1,),
        4:  ((4,), 4, 1, 1,),
        5:  ((5,), 4, 1, 1,),
        6:  ((6, 1), 5, 2, 2,),
        7:  ((7, 2), 5, 2, 2,),
        8:  ((8, 3), 6, 2, 2,),
        9:  ((9, 4), 6, 3, 3,),
        10: ((10, 5), 7, 3, 3,),
        11: ((11, 6, 1), 7, 3, 3,),
        12: ((12, 7, 2), 8, 4, 4,),
        13: ((13, 8, 3), 8, 4, 4,),
        14: ((14, 9, 4), 9, 4, 4,),
        15: ((15, 10, 5), 9, 5, 5,),
        16: ((16, 11, 6, 1), 10, 5, 5,),
        17: ((17, 12, 7, 2), 10, 5, 5,),
        18: ((18, 13, 8, 3), 11, 6, 6,),
        19: ((19, 14, 9, 4), 11, 6, 6,),
        20: ((20, 15, 10, 5), 12, 6, 6,),
    }
    def __init__(self, LVL: int = 1, alignment: str = 'TN') -> None:
        self.resolve_stats(LVL)
        self.class_skills = [
            Acrobatics, Climb, Craft, Handle_Animal, Intimidate, Knowledge_Nature, Perception, Ride, Survival, Swim,
        ]
        self.skill_ranks = 4 * self.LVL

class Bard(_BaseClass):
    progression: ProgressionTH = {
        1: ((0,), 0, 2, 2),
        2: ((1,), 0, 3, 3),
        3: ((2,), 1, 3, 3),
        4: ((3,), 1, 4, 4),
        5: ((3,), 1, 4, 4),
        6: ((4,), 2, 5, 5),
        7: ((5,), 2, 5, 5),
        8: ((6, 1), 2, 6, 6),
        9: ((6, 1), 3, 6, 6),
        10: ((7, 2), 3, 7, 7),
        11: ((8, 3), 3, 7, 7),
        12: ((9, 4), 4, 8, 8),
        13: ((9, 4), 4, 8, 8),
        14: ((10, 5), 4, 9, 9),
        15: ((11, 6, 1), 5, 9, 9),
        16: ((12, 7, 2), 5, 10, 10),
        17: ((12, 7, 2), 5, 10, 10),
        18: ((13, 8, 3), 6, 11, 11),
        19: ((14, 9, 4), 6, 11, 11),
        20: ((15, 10, 5), 6, 12, 12),
    }
    _spells_perday: SpellsTH = {
        1:  (float('inf'), 1),
        2:  (float('inf'), 2),
        3:  (float('inf'), 3),
        4:  (float('inf'), 3, 1),
        5:  (float('inf'), 4, 2),
        6:  (float('inf'), 4, 3),
        7:  (float('inf'), 4, 3, 1),
        8:  (float('inf'), 4, 4, 2),
        9:  (float('inf'), 5, 4, 3),
        10: (float('inf'), 5, 4, 3, 1),
        11: (float('inf'), 5, 4, 4, 2),
        12: (float('inf'), 5, 5, 4, 3),
        13: (float('inf'), 5, 5, 4, 3, 1),
        14: (float('inf'), 5, 5, 4, 4, 2),
        15: (float('inf'), 5, 5, 5, 4, 3),
        16: (float('inf'), 5, 5, 5, 4, 3, 1),
        17: (float('inf'), 5, 5, 5, 4, 4, 2),
        18: (float('inf'), 5, 5, 5, 5, 4, 3),
        19: (float('inf'), 5, 5, 5, 5, 5, 4),
        20: (float('inf'), 5, 5, 5, 5, 5, 5),
    }
    _spells_known: SpellsTH = {
        1:  (4, 2),
        2:  (5, 3),
        3:  (6, 4),
        4:  (6, 4, 2),
        5:  (6, 4, 3),
        6:  (6, 4, 4),
        7:  (6, 5, 4, 2),
        8:  (6, 5, 4, 3),
        9:  (6, 5, 4, 4),
        10: (6, 5, 5, 4, 2),
        11: (6, 6, 5, 4, 3),
        12: (6, 6, 5, 4, 4),
        13: (6, 6, 5, 5, 4, 2),
        14: (6, 6, 6, 5, 4, 3),
        15: (6, 6, 6, 5, 4, 4),
        16: (6, 6, 6, 5, 5, 4, 2),
        17: (6, 6, 6, 6, 5, 4, 3),
        18: (6, 6, 6, 6, 5, 4, 4),
        19: (6, 6, 6, 6, 5, 5, 4),
        20: (6, 6, 6, 6, 6, 5, 5),
    }
    def __init__(self, LVL: int = 1, alignment: str = 'TN') -> None:
        self.resolve_stats(LVL)
        self.class_skills = [
            Acrobatics, Appraise, Bluff, Climb, Craft, Diplomacy, Disguise, Escape_Artist, Intimidate, *Knowledge_All, Linguistics, Perception, Perform, Profession, Sense_Motive, Sleight_Of_Hand, Spellcraft, Stealth, Use_Magic_Device
        ]


