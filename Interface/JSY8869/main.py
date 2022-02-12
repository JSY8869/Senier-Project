import weather


def main():
    nx, ny = input("nx, ny 입력: ").split()
    weather.how_weather(nx,ny)


if __name__ == '__main__':
    main()