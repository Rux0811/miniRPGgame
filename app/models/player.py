class Player:
    def __init__(self, name="勇者", hp=100, mp=30, attack=20, defense=10):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mp = mp  # MPを追加
        self.max_mp = mp  # 最大MP
        self.attack = attack
        self.defense = defense
        self.defending = False  # 防御フラグ
        self.items = {"MPポーション": 0}  # アイテム管理

    def use_item(self, item_name):
        if item_name == "MPポーション" and self.items[item_name] > 0:
            self.mp = min(self.max_mp, self.mp + 15)
            self.items[item_name] -= 1
            print(f"{self.name} は MPポーションを使った！ (+15 MP)")
        else:
            print("そのアイテムは使えない！")

    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.hp = max(0, self.hp - actual_damage)
        print(f"{self.name} は {actual_damage} ダメージを受けた！")

    def is_alive(self):
        return self.hp > 0  # HPが0より大きければ生存している    
    
    def __str__(self):
        return f"{self.name} - HP: {self.hp}/{self.max_hp}, MP: {self.mp}/{self.max_mp}"


    def use_skill(self, skill_name):
        skills = {
            "火炎斬り": {"mp_cost": 10, "damage": self.attack * 2, "message": "炎をまとった剣で敵を切り裂いた！"},
            "クリティカルヒット": {"mp_cost": 15, "damage": self.attack * 3, "message": "敵の急所を突いた！"},
            "マダンテ": {"mp_cost": 30, "damage": self.attack * 5, "message": "破滅の魔法を唱えた！"},
            "瞑想": {"mp_cost": 0, "mp_recover": 15, "message": "精神を集中し、MPを回復した！"}  # 新スキル
        }

        if skill_name in skills:
            skill = skills[skill_name]

            # MP回復スキルの場合
            if "mp_recover" in skill:
                self.mp = min(self.max_mp, self.mp + skill["mp_recover"])
                print(f"{self.name} は {skill_name} を使った！ {skill['message']} (+{skill['mp_recover']} MP)")
                return None  # 攻撃ではないのでダメージなし

            # 通常の攻撃スキル
            if self.mp >= skill["mp_cost"]:
                self.mp -= skill["mp_cost"]
                print(f"{self.name} は {skill_name} を使った！ {skill['message']}")
                return skill["damage"]
            else:
                print(f"MPが足りない！{skill_name} を使えない！")
                return None  # スキル発動不可
        return None  # 存在しないスキル
