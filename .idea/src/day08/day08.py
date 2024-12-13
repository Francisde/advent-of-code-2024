import util.util


def solve_part_one(grid):
    antinodes = [["." for x in range(len(grid[0]))] for y in range(len(grid))]
    frequences = get_all_frequences(grid)
    for frequence in frequences:
        coordinates = get_all_coordinates(grid, frequence)
        for point1 in coordinates:
            for point2 in coordinates:
                if point1 != point2:
                    y_diff = point1[0] - point2[0]
                    x_diff = point1[1] - point2[1]
                    mark_y = point1[0] + y_diff
                    mark_x = point1[1] + x_diff
                    if mark_y >= 0 and mark_x >= 0 and mark_y < len(grid) and mark_x < len(grid[0]):
                        antinodes[mark_y][mark_x] = "#"
    result = 0
    for row in antinodes:
        for char in row:
            if char == "#":
                result += 1
    return result

def solve_part_two(grid):
    antinodes = [["." for x in range(len(grid[0]))] for y in range(len(grid))]
    frequences = get_all_frequences(grid)
    for frequence in frequences:
        coordinates = get_all_coordinates(grid, frequence)
        for point1 in coordinates:
            for point2 in coordinates:
                if point1 != point2:
                    y_diff = point1[0] - point2[0]
                    x_diff = point1[1] - point2[1]
                    mark_y = point1[0]
                    mark_x = point1[1]
                    mark = True
                    while mark:
                        mark = False
                        if mark_y >= 0 and mark_x >= 0 and mark_y < len(grid) and mark_x < len(grid[0]):
                            antinodes[mark_y][mark_x] = "#"
                            mark = True
                            mark_y += y_diff
                            mark_x += x_diff
    util.util.print2D(antinodes)
    result = 0
    for row in antinodes:
        for char in row:
            if char == "#":
                result += 1
    return result




def get_all_frequences(grid):
    result = set()
    for row in grid:
        for char in row:
            if char != ".":
                result.add(char)
    return list(result)

def get_all_coordinates(grid, frequence):
    result = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == frequence:
                result.append((y, x))
    return result


file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0
map = []

for line in Lines:
    input_line= line.strip()
    row = list(input_line)
    map.append(row)
    print("Line {}: {}".format(count, input_line))
    count += 1


print("TASK 1 - sol: {}".format(solve_part_one(map)))

print("TASK 2 - sol: {}".format(solve_part_two(map)))
