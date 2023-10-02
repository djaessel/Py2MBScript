# This Python file uses the following encoding: utf-8


class MBParty:
    id = ""
    name = ""
    extra_text = ""
    current_town = ""
    template_id = ""
    active = True
    slots = []
    members = []
    companions = []
    prisoners = []
    flags = 0x000000
    marshall = ""
    leader = ""
    leaders = []
    aggressiveness = 0
    courage = 100
    faction = 3
    extra_icon = ""
    icon = ""


    def __init__(self, id):
        self.id = id


        def can_join_party(self, host_party_id, flit_prisoners=False): # party_id_2
            return True

        def end_battle(self):
            print("Party", self.id, "end battle")

        def is_in_town(self, town_id): # party_id_2
            return self.current_town == town_id

        def is_in_any_town(self):
            return self.current_town != ""

        def is_active(self):
            return self.active


        def set_slot(self, slot_no, value):
            self.slots[slot_no] = value

        def get_slot(self, slot_no):
            return self.slots[slot_no]

        def slot_eq(self, slot_no, value):
            return self.slots[slot_no] == value

        def slot_ge(self, slot_no, value):
            return self.slots[slot_no] >= value


        def set_note_available(self, value : bool):
            print("Set note available", value)

        def get_num_companions(self):
            return self.companions.length

        def get_num_prisoners(self):
            return self.prisoners.length

        def set_flags(self, flag, clear_or_set : bool):
            pass

        def set_marshall(self, value):
            self.marshall = value

        def set_extra_text(self, text):
            self.extra_text = text

        def set_aggressiveness(self, number):
            self.aggressiveness = number

        def set_courage(self, number):
            self.courage = number

        def get_current_terrain(self):
            print("Return party current terrain")
            return "0x12345678901234567890"

        def get_template_id(self):
            return self.template_id


        def add_members(self, troop_id, number):
            self.members.append((troop_id, number)) # make better later on
            # reg0 return value

        def add_prisoners(self, troop_id, number):
            self.prisoners.append((troop_id, number)) # make better later on
            # reg0 return value

        def add_leader(self, troop_id, number=0):
            self.leader = troop_id

        def force_add_members(self, troop_id, number):
            self.members.append((troop_id, number)) # make better later on
            # reg0 return value ?

        def force_add_prisoners(self, troop_id, number):
            self.prisoners.append((troop_id, number)) # make better later on
            # reg0 return value ?


        def remove_members(self, troop_id, number):
            print("Remove", number, "members of type", troop_id, "from party", self.id)
            # reg0 return value

        def remove_prisoners(self, troop_id, number):
            print("Remove", number, "prisoners of type", troop_id, "from party", self.id)
            # reg0 return value

        def clear(self):
            self.members.clear()
            self.prisoners.clear()
            self.companions.clear()
            for i in range(len(self.slots)):
                self.slots[i] = 0
            self.flags = 0
            self.marshall = ""
            self.leader = ""
            print("Clear party", self.id)
            pass

        def wound_members(self, troop_id, number):
            print("Wound", number, "members of type", troop_id, "of party", self.id)

        def remove_members_wounded_first(self, troop_id, number):
            print("Remove wounded first -", number, "members of type", troop_id, "- party", self.id)


        def set_faction(self, faction_id):
            self.faction = faction_id

        def relocate_near_party(self, target_party_id, value_spawn_radius):
            print("Relocate near party", target_party_id, "- radius:", value_spawn_radius, "- party", self.id)


        def get_position(self):
            pass

        def set_position(self, position_no):
            pass


        def count_members_of_type(self, troop_id):
            pass

        def count_companions_of_type(self, troop_id):
            pass

        def count_prisoners_of_type(self, troop_id):
            pass


        def get_free_companions_capacity(self):
            pass

        def get_free_prisoners_capacity(self):
            pass


        def get_ai_initiative(self): # is between 0-100
            pass

        def set_ai_initiative(self, value): # is between 0-100
            pass

        def set_ai_behavior(self, ai_bhvr):
            pass

        def set_ai_object(self, party_id_2):
            pass

        def set_ai_target_position(self, position_no):
            pass

        def set_ai_patrol_radius(self, radius_in_km):
            pass

        def ingore_player(self, duration_in_hours):
            pass

        def set_bandit_attraction(self):
            pass

        def get_helpfulness(self):
            pass

        def set_helpfulness(self, number): # tendency to help friendly parties under attack. (self, 0-10000, 100 default.)
            pass

        def set_ignore_with_player_party(self, value):
            pass

        def get_ignore_with_player_party(self):
            pass


        def get_num_companions_stacks(self):
            return 0

        def get_num_prisoner_stacks(self):
            return 0

        def stack_get_troop_id(self, stack_no):
            return self.stack[stack_no]

        def stack_get_size(self, stack_no):
            return self.stack[stack_no].length

        def stack_get_num_wounded(self, stack_no):
            return 0

        def stack_get_troop_dna(self, stack_no):
            return ""

        def prisoner_stack_get_troop_id(self, stack_no):
            return self.prisoners[stack_no][0]

        def prisoner_stack_get_size(self, stack_no):
            return self.prisoners[stack_no].length

        def prisoner_stack_get_troop_dna(self, stack_no):
            return ""


        def attach_to_party(self, party_to_attach_to):
            print("Attach party", self.id, "to party", party_to_attach_to)

        def detach(self):
            print("Detach party", self.id)

        def collect_attachments_to_party(self, destination_party_id):
            pass

        def quick_attach_to_current_battle(self, side): # 0: player, 1: enemy
            sideText = "Player"
            if side == 1:
                sideText = "Enemy"
            print("Attach party", self.id, "to side", sideText)


        def get_cur_town(self):
            return self.current_town

        def leave_cur_battle(self):
            print("Party", self.id, "leave current battle")

        def set_next_battle_simulation_time(self, next_simulation_time_in_hours):
            self.next_simulation_time_in_hours = next_simulation_time_in_hours


        def set_name(self, new_name):
            self.name = new_name


        def add_xp_to_stack(self, stack_no, xp_amount):
            pass


        def get_morale(self):
            return self.morale

        def set_morale(self, morale): # range 0...100
            self.morale = morale


        def upgrade_with_xp(self, xp_amount, upgrade_path): # 0 = choose random, 1 = choose first, 2 = choose second
            pass

        def add_xp(self, xp_amount):
            pass

        def add_template(self, party_template_id, reverse_prisoner_status=0):
            pass

        def set_icon(self, map_icon_id):
            self.icon = map_icon_id

        def set_banner_icon(self, map_icon_id):
            self.banner_icon = map_icon_id

        def add_particle_system(self, particle_system):
            pass

        def clear_particle_systems(self):
            pass


        def get_battle_opponent(self):
            return 1

        def get_icon(self):
            return self.icon

        def set_extra_icon(self, map_icon_id, up_down_distance_fixed_point, up_down_frequency_fixed_point, rotate_frequency_fixed_point, fade_in_out_frequency_fixed_point):
            # frequencies are in number of revolutions per second
            self.extra_icon = map_icon_id


        def get_skill_level(self, skill_no):
            return 0

        def get_attached_to(self):
            return ""

        def get_num_attached_parties(self):
            return 0

        def get_attached_party_with_rank(self, attached_party_no):
            return ""
