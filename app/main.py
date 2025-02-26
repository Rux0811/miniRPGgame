from core.game_manager import GameManager


def title_screen():
    print("\n=================================")
    print("      🏆 ミニRPGアリーナ 🏆")
    print("=================================")
    print("\n📜 ストーリー 📜")
    print("あなたは勇敢な冒険者。ダンジョンに潜む強敵を倒し、")
    print("最深部に待つドラゴンを討伐することが使命だ！")
    print("\n=== メニュー ===")
    print("1) ゲーム開始")
    print("2) オプション")
    print("3) 終了")

    choice = input("\n選択してください: ")

    if choice == "1":
        game = GameManager()
        game.start_game()
    elif choice == "2":
        show_options()
    elif choice == "3":
        print("\n🔚 ゲームを終了します。")
        exit()
    else:
        print("\n⚠ 無効な入力です。もう一度選んでください。")
        title_screen()  # 再表示

def show_options():
    print("\n=== 🎮 オプション 🎮 ===")
    print("🔹 操作方法")
    print("・戦闘では「攻撃」「スキル」「防御」「アイテム」などを選択して戦います。")
    print("・MPを消費することで強力なスキルを使えます。")
    print("・HPやMPが減ったらアイテムを使って回復しましょう！")
    print("\n🔹 ゲームの目的")
    print("・強敵を倒しながらダンジョンを進み、最深部のドラゴンを討伐することが目標です！")
    
    input("\n🔙 [Enter]キーを押してタイトル画面に戻る")
    title_screen()

# 🔽 ここで title_screen() を呼び出す！
if __name__ == "__main__":
    title_screen()