class Entity(object):
    def __init__(self, name):
        self.name = name


class LivingEntity(Entity):
    def __init__(self, name, hp=100, damage=20, speed=5):
        super().__init__(name=name)
        self.hp = hp
        self.damage = damage
        self.speed = speed

    def attack(self, other_entity):
        other_entity.hp -= self.damage


class Player(LivingEntity):
    def __init__(self, name):
        super().__init__(name=name, hp=1000, damage=20, speed=7)
        self.item = None
        self.dmg_mod = 0
        self.spd_mod = 0

    def get_speed(self):
        return self.speed + self.spd_mod

    def get_damage(self):
        return self.damage + self.dmg_mod

    def pickup(self, item):
        if self.item is None:
            self.item = item
            self.item.effect(player=self)


class Item(Entity):
    def __init__(self, name):
        super().__init__(name=name)


class Weapon(Item):
    def __init__(self, name, damage, speed):
        super().__init__(name=name)
        self.damage = damage
        self.speed = speed

    def effect(self, player):
        player.dmg_mod += self.damage
        player.spd_mod += self.speed


class Katana(Weapon):
    def __init__(self):
        super().__init__(name='Katana', damage=80, speed=-2)


class Nunchucku(Weapon):
    def __init__(self):
        super().__init__(name='Nunchucks', damage=20, speed=0)


class Boost(Item):
    def __init__(self, name, hp, damage, speed):
        super().__init__(name=name)
        self.hp = hp
        self.damage = damage
        self.speed = speed

    def effect(self, player):
        player.spd_mod += self.speed
        player.hp += self.hp


class SpeedBoost(Boost):
    def __init__(self):
        super().__init__(name='Speed Boost', hp=0, damage=0, speed=5)


class HPBoost(Boost):
    def __init__(self):
        super().__init__(name='HP Boost', hp=10, damage=0, speed=0)


