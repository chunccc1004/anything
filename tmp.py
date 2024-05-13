from turtle import *


def rect(width, height, fill_color, angle=0.0):
    if fill_color:
        fillcolor(fill_color)
    begin_fill()
    rt(angle)
    for _ in range(2):
        fd(width)
        rt(90)
        fd(height)
        rt(90)
    lt(angle)
    end_fill()


# 별그리기
def star(l, fill_color):
    if fill_color:
        fillcolor(fill_color)
    setheading(0)
    begin_fill()
    for i in range(5):
        fd(l)
        rt(144)
        fd(l)
        lt(144)
        rt(360 / 5)
    end_fill()


def maple(t):
    setheading(0)
    switch = 1
    if t != "left":
        switch = -1
    rt(switch * 180)
    fd(switch * 4)
    rt(switch * 88.49)
    fd(switch * 38.01)
    rt(switch * (-45))
    fd(switch * 4.24)
    lt(switch * (45 + 11.44))
    fd(switch * 38.64)
    rt(switch * (11.44 + 110.6))
    fd(switch * 17.09)
    lt(switch * (20.6 + 39))
    fd(switch * 54.04)
    rt(switch * (141 - 24.4))
    fd(switch * 12.08)
    lt(switch * (108.43 - 24.4))
    fd(switch * 28.46)
    rt(switch * (180 - 71.57 + 21.31))
    fd(switch * 25.5)
    lt(switch * (21.31 + 68.96))
    fd(switch * 13.93)
    rt(switch * (68.96 + 47.47))
    fd(switch * 27.59)
    lt(switch * (11.31 + 47.47))
    fd(switch * 5.1)
    lt(switch * 100.62)
    fd(switch * 48.84)
    rt(switch * (100.62 + 29.36))
    fd(switch * 18.36)
    lt(switch * (62.65 + 29.36))
    fd(switch * 28)


def nuw_zealand():
    # 기본 설정
    speed(1)
    width(1)
    penup()
    goto(-200, 100)

    # 플래그 기본 사각형, 배경 그리기
    pendown()
    color('#012169')
    rect(400, 200, '#012169')
    penup()

    # 흰색 십자가 + X 그리기
    color('#FFFFFF')
    # 가로
    goto(-200, 67)
    pendown()
    rect(198, 32, '#FFFFFF')
    penup()
    # 세로
    goto(-84, 100)
    pendown()
    rect(99, 32, '#FFFFFF', 90)
    penup()
    # 흰색 대각선들은 사각형을 이용할 수 없음. 하드코딩
    goto(-200, 100)
    pendown()
    begin_fill()
    for _ in range(2):
        fd(23)
        rt(26.19)
        fd(195)
        rt(90 - 26.19)
        fd(11)
        rt(90)
    end_fill()
    penup()
    goto(-2, 100)
    lt(180)
    pendown()
    begin_fill()
    for _ in range(2):
        fd(23)
        lt(26.19)
        fd(195)
        lt(90 - 26.19)
        fd(11)
        lt(90)
    end_fill()
    lt(180)
    penup()

    # 빨간 선
    color('#C8102E')
    # 가로
    goto(-200, 60)
    pendown()
    rect(198, 18, '#C8102E')
    penup()
    # 세로
    goto(-91, 100)
    pendown()
    rect(99, 18, '#C8102E', 90)
    penup()
    # 빨간색 대각선들은 사각형을 이용할 수 없음. 하드코딩
    # 좌측 위 <-> 우측 아래 대칭 // 우측 위 <-> 좌측 아래 대칭
    # 좌측 위
    goto(-200, 100)
    pendown()
    begin_fill()
    rt(26.57)
    fd(72)
    lt(180 + 26.57)
    fd(15)
    rt(26.57)
    fd(56.8)
    rt(90 - 26.57)
    fd(8)
    rt(90)
    end_fill()
    penup()
    # 우측 아래
    goto(-3, 3)
    pendown()
    begin_fill()
    rt(180 + 26.57)
    fd(72)
    lt(180 + 26.57)
    fd(15)
    rt(26.57)
    fd(56.8)
    rt(90 - 26.57)
    fd(8)
    lt(90)
    end_fill()
    penup()
    # 좌측 아래
    goto(-200, 3)
    pendown()
    begin_fill()
    for _ in range(2):
        fd(15)
        lt(180 - 153.79)
        fd(70)
        rt(360 - 153.79)
    end_fill()
    penup()
    # 우측 위
    goto(-1, 100)
    pendown()
    begin_fill()
    rt(180)
    for _ in range(2):
        fd(15)
        lt(180 - 153.79)
        fd(70)
        rt(360 - 153.79)
    end_fill()
    rt(180)
    penup()

    # 별들 그리기
    infos = [{'xy': (39, 18), 'l': 12}, {'xy': (85, 65), 'l': 12}, {'xy': (126, 30), 'l': 11}, {'xy': (83, -56), 'l': 14}, ]
    for info in infos:
        goto(info['xy'])
        pendown()
        color('#FFFFFF')
        star(info['l'], '#C80F2D')
        penup()

    hideturtle()
    done()


def taiwan():
    # 기본 설정
    speed(100)
    width(1)

    # 플래그 배경
    penup()
    goto(-200, 100)
    pendown()
    color('#FE0000')
    rect(400, 266.39, '#FE0000')
    color('#000096')
    rect(200, 133, '#000096')
    penup()
    # 사자 갈퀴 그리기
    goto(-100, 85)
    color('#FFFFFF')
    pendown()
    rt(78.5)
    begin_fill()
    for _ in range(12):
        fd(25.51)
        lt(78.5 + 48.5)
        fd(25.51)
        rt(48.5 + 108.5)
    end_fill()
    penup()
    # 삼각형 곡선 만들기
    goto(-127, 34)
    pendown()
    color('#000096', '#000096')
    begin_fill()
    circle(27.5)
    end_fill()
    penup()
    # 하얀 원 채우기
    goto(-123.5, 35)
    pendown()
    color('#FFFFFF', '#FFFFFF')
    begin_fill()
    circle(24)
    end_fill()

    hideturtle()
    done()


def canada():
    # 기본 설정
    speed(1000)
    width(1)
    penup()
    CANADA_RED = '#D52B1E'

    # 플래그 기본 사각형, 배경 그리기
    goto(-200, 100)
    pendown()
    color(CANADA_RED)
    rect(400, 200, CANADA_RED)
    penup()
    goto(-100, 100)
    pendown()
    color('#FFFFFF')
    rect(200, 200, '#FFFFFF')
    penup()

    # 나뭇잎 그리기
    # 튀어나온 부분의 크기 다름 -> 하드코딩 필요
    # 좌우 대칭이므로 왼쪽 그리고 대칭으로 오른쪽 그리도록 구현
    color(CANADA_RED)
    fillcolor(CANADA_RED)
    goto(-1, -84)
    pendown()
    begin_fill()
    maple('left')
    penup()
    goto(0, -84)
    pendown()
    maple('right')
    end_fill()

    hideturtle()
    done()
