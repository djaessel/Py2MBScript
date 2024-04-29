# Converting: use_item
var1 = store_script_param(1)
var2 = store_script_param(2)
if game_in_multiplayer_mode:
	var3 = prop_instance_get_scene_prop_kind(var1)
	eq(":var3",1080863910568919844)
	this_or_next|gt,":var4",0;
	neg|multiplayer_is_dedicated_server;
	var4 = multiplayer_get_my_player()
	ge(":var4",0)
	var5 = player_get_agent_id(var4)
	ge(":var5",0)
	agent_is_active(":var5")
	var6 = agent_get_team(var5)
	eq(":var6",0)
	var7 = scene_prop_get_slot(var1,1)
	ge(":var2",0)
	agent_is_active(":var2")
	var8 = agent_get_player_id(var2)
	s7 = str_store_player_username(var8)
	if var7 == 0:
		display_message(1585267068834414691)
	else:
		display_message(1585267068834414692)
	#end
#end
var3 = prop_instance_get_scene_prop_kind(var1)
if var3 == 1080863910568919844 or var3 == 1080863910568919843:
	var9 = 1080863910568919754
elif var3 == 1080863910568919198 or var3 == 1080863910568919994 or var3 == 1080863910568919654 or var3 == 1080863910568919244 or var3 == 1080863910568919986 or var3 == 1080863910568919987 or var3 == 1080863910568919993 or var3 == 1080863910568919992 or var3 == 1080863910568919242 or var3 == 1080863910568919749 or var3 == 1080863910568919750 or var3 == 1080863910568919751 or var3 == 1080863910568919752 or var3 == 1080863910568919753:
	var9 = var3
#end
var10 = -1
s0 = prop_instance_get_position(var1)
var11 = scene_prop_get_num_instances(var9)
for;":var12";0;":var11"
var11 = scene_prop_get_num_instances(var9)
var13 = scene_prop_get_instance(var9,var12)
s1 = prop_instance_get_position(var13)
this_or_next|eq,":var10",-1;
neg|ge,":var14",":var10";
var14 = get_sq_distance_between_positions(0,1)
var10 = var14
var15 = var13
#end
if var9 == 1080863910568919754:
	var7 = scene_prop_get_slot(var1,1)
	if var7 == 0:
		scene_prop_enable_after_time(":var1",400)
		if multiplayer_is_server or neg|game_in_multiplayer_mode:
			s0 = prop_instance_get_position(var15)
			position_move_z(0,375)
			prop_instance_animate_to_position(":var15",0,400)
		#end
		scene_prop_set_slot(":var1",1,1)
		if var3 == 1080863910568919844 and multiplayer_is_server or neg|game_in_multiplayer_mode:
			s1 = prop_instance_get_position(var1)
			prop_instance_rotate_to_position(":var1",1,400,72000)
		#end
	else:
		scene_prop_enable_after_time(":var1",400)
		if multiplayer_is_server or neg|game_in_multiplayer_mode:
			s0 = prop_instance_get_position(var15)
			position_move_z(0,-375)
			prop_instance_animate_to_position(":var15",0,400)
		#end
		scene_prop_set_slot(":var1",1,0)
		if var3 == 1080863910568919844 and multiplayer_is_server or neg|game_in_multiplayer_mode:
			s1 = prop_instance_get_position(var1)
			prop_instance_rotate_to_position(":var1",1,400,-72000)
		#end
	#end
	if var9 == 1080863910568919749:
		var16 = 120
		var17 = 240
	elif var9 == 1080863910568919750:
		var16 = 140
		var17 = 280
	elif var9 == 1080863910568919751:
		var16 = 160
		var17 = 320
	elif var9 == 1080863910568919752:
		var16 = 190
		var17 = 360
	elif var9 == 1080863910568919753:
		var16 = 230
		var17 = 400
	#end
	var7 = scene_prop_get_slot(var1,1)
	scene_prop_enable_after_time(":var15",":var17")
	eq(":var7",0)
	s0 = prop_instance_get_starting_position(var15)
	prop_instance_enable_physics(":var15",0)
	prop_instance_animate_to_position(":var15",0,300)
	scene_prop_set_slot(":var15",1,1)
else:
	scene_prop_enable_after_time(":var15",":var16")
	s0 = prop_instance_get_position(var1)
	var10 = -1
	for;":var18";100;110
	var10 = -1
	s1 = entry_point_get_position(var18)
	this_or_next|eq,":var10",-1;
	neg|ge,":var14",":var10";
	var14 = get_sq_distance_between_positions(0,1)
	var10 = var14
	var19 = var18
#end
if ge,":var10",0 and neg|ge,":var10",22500:
	s1 = entry_point_get_position(var19)
	position_rotate_x(1,-90)
	scene_prop_set_slot(":var15",2,0)
	prop_instance_enable_physics(":var15",0)
	prop_instance_animate_to_position(":var15",1,130)
#end
scene_prop_set_slot(":var15",1,0)
#end
elif var9 == 1080863910568919198 or var9 == 1080863910568919994 or var3 == 1080863910568919654 or var3 == 1080863910568919244 or var3 == 1080863910568919986 or var3 == 1080863910568919987 or var3 == 1080863910568919993 or var3 == 1080863910568919992 or var3 == 1080863910568919242:
	var15 = var1
	var7 = scene_prop_get_slot(var15,1)
	if var7 == 0:
		s0 = prop_instance_get_starting_position(var15)
		scene_prop_enable_after_time(":var15",100)
		if neg|eq,":var3",1080863910568919993 and neg|eq,":var3",1080863910568919986:
			position_rotate_z(0,-85)
		else:
			position_rotate_z(0,85)
		#end
		prop_instance_animate_to_position(":var15",0,100)
		scene_prop_set_slot(":var15",1,1)
	else:
		s0 = prop_instance_get_starting_position(var15)
		scene_prop_enable_after_time(":var15",100)
		prop_instance_animate_to_position(":var15",0,100)
		scene_prop_set_slot(":var15",1,0)
	#end
#end
#end

