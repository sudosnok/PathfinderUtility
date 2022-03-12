from __future__ import annotations
from typing import Any, Literal, Optional, Callable, Union
import json

def _level_factory(levels: str) -> dict[str, int]:
    ret = {}
    for level in levels.split(', '):
        level = level.strip().capitalize()
        if level.count(' ') > 1:
            *cls, level = level.split(' ')
            cls = ' '.join(cls)
        else:

            cls, level = level.split(' ')
        if '/' not in cls:
            ret[cls.capitalize()] = int(level.strip(','))
        else:
            for classes in cls.split('/'):
                ret[classes.capitalize()] = int(level)
    return ret

def _domain_factory(domains: str) -> dict[str, int]:
    return domains

def _subdomain_factory(subdomains: str) -> dict[str, int]:
    return subdomains

def _mystery_factory(mysteries: str) -> dict[str, int]:
    return mysteries

def _bloodlines_factory(bloodlines: str) -> dict[str, int]:
    return bloodlines

class _BaseSpell:
    name: str
    levels: dict[str, int]
    school: str
    casting_time: str
    components: tuple[str]
    range: str
    target: Optional[str]
    effect: Optional[str]
    duration: str
    saving_throw: Optional[str]
    spell_resistance: Optional[str]
    description: str
    dispatch_route: dict[str, Callable[[str], Any]] = {
        'name':                 lambda name: name.title().rstrip(),
        'school':               lambda school: school.strip().capitalize(),
        'levels':               lambda levels: levels, #adjusted since levels are already dict
        'bloodlines':           lambda bloodlines: _bloodlines_factory(bloodlines),
        'domains':              lambda domains: _domain_factory(domains),
        'subdomains':           lambda subdomains: _subdomain_factory(subdomains),
        'mysteries':              lambda mysteries: _mystery_factory(mysteries),
        'casting_time':         lambda time: time.strip(),
        'components':           lambda comp: [item.strip() for item in comp.split(', ')],
        'range':                lambda _range: _range.strip().capitalize(),
        'area':                 lambda area: area.strip().capitalize(),
        'target':               lambda target: target.strip().capitalize(),
        'duration':             lambda duration: duration.strip().capitalize(),
        'saving_throw':         lambda throw: throw.strip().capitalize(),
        'spell_resistance':     lambda resistance: resistance.strip().capitalize(),
        'description':          lambda desc: desc.strip().capitalize(),
    }

    def __repr__(self) -> str:
        try:
            sort = sorted(self.levels, key=self.levels.get, reverse=True)
        except AttributeError:
            print(self.name)
        highest = f'{sort[0]} - {self.levels[sort[0]]}'
        lowest = f'{sort[-1]} - {self.levels[sort[-1]]}'
        return f'<{self.name}: School: {self.school}, Higest: {highest}, Lowest: {lowest}>'

    def __str__(self) -> str: return repr(self)

    @classmethod
    def _from_json(cls, **data) -> _BaseSpell:
        self = cls()
        for key, value in data.items():
            setattr(self, key, self.dispatch_route.get(key)(value))
        return self

def SpellFactory() -> list[_BaseSpell]:
    '''
    Returns a list of all Spell objects from the json file
    Use SpellFilter if you want to limit how many results you can see
    '''
    with open('./Pathfinder/spells/spells.json') as file:
        spells: list[dict[str, str]] = json.load(file)
    object_list = []
    for spell in spells:
        object_list.append(_BaseSpell._from_json(**spell))
    
    return object_list

def SpellFilter(**kwargs: dict[str, str | dict[str, int]]) -> list[_BaseSpell]:
    with open('./Pathfinder/spells/spells.json') as file:
        spells: list[dict[str, str]] = json.load(file)
    spell_list = []

    for key, value in kwargs.items():
        if isinstance(value, str):
            value = value.capitalize()
            f = filter(lambda s: value in s.get(key, ''), spells)
            spells = list(f)
        if isinstance(value, dict):
            value: dict[str, int]
            for i_key, i_value in value.items():
                f = filter(lambda s: s['levels'].get(i_key, float('inf')) <= i_value, spells)
                spells = list(f)
    for spell in spells:
        spell_list.append(_BaseSpell._from_json(**spell))
    return spell_list
