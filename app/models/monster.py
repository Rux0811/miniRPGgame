import random

class Monster:
    def __init__(self, name="スライム", hp=50, attack=15, defense=5):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)  # 防御力を考慮しつつ最低1ダメージ
        self.hp = max(0, self.hp - actual_damage)  # HPが0未満にならないようにする
        print(f"{self.name} は {actual_damage} ダメージを受けた！")


    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name} - HP: {self.hp}/{self.max_hp}"


# モンスターのリスト
MONSTER_TYPES = {
    "slime": {"name": "スライム", "hp": 40, "attack": 10, "defense": 3},
    "goblin": {"name": "ゴブリン", "hp": 65, "attack": 15, "defense": 6},
    "dragon": {"name": "ドラゴン", "hp": 150, "attack": 30, "defense": 12}
}

def get_random_monster(enemy_type):
    monster_data = MONSTER_TYPES.get(enemy_type, MONSTER_TYPES["slime"])
    return Monster(**monster_data)