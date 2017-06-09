# THIS CODE IS MULTIPLE ARGUMENT
# WHICH TAKE MAY VALUES


def StudentScore(name, *score):
    print(name)
    print(score)

StudentScore("Suru", 55, 77, 60, 87, 54)


def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(3)
add_numbers(3, 54)
add_numbers(3, 525, 658, 865, 785)
