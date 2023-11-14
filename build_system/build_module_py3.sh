#!/bin/bash

python3 -B "./process_init.py"
python3 -B "./process_global_variables.py"
python3 -B "./process_strings.py"
python3 -B "./process_skills.py"
python3 -B "./process_music.py"
python3 -B "./process_animations.py"
python3 -B "./process_meshes.py"
python3 -B "./process_sounds.py"
python3 -B "./process_skins.py"
python3 -B "./process_map_icons.py"
python3 -B "./process_factions.py"
python3 -B "./process_items.py"
python3 -B "./process_scenes.py"
python3 -B "./process_troops.py"
python3 -B "./process_particle_sys.py"
python3 -B "./process_scene_props.py"
python3 -B "./process_tableau_materials.py"
python3 -B "./process_presentations.py"
python3 -B "./process_party_tmps.py"
python3 -B "./process_parties.py"
python3 -B "./process_quests.py"
python3 -B "./process_info_pages.py"
python3 -B "./process_scripts.py"
python3 -B "./process_mission_tmps.py"
python3 -B "./process_game_menus.py"
python3 -B "./process_simple_triggers.py"
python3 -B "./process_dialogs.py"
python3 -B "./process_global_variables_unused.py"
python3 -B "./process_postfx.py"

python3 -B "./process_module_ini.py"

python3 -B "./process_languages.py"

#rm *.pyc

echo ""
echo "______________________________"
echo ""
echo "Script processing has ended."
#echo "Press any key to exit . . ."
echo

