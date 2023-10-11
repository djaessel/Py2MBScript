# This Python file uses the following encoding: utf-8
import sys

sys.path.append("./converter/")
sys.path.append("./data_objects/")
sys.path.append("./test_cases/")

from ScriptConverter import ScriptConverter
from SimpleTriggerConverter import SimpleTriggerConverter
from TriggerConverter import TriggerConverter
from GameMenuConverter import GameMenuConverter
from ItemConverter import ItemConverter
from TroopConverter import TroopConverter
from SkillConverter import SkillConverter
from PresentationConverter import PresentationConverter
from PartyConverter import PartyConverter
from InfoPageConverter import InfoPageConverter
from StringConverter import StringConverter
from MusicConverter import MusicConverter


if __name__ == "__main__":
    # Module InfoPage
    infoPager = InfoPageConverter()
    infoPages = infoPager.retrieveInfoPages()
    infoPager.writeScriptOutputFile(infoPages)

    # Module Strings
    stringer = StringConverter()
    strings = stringer.retrieveStrings()
    stringer.writeScriptOutputFile(strings)

    # Module Music
    musicer = MusicConverter()
    music = musicer.retrieveTracks()
    musicer.writeScriptOutputFile(music)

    # Module Animations
    # Module Meshes
    # Module Sounds
    # Module Skins
    # Module Map Icons
    # Module Factions
    # Module Scenes
    # Module Particle System
    # Module Scene Props
    # Module Tableau Materials
    # Module Quests
    # Module Dialogs
    # Module PostFX

    # Module Scripts
    scripter = ScriptConverter()
    lines = scripter.readScriptTestCode()
    codeLines = scripter.transformScriptBlock(lines)
    scripter.writeScriptOutputFile(codeLines)

    # Module Simple Triggers
    simpleTriggerer = SimpleTriggerConverter()
    simpleTriggers = simpleTriggerer.retrieveTriggers()
    simpleTriggerer.writeScriptOutputFile(simpleTriggers)

    # Module Triggers
    triggerer = TriggerConverter()
    triggerers = triggerer.retrieveTriggers()
    triggerer.writeScriptOutputFile(triggerers)

    # Module Party Templates

    # Module Parties
    partier = PartyConverter()
    parties = partier.retrieveParties()
    partier.writeScriptOutputFile(parties)

    # Module Game Menus
    gameMenuer = GameMenuConverter()
    gameMenus = gameMenuer.retrieveGameMenus()
    gameMenuer.writeScriptOutputFile(gameMenus)

    # Module Skills
    skiller = SkillConverter()
    skills = skiller.retrieveSkills()
    skiller.writeScriptOutputFile(skills)

    # Module Items
    itemer = ItemConverter()
    items = itemer.retrieveItems()
    itemer.writeScriptOutputFile(items)

    # Module Troops
    trooper = TroopConverter()
    troops = trooper.retrieveTroops()
    trooper.writeScriptOutputFile(troops)

    # Module Mission Template

    # Module Presentations
    presenter = PresentationConverter()
    presentations = presenter.retrievePresentations()
    presenter.writeScriptOutputFile(presentations)

    sys.exit()

