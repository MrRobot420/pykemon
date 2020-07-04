
class Pokemon:

    def __init__(self, health, attacks, appearance, effect):
        self.health = health
        self.attacks = attacks
        self.level = 1
        self.appearance = appearance
        self.effect = effect
        self.alive = True