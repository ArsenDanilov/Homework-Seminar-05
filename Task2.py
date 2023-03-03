import random


def chose_player():  
    print("Выбор первого хода")
    print("Загадайте число от 1 до 10")
    print("Первым ходит тот игрок, у которого больше число")
    player_move = random.randint(0, 1)  
    print(player_move)
    candles_game()


def candles_game(): 
    candles = 150
    max_candles_move = 28
    player_move = 0
    while candles:
        player = int(
            input(f"Ход игрока {player_move + 1}, выберите количество конфет от 1 до 28: "))
        if candles >= player <= max_candles_move:
            candles = candles - player
            print("Конфет осталось: ", candles)
            player_move = 0 if player_move else 1
        else:
            print("Нельзя выбрать больше 28 конфет")

            continue
    print("Выиграл игрок: ", 1 if player_move else 2)


def main():
    chose_player()


if __name__ == "__main__":
    main()