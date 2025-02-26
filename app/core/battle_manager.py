import time
import random
from models.player import Player
from models.monster import Monster

class BattleManager:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster
        self.turn_count = 1 # ターン数を追加

    def start_battle(self):
        print("\n=== バトル開始！ ===")
        while self.player.is_alive() and self.monster.is_alive():
            print(f"\n===== ターン {self.turn_count} =====")  # ターン数を表示
            self.execute_turn()
            self.turn_count += 1  # ターン数を増やす

        self.display_battle_result()

    def execute_turn(self):
        print("\n--- ターン開始 ---")
        print(self.player)
        print(self.monster)

        # プレイヤの行動選択
        self.player_action()
        if not self.monster.is_alive():
            return #モンスターが倒れたら終了
        
        # モンスターの攻撃
        self.monster_attack()

    def player_action(self):
        print("\nあなたのターン！")
        print("1)攻撃")
        print("2)スキルを使う")
        print("3)防御")
        print("4)回復")
        print("5)アイテムを使う")  # アイテム追加

        choice = input("行動を選択してください")

        if choice == "1":
            self.player_attack()
        elif choice == "2":
            self.use_skill()
        elif choice == "3":
            self.defend()
        elif choice == "4":
            self.heal()
        elif choice == "5":
            self.use_item()  # アイテム使用メソット   
        else:
            print("無効な入力です。攻撃を行います")
            self.player_attack()    


    def player_attack(self):
        print("\nあなたのターン！")
        base_damage = self.player.attack
        damage_variation = random.randint(-5, 5)  # -5 から +5 の範囲でブレる
        final_damage = max(1, base_damage + damage_variation)  # 最低1ダメージは保証
        print(f"{self.player.name} の攻撃！ {self.monster.name} に {final_damage} ダメージを与えようとした！")
        self.monster.take_damage(final_damage)

    def use_skill(self):
        print("\n使用できるスキル:")
        print("1) 火炎斬り (MP 10消費, 大ダメージ)")
        print("2) クリティカルヒット (MP 15消費, 超大ダメージ)")
        print("3) マダンテ (MP 30消費,特大ダメージ)")
        print("4) 瞑想 (MPを10回復)")
        print("5) キャンセル")

        choice = input("スキルを選択してください: ")

        if choice == "1":
            damage = self.player.use_skill("火炎斬り")
        elif choice == "2":
            damage = self.player.use_skill("クリティカルヒット")
        elif choice == "3":
            damage = self.player.use_skill("マダンテ")
        elif choice == "4":
            damage = self.player.use_skill("瞑想")  # MP回復スキル
            return  # 瞑想は攻撃しないのでターン終了    
        else:
            print("スキル使用をキャンセルしました。")
            return

        if damage:
            self.monster.take_damage(damage)

    def defend(self):
        print(f"{self.player.name} は防御態勢を取った！")
        self.player.defending = True  # 防御フラグを立てる

    def heal(self):
        heal_amount = 10
        if self.player.hp == self.player.max_hp:
            print(f"{self.player.name} のHPは満タンだ！回復の必要がない。")
        else:
            self.player.hp = min(self.player.max_hp, self.player.hp + heal_amount)
            print(f"{self.player.name} は {heal_amount} HP 回復した！")

    def use_item(self):
        print("\n使用可能なアイテム:")
        for item, quantity in self.player.items.items():
            print(f"{item}: {quantity}個")

        item_name = input("使用するアイテムを選択してください（キャンセル: 0）: ")

        if item_name == "0":
            print("アイテム使用をキャンセルしました。")
            return

        if item_name in self.player.items and self.player.items[item_name] > 0:
            self.player.use_item(item_name)  # Playerクラスの `use_item` を呼び出す
        else:
            print("そのアイテムは使えません！")

    def monster_attack(self):
        print("\nモンスターのターン！")

        # モンスターの行動をランダムに決定
        action = random.choice(["attack", "strong_attack", "heal"])

        if action == "attack":
            self.normal_attack()
        elif action == "strong_attack":
            self.strong_attack()
        elif action == "heal":
            self.monster_heal()

    def normal_attack(self):
        base_damage = self.monster.attack
        damage_variation = random.randint(-3, 3)
        final_damage = max(1, base_damage + damage_variation)

        # プレイヤーが防御中ならダメージを半減
        if self.player.defending:
            final_damage //= 2
            print(f"{self.player.name} は防御している！ダメージが半減！")
            self.player.defending = False  # 防御フラグをリセット

        print(f"{self.monster.name} の攻撃！ {self.player.name} に {final_damage} ダメージを与えようとした！")
        self.player.take_damage(final_damage)

    def strong_attack(self):
        base_damage = self.monster.attack * 1.5  # 通常攻撃の1.5倍
        damage_variation = random.randint(-5, 5)
        final_damage = max(1, int(base_damage + damage_variation))

        # プレイヤーが防御中ならダメージを半減
        if self.player.defending:
            final_damage //= 2
            print(f"{self.player.name} は防御している！しかし、強攻撃のため一部ダメージを受ける！")
            self.player.defending = False  # 防御フラグをリセット

        print(f"{self.monster.name} の強攻撃！ {self.player.name} に {final_damage} ダメージを与えようとした！")
        self.player.take_damage(final_damage)

    def monster_heal(self):
        heal_amount = random.randint(5, 15)  # 5～15の範囲で回復
        if self.monster.hp == self.monster.max_hp:
            print(f"{self.monster.name} は休憩しようとしたが、HPは満タンだ！")
        else:
            self.monster.hp = min(self.monster.max_hp, self.monster.hp + heal_amount)
            print(f"{self.monster.name} は休憩し、{heal_amount} HP 回復した！")


    def display_battle_result(self):
        print("\n=== バトル終了 ===")
        if self.player.is_alive():
            print(f"{self.player.name} の勝利！")

            #  ランダムでMPポーションを獲得（50％の確率）
            if random.random() < 0.5:
                self.player.items["MPポーション"] += 1
                print("🏆 MPポーションを獲得した")
                
        else:
            print(f"{self.monster.name} に敗北した...")
