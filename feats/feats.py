import json
import re

char_level_filter       = re.compile(r'(?:Character Level )(?P<char_level>\d)(?:th)')
caster_lvl_filter       = re.compile(r'(?:Caster Level )(?P<caster_lvl>\d)(?:th)')
old_skill_rank_filter   = re.compile(r'(?P<skill>[\S\(\)]+) (?P<skill_level>\d?)(?: Rank[s]?)')
skill_rank_filter       = re.compile(r'(?P<skill>[\S \(\)]+) (?P<skill_level>\d?)(?: rank[s]?)')
ability_score_filter    = re.compile(r'(?P<ability>\S+) (?P<score>\d+)$')
bab_filter              = re.compile(r'(?:Base Attack Bonus \+)(?P<bab>\d+)\.?')



class Feat:
    def __init__(self, name, desc, types, prereq, benefit, special, link):
        self.name: str = name
        self.desc: str = desc
        self.types: list[str] = types
        self.character_level: int = 0
        self.caster_level: int = 0
        self.bab: int = 0
        self.ability_scores: dict[str, int] = {'Str': 0, 'Dex': 0, 'Con': 0, 'Int': 0, 'Wis': 0, 'Cha': 0}
        self.skill_ranks: dict[str, int] = {
            'Acrobatics': 0,
            'Appraise': 0,
            'Bluff': 0,
            'Climb': 0,
            'Craft': 0,
            'Diplomacy': 0,
            'Disable Device': 0,
            'Disguise': 0,
            'Escape Artist': 0,
            'Fly': 0,
            'Handle Animal': 0,
            'Heal': 0,
            'Intimidate': 0,
            'Knowledge (Arcana)': 0,
            'Knowledge (Dungeoneering)': 0,
            'Knowledge (Engineering)': 0,
            'Knowledge (Geography)': 0,
            'Knowledge (History)': 0,
            'Knowledge (Local)': 0,
            'Knowledge (Nature)': 0,
            'Knowledge (Nobiliy)': 0,
            'Knowledge (Planes)': 0,
            'Knowledge (Religion)': 0,
            'Linguistics': 0,
            'Perception': 0,
            'Perform': 0,
            'Profession': 0,
            'Ride': 0,
            'Sense Motive': 0,
            'Sleight of Hand': 0,
            'Spellcraft': 0,
            'Stealth': 0,
            'Survival': 0,
            'Swim': 0,
            'Use Magic Device': 0,
        }
        self.benefit: str = benefit
        self.special: str = special
        self.link: str = link
        self.prereq: dict[str, str] = self._prereq_factory(prereq)

    @classmethod
    def _from_dict(cls, **kwargs):
        name = kwargs.get('name')
        desc = kwargs.get('desc')
        types = kwargs.get('types')
        prereq = kwargs.get('prereq')
        benefit = kwargs.get('benefit')
        special = kwargs.get('special')
        link = kwargs.get('link')
        self = cls(name, desc, types, prereq, benefit, special, link)
        return self
    
    def _prereq_factory(self, prereqs: list[str]) -> list[str]:
        ret: list[str] = []
        for prereq in prereqs:
            if char_match := char_level_filter.match(prereq):
                self.character_level = int(char_match.groupdict().get('char_level'))

            elif caster_match := caster_lvl_filter.match(prereq):
                self.caster_level = int(caster_match.groupdict().get('caster_lvl'))

            elif skill_match := skill_rank_filter.match(prereq):
                self.skill_ranks[skill_match.groupdict().get('skill')] = int(skill_match.groupdict().get('skill_level'))

            elif ability_match := ability_score_filter.match(prereq):
                self.ability_scores[ability_match.groupdict().get('ability')] = int(ability_match.groupdict().get('score'))
            
            elif bab_match := bab_filter.match(prereq):
                self.bab = int(bab_match.groupdict().get('bab'))

            else:
                ret.append(prereq)

        return ret

def FeatFactory() -> list[Feat]:
    with open('./Pathfinder/feats/aonfeats.json') as f:
        data = json.load(f)
    ret = [Feat._from_dict(**feat) for feat in data]
    return ret

def FeatFilter(supp_feats: list[Feat] | None = None, **kwargs: dict[str, str | list[str]]) -> list[Feat]:
    feats = supp_feats or FeatFactory()

    ret: list[Feat] = []
    print(kwargs)


    for feat in feats:
        for key, value in kwargs.items(): # key, value are character's scores, userinput
            target = feat.skill_ranks.get(key)
            if target and 0 < target <= value:
                ret.append(feat)
            target = feat.ability_scores.get(key)
            if target and 0 < target < value:
                ret.append(feat)
            if key == "character_level" and 0 < feat.character_level <= value :
                ret.append(feat)
            if key == 'caster_level' and 0 < feat.caster_level <= value:
                ret.append(feat)
            if key == 'bab' and 0 < feat.bab <= value:
                ret.append(feat)

    return ret

def NamedFeatFilter(supp_feats: list[Feat] | None = None, *, name: str = None) -> Feat:
    feats = supp_feats or FeatFactory()
    print(len(feats))
    import difflib
    print(difflib.get_close_matches(name, [item.name for item in feats]))
    return [item for item in feats if item.name.lower() == name.lower()][0]
