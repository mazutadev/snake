import os
import random
import time

from pynput import keyboard


# def function game area, generated and visualise

def generate_game_area(x: int, y: int) -> list:
    return [["[ ]" for _ in range(x)] for _ in range(y)]


def visualise_game_area(area: list) -> None:
    for row in area:
        for column in row:
            print(column, end="")
        print()


def find_max_position(area: list) -> tuple[int, int]:
    max_x_position = len(area[0]) - 1
    max_y_position = len(area) - 1

    size = (max_x_position, max_y_position)

    return size


def set_position(x: int, y: int, length: int, area: list):
    x_position = x  # 4
    y_position = y  # 0

    max_position = len(area) - 1

    if y_position > max_position:
        y_position = 0

    for i in range(y_position, y_position + length):  # 4
        area[i][x] = " ■ "


def del_position(x: int, y: int, area: list):
    area[y][x] = "[ ]"


def move_vector_snake(key, game_area):
    if key.name == "up":
        visualise_game_area(game_area)
    elif key.name == "down":
        print("Key.down")


def on_press_key(key):
    game_area = generate_game_area(5, 5)
    move_vector_snake(key, game_area)


def main():
    # listener = keyboard.Listener(on_press=on_press_key)
    # listener.start()

    move_directions = ("left", "right", "up", "down")

    move_button = "down"

    game_area = generate_game_area(10, 10)
    max_x_position, max_y_position = find_max_position(game_area)
    snake_length = 4

    position_x = int(len(game_area[0]) / 2 - 1)
    position_y = int(len(game_area) / 2)

    set_position(position_x, position_y, snake_length, game_area)

    while True:
        # move_button = random.choice(move_directions)
        os.system("clear")
        visualise_game_area(game_area)
        del_position(position_x, position_y, game_area)

        if move_button == "up":
            position_y -= 1

            if position_y < 0:
                position_y = max_y_position

            for i in range(snake_length):
                set_position(position_x, position_y, snake_length, game_area)

        if move_button == "down":
            position_y += 1

            if position_y > max_y_position:
                position_y = 0

            set_position(position_x, position_y, snake_length, game_area)

        if move_button == "right":
            position_x += 1

            if position_x > max_x_position:
                position_x = 0

            set_position(position_x, position_y, snake_length, game_area)

        if move_button == "left":
            position_x -= 1

            if position_x < 0:
                position_x = max_x_position

            set_position(position_x, position_y, snake_length, game_area)

        time.sleep(0.1)


if __name__ == "__main__":
    main()
