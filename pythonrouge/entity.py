class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x, y, char, color, hp, defence):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.hp = hp
        self.defence = defence 

    def move(self, dx, dy):
        # Move the entity by a given amount
        self.x += dx
        self.y += dy

    def take_damage(self, dmg):
        if (dmg > self.defence):
            self.hp -= dmg - self.defence