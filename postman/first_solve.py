from itertools import permutations
from math import inf


def calculate_distance(point_1, point_2):
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


def short_way(lst, start):
    min_total_distance = inf
    min_out = ''
    for order in permutations(lst):
        prev_point = start
        out = str(start)
        total_distance = 0
        for point in order:
            total_distance += calculate_distance(prev_point, point)
            out += ' -> ' + str(point) + '[' + str(total_distance) + ']'
            prev_point = point
        total_distance += calculate_distance(prev_point, start)
        out += ' -> ' + str(start) + '[' + str(total_distance) + ']'
        if total_distance < min_total_distance:
            min_total_distance = total_distance
            min_out = out

    return min_out + ' = ' + str(min_total_distance)


start_point = (0, 2)
lst_points = [
    (2, 5),
    (5, 2),
    (6, 6),
    (8, 3)
]

start_point_2 = (0, 1)
lst_points_2 = [
    (1, 4),
    (4, 1),
    (5, 5),
    (7, 2),
]

if __name__ == '__main__':
    print(short_way(lst_points, start_point))
    print(short_way(lst_points_2, start_point_2))
