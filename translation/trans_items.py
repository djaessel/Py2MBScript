# This Python file uses the following encoding: utf-8

import os

import sys
sys.path.append("../modules/")

from translator import Translator
import items as itm

languages_dir = "./build_system/languages"


class ItemTranslator(Translator):
    def __init__(self, language : str):
        super().__init__(language, "item_kinds", "itm")


def createTranslations():
    # Initialize Translators
    locale = dict()
    for d in os.listdir(languages_dir):
        if os.path.isdir(os.path.join(languages_dir, d)):
            locale[d] = ItemTranslator(d)
    # -------------------------------------------------------------------------

    # no_item - INVALID ITEM
    # -------------------------------------------------------------------------
    locale["de"].translate(itm.no_item.id, "UNGÜLTIGER GEGENSTAND")
    locale["de"].translate(itm.no_item.id + "_pl", "UNGÜLTIGER GEGENSTAND")
    locale["cz"].translate(itm.no_item.id, "NEPLATNÁ POLOŽKA")
    locale["cz"].translate(itm.no_item.id + "_pl", "NEPLATNÁ POLOŽKA")
    locale["es"].translate(itm.no_item.id, "OBJETO INVALIDO")
    locale["es"].translate(itm.no_item.id + "_pl", "OBJETOS INVALIDOS")
    locale["fr"].translate(itm.no_item.id, "OBJET INVALIDE")
    locale["fr"].translate(itm.no_item.id + "_pl", "OBJETS INVALIDES")
    locale["hu"].translate(itm.no_item.id, "NEM MEGFELELŐ TÁRGY")
    locale["hu"].translate(itm.no_item.id + "_pl", "NEM MEGFELELŐ TÁRGY")
    locale["pl"].translate(itm.no_item.id, "NIEPRAWIDŁOWY PRZEDMIOT")
    locale["pl"].translate(itm.no_item.id + "_pl", "NIEPRAWIDŁOWY PRZEDMIOT")
    # -------------------------------------------------------------------------

    ### ADD TRANSLATIONS BELOW THIS POINT ###


    # TODO: add more item translations


    ### ADD TRANSLATIONS ABOVE THIS POINT ###

    # items_end - Items End
    # -------------------------------------------------------------------------
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Saving all translations
    for l in locale:
        locale[l].save()

