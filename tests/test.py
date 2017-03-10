import unittest

from zombiegame.entities import (LivingEntity,
                                 Entity,
                                 Item,
                                 Player,
                                 Katana)


class TestEntity(unittest.TestCase):
    def test_create_entity(self):
        entity = Entity(name='Jamal')
        self.assertEqual(entity.name, 'Jamal', msg='Error: Unexpected Entity name')


class TestLivingEntity(unittest.TestCase):
    def test_create_living_entity(self):
        entity = LivingEntity(name='Jamal', hp=1000, damage=20, speed=7)
        self.assertEqual(entity.name, 'Jamal', msg='Error: Unexpected Entity name')
        self.assertEqual(entity.hp, 1000, msg='Error: Unexpected Entity hp Value')
        self.assertEqual(entity.damage, 20, msg='Error: Unexpected Entity damage Value')
        self.assertEqual(entity.speed, 7, msg='Error: Unexpected Entity speed Value')

    def test_attack(self):
        entity1 = LivingEntity(name='player')
        entity2 = LivingEntity(name='zombie')
        expected = entity1.hp - entity2.damage
        entity2.attack(other_entity=entity1)
        result = entity1.hp
        self.assertEqual(result, expected, msg='Error: Unexpected attack result')


class TestPlayer(unittest.TestCase):
    def test_Pickup_Item(self):
        item = Katana()
        player = Player(name='Jamal')
        player.pickup(item=item)
        self.assertEqual(player.get_damage(), 100, msg='Unexpected Weapon effect on Damage')
        self.assertEqual(player.get_speed(), 5, msg='Unexpected Weapon effect on Speed')


class TestItem(unittest.TestCase):
    def test_create_item(self):
        entity = Item(name= 'Katana')
        self.assertEqual(entity.name, 'Katana', msg='Error: Unexpected Entity')

