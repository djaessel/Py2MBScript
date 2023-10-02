# This Python file uses the following encoding: utf-8

from item import Item, ItemType, IModBit


class MBShield(Item):
    def __init__(self, id, name, price):
        super().__init__(id, name, price)

        self.set_type(ItemType.SHIELD)
        self.add_modifier(IModBit.SHIELD)


    def set_width(self, width):
        self.shield_width = width


    def set_height(self, height):
        self.shield_height = height


    def set_body_armor(self, body_armor : int):
        self.body_armor = body_armor


    def set_hit_points(self, hit_points : int):
        self.hit_points = hit_points


    def set_speed(self, speed_rating : int):
        self.speed_rating = speed_rating


