from models import Subject

# 参数 time: 第几周/(星期几-1)/时/分
test_data = [
    (1, 4-1, 16, 20),
    (1, 3-1, 19, 20),
    (1, 3-1, 7, 20),
    (1, 3-1, 8, 20),
    (1, 4-1, 17, 20),
    (1, 1-1, 9, 20),
    (1, 5-1, 7, 20),
    (1, 5-1, 18, 20),
    (1, 2-1, 18, 20),
    (2, 2-1, 18, 20),
]


def benchmark():
    for d in test_data:
        day = d[1] + 1
        clock = f'{d[2]}:{d[3]}'
        s = Subject.next(d)
        r = f'**********************************\n'\
            f'现在是 星期 {day}, 北京时间 {clock}\n' \
            f'下一节课:\n'\
            f'{s.get("name")}\n'\
            f'**********************************'
        print(r)

# def ():
