# This Python file uses the following encoding: utf-8

import os
import random
import scripts

import ID_animations as animID
import module_constants as mconst
import header_common as mcom
import strings as gstr
import scene_props as spr
import sounds as snd
import troops as trp
import items as itm
import map_icons as icon
import game_menus as mnu
import animations as anim
import factions as fac
import meshes as mesh
#import info_pages as ip
import dialogs as dlg
import mission_templates as mt
import parties as p
import party_templates as pt
import particle_systems as psys
import presentations as prnst
import postfxs as pfx
import quests as qst
import scenes as scn
import skills as skl


typeDictX = dict()
typeDictX["scripts"] = "script"
typeDictX["troops"] = "trp"
typeDictX["map_icons"] = "icon"
typeDictX["items"] = "itm"
typeDictX["game_menus"] = "mnu"
typeDictX["strings"] = "gstr"
typeDictX["scene_props"] = "spr"
typeDictX["sounds"] = "snd"
typeDictX["animations"] = "anim"
typeDictX["factions"] = "fac"
typeDictX["meshes"] = "mesh"
typeDictX["info_pages"] = "ip"
typeDictX["dialogs"] = "dlg"
typeDictX["mission_templates"] = "mt"
typeDictX["parties"] = "p"
typeDictX["party_templates"] = "pt"
typeDictX["music"] = "track"
typeDictX["particle_systems"] = "psys"
typeDictX["postfxs"] = "pfx"
typeDictX["presentations"] = "prnst"
typeDictX["quests"] = "qst"
typeDictX["scenes"] = "scn"
typeDictX["skills"] = "skl"
typeDictX["tableau_materials"] = "tableau"
typeDictX["skins"] = "skin"


class ScriptConverter:
    registers = []
    str_registers = []
    pos_registers = []

    codex = dict()
    cur_lists = dict()

    cur_players = dict()
    cur_parties = dict()
    cur_options = dict()
    cur_items = dict()
    cur_scripts = []

    while_active = False
    list_active = False
    list_active_name = ""

    is_trigger_code = False

    # presentation overlays (maybe separate)
    prsnt_text_overlays = dict()

    def __init__(self):
        with open("./build_system/header_operations.py") as f:
            for line in f:
                if "=" in line and "#" in line:
                    code = line.split('=')[0].strip()
                    self.codex[code] = line.split('#')[1].strip()

        for i in range(66):#128
            self.registers.append("reg" + str(i))

        for i in range(68):#128
            self.str_registers.append("s" + str(i))

        for i in range(64):#128
            self.pos_registers.append("pos" + str(i))

        self.cur_scripts = self.retrieveScriptNames()
        self.codeTypes = self.readAllTypes()


    def retrieveScriptNames(self):
        scriptNames = []
        for i in vars(scripts):
            if not (i.startswith("__") and i.endswith("__")) and not i[0:1].isupper():
                attr = getattr(scripts,i)
                scriptNames.append(attr.__name__)
        return scriptNames


    def is_float(self, v):
        try:
          f=float(v)
        except ValueError:
          return False
        return True


    def handleEqualsSign(self, code):
        tmp = code.split('=')
        varName = tmp[0].strip()
        funcCall = tmp[1].strip()
        liny = self.getFuncCodeLine(funcCall)
        if liny.endswith("# ERROR 1"):
            xelly = liny.split('.')[0].split(' ')
            if "." in liny and not liny.split('.')[0].strip() in self.codeTypes and not xelly[-1] in typeDictX.values():
                liny = self.handleDotSignInEqualLine(liny, funcCall, varName)
            elif funcCall.startswith("MBParty("):
                self.cur_parties[varName] = funcCall.split(')')[0].split('(')[1]
                liny = ""
            elif funcCall.startswith("MBPlayer("):
                self.cur_players[varName] = funcCall.split(')')[0].split('(')[1]
                liny = ""
            elif funcCall.startswith("MBOptions("):
                self.cur_options[varName] = funcCall.split(')')[0].split('(')[1] # should be string empty here
                liny = ""
            elif funcCall.startswith("Item("):
                self.cur_items[varName] = funcCall.split(')')[0].split('(')[1] # should be string empty here
                liny = ""
            elif funcCall.startswith("[") and funcCall.endswith("]"):
                lll = funcCall.split(']')[0].split('[')[1].split(',')
                for i in range(len(lll)):
                    lll[i] = lll[i].strip()
                self.cur_lists[varName] = lll
                liny = ""
            elif funcCall.startswith("["):
                ScriptConverter.list_active = True
                lll = funcCall.split('[')[1].split(',')
                for i in range(len(lll)):
                    lll[i] = lll[i].strip()
                if lll[-1] == "":
                    del lll[-1]
                self.cur_lists[varName] = lll
                ScriptConverter.list_active_name = varName
                liny = ""
            elif funcCall.startswith("MBTextOverlay("):
                tmp = funcCall.split(')')[0].split('(')[1]
                liny = "(create_text_overlay, <reg>, <str_text>, <text_flags>)"
                tmp = tmp.split(',')
                self.prsnt_text_overlays[varName] = tmp[0].strip()
                liny = liny.replace("<reg>", tmp[0].strip()).replace('<str_text>', tmp[1].strip()).replace("<text_flags>", tmp[2].strip())
            elif varName in self.str_registers:
                liny = "(str_store_string,<var1>,<var2>)"
                liny = self.replaceVarWithPlaceholder(liny, "<var1>", varName)
                if '"' in funcCall and not funcCall.strip('"').startswith("str_"):
                    liny = self.replaceVarWithPlaceholder(liny, "<var2>", funcCall.replace('"', '"@').rstrip('@'))
                else:
                    liny = self.replaceVarWithPlaceholder(liny, "<var2>", funcCall)
            elif "+" in funcCall or "*" in funcCall or "/" in funcCall or ("-" in funcCall and not "=-" in code.replace(" ", "")):
                liny = self.handleBasicMath(code)
            else:
                liny = "(assign,<var1>,<var2>)"
                liny = self.replaceVarWithPlaceholder(liny, "<var1>", varName)
                liny = self.replaceVarWithPlaceholder(liny, "<var2>", funcCall)
        else:
            if varName in self.str_registers:
                #if "str_store_string" in funcCall:
                #    liny = "(str_store_string,<var1>,<var2>)"
                #    liny = self.replaceVarWithPlaceholder(liny, "<var1>", varName)
                #    if '"' in funcCall and not funcCall.strip('"').startswith("str_"):
                #        liny = self.replaceVarWithPlaceholder(liny, "<var2>", funcCall.replace('"', '"@').rstrip('@'))
                #    else:
                #        liny = self.replaceVarWithPlaceholder(liny, "<var2>", funcCall)
                #else:
                xy = funcCall.split('(')
                liny = "(" + xy[0] + ",<var1>,<var2>)"
                liny = self.replaceVarWithPlaceholder(liny, "<var1>", varName)
                liny = self.replaceVarWithPlaceholder(liny, "<var2>", xy[1].split(')')[0])
            elif varName in self.pos_registers:
                liny = self.replaceVarWithPlaceholder(liny, "<position_no>", varName)
                liny = self.replaceVarWithPlaceholder(liny, "<position>", varName)
                liny = self.replaceVarWithPlaceholder(liny, "<pos_no>", varName)
                liny = self.replaceFuncParams(liny, funcCall)
            else:
                liny = self.replaceVarWithPlaceholder(liny, "<destination>", varName)
                liny = self.replaceVarWithPlaceholder(liny, "<destination_fixed_point>", varName)
                liny = self.replaceFuncParams(liny, funcCall)
        if not isinstance(liny, list):
            liny = [liny]
        for i in range(len(liny)):
            liny[i] = liny[i].replace(":::","$")
            liny[i] = liny[i].replace("[[[","(")
            liny[i] = liny[i].replace("]]]",")")
            liny[i] = liny[i].replace(";;;",",")
        return liny


    def handleDotSignInEqualLine(self, liny, funcCall, varName):
        tmp = funcCall.split('.')
        curP = tmp[0].strip()
        if curP in self.cur_players:
            p_func_name = "player_" + tmp[1].strip()
            liny = self.getFuncCodeLine(p_func_name)
            liny = self.replaceVarWithPlaceholder(liny, "<destination>", varName)
            liny = self.replaceVarWithPlaceholder(liny, "<player_id>", self.cur_players[curP])
        elif curP in self.cur_parties:
            p_func_name = "party_" + tmp[1].strip()
            liny = self.getFuncCodeLine(p_func_name)
            liny = self.replaceVarWithPlaceholder(liny, "<destination>", varName)
            liny = self.replaceVarWithPlaceholder(liny, "<party_id>", self.cur_parties[curP])
        elif curP in self.cur_items:
            p_func_name = "item_" + tmp[1].strip()
            liny = self.getFuncCodeLine(p_func_name)
            liny = self.replaceVarWithPlaceholder(liny, "<destination>", varName)
            liny = self.replaceVarWithPlaceholder(liny, "<item_id>", self.cur_items[curP])
            liny = self.replaceVarWithPlaceholder(liny, "<item_kind_no>", self.cur_items[curP])
        elif curP in self.cur_options:
            p_func_name = "options_" + tmp[1].strip()
            liny = self.getFuncCodeLine(p_func_name)
            liny = self.replaceVarWithPlaceholder(liny, "<destination>", varName)
        else:
            liny = varName + " = " + str(eval(funcCall)) # check imports if something goes wrong
            liny = self.handleEqualsSign(liny)[0]
        liny = liny.replace(":::","$")
        liny = liny.replace("[[[","(")
        liny = liny.replace("]]]",")")
        liny = liny.replace(";;;",",")
        return liny


    def handleDotSign(self, code):
        tmp = code.split('.')
        curP = tmp[0].strip()
        if curP in self.cur_players:
            p_func_name = "player_" + tmp[1].strip()
            liny = self.getFuncCodeLine(p_func_name)
            liny = self.replaceVarWithPlaceholder(liny, "<player_id>", self.cur_players[curP])
            liny = self.replaceFuncParams(liny, p_func_name)
        elif curP in self.cur_parties:
            p_func_name = "party_" + tmp[1].strip()
            liny = self.getFuncCodeLine(p_func_name)
            liny = self.replaceVarWithPlaceholder(liny, "<party_id>", self.cur_parties[curP])
            liny = self.replaceFuncParams(liny, p_func_name)
        elif curP in self.cur_items:
            p_func_name = "item_" + tmp[1].strip()
            liny = self.getFuncCodeLine(p_func_name)
            liny = self.replaceVarWithPlaceholder(liny, "<item_id>", self.cur_items[curP])
            liny = self.replaceVarWithPlaceholder(liny, "<item_kind_no>", self.cur_items[curP])
            liny = self.replaceFuncParams(liny, p_func_name)
        elif curP in self.cur_options:
            p_func_name = "options_" + tmp[1].strip()
            liny = self.getFuncCodeLine(p_func_name)
            liny = self.replaceFuncParams(liny, p_func_name)
        elif curP in self.prsnt_text_overlays:
            regi = self.prsnt_text_overlays[curP]
            if "set_position" in tmp[1]:
                pos = tmp[1].split(')')[0].split('(')[1].split(',')
                return ["(position_set_x, pos1, <pos_x>)".replace("<pos_x>", pos[0].strip()),
                        "(position_set_y, pos1, <pos_y>)".replace("<pos_y>", pos[1].strip()),
                        "(overlay_set_position, <reg>, pos1)".replace("<reg>", regi)]
            elif "set_size" in tmp[1]:
                pos = tmp[1].split(')')[0].split('(')[1].split(',')
                return ["(position_set_x, pos1, <pos_x>)".replace("<pos_x>", pos[0].strip()),
                        "(position_set_y, pos1, <pos_y>)".replace("<pos_y>", pos[1].strip()),
                        "(overlay_set_size, <reg>, pos1)".replace("<reg>", regi)]
            else:
                tmp[1] = tmp[1].replace("(", "(" + regi + ",")
                p_func_name = "overlay_" + tmp[1].strip()
                liny = self.getFuncCodeLine(p_func_name)
                #liny = self.replaceVarWithPlaceholder(liny, "<party_id>", self.cur_parties[curP])
                liny = self.replaceFuncParams(liny, p_func_name)
        else:
            print("UNHANDLED CODE:", code)
        liny = liny.replace(":::","$")
        liny = liny.replace("[[[","(")
        liny = liny.replace("]]]",")")
        liny = liny.replace(";;;",",")
        return [liny]


    def handlePrint(self, code):
        if "print(" in code and "," in code:
            sx = ""
            b = []
            pseudoCode = code.split('(')[1].split(')')[0]
            data = [x.strip() for x in pseudoCode.split(',')]
            for i, d in enumerate(data):
                if d in self.str_registers or d in self.registers:
                    sx += "{" + d + "} "
                elif d.startswith('"') and d.endswith('"'):
                    sx += d.strip('"') + " "
                elif d in self.pos_registers:
                    b.append(self.replaceVarWithPlaceholder("(position_get_x, reg" + str(68+i) + ", <placeholder>)", "<placeholder>", d))
                    b.append(self.replaceVarWithPlaceholder("(position_get_y, reg" + str(68+i+1) + ", <placeholder>)", "<placeholder>", d))
                    b.append(self.replaceVarWithPlaceholder("(position_get_z, reg" + str(68+i+2) + ", <placeholder>)", "<placeholder>", d))
                    idx = self.pos_registers.index(d)
                    sx += "Pos" + str(idx) + " :[{reg"+str(68+i)+"}, {reg"+str(68+i+1)+"}, {reg"+str(68+i+2)+"}] "
                else:
                    b.append(self.replaceVarWithPlaceholder("(assign, reg" + str(i)+ ", <placeholder>)", "<placeholder>", d).replace(":::", "$"))
                    sx += "{reg" + str(i) + "} "

            sx = sx.rstrip()
            b.append("(display_message, \"@"+sx+"\")")
        elif "print(\"str_" in code:
            text_id = code.split('"')[1]
            b = ["(display_message, \"" + text_id + "\")"]
        elif "print(\"" in code:
            text = code.split('"')[1]
            b = ["(display_message, \"@" + text + "\")"]
        else:
            pseudoCode = code.split('(')[1].split(')')[0]
            if pseudoCode in self.str_registers or pseudoCode in self.registers:
                b = ["(display_message, \"@{" + pseudoCode + "}\")"]
            elif pseudoCode in self.pos_registers:
                b = []
                b.append(self.replaceVarWithPlaceholder("(position_get_x, reg66, <placeholder>)", "<placeholder>", pseudoCode))
                b.append(self.replaceVarWithPlaceholder("(position_get_y, reg67, <placeholder>)", "<placeholder>", pseudoCode))
                b.append(self.replaceVarWithPlaceholder("(position_get_z, reg68, <placeholder>)", "<placeholder>", pseudoCode))
                idx = self.pos_registers.index(pseudoCode)
                b.append("(display_message, \"@Pos" + str(idx) + " :[{reg60}, {reg61}, {reg62}]\")")
            else:
                b = [self.replaceVarWithPlaceholder("(assign, reg0, <placeholder>)", "<placeholder>", pseudoCode).replace(":::", "$")]
                b.append("(display_message, \"@{reg0}\")")
        return b


    def handleBasicMathHelper1(self, linyx, code):
        countz = 1
        while "(" in code and ")" in code:
            lh = code.split('(')[1]
            lh = lh.split(')')[0]
            codex = "(" + lh + ")"
            va = "var___z" + str(countz)
            code = code.replace(codex, va, 1)
            lh = va + " = " + lh
            va = self.handleBasicMath(lh)
            linyx.extend(va)
            countz += 1
        return code, linyx


    def handleBasicMathHelper2(self, code, linyx, ccy):
        countx = 1
        idx = 0
        for cy in ccy:
            xy = cy.split('*')
            yx = cy.split('/')
            if len(xy) > 1:
                idx2 = 0
                county = 1
                for yd in xy:
                    if "/" in yd:
                        los = "var___y" + str(county)
                        hhh = self.handleStoreDiv(los + " = " + yd)
                        linyx.extend(hhh)
                        xy[idx2] = los
                        county += 1
                    idx2 += 1
                los = "var___x" + str(countx)

                if ("-" in xy[0] and not xy[0].strip().startswith("-")) or ("-" in xy[1] and not xy[1].strip().startswith("-")):
                    ll = self.handleBasicMathHelper3(code, xy, linyx)
                    print("LL:", ll)

                cy = " * ".join(xy)
                xyz = self.handleStoreMul(los + " = " + cy)
                linyx.extend(xyz)
                ccy[idx] = los
                countx += 1
            elif len(yx) > 1:
                idx2 = 0
                county = 1
                for yd in yx:
                    if "*" in yd:
                        los = "var___y" + str(county)
                        hhh = self.handleStoreMul(los + " = " + yd)
                        linyx.extend(hhh)
                        yx[idx2] = los
                        county += 1
                    idx2 += 1
                los = "var___x" + str(countx)

                if ("-" in yx[0] and not yx[0].strip().startswith("-")) or ("-" in yx[1] and not yx[1].strip().startswith("-")):
                    ll = self.handleBasicMathHelper3(code, yx, linyx)
                    print("LL:", ll)

                cy = " / ".join(yx)
                xyz = self.handleStoreDiv(los + " = " + cy)
                linyx.extend(xyz)
                ccy[idx] = los
                countx += 1
            idx += 1
        return ccy, linyx


    def handleBasicMathHelper3(self, code, ccy, linyx):
        if len(ccy) >= 2:
            lll = code.split('=')[0].strip()
            ccy0 = ccy[0].strip()
            ccy1 = ccy[1].strip()
            if "-" in ccy0:
                ll = self.handleStoreSub("var___a1 = " + ccy0)
                linyx.extend(ll)
                ccy0 = "var___a1"
            if "-" in ccy1:
                ll = self.handleStoreSub("var___a2 = " + ccy1)
                linyx.extend(ll)
                ccy1 = "var___a2"
            ooo = lll + " = " + ccy0 + " + " + ccy1
            linyx.extend(self.handleStoreAdd(ooo))
            if len(ccy) > 2:
                for ix in range(2, len(ccy)):
                    linyx.extend(self.handleValAdd(lll + " += " + ccy[ix].strip()))
        elif "-" in ccy[0] and not "=-" in ccy[0].replace(" ",""):
            lll = code.split('=')[0].strip()
            selx = ccy[0].split('-')
            if len(selx[0].strip()) > 0:
                ll = self.handleStoreSub(lll + " = " + selx[0].strip() + " - " + selx[1].strip())
                linyx.extend(ll)
        elif "var___x1" in ccy[0] and len(linyx) == 1 and linyx[0].startswith("(store_mul, \":var___x1\","): # special case multiplication!
            linyx[0] = linyx[0].replace("(store_mul, \":var___x1\",", "(store_mul, \":" + code.split('=')[0].strip() + "\",")
        else:
            ccy = self.handleEqualsSign(code.split('=')[0] + " = " + ccy[0])
            linyx.extend(ccy)
        return linyx


    def handleBasicMath(self, code):
        linyx = []

        code, linyx = self.handleBasicMathHelper1(linyx, code)

        codex = code.split('=')[1].strip()
        ccy = codex.split('+')
        ccc = codex.split(" - ")

        if len(ccy) == 1 and len(ccc) > 1:
            #print("CCC:", ccc, "CCY:", ccy)
            ll = self.handleStoreSub(code)
            linyx.extend(ll)
        else:
            ccy, linyx = self.handleBasicMathHelper2(code, linyx, ccy)
            linyx = self.handleBasicMathHelper3(code, ccy, linyx)

        return linyx


    def handleValSub(self, code):
        liny = "(val_sub, <val1>, <val2>)"
        sx = code.split('-')[0].strip()
        sy = code.split('=')[1].strip()
        liny = self.replaceVarWithPlaceholder(liny, "<val1>", sx)
        rigx = []
        if "+" in sy or "*" in sy or "/" in sy or ("-" in sy and not sy.replace(" ","").startswith("-")):
            rigx = self.handleBasicMath("var___s1 = " + sy)
            liny = self.replaceVarWithPlaceholder(liny, "<val2>", "var___s1")
        else:
            liny = self.replaceVarWithPlaceholder(liny, "<val2>", sy)
        rigx.append(liny)
        return rigx


    def handleValAdd(self, code):
        liny = "(val_add, <val1>, <val2>)"
        sx = code.split('+')[0].strip()
        sy = code.split('=')[1].strip()
        liny = self.replaceVarWithPlaceholder(liny, "<val1>", sx)
        rigx = []
        if "+" in sy or "*" in sy or "/" in sy or ("-" in sy and not sy.replace(" ","").startswith("-")):
            rigx = self.handleBasicMath("var___add1 = " + sy)
            liny = self.replaceVarWithPlaceholder(liny, "<val2>", "var___add1")
        else:
            liny = self.replaceVarWithPlaceholder(liny, "<val2>", sy)
        rigx.append(liny)
        return rigx


    def handleValMul(self, code):
        liny = "(val_mul, <val1>, <val2>)"
        sx = code.split('*')[0].strip()
        sy = code.split('=')[1].strip()
        liny = self.replaceVarWithPlaceholder(liny, "<val1>", sx)
        rigx = []
        if "+" in sy or "*" in sy or "/" in sy or ("-" in sy and not sy.replace(" ","").startswith("-")):
            rigx = self.handleBasicMath("var___m1 = " + sy)
            liny = self.replaceVarWithPlaceholder(liny, "<val2>", "var___m1")
        else:
            liny = self.replaceVarWithPlaceholder(liny, "<val2>", sy)
        rigx.append(liny)
        return rigx


    def handleValDiv(self, code):
        liny = "(val_div, <val1>, <val2>)"
        sx = code.split('/')[0].strip()
        sy = code.split('=')[1].strip()
        liny = self.replaceVarWithPlaceholder(liny, "<val1>", sx)
        rigx = []
        if "+" in sy or "*" in sy or "/" in sy or ("-" in sy and not sy.replace(" ","").startswith("-")):
            rigx = self.handleBasicMath("var___d1 = " + sy)
            liny = self.replaceVarWithPlaceholder(liny, "<val2>", "var___d1")
        else:
            liny = self.replaceVarWithPlaceholder(liny, "<val2>", sy)
        rigx.append(liny)
        return rigx


    def handleValMod(self, code):
        liny = "(val_mod, <val1>, <val2>)"
        sx = code.split('%')[0].strip()
        sy = code.split('=')[1].strip()
        liny = self.replaceVarWithPlaceholder(liny, "<val1>", sx)
        rigx = []
        if "+" in sy or "*" in sy or "/" in sy or ("-" in sy and not sy.replace(" ","").startswith("-")):
            rigx = self.handleBasicMath("var___p1 = " + sy)
            liny = self.replaceVarWithPlaceholder(liny, "<val2>", "var___p1")
        else:
            liny = self.replaceVarWithPlaceholder(liny, "<val2>", sy)
        rigx.append(liny)
        return rigx


    def handleStoreAdd(self, code):
        liny = "(store_add, <val1>, <val2>, <val3>)"
        sx = code.split('=')[0].strip()
        poi = code.split('=')[1].strip()
        ccy = poi.split('+')
        sy = ccy[0].strip()
        sz = ccy[1].strip()
        liny = self.replaceVarWithPlaceholder(liny, "<val1>", sx)
        liny = self.replaceVarWithPlaceholder(liny, "<val2>", sy)
        liny = self.replaceVarWithPlaceholder(liny, "<val3>", sz)
        if len(ccy) > 2:
            rigx = self.handleBasicMath(code)
        else:
            rigx = [liny]
        return rigx


    def handleStoreSub(self, code):
        liny = "(store_sub, <val1>, <val2>, <val3>)"
        sx = code.split('=')[0].strip()
        poi = code.split('=')[1].strip()
        ccy = poi.split('-')
        sy = ccy[0].strip()
        sz = ccy[1].strip()
        liny = self.replaceVarWithPlaceholder(liny, "<val1>", sx)
        liny = self.replaceVarWithPlaceholder(liny, "<val2>", sy)
        liny = self.replaceVarWithPlaceholder(liny, "<val3>", sz)
        if len(ccy) > 2:
            rigx = [liny]
            lll = code.split('=')[0].strip()
            for ix in range(2, len(ccy)):
                rigx.extend(self.handleValSub(lll + " -= " + ccy[ix].strip()))
        else:
            rigx = [liny]
        return rigx


    def handleStoreMul(self, code):
        liny = "(store_mul, <val1>, <val2>, <val3>)"
        sx = code.split('=')[0].strip()
        poi = code.split('=')[1].strip().split('*')
        sy = poi[0].strip()
        sz = poi[1].strip()
        liny = self.replaceVarWithPlaceholder(liny, "<val1>", sx)
        liny = self.replaceVarWithPlaceholder(liny, "<val2>", sy)
        liny = self.replaceVarWithPlaceholder(liny, "<val3>", sz)
        if len(poi) > 2:
            rigx = self.handleBasicMath(code)
        else:
            rigx = [liny]
        return rigx
        return [liny]


    def handleStoreDiv(self, code):
        liny = "(store_div, <val1>, <val2>, <val3>)"
        sx = code.split('=')[0].strip()
        poi = code.split('=')[1].strip().split('/')
        sy = poi[0].strip()
        sz = poi[1].strip()
        liny = self.replaceVarWithPlaceholder(liny, "<val1>", sx)
        liny = self.replaceVarWithPlaceholder(liny, "<val2>", sy)
        liny = self.replaceVarWithPlaceholder(liny, "<val3>", sz)
        if len(poi) > 2:
            rigx = self.handleBasicMath(code)
        else:
            rigx = [liny]
        return rigx


    def replaceTypex2(self, code):
        codeNew = code.split('(')[0] + "("
        xol = code.split('(')[1].split(')')[0].split(',')
        for i in range(len(xol)):
            xol[i] = xol[i].strip()
            if "." in xol[i]:
                tmp = xol[i].split('.')
                if tmp[0] in self.codeTypes:
                    xxy = getattr(self.codeTypes[tmp[0]], tmp[1])
                    if xxy:
                        if tmp[0] == "gstr":
                            tmp[0] = "str"
                        if tmp[0] == "script":
                            xol[i] = tmp[0] + "_" + xxy.__name__
                        else:
                            xol[i] = tmp[0] + "_" + xxy.id
                        codeNew += '"' + xol[i] + "\","
                    else:
                        print("ERROR 0x533D1")
            else:
                codeNew += xol[i] + ","
        codeNew = codeNew.rstrip(',') + ")"
        return codeNew


    def replaceTypex3(self, code):
        comma = False
        if "=" in code:
            codeNew = code.split('=')[0] + " = "
            xol = code.split('=')[1].strip()
        else:
            codeNew = ""
            xol = code.split(',')[0].strip()
            if "," in code:
                comma = True
        if "." in xol:
            tmp = xol.split('.')
            if tmp[0] in self.codeTypes:
                xxy = getattr(self.codeTypes[tmp[0]], tmp[1])
                if xxy:
                    if tmp[0] == "gstr":
                        tmp[0] = "str"
                    xol = tmp[0] + "_" + xxy.id
                    codeNew += '"' + xol + "\""
                else:
                    print("ERROR 0x533D2")
            else:
                codeNew = code
        else:
            codeNew = code
        if comma:
            codeNew += ","
        return codeNew


    def transformCode(self, code):
        if len(code.strip()) == 0:
            return [""]

        if "#" in code:
            code = code.split('#')[0].rstrip()

        if "." in code:
            if "(" in code and ")" in code:
                if code.index("(") < code.index(".") and code.index(")") > code.index("."):
                    code = self.replaceTypex2(code)
            else:
                code = self.replaceTypex3(code)

        if code.strip().startswith('#'):
            # return [code.strip()]
            return [""]
        elif code.startswith("print("):
            return self.handlePrint(code)
        elif ScriptConverter.list_active:
            lll = code.split(']')[0].split(',')
            for i in range(len(lll)):
                lll[i] = lll[i].strip()
            if lll[-1] == "":
                del lll[-1]
            self.cur_lists[ScriptConverter.list_active_name].extend(lll)
            if "]" in code:
                ScriptConverter.list_active = False
                ScriptConverter.list_active_name = ""
            return [""]
        elif "+=" in code:
            return self.handleValAdd(code)
        elif "-=" in code:
            return self.handleValSub(code)
        elif "*=" in code:
            return self.handleValMul(code)
        elif "/=" in code:
            return self.handleValDiv(code)
        elif "%=" in code:
            return self.handleValMod(code)
        elif "=" in code:
            return self.handleEqualsSign(code)
        elif "." in code:
            return self.handleDotSign(code)
        elif "(" in code and ")" in code:
            fName = code.split('(')[0].strip()
            fVars = code.split('(')[1].split(')')[0]
            if fName in self.cur_scripts:
                liny = "(call_script, \"script_" + fName + "\""
                if len(fVars) > 0:
                    for f in fVars.split(','):
                        liny += ", " + f.strip()
                liny += "),"
                if len(fVars) > 0:
                    liny = self.replaceScriptParams(liny, fVars)
            elif fName == "tutorial_message" and "(-1)" in code:
                liny = "(tutorial_message, -1),"
            else:
                liny = self.getFuncCodeLine(code)
                liny = self.replaceFuncParams(liny, code.split(')')[0])
            liny = liny.replace(":::", "$")
            liny = liny.replace("[[[","(")
            liny = liny.replace("]]]",")")
            liny = liny.replace(";;;",",")
            return [liny]

        return [""] # ERROR 2 # ignored code


    def findParams(self, funcCall, startIdx = 1):
        params = funcCall.rstrip('),').split(',')[startIdx:]
        idx = -1
        for i, param in enumerate(params):
            if ":" in param:
                idx = i
            params[i] = params[i].strip()
        if idx > 0:
            del params[idx]
        if startIdx > 0 and len(params) > 0 and (":" in params[0] or params[0] in self.str_registers or params[0] in self.pos_registers or params[0] in self.registers):
            del params[0]
        return params


    def replaceScriptParams(self, liny, vars):
        actParams = self.findParams(vars, 0)
        for p in actParams:
            px = p
            if p == "True":
                px = "1"
            elif p == "False":
                px = "0"
            liny = self.replaceVarWithPlaceholder(liny, p, px)
        liny = liny.replace(":::", "$")
        liny = liny.replace("[[[","(")
        liny = liny.replace("]]]",")")
        liny = liny.replace(";;;",",")
        return liny


    def replaceFuncParams(self, liny, funcCall):
        params = self.findParams(liny)
        actParams = self.findParams(funcCall.split('(')[1], 0)
        for i in range(len(params)):
            if (not "[" in params[i] and not "]" in params[i]) or ("[" in params[i] and "]" in params[i] and len(actParams) > i):
                # print(liny, params, len(params), len(actParams), actParams)
                actParamx = actParams[i]
                if actParamx == "True":
                    actParamx = "1"
                elif actParamx == "False":
                    actParamx = "0"
                liny = self.replaceVarWithPlaceholder(liny, params[i], actParamx)
            else:
                # print("Ignored optional parameter:", params[i], "|", funcCall, "|", liny)
                liny = liny.replace(", " + params[i], "").replace("," + params[i], "")
        liny = liny.replace(":::", "$")
        liny = liny.replace("[[[","(")
        liny = liny.replace("]]]",")")
        liny = liny.replace(";;;",",")
        return liny


    def getFuncCodeLine(self, funcCall):
        funcName = funcCall.split('(')[0].strip()
        liny = funcCall + " # ERROR 1"
        if funcName in self.codex:
            liny = self.codex[funcName]
        return liny


    def resolveSimpleCondition(self, cond):
        codeFunc = False
        notTrue = False
        b = []

        cond = cond.strip()

        if "not True" == cond:
            cond = "False"
        elif "not False" == cond:
            cond = "True"

        if "> " in cond:
            l = "(gt,<var1>,<var2>)"
            tmp = cond.split('>')
            tmp[0] = self.replaceTypex3(tmp[0])
            tmp[1] = self.replaceTypex3(tmp[1])
            l = self.replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip())
            l = self.replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip())
            b.append(l)
        elif "< " in cond:
            l = "(lt,<var1>,<var2>)"
            tmp = cond.split('<')
            tmp[0] = self.replaceTypex3(tmp[0])
            tmp[1] = self.replaceTypex3(tmp[1])
            l = self.replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip())
            l = self.replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip())
            b.append(l)
        elif "==" in cond:
            l = "(eq,<var1>,<var2>)"
            tmp = cond.split('==')
            tmp[0] = self.replaceTypex3(tmp[0])
            tmp[1] = self.replaceTypex3(tmp[1])
            if "(" in tmp[0] and ")" in tmp[0] and "True" == tmp[1].strip():
                l = self.transformCode(tmp[0])
                codeFunc = True
                b.extend(l)
            elif "(" in tmp[0] and ")" in tmp[0] and "False" == tmp[1].strip():
                l = self.transformCode(tmp[0])
                codeFunc = True
                notTrue = True
                b.extend(l)
            else:
                l = self.replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip().replace("True","1").replace("False","0"))
                l = self.replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip().replace("True","1").replace("False","0"))
                b.append(l)
        elif "!=" in cond or "<>" in cond:
            l = "(neq,<var1>,<var2>)"
            tmp = cond.split('!=')
            tmp[0] = self.replaceTypex3(tmp[0])
            tmp[1] = self.replaceTypex3(tmp[1])
            if "(" in tmp[0] and ")" in tmp[0] and "False" == tmp[1].strip():
                l = self.transformCode(tmp[0])
                codeFunc = True
                b.extend(l)
            elif "(" in tmp[0] and ")" in tmp[0] and "True" == tmp[1].strip():
                l = self.transformCode(tmp[0])
                codeFunc = True
                notTrue = True
                b.extend(l)
            else:
                l = self.replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip().replace("True","1").replace("False","0"))
                l = self.replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip().replace("True","1").replace("False","0"))
                b.append(l)
        elif "<=" in cond:
            l = "(le,<var1>,<var2>)"
            tmp = cond.split('<=')
            tmp[0] = self.replaceTypex3(tmp[0])
            tmp[1] = self.replaceTypex3(tmp[1])
            l = self.replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip())
            l = self.replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip())
            b.append(l)
        elif ">=" in cond:
            l = "(ge,<var1>,<var2>)"
            tmp = cond.split('>=')
            tmp[0] = self.replaceTypex3(tmp[0])
            tmp[1] = self.replaceTypex3(tmp[1])
            l = self.replaceVarWithPlaceholder(l, "<var1>", tmp[0].strip())
            l = self.replaceVarWithPlaceholder(l, "<var2>", tmp[1].strip())
            b.append(l)
        elif "True" == cond or "False" == cond:
            if "True" == cond:
                l = "(eq,1,1)"
            else:
                l = "(eq,1,0)"
            b.append(l)
        else:
            if cond.startswith("not "):
                notTrue = True
                cond = cond[4:]
            l = self.transformCode(cond)
            if len(l[0].strip()) == 0:
                cond = cond.strip()
                if len(cond.split()) == 1:
                    l = ['(eq,\":'+cond+"\",1)"]
            b.extend(l)
            codeFunc = True

        if "not" in b[0] or notTrue:
            if codeFunc:
                b[0] = b[0].replace("(", "(neg|")
            else:
                b[0] = b[0].replace("(", "(neg|").replace(":not ", ":")

        return b


    def readAllTypes(self):
        typesx = dict()
        pathx = "./modules"
        filesAndDirs = os.listdir(pathx)
        for fx in filesAndDirs:
            if os.path.isfile(pathx + "/" + fx):
                typex = fx.split('.')[0]
                typex2 = self.replaceTypex(typex)
                typesx[typex2] = __import__(typex)
        return typesx


    def replaceTypex(self, t):
        s = "ERROR"
        t = t.strip()
        if t in typeDictX:
            s = typeDictX[t]
        return s


    def replaceVarWithPlaceholder(self, line, placeholder, varname):
        if varname in self.registers or varname in self.pos_registers or varname in self.str_registers or self.is_float(varname) or varname.startswith("0x"):
            line = line.replace(placeholder, varname)
        elif '"' in varname and varname.startswith('"') and varname.endswith('"'):
            line = line.replace(placeholder, varname)
        elif varname.startswith("_"):
            if len(varname) > 1:
                if varname[1] != "_":
                    line = line.replace(placeholder, "\":::" + varname[1:] + "\"")
            else:
                line = line.replace(placeholder, "\":unused\"")
        elif varname == "True":
            line = line.replace(placeholder, "1")
        elif varname == "False":
            line = line.replace(placeholder, "0")
        else:
            line = line.replace(placeholder, "\":" + varname + "\"")
        return line


    def resolveOr(self, cond):
        conds = cond.split('|')
        x = len(conds)
        b = []
        for i in range(x):
            l = self.resolveSimpleCondition(conds[i])
            if i < x - 1:
                l[0] = l[0].replace("(", "(this_or_next|")
            b.extend(l)
        return b


    def transformScriptLine(self, scriptLine):
        scriptLine = scriptLine.strip()[4:]
        scriptName = scriptLine.split('(')[0]
        scriptParams = scriptLine.split('(')[1].split(')')[0].split(',')
        b = ["(\"" + scriptName + "\", ["]
        if len(scriptParams[0].strip()) > 0:
            for i, param in enumerate(scriptParams):
                pss = param.strip()
                if pss != "self":
                    if scriptParams[0].strip() == "self":
                        i += 1
                    if pss.startswith("_") and len(pss) > 1:
                        if ScriptConverter.is_trigger_code:
                            b.append("(store_trigger_param, \"$" + pss[1:] + "\", " + str(i + 1) + ")")
                        else:
                            b.append("(store_script_param, \"$" + pss[1:] + "\", " + str(i + 1) + ")")
                    else:
                        if ScriptConverter.is_trigger_code:
                            b.append("(store_trigger_param, \":" + pss + "\", " + str(i + 1) + ")")
                        else:
                            b.append("(store_script_param, \":" + pss + "\", " + str(i + 1) + ")")
                    # TODO: check for regX as param
        return b

    # TODO: actually count these and correctly check
    def transformTryBlock(self, tryCode):
        b = ["(try_begin)"]
        return b


    def transformExceptBlock(self, tryCode):
        b = ["(else_try)"]
        return b


    def conditionListSplit(self, cond, idx):
        tmp = cond.split(' in ')
        varx = tmp[0].strip()
        varName = tmp[1].strip()
        vals = self.cur_lists[varName]
        resx = ""
        for v in vals:
            resx += varx + " == " + v + " |"
        if idx <= 0:
            resx = resx.rstrip('|').rstrip()
        return resx


    def conditionalBlockHead(self, ifCode, b, startIndex=3):
        conditionsLine = ifCode.lstrip()[startIndex:].replace(" and ", " & ").replace(" or ", " | ")
        conditionsLine = conditionsLine.split(':')[0]

        conditions = conditionsLine.split('&')

        extra_conditions = []
        for cond in conditions:
            if " in " in cond:
                condes = cond.split('|')
                x = len(condes)
                for c in condes:
                    x -= 1
                    resx = self.conditionListSplit(c, x)
                    extra_conditions.append(resx)

        conditions.extend(extra_conditions)

        for cond in conditions:
            if "|" in cond:
                condx = self.resolveOr(cond)
            else:
                condx = self.resolveSimpleCondition(cond)
            b.extend(condx)

        return b


    # TODO: actually count these and correctly check
    def transformIfBlock(self, ifCode):
        b = ["(try_begin)"]
        b = self.conditionalBlockHead(ifCode, b)
        return b


    def transformElseIfBlock(self, ifCode):
        b = ["(else_try)"]
        b = self.conditionalBlockHead(ifCode, b, 5)
        return b


    def transformElseBlock(self, code):
        b = ["(else_try)"]
        return b


    def transformForBlock(self, code):
        b = ["(try_for_range, <var1>, <var2>, <var3>)"]
        b[0] = self.replaceVarWithPlaceholder(b[0], "<var1>", code[4:code.index(' in range(')])
        tmp = code.split('(')[1].split(')')[0].split(',')
        if len(tmp) == 2:
            start = tmp[0].strip()
            end = tmp[1].strip()
        elif len(tmp) == 3 and int(tmp[2]) < 0:
            start = tmp[1].strip()
            end = tmp[0].strip()
            b[0] = b[0].replace("try_for_range", "try_for_range_backwards")
        else:
            start = 0
            end = tmp[0].strip()

        b[0] = self.replaceVarWithPlaceholder(b[0], "<var2>", str(start))
        b[0] = self.replaceVarWithPlaceholder(b[0], "<var3>", str(end))

        return b


    def transformForPartiesBlock(self, code):
        b = ["(try_for_parties, <var1>)"]
        b[0] = self.replaceVarWithPlaceholder(b[0], "<var1>", code[4:code.index(' in ')])
        return b


    def transformForAgentsBlock(self, code):
        b = ["(try_for_agents, <var1>)"]
        b[0] = self.replaceVarWithPlaceholder(b[0], "<var1>", code[4:code.index(' in ')])
        return b


    def transformForPlayersBlock(self, code):
        b = ["(try_for_players, <var1>)"]
        b[0] = self.replaceVarWithPlaceholder(b[0], "<var1>", code[4:code.index(' in ')])
        return b


    def transformForPropInstancesBlock(self, code):
        b = ["(try_for_prop_instances, <var1>)"]
        b[0] = self.replaceVarWithPlaceholder(b[0], "<var1>", code[4:code.index(' in ')])
        return b


    def transformWhileBlock(self, whileCode):
        self.while_active = True
        b = [
            "(assign,\":__while_range_end_0__\",1)",
            "(try_for_range,\":unused\",0,\":__while_range_end_0__\")",
        ]
        b = self.conditionalBlockHead(whileCode, b, 6)
        b.append("#while_code_ptr")
        b.append("(val_add,\":__while_range_end_0__\",1)")
        b.append("#(else_try)")
        b.append("# stop while here")
        #b.append("(try_end)")
        return b


    def transformScriptBlock(self, codeBlock : list):
        lastScriptIdx = -1

        ifCl = []

        curIdx = -1
        allCodes = []
        for codeLine in codeBlock:
            code = codeLine
            inlineIndentCount = 0
            curIdx += 1

            coy = []
            while code.startswith("    "):
                code = code[4:]
                inlineIndentCount += 1
            if code.startswith("if "):
                self.fixIndentionProblem(allCodes, ifCl, inlineIndentCount, code)
                coy = self.transformIfBlock(code)
                ifCl.append((inlineIndentCount, code))
            elif code.startswith("elif "):
                coy = self.transformElseIfBlock(code)
            elif code.startswith("else:"):
                coy = self.transformElseBlock(code)
            elif code.startswith("for "):
                self.fixIndentionProblem(allCodes, ifCl, inlineIndentCount, code)
                if " in __all_parties__:" in code:
                    coy = self.transformForPartiesBlock(code)
                elif " in __all_agents__:" in code:
                    coy = self.transformForAgentsBlock(code)
                elif " in __all_players__:" in code:
                    coy = self.transformForPlayersBlock(code)
                elif " in __all_prop_instances__:" in code:
                    coy = self.transformForPropInstancesBlock(code)
                else:
                    coy = self.transformForBlock(code)
                ifCl.append((inlineIndentCount, code))
            elif code.startswith("try:"):
                self.fixIndentionProblem(allCodes, ifCl, inlineIndentCount, code)
                coy = self.transformTryBlock(code)
                ifCl.append((inlineIndentCount, code))
            elif code.startswith("except:"):
                coy = self.transformExceptBlock(code)
            elif code.startswith("while "):
                print("'while' is not fully supported yet!", "\n", "And should only be used with caution!")
                coy = self.transformWhileBlock(code)
                ifCl.append((inlineIndentCount, code))
            elif code.strip() == "break":
                print("WARNING: 'break' is not fully supported yet!")
                idxB = -1
                for_range = False
                for i in range(len(allCodes)-1,-1,-1):
                    if "try_for_" in allCodes[i]:
                        idxB = i
                        if "try_for_range" in allCodes[i]:
                            for_range = True
                        break
                if not for_range:
                    adder = ""
                    for c in allCodes:
                        if "__break" in c and "__\", 1)" in c:
                            while "__break" + adder + "__" in c:
                                adder = str(random.randint(10,100))

                    allCodes.insert(idxB+1, "(eq, \":__break"+adder+"__\", 0)")
                    allCodes.insert(idxB, "(assign, \":__break"+adder+"__\", 0)")
                    coy.append("(assign, \":__break"+adder+"__\", 1)")
                else:
                    last_two = allCodes[idxB].split(',')
                    last_two = [last_two[-1].strip().strip(")"), last_two[-2].strip().strip(")")]
                    if "backwards" in allCodes[idxB]:
                        coy.append("(assign, " + last_two[1] + ", " + last_two[0] + ")")
                    else:
                        coy.append("(assign, " + last_two[0] + ", " + last_two[1] + ")")
            elif code == "continue":
                print("'continue' is not supported!")
            elif code.startswith("def "):
                for _ in ifCl:
                    allCodes.append("(try_end)")
                ifCl.clear()

                if len(allCodes) > 0 and lastScriptIdx >= 0:
                    allCodes.append("])")
                coy = self.transformScriptLine(code)
                lastScriptIdx = curIdx
            elif self.while_active:
                code_ptr = -1
                for i in range(len(allCodes)-1,0,-1):
                    if "#while_code_ptr" == allCodes[i].strip():
                        code_ptr = i
                        break
                if code_ptr >= 0:
                    coy = self.transformCode(code)
                    coy.reverse()
                    for co in coy:
                        allCodes.insert(code_ptr, co)
                coy=[]
            else:
                coy = self.transformCode(code)
                self.fixIndentionProblem(coy, ifCl, inlineIndentCount, code, True)

            for i in range(len(coy)):
                coy[i] = coy[i].replace(":::","$")

            allCodes.extend(coy)

        # TODO: check for try_ends more carefully

        for _ in ifCl:
            allCodes.append("(try_end)")
        ifCl.clear()

        allCodes = [x.rstrip(',') for x in allCodes if x]
        allCodes.append("])")

        return allCodes


    def fixIndentionProblem(self, c, ifCl, inlineIndentCount, code, spec=False):
        xyz = []
        self.while_active = False
        for i, ifx in enumerate(ifCl):
            if inlineIndentCount <= ifx[0] and code.strip() != "":
                xyz.append(i)

        if len(xyz) > 0:
            xyz.reverse()
            for x in xyz:
                del ifCl[x]
                if spec:
                    c.insert(len(c)-1, "(try_end)")
                else:
                    c.append("(try_end)")


    def writeScriptCode(self, f, codeData):
        #codeData = self.optimize(codeData)

        curIndent = 0
        for line in codeData:
            if "else_try" in line or "try_end" in line:
                curIndent -= 1

            for i in range(curIndent):
                f.write("    ")

            f.write(line.split('#')[0].rstrip())

            if "else_try" in line or "try_begin" in line or "try_for" in line:
                curIndent += 1

            if not line.endswith("["):
                f.write(",")
                if "#" in line:
                    tmp = line.split('#')[1].lstrip()
                    f.write(" # " + tmp)

            if line == "])":
                f.write("\n")
            f.write("\n")


    def writeScriptOutputFile(self, codeData):
        with open("./build_system/module_scripts.py", "w") as f:
            f.write("# -*- coding: cp1254 -*-\n")
            f.write("from header_common import *\n")
            f.write("from header_operations import *\n")
            f.write("from module_constants import *\n")
            f.write("from header_parties import *\n")
            f.write("from header_skills import *\n")
            f.write("from header_mission_templates import *\n")
            f.write("from header_items import *\n")
            f.write("from header_triggers import *\n")
            f.write("from header_terrain_types import *\n")
            f.write("from header_music import *\n")
            f.write("from header_map_icons import *\n")
            f.write("from header_presentations import *\n")
            f.write("from ID_animations import *\n\n")

            f.write("scripts = [\n\n")
            self.writeScriptCode(f, codeData)
            f.write("]\n")


    # make this base later for all and create reusable code
    def createCode(self):
        ScriptConverter.is_trigger_code = False
        lines = self.readScriptCode()
        codeLines = self.transformScriptBlock(lines)
        self.writeScriptOutputFile(codeLines)


    def readScriptCode(self):
        lines = []
        with open("./modules/scripts.py") as f:
            for line in f:
                lines.append(line)
        return lines


    def searchOccurancesVarReplace(self, codeData : list, startx : int, varx, data):
        # to start in current function scope
        # only used for script module - not needed for others
        for i in range(startx, 0, -1):
            code = codeData[i]
            if "(\"" in code and "[" in code:
                startx = i + 1
                break

        count = 0
        lastIndex = -1
        for i in range(startx, len(codeData)):
            code = codeData[i]
            if varx in code:
                count += 1
                lastIndex = i
            if "(\"" in code and "[" in code: # to stop at next function and only stay in current function scope
                break

        if count == 2:
            old__data = codeData[lastIndex]
            if "#" in codeData[lastIndex]: # for additional comments
                codeData[lastIndex] = codeData[lastIndex].replace(varx, data) + ", " + varx.strip('"').lstrip(':')
            else:
                codeData[lastIndex] = codeData[lastIndex].replace(varx, data) + " # " + varx.strip('"').lstrip(':')
            return True

        return False


    def findIndexOfCondBlockEnd(self, codeData : list, idx : int):
        try_begin_count = 0
        try_end_count = 0
        for i in range(idx, len(codeData)):
            if "try_begin" in codeData[i]:
                try_begin_count += 1
            elif "try_end" in codeData[i]:
                try_end_count += 1
            if try_end_count == try_begin_count:
                idx = i
                break
        return idx


    def hasPrevIfElseOrNotTrivialBlock(self, codeData : list, startx : int):
        beginx = 0
        # to start in current function scope
        # only used for script module - not needed for others
        for i in range(startx, 0, -1):
            code = codeData[i]
            if "(\"" in code and "[" in code:
                beginx = i + 1
                # print("START:", code)
                break

        open_try = 0
        elseD = dict()
        for i in range(beginx, startx):
            code = codeData[i]
            if "try_begin" in code or "try_for_" in code:
                open_try += 1
            elif "try_end" in code:
                if str(open_try) in elseD:
                    elseD.pop(str(open_try))
                open_try -= 1
            elif "else_try" in code:
                elseD[str(open_try)] = True # optimize this further later on

        for i in range(startx + 1, len(codeData)):
            code = codeData[i]
            if "try_" in code:
                break
            elif "else_try" in code:
                elseD[str(open_try)] = True # optimize this further later on

        hasElse = len(elseD) > 0 or open_try == 0
        if not hasElse:
            startx2 = -1
            skipNextBegin = False
            skippedTrys = 0

            for i in range(startx - 1, 0, -1):
                code = codeData[i]
                if "try_" in code and not "try_end" in code:
                    if not skipNextBegin:
                        startx2 = i
                        break
                    else:
                        skipNextBegin = False
                elif "try_end" in code:
                    skipNextBegin = True
                    skippedTrys += 1

            if startx2 >= 0:
                try_count = 0
                for i in range(startx2, len(codeData)):
                    code = codeData[i]
                    if "(" in code and ")" in code:
                        code = code.split('(')[1].split(')')[0]
                        code = code.split(',')[0].strip()
                        if "try_end" == code:
                            if try_count == 0:
                                break
                            else:
                                try_count -= 1
                        elif "else_try" == code and try_count == 1:
                            hasElse = True
                            break
                        elif "try_begin" in code or "try_for_" in code:
                            try_count += 1

        return hasElse


    def searchFirstCodeOfType(self, codeData : list, codex : str, startx : int = 0):
        remIdx = -1
        for i in range(startx, len(codeData)):
            code = codeData[i]
            if "(" in code and ")" in code:
                code = code.split('(')[1].split(')')[0]
                code = code.split(',')[0].strip()
                if codex == code:
                    remIdx = i
                    break
        return remIdx


    def searchCurClosingTag(self, codeData : list, startx : int = 0):
        remIdx = -1
        try_count = 0
        for i in range(startx, len(codeData)):
            code = codeData[i]
            if "(" in code and ")" in code:
                code = code.split('(')[1].split(')')[0]
                code = code.split(',')[0].strip()
                if "try_end" == code:
                    if try_count == 0:
                        remIdx = i
                        break
                    else:
                        try_count -= 1
                elif "try_begin" in code or "try_for_" in code:
                    try_count += 1
        return remIdx


    def hasRelevance(self, codeData : list, startx : int = 0):
        hasRelevance = False

        startx2 = -1
        skipNextBegin = False
        skippedTrys = 0

        for i in range(startx - 1, 0, -1):
            code = codeData[i]
            if "try_" in code and not "try_end" in code:
                if not skipNextBegin:
                    startx2 = i
                    break
                else:
                    skipNextBegin = False
            elif "try_end" in code:
                skipNextBegin = True
                skippedTrys += 1

        if startx2 >= 0:
            try_count = 0
            for i in range(startx2, len(codeData)):
                code = codeData[i]
                if "(" in code and ")" in code:
                    code = code.split('(')[1].split(')')[0]
                    code = code.split(',')[0].strip()
                    if "try_end" == code:
                        if try_count == 0:
                            break
                        else:
                            try_count -= 1
                            ixx = i + 1
                            if len(codeData) > ixx:
                                if not "try" in codeData[ixx]:
                                    hasRelevance = True
                    elif "try_begin" in code or "try_for_" in code:
                        try_count += 1

        return hasRelevance


    def optimize(self, codeData : list):
        delx = []
        lastCode = ""
        for i, code in enumerate(codeData):
            if "assign" in code:
                tmp = code.rstrip(')').split(',')
                if len(tmp) > 2 and self.is_float(tmp[2]) and not "$" in tmp[1]:
                    if self.searchOccurancesVarReplace(codeData, i, tmp[1], tmp[2]):
                        delx.append(i)
            elif "try_begin" in code:
                if "try_for_" in lastCode:
                    delx.append(i)
                    ix = self.findIndexOfCondBlockEnd(codeData, i)
                    delx.append(ix)
                else:
                    hasElse = self.hasPrevIfElseOrNotTrivialBlock(codeData, i)
                    hasRelevance = self.hasRelevance(codeData, i)
                    if not hasElse and not hasRelevance:
                        remIdx = self.searchCurClosingTag(codeData, i)
                        if remIdx >= 0:
                            delx.append(i)
                            delx.append(remIdx)
            lastCode = code

        delx = list(set(delx)) # fix because of duplicates
        delx.sort()
        delx.reverse()
        for i in delx:
            del codeData[i]
        return codeData

