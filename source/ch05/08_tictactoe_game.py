# 08_tictactoe_game.py - 函式綜合應用：雙人井字棋遊戲 (Tic Tac Toe)

# 初始化棋盤 (以 1-9 的數字代表空位，方便玩家對應輸入)
board = [str(i) for i in range(1, 10)]

def draw_board():
    """繪製目前棋盤狀態"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(player):
    """檢查傳入的 player (O 或 X) 是否贏得遊戲"""
    # 八種可能的連線連成一線
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # 橫線
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # 直線
        [0, 4, 8], [2, 4, 6]             # 對角線
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False

def play_game():
    """遊戲主流程"""
    current_player = "O"
    steps = 0
    draw_board()
    
    while steps < 9:
        move = input(f"輪到玩家 {current_player}，請輸入棋格位置 (1-9): ")
        if not move.isdigit() or int(move) < 1 or int(move) > 9:
            print("⚠️ 格式錯誤！請輸入 1 至 9 之間的整數數字。")
            continue
            
        index = int(move) - 1
        if board[index] in ["O", "X"]:
            print("⚠️ 該位置已經有棋子了，請選擇別的位置！")
            continue
            
        # 落子
        board[index] = current_player
        steps += 1
        draw_board()
        
        # 檢查是否獲勝
        if check_win(current_player):
            print(f"🎉 恭喜玩家 {current_player} 贏得了遊戲！")
            return
            
        # 切換玩家
        current_player = "X" if current_player == "O" else "O"
        
    print("平手！這場精彩的對局結束了。")

if __name__ == "__main__":
    print("====== 井字棋遊戲開始 ======")
    play_game()
