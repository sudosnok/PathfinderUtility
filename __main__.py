from . import SpellFilter, Feat, FeatFilter, NamedFeatFilter

class_list = [
            'Alchemist',
            'Barbarian',
            'Bard',
            'Cavalier',
            'Cleric',
            'Druid',
            'Fighter',
            'Gunslinger',
            'Inquisitor',
            'Magus',
            'Monk',
            'Omdura',
            'Oracle',
            'Paladin',
            'Ranger',
            'Shifter',
            'Sorcerer',
            'Summoner',
            'Vigilante',
            'Witch',
            'Wizard'
        ]
skill_list = [
            'Acrobatics',
            'Appraise',
            'Bluff',
            'Climb',
            'Craft',
            'Diplomacy',
            'Disable Device',
            'Disguise',
            'Escape Artist',
            'Fly',
            'Handle Animal',
            'Heal',
            'Intimidate',
            'Knowledge (Arcana)',
            'Knowledge (Dungeoneering)',
            'Knowledge (Engineering)',
            'Knowledge (Geography)',
            'Knowledge (History)',
            'Knowledge (Local)',
            'Knowledge (Nature)',
            'Knowledge (Nobiliy)',
            'Knowledge (Planes)',
            'Knowledge (Religion)',
            'Linguistics',
            'Perception',
            'Perform',
            'Profession',
            'Ride',
            'Sense Motive',
            'Sleight of Hand',
            'Spellcraft',
            'Stealth',
            'Survival',
            'Swim',
            'Use Magic Device',
        ]
school_list = [
            'Abjuration',
            'Conjuration',
            'Divination',
            'Enchantment',
            'Evocation',
            'Illusion',
            'Necromancy',
            'Transmutation',
            'Universalist'
        ]

import json
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import *

class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.spells: list = []
        self.feats: list = []
        self.spells_loaded: bool = False
        self.feats_loaded: bool = False

        uic.loadUi('test.ui', self)

        #=== Spells page ===#
        self.s_school_combo: QComboBox = self.findChild(QComboBox, 'spell_school_comboBox')
        self.s_school_combo.addItems(school_list)

        self.s_class_combo: QComboBox = self.findChild(QComboBox, 'spell_class_comboBox')
        self.s_class_combo.addItems(class_list)

        self.s_class_spin: QSpinBox = self.findChild(QSpinBox, 'spell_class_spinBox')

        self.s_search_button: QPushButton = self.findChild(QPushButton, 'spell_search_button')
        self.s_search_button.clicked.connect(self.s_search_clicked)

        self.s_clear_button: QPushButton = self.findChild(QPushButton, 'spell_clear_button')
        self.s_clear_button.clicked.connect(self.s_clear_clicked)

        self.s_results: QTreeWidget = self.findChild(QTreeWidget, 'spell_results_box')

        self.s_description_label: QLabel = self.findChild(QLabel, 'spell_description_label')
        #=== End of spells page ===#
        #=== Feats page ===#

        #== Top left ==#
        self.f_char_lvl: QSpinBox       = self.findChild(QSpinBox, 'char_lvl_spinbox')
        self.f_caster_lvl: QSpinBox     = self.findChild(QSpinBox, 'caster_lvl_spinbox')
        self.f_bab: QSpinBox            = self.findChild(QSpinBox, 'bab_spinbox')
        self.f_type_general: QCheckBox  = self.findChild(QCheckBox, 'feat_type_general_checkbox')
        self.f_type_combat: QCheckBox   = self.findChild(QCheckBox, 'feat_type_combat_checkbox')

        #== Top middle ==#
        self.f_skill_combo: QComboBox = self.findChild(QComboBox, 'skill_combobox')
        self.f_skill_combo.addItems(skill_list)
        self.f_skill_lvl: QSpinBox    = self.findChild(QSpinBox, 'skill_lvl_spinbox')
        self.f_filter_apply: QPushButton  = self.findChild(QPushButton, 'filter_apply_button')
        self.f_filter_remove: QPushButton = self.findChild(QPushButton, 'filter_remove_button')
        self.f_skill_filters: QListWidget = self.findChild(QListWidget, 'skill_filters_listwidget')

        self.f_filter_apply.clicked.connect(self.f_filter_apply_clicked)
        self.f_filter_remove.clicked.connect(self.f_filter_remove_clicked)

        #== Top right ==#
        self.feat_search: QPushButton   = self.findChild(QPushButton, 'feat_search_button')
        self.feat_clear: QPushButton    = self.findChild(QPushButton, 'feat_clear_button')
        self.feat_search.clicked.connect(self.f_search_clicked)
        self.feat_clear.clicked.connect(self.f_full_clear)

        self.str_spin: QSpinBox = self.findChild(QSpinBox, 'str_spinbox')
        self.dex_spin: QSpinBox = self.findChild(QSpinBox, 'dex_spinbox')
        self.con_spin: QSpinBox = self.findChild(QSpinBox, 'con_spinbox')
        self.wis_spin: QSpinBox = self.findChild(QSpinBox, 'wis_spinbox')
        self.int_spin: QSpinBox = self.findChild(QSpinBox, 'int_spinbox')
        self.cha_spin: QSpinBox = self.findChild(QSpinBox, 'cha_spinbox')

        #== Dead centre ==#
        self.feat_results: QTreeWidget  = self.findChild(QTreeWidget, 'feat_results_tree')
        self.feat_results.clicked.connect(self.on_feat_selection_changed)

        #== Bottom displays ==#
        self.f_str: QLabel = self.findChild(QLabel, 'feat_str_label')
        self.f_str.setText('0')
        self.f_dex: QLabel = self.findChild(QLabel, 'feat_dex_label')
        self.f_dex.setText('0')
        self.f_con: QLabel = self.findChild(QLabel, 'feat_con_label')
        self.f_con.setText('0')
        self.f_wis: QLabel = self.findChild(QLabel, 'feat_wis_label')
        self.f_wis.setText('0')
        self.f_int: QLabel = self.findChild(QLabel, 'feat_int_label')
        self.f_int.setText('0')
        self.f_cha: QLabel = self.findChild(QLabel, 'feat_cha_label')
        self.f_cha.setText('0')
        self.f_bab_label: QLabel = self.findChild(QLabel, 'feat_bab_label')
        self.f_bab_label.setText('0')
        self.f_caster: QLabel       = self.findChild(QLabel, 'feat_caster_lvl_label')
        self.f_character: QLabel    = self.findChild(QLabel, 'feat_character_lvl_label')
        self.f_misc: QTextEdit      = self.findChild(QTextEdit, 'feat_misc_label')
        self.f_name: QLabel         = self.findChild(QLabel, 'feat_name_label')
        self.f_link: QTextEdit      = self.findChild(QTextEdit, 'feat_link_label')
        self.f_desc: QTextEdit      = self.findChild(QTextEdit, 'feat_desc_label')
        self.f_benefit: QTextEdit   = self.findChild(QTextEdit, 'feat_benefit_label')
        #=== End of feats page ===#



        self.show()

    def s_load_file(self):
        if not self.spells_loaded:
            with open('./Pathfinder/spells/spells.json') as f:
                self.spells = json.load(f)
            self.spells_loaded = True
    
    def f_load_file(self):
        if not self.feats_loaded:
            with open('./Pathfinder/feats/aonfeats.json') as f:
                data = json.load(f)
            self.feats = [Feat._from_dict(**item) for item in data]
            self.feats_loaded = True

    def f_filter_apply_clicked(self):
        skill = self.f_skill_combo.currentText()
        level = int(self.f_skill_lvl.text())
        item = QListWidgetItem(f'{skill} : {level}')
        if (matches := self.f_skill_filters.findItems(f'{skill} : ', QtCore.Qt.MatchContains)):
            # if a filter for a skill already exists
            for match in matches:
                if int(match.text().split(' : ')[1]) < level:
                    # if a filter has a lower level, edit it to match
                    match.setText(f'{skill} : {level}')
        else:
            self.f_skill_filters.addItem(item)

    def f_filter_remove_clicked(self):
        self.f_skill_filters.takeItem(self.f_skill_filters.currentRow())

    def f_search_clicked(self):
        self.f_load_file()
        char_lvl = int(self.f_char_lvl.text())
        cast_lvl = int(self.f_caster_lvl.text())
        bab = int(self.f_bab.text())

        filters: dict[str, int] = {}
        for _ in range(self.f_skill_filters.count()):
            item = self.f_skill_filters.takeItem(0)
            skill, level = item.text().split(' : ')
            level = int(level)
            #print(skill, level)
            filters[skill] = level
        
        ability_scores = {
            'Str': int(self.str_spin.text()),
            'Dex': int(self.dex_spin.text()),
            'Con': int(self.con_spin.text()),
            'Wis': int(self.wis_spin.text()),
            'Int': int(self.int_spin.text()),
            'Cha': int(self.cha_spin.text()),
        }

        filters |= {k: v for k, v in ability_scores.items() if v != 0}

        if char_lvl != 0:
            filters |= {'character_level': char_lvl}
        if cast_lvl != 0:
            filters |= {'caster_level': cast_lvl}
        if bab != 0:
            filters |= {'bab': bab}

        filtered = FeatFilter(self.feats, **filters)
        print(len(filtered), self.feat_results)
        for feat in filtered:
            self.feat_results.addTopLevelItem(QTreeWidgetItem([feat.name]))

    def on_feat_selection_changed(self, args: QtCore.QModelIndex):
        self.f_clear_clicked()

        item = self.feat_results.itemFromIndex(args)
        name = item.text(0)
        feat = NamedFeatFilter(self.feats, name=name)

        for ability, score in feat.ability_scores.items():
            if score != 0:
                getattr(self, f'f_{ability.lower()}').setText(str(score))

        misc = ''
        for skill, score in feat.skill_ranks.items():
            if score != 0:
                misc += f'\n{skill}: {score}\n'

        misc += '\n'.join(feat.prereq)

        name = feat.name.replace('-S-', "'s ")

        self.f_name.setText(name.title())
        self.f_link.setText(feat.link)
        self.f_desc.setText(feat.desc)
        self.f_misc.setText(misc)
        self.f_benefit.setText(feat.benefit)
        self.f_bab_label.setText(str(feat.bab))



    def f_clear_clicked(self):
        self.f_name.clear()
        self.f_link.clear()
        self.f_desc.clear()
        self.f_benefit.clear()
        self.f_misc.clear()
        self.f_str.clear()
        self.f_dex.clear()
        self.f_con.clear()
        self.f_wis.clear()
        self.f_int.clear()
        self.f_cha.clear()
        self.f_bab_label.clear()

    def f_full_clear(self):
        self.feat_results.clear()
        self.f_clear_clicked()

    def s_search_clicked(self):
        school = self.s_school_combo.currentText()
        level = {self.s_class_combo.currentText(): int(self.s_class_spin.text())}
        
        self.s_load_file()
        spell_list = SpellFilter(school=school, levels={**level})

        for item in spell_list:
            top = QTreeWidgetItem([item.name])

            school = QTreeWidgetItem(['School', item.school])

            levels = QTreeWidgetItem(['Levels'])
            for k, v in item.levels.items():
                levels.addChild(QTreeWidgetItem([k, str(v)]))

            description = QTreeWidgetItem(['Description', item.description])

            top.addChildren([school, levels, description])
            self.s_results.addTopLevelItem(top)
        self.s_results.itemClicked.connect(self.onItemClicked)

        #self.results.addItems([repr(item) for item in s])
    
    @QtCore.pyqtSlot(QTreeWidgetItem, int)
    def onItemClicked(self, item: QTreeWidgetItem, column: int):
        if item.childCount() == 3:
            try:
                desc = item.child(2).text(1)
                self.s_description_label.setText(desc)
            except AttributeError:
                print('AttributeError from listener')
        else:
            print(item.childCount(), column)

    def s_clear_clicked(self):
        self.s_results.clear()

#TODO: Cure light/moderate/serious etc is fucked since theres `x, mass` versions of them
#TODO: add a tab for feats at some point


def main_foo():
    app = QApplication([])
    UIWindow = UI()
    app.exec()
    


if __name__ == '__main__':
    main_foo()
    #print(help(QTreeWidget.addTopLevelItem))