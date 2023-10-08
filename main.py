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


if __name__ == "__main__":

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

    # Module Presentations
    presenter = PresentationConverter()
    presentations = presenter.retrievePresentations()
    presenter.writeScriptOutputFile(presentations)

    sys.exit()

