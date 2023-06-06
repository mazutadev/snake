# def function game area, generated and visualise

def generate_game_area(width: int, length: int) -> list:
    return [[" " for _ in range(width)] for _ in range(length)]


def visualise_game_area(area: list) -> None:
    for row in area:
        for column in row:
            print(column, end="")
        print()


def main():
    pass


if __name__ == "__main__":
    main()
