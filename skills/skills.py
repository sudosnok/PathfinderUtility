class _BaseSkill:
    def __init__(self, name: str, total: int = 0, ability: int = 0, ranks: int = 0, misc: int = 0, temp: int = 0, *, ability_mod: str = None, extra: str = None) -> None:
        self.name = name
        self.total = total
        self.ability = ability
        self.ranks = ranks
        self.misc = misc
        self.temp = temp
        self.ability_mod = ability_mod
        self.extra = extra

    def __repr__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return repr(self)

class _StrengthSkill(_BaseSkill):
    def __init__(self, name, *args, **kwargs):
        super().__init__(name, *args, ability_mod='Strength', **kwargs)

class _DexteritySkill(_BaseSkill):
    def __init__(self, name, *args, **kwargs):
        super().__init__(name, *args, ability_mod='Dexterity', **kwargs)

class _ConstitutionSkill(_BaseSkill):
    def __init__(self, *args):
        super().__init__(*args, ability_mod='Constitution')

class _IntelligenceSkill(_BaseSkill):
    def __init__(self, name, *args, **kwargs):
        super().__init__(name, *args, ability_mod='Intelligence', **kwargs)

class _WisdomSkill(_BaseSkill):
    def __init__(self, name, *args, **kwargs):
        super().__init__(name, *args, ability_mod='Wisdom', **kwargs)

class _CharismaSkill(_BaseSkill):
    def __init__(self, name, *args, **kwargs):
        super().__init__(name, *args, ability_mod='Charisma', **kwargs)

class Acrobatics(_DexteritySkill):
    def __init__(self, *args):
        super().__init__('Acrobatics', *args)

class Appraise(_IntelligenceSkill):
    def __init__(self, *args):
        super().__init__('Appraise', *args)

class Bluff(_CharismaSkill):
    def __init__(self, *args):
        super().__init__('Bluff', *args)

class Climb(_StrengthSkill):
    def __init__(self, *args):
        super().__init__('Climb', *args)

class Craft(_IntelligenceSkill):
    def __init__(self, extra: str = 'None', *args):
        super().__init__('Craft', *args, extra=extra)

class Diplomacy(_CharismaSkill):
    def __init__(self, *args):
        super().__init__('Diplomacy', *args)

class Disable_Device(_DexteritySkill):
    def __init__(self, *args):
        super().__init__('Disable Device', *args)

class Disguise(_CharismaSkill):
    def __init__(self, *args):
        super().__init__('Disguise', *args)

class Escape_Artist(_DexteritySkill):
    def __init__(self, *args):
        super().__init__('Escape Artist', *args)

class Fly(_DexteritySkill):
    def __init__(self, *args):
        super().__init__('Fly', *args)

class Handle_Animal(_CharismaSkill):
    def __init__(self, *args):
        super().__init__('Handle Animal', *args)

class Heal(_WisdomSkill):
    def __init__(self, *args):
        super().__init__('Heal', *args)

class Intimidate(_CharismaSkill):
    def __init__(self, *args):
        super().__init__('Intimidate', *args)

class Knowledge_Arcana(_IntelligenceSkill):
    def __init__(self, *args):
        super().__init__('Knowledge Arcana', *args)

class Knowledge_Dungeoneering(_IntelligenceSkill):
    def __init__(self, *args):
        super().__init__('Knowledge Dungeoneering', *args)

class Knowledge_Engineering(_IntelligenceSkill):
    def __init__(self, *args):
        super().__init__('Knowledge Engineering', *args)

class Knowledge_Geography(_IntelligenceSkill):
    def __init__(self, *args):
        super().__init__('Knowledge Geography', *args)

class Knowledge_History(_IntelligenceSkill):
    def __init__(self, *args):
        super().__init__('Knowledge History', *args)

class Knowledge_Local(_IntelligenceSkill):
    def __init__(self, *args):
        super().__init__('Knowledge Local', *args)

class Knowledge_Nature(_IntelligenceSkill):
    def __init__(self, *args):
        super().__init__('Knowledge Nature', *args)

class Knowledge_Nobility(_IntelligenceSkill):
    def __init__(self, *args):
        super().__init__('Knowledge Nobility', *args)

class Knowledge_Planes(_IntelligenceSkill):
    def __init__(self, *args):
        super().__init__('Knowledge Planes', *args)

class Knowledge_Religion(_IntelligenceSkill):
    def __init__(self, *args):
        super().__init__('Knowledge Religion', *args)

Knowledge_All = [Knowledge_Arcana, Knowledge_Dungeoneering, Knowledge_Engineering, Knowledge_Geography, Knowledge_History, Knowledge_Local, Knowledge_Nature, Knowledge_Nobility, Knowledge_Planes, Knowledge_Religion]

class Linguistics(_IntelligenceSkill):
    def __init__(self, *args):
        super().__init__('Linguistics', *args)

class Perception(_WisdomSkill):
    def __init__(self, *args):
        super().__init__('Perception', *args)

class Perform(_CharismaSkill):
    def __init__(self, extra: str = 'None', *args):
        super().__init__('Perform', *args, extra=extra)

class Profession(_WisdomSkill):
    def __init__(self, extra: str = 'None', *args):
        super().__init__('Profession', *args, extra=extra)

class Ride(_DexteritySkill):
    def __init__(self, *args):
        super().__init__('Ride', *args)

class Sense_Motive(_WisdomSkill):
    def __init__(self, *args):
        super().__init__('Sense Motive', *args)

class Sleight_Of_Hand(_DexteritySkill):
    def __init__(self, *args):
        super().__init__('Sleight of Hand', *args)

class Spellcraft(_IntelligenceSkill):
    def __init__(self, *args):
        super().__init__('Spellcraft', *args)

class Stealth(_DexteritySkill):
    def __init__(self, *args):
        super().__init__('Stealth', *args)

class Survival(_WisdomSkill):
    def __init__(self, *args):
        super().__init__('Survival', *args)

class Swim(_StrengthSkill):
    def __init__(self, *args):
        super().__init__('Swim', *args)

class Use_Magic_Device(_CharismaSkill):
    def __init__(self, *args):
        super().__init__('Use Magic Device', *args)

ALL = [
    Acrobatics,
    Appraise,
    Bluff,
    Climb,
    Craft,
    Diplomacy,
    Disguise,
    Disable_Device,
    Escape_Artist,
    Fly,
    Intimidate,
    Handle_Animal,
    Heal,
    *Knowledge_All,
    Linguistics,
    Perception,
    Perform,
    Profession,
    Ride,
    Sense_Motive,
    Sleight_Of_Hand,
    Spellcraft,
    Stealth,
    Survival,
    Swim,
    Use_Magic_Device
]