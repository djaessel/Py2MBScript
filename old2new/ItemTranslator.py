
import sys
sys.path.append("../modules/")
sys.path.append("../build_system/")
sys.path.append("../data_objects/")

import header_items as itmHeader
import item as itmData


module_path = "/home/djaessel/warband/Modules/Native/"

factions = []
def readFactions():
    with open(module_path + "factions.txt") as f:
        lineCount = 0
        for line in f:
            if line.startswith("fac_") or " fac_" in line:
                tmp = line.strip().replace("  ", " ").split(' ')
                if not line.startswith("fac_"):
                    factions[len(factions)-1].append(tmp[0])
                    factions.append([tmp[1:]])
                else:
                    factions.append([tmp])
            elif lineCount > 2 and len(line.strip()) > 0:
                factions[len(factions)-1].append(line.strip().replace("  ", " ").split(' '))
            lineCount += 1


def readItems():
    itemsx = dict()
    with open(module_path + "item_kinds1.txt") as f:
        lineCount = 0
        curItem = ""
        for line in f:
            if line.startswith(" itm_"):
                tmp = line.strip().replace("  ", " ").split(' ')
                itemsx[tmp[0]] = [tmp]
                curItem = tmp[0]
            elif lineCount > 2 and len(line.strip()) > 0:
                itemsx[curItem].append(line.strip().split(' '))
            lineCount += 1
    return itemsx


def processFlags(flagsGZ : int):
    flagsx = []
    final_flags = []
    if int(flagsGZ) > 0:
        item_consts = dict()
        for i in vars(itmHeader):
            if i.startswith("itp_"):
                item_consts[i] = getattr(itmHeader,i)
        for t in item_consts:
            v = item_consts[t]
            if (v & 0xff) > 0:
                if (flagsGZ & 0xff) == v:
                    flagsx.append(t)
            elif (v & itmHeader.itp_attachment_mask) > 0 and not t.endswith("_mask"):
                if (flagsGZ & itmHeader.itp_attachment_mask) == v:
                    flagsx.append(t)
            elif (flagsGZ & v) == v and not t.endswith("_mask"):
                flagsx.append(t)

        mapx = None
        mapx2 = None
        for tfx in vars(itmData):
            if "ItemFlag" in tfx:
                atx = getattr(itmData,tfx)
                for lll in vars(atx):
                    if lll == "_value2member_map_":
                        mapx = getattr(atx, lll)
                        break
            elif "ItemType" in tfx:
                atx = getattr(itmData,tfx)
                for lll in vars(atx):
                    if lll == "_value2member_map_":
                        mapx2 = getattr(atx, lll)
                        break

        if mapx != None and mapx2 != None:
            for itp in flagsx:
                if itp in mapx:
                    final_flags.append(str(mapx[itp]))
                elif itp in mapx2:
                    final_flags.append(str(mapx2[itp]))
                else:
                    print("WARNING: Ignored itp >", itp)
        else:
            print("ERROR: MAPX EMPTY!")
    return final_flags


def processCapabilities(x : int):
    caps = []
    final_caps = []
    if int(x) > 0:
        item_consts = dict()
        for i in vars(itmHeader):
            if i.startswith("itcf_"):
                item_consts[i] = getattr(itmHeader,i)
        for t in item_consts:
            v = item_consts[t]
            if (v & itmHeader.itcf_carry_mask) > 0:
                if (x & itmHeader.itcf_carry_mask) == v:
                    caps.append(t)
            elif (x & v) == v:
                caps.append(t)

        mapx = None
        for tfx in vars(itmData):
            if "ItemCapability" in tfx:
                atx = getattr(itmData,tfx)
                for lll in vars(atx):
                    if lll == "_value2member_map_":
                        mapx = getattr(atx, lll)
                        break
                break

        if mapx != None:
            for itcf in caps:
                if itcf in mapx:
                    final_caps.append(str(mapx[itcf]))
                else:
                    print("WARNING: Ignored itcf >", itcf)
        else:
            print("ERROR: MAPX EMPTY!")
    return final_caps


def processModifiers(x : int):
    modifiers = []
    final_modifiers = []
    if int(x) > 0:
        item_consts = dict()
        for i in vars(itmHeader):
            if i.startswith("imodbit_"):
                item_consts[i] = getattr(itmHeader,i)
        for t in item_consts:
            v = item_consts[t]
            if (x & v) == v:
                modifiers.append(t)

        mapx = None
        for tfx in vars(itmData):
            if "IModBit" in tfx:
                atx = getattr(itmData,tfx)
                for lll in vars(atx):
                    if lll == "_value2member_map_":
                        mapx = getattr(atx, lll)
                        break
                break

        if mapx != None:
            for imodbit in modifiers:
                if imodbit in mapx:
                    final_modifiers.append(str(mapx[imodbit]))
                else:
                    print("WARNING: Ignored imodbit >", imodbit)
        else:
            print("ERROR: MAPX EMPTY!")
    return final_modifiers



def writeItem(item : list):
    with open("test_items.py", "a") as f:
        idx = item[0][0][4:]
        name = item[0][1]
        plural_name = item[0][2]

        f.write(idx + " = Item(\"" + idx + "\", \"" + name + "\")\n") # TODO: plural_name

        currentIndex = 3
        meshCount = int(item[0][currentIndex])
        if meshCount > 0:
            currentIndex += 1 # 4
            for i in range(meshCount):
                typex = int(item[0][currentIndex + 1])
                if typex == 0 or typex == itmHeader.ixmesh_inventory or typex == itmHeader.ixmesh_flying_ammo or typex == itmHeader.ixmesh_carry:
                    f.write(idx + ".add_mesh(ItemMesh(\"" + item[0][currentIndex] + "\"")
                    if typex > 0:
                        f.write(", ")
                        if typex == itmHeader.ixmesh_inventory:
                            f.write("ItemMesh.ixmesh_inventory")
                        elif typex == itmHeader.ixmesh_flying_ammo:
                            f.write("ItemMesh.ixmesh_flying_ammo")
                        elif typex == itmHeader.ixmesh_carry:
                            f.write("ItemMesh.ixmesh_carry")
                        else: # unused
                            f.write(str(typex)) # handle mesh modifiers
                    f.write("))\n")
                elif typex > 0:
                    f.write("meshx = ItemMesh(\"" + item[0][currentIndex] + "\"")
                    if (typex & itmHeader.ixmesh_carry) > 0:
                        f.write(", ")
                        if (typex & itmHeader.ixmesh_carry) == itmHeader.ixmesh_carry:
                            f.write("ItemMesh.ixmesh_carry")
                        elif (typex & itmHeader.ixmesh_inventory) == itmHeader.ixmesh_inventory:
                            f.write("ItemMesh.ixmesh_inventory")
                        elif (typex & itmHeader.ixmesh_flying_ammo) == itmHeader.ixmesh_flying_ammo:
                            f.write("ItemMesh.ixmesh_flying_ammo")
                    f.write(")\n")
                    mods = processModifiers(typex)
                    for mod in mods:
                        f.write("meshx.add_modifier(" + mod + ")\n")
                    f.write(idx + ".add_mesh(meshx)\n")
                currentIndex += 2

        flagsGZ = int(item[0][currentIndex])
        flags = processFlags(flagsGZ)
        for fl in flags:
            f.write(idx + ".add_flag(" + fl + ")\n")
        currentIndex += 1

        capabilitiesGZ = int(item[0][currentIndex])
        capabilities = processCapabilities(capabilitiesGZ)
        for cb in capabilities:
            f.write(idx + ".add_capability(" + cb + ")\n")
        currentIndex += 1

        price = int(item[0][currentIndex])
        if price > 0:
            f.write(idx + ".set_price(" + str(price) + ")\n")
        currentIndex += 1

        modifiersGZ = int(item[0][currentIndex])
        modifiers = processModifiers(modifiersGZ)
        for mod in modifiers:
            f.write(idx + ".add_modifier(" + mod + ")\n")
        currentIndex += 1

        weight = float(item[0][currentIndex])
        if weight != 0.000000:
            f.write(idx + ".set_weight(" + str(weight) + ")\n")
        currentIndex += 1

        abundance = int(item[0][currentIndex])
        if abundance != 0:
            f.write(idx + ".set_abundance(" + str(abundance) + ")\n")
        currentIndex += 1

        head_armor = int(item[0][currentIndex])
        if head_armor != 0:
            f.write(idx + ".set_head_armor(" + str(head_armor) + ")\n")
        currentIndex += 1

        body_armor = int(item[0][currentIndex])
        if body_armor != 0:
            f.write(idx + ".set_body_armor(" + str(body_armor) + ")\n")
        currentIndex += 1

        leg_armor = int(item[0][currentIndex])
        if leg_armor != 0:
            f.write(idx + ".set_leg_armor(" + str(leg_armor) + ")\n")
        currentIndex += 1

        difficulty = int(item[0][currentIndex])
        if difficulty != 0:
            f.write(idx + ".set_difficulty(" + str(difficulty) + ")\n")
        currentIndex += 1

        hit_points = int(item[0][currentIndex])
        if hit_points != 0:
            f.write(idx + ".set_hit_points(" + str(hit_points) + ")\n")
        currentIndex += 1

        speed_rating = int(item[0][currentIndex])
        if speed_rating != 0:
            f.write(idx + ".set_speed_rating(" + str(speed_rating) + ")\n")
        currentIndex += 1

        missile_speed = int(item[0][currentIndex])
        if missile_speed != 0:
            f.write(idx + ".set_missile_speed(" + str(missile_speed) + ")\n")
        currentIndex += 1

        weapon_length = int(item[0][currentIndex])
        if weapon_length != 0:
            f.write(idx + ".set_weapon_length(" + str(weapon_length) + ")\n")
        currentIndex += 1

        max_ammo = int(item[0][currentIndex])
        if max_ammo != 0:
            f.write(idx + ".set_max_ammo(" + str(max_ammo) + ")\n")
        currentIndex += 1

        thrust_damage = int(item[0][currentIndex])
        if thrust_damage != 0:
            damage_type = (thrust_damage >> 8) & 0xff
            damage = thrust_damage & 0xff
            f.write(idx + ".set_thrust_damage(" + str(damage) + ", " + str(damage_type) + ")\n")
        currentIndex += 1

        swing_damage = int(item[0][currentIndex])
        if swing_damage != 0:
            damage_type = (swing_damage >> 8) & 0xff
            damage = swing_damage & 0xff
            f.write(idx + ".set_swing_damage(" + str(damage) + ", " + str(damage_type) + ")\n")
        currentIndex += 1

        
        factionCount = int(item[1][0])
        currentIndex = 2
        if factionCount > 0:
            for i in item[currentIndex]:
                f.write(idx + ".allow_in_faction(fac." + factions[int(i)][0][0][4:] + ")\n") # TODO: add actual faction
            currentIndex += 1

        # Triggers
        triggerCount = int(item[currentIndex][0])
        if triggerCount > 0:
            currentIndex += 1
            for tr in range(currentIndex, len(item)):
                f.write("# " + " ".join(item[tr]) + "\n")

        f.write("\n\n")
        

        
# main program
if __name__ == "__main__":
    readFactions()
    all_items = readItems()
    for itm in all_items:
        writeItem(all_items[itm])




