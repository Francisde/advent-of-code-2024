def solve_part_one(grid):
    # find all 0
    trainheads = find_all_trailheads(grid)
    score = 0
    for trainhead in trainheads:
        result = get_trailhead_score(grid, trainhead[0], trainhead[1])
        score += len(set(result))
    return score

def solve_part_two(grid):
    # find all 0
    trainheads = find_all_trailheads(grid)
    score = 0
    for trainhead in trainheads:
        result = get_trailhead_ranking(grid, trainhead[0], trainhead[1], "")
    return len(set(rankings))

def get_trailhead_score(grid, current_y, current_x):
    result = []
    if grid[current_y][current_x] == 9:
        return [(current_y, current_x)]
    current_value = grid[current_y][current_x]
    if current_y > 0:
        if grid[current_y - 1][current_x] == current_value + 1:
            result += get_trailhead_score(grid, current_y - 1, current_x)
    if current_y < len(grid) - 1:
        if grid[current_y + 1][current_x] == current_value + 1:
            result += get_trailhead_score(grid, current_y + 1, current_x)
    if current_x > 0:
        if grid[current_y][current_x - 1] == current_value + 1:
            result += get_trailhead_score(grid, current_y, current_x - 1)
    if current_x < len(grid[current_y]) - 1:
        if grid[current_y][current_x + 1] == current_value + 1:
            result += get_trailhead_score(grid, current_y, current_x + 1)
    return result

rankings = []
def get_trailhead_ranking(grid, current_y, current_x, way):
    result = []
    if grid[current_y][current_x] == 9:
        way += "-{}.{}".format(current_y, current_x)
        rankings.append(way)
        return [(current_y, current_x)]
    current_value = grid[current_y][current_x]
    way += "-{}.{}".format(current_y, current_x)
    if current_y > 0:
        if grid[current_y - 1][current_x] == current_value + 1:
            result += get_trailhead_ranking(grid, current_y - 1, current_x, way)
    if current_y < len(grid) - 1:
        if grid[current_y + 1][current_x] == current_value + 1:
            result += get_trailhead_ranking(grid, current_y + 1, current_x, way)
    if current_x > 0:
        if grid[current_y][current_x - 1] == current_value + 1:
            result += get_trailhead_ranking(grid, current_y, current_x - 1, way)
    if current_x < len(grid[current_y]) - 1:
        if grid[current_y][current_x + 1] == current_value + 1:
            result += get_trailhead_ranking(grid, current_y, current_x + 1, way)
    return result


def find_all_trailheads(grid):
    result = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                result.append((y, x))
    return result
file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0

map = []

for line in Lines:
    input_line= line.strip()
    map.append(list(input_line))
    print("Line {}: {}".format(count, input_line))
    count += 1

int_map = []
for row in map:
    int_row = []
    for char in row:
        if char == ".":
            int_row.append(-1)
        else:
            int_row.append(int(char))
    int_map.append(int_row)


print("TASK 1 - sol: {}".format(solve_part_one(int_map)))

print("TASK 2 - sol: {}".format(solve_part_two(int_map)))
