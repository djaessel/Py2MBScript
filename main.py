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
from MeshConverter import MeshConverter
from SoundConverter import SoundConverter
from FactionConverter import FactionConverter
from SceneConverter import SceneConverter
from MapIconConverter import MapIconConverter
from ParticleSystemConverter import ParticleSystemConverter
from TableauMaterialConverter import TableauMaterialConverter
from QuestConverter import QuestConverter
from PostFXConverter import PostFXConverter
from PartyTemplateConverter import PartyTemplateConverter
from MissionTemplateConverter import MissionTemplateConverter
from AnimationConverter import AnimationConverter


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

    # Module Meshes
    mesher = MeshConverter()
    meshes = mesher.retrieveMeshes()
    mesher.writeScriptOutputFile(meshes)

    # Module Sounds
    sounder = SoundConverter()
    sounds = sounder.retrieveSounds()
    sounder.writeScriptOutputFile(sounds)

    # Module Factions
    factioner = FactionConverter()
    factions = factioner.retrieveFactions()
    factioner.writeScriptOutputFile(factions)

    # Module Scenes
    scener = SceneConverter()
    scenes = scener.retrieveScenes()
    scener.writeScriptOutputFile(scenes)

    # Module Particle System
    psyser = ParticleSystemConverter()
    psys = psyser.retrieveParticleSystems()
    psyser.writeScriptOutputFile(psys)

    # Module Skins

    # Module Animations
    animator = AnimationConverter()
    anims = animator.retrieveAnimations()
    animator.writeScriptOutputFile(anims)

    # Module PostFX
    postfxer = PostFXConverter()
    postfx = postfxer.retrievePostFX()
    postfxer.writeScriptOutputFile(postfx)

    # Module Quests
    quester = QuestConverter()
    quests = quester.retrieveQuests()
    quester.writeScriptOutputFile(quests)

    # Module Tableau Materials
    tabMater = TableauMaterialConverter()
    tabMats = tabMater.retrieveTableauMaterials()
    tabMater.writeScriptOutputFile(tabMats)

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

    # Module Map Icons
    mapIconer = MapIconConverter()
    mapIcons = mapIconer.retrieveMapIcons()
    mapIconer.writeScriptOutputFile(mapIcons)

    # Module Party Templates
    partierTemp = PartyTemplateConverter()
    partyTemps = partierTemp.retrievePartyTemplates()
    partierTemp.writeScriptOutputFile(partyTemps)

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
    missioner = MissionTemplateConverter()
    missionTemps = missioner.retrieveMissionTemplates()
    missioner.writeScriptOutputFile(missionTemps)

    # Module Dialogs

    # Module Scene Props

    # Module Presentations
    presenter = PresentationConverter()
    presentations = presenter.retrievePresentations()
    presenter.writeScriptOutputFile(presentations)

    sys.exit()

