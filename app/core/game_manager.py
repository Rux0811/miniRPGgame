from models.player import Player
from models.monster import get_random_monster
from core.battle_manager import BattleManager
from core.stage_data import STAGES

class GameManager:
    def __init__(self):
        self.player = Player()
        self.current_stage = 0

    def start_game(self):
        print("\n=== RPGアドベンチャー開始！ ===")
        self.next_stage()

    def next_stage(self):
        if self.current_stage >= len(STAGES):
            self.game_clear()
            return

        stage_info = STAGES[self.current_stage]
        print(f"\n=== {stage_info['name']} ===")
        print(stage_info["story_start"])

        enemy = get_random_monster(stage_info["enemy_type"])
        print(f"【敵出現！】{enemy.name} が現れた！")

        battle = BattleManager(self.player, enemy)
        battle.start_battle()

        if self.player.is_alive():
            print(stage_info["story_end"])
            self.current_stage += 1
            self.next_stage()
        else:
            self.game_over()

    def game_clear(self):
        print("\n=== 🎉 おめでとう！ダンジョンを攻略した！ 🎉 ===")

    def game_over(self):
        print("\n=== 💀 ゲームオーバー 💀 ===")

        while True:
            print("\n1) リトライ")
            print("2) ゲームを終了")

            choice = input("選択してください: ")

            if choice == "1":
                print("\n🏆️ 再挑戦します！")
                self.__init__() # ゲームマネージャーをリセット
                self.start_game()  # 再スタート
                break
            elif choice == "2":
                print("\n🔚 ゲームを終了します。")
                exit()
            else:
                print("⚠ 無効な入力です。もう一度選んでください。")
                