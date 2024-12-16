def solve_part_one(grid, moves):
    cur_y, cur_x = found_init(grid)

    for move in moves:
        #print_grid(grid)
        #print("next move: {}, cur_y: {}, cur_x: {}".format(move, cur_y, cur_x))
        #input("weiter")
        if move == "<":
            if grid[cur_y][cur_x - 1] == "#":
                continue
            if grid[cur_y][cur_x - 1] == ".":
                cur_x -=1
                continue
            if grid[cur_y][cur_x - 1] == "O":
                res = bounce(grid, cur_y, cur_x, "<")
                if res:
                    cur_x -= 1
                    continue

        if move == "^":
            if grid[cur_y -1][cur_x ] == "#":
                continue
            if grid[cur_y - 1][cur_x] == ".":
                cur_y -=1
                continue
            if grid[cur_y - 1][cur_x] == "O":
                res = bounce(grid, cur_y, cur_x, "^")
                if res:
                    cur_y -= 1
                    continue
        if move == ">":
            if grid[cur_y][cur_x + 1] == "#":
                continue
            if grid[cur_y][cur_x + 1] == ".":
                cur_x += 1
                continue
            if grid[cur_y][cur_x + 1] == "O":
                res = bounce(grid, cur_y, cur_x, ">")
                if res:
                    cur_x += 1
                    continue
        if move == "v":
            if grid[cur_y + 1][cur_x] == "#":
                continue
            if grid[cur_y + 1][cur_x] == ".":
                cur_y +=1
                continue
            if grid[cur_y + 1][cur_x] == "O":
                res = bounce(grid, cur_y, cur_x, "v")
                if res:
                    cur_y += 1
                    continue
    print_grid(grid)
    return get_gps(grid)

def found_init(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@":
                grid[y][x] = "."
                return y, x

def print_grid(grid):
    for row in grid:
        print(row)

def get_gps(grid):
    result = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "O":
                result += (100 * y + x)
    return result
def bounce(grid, current_y, current_x, direction):
    print("bounce")
    if direction == "^":
        for i in range(current_y -1, 0, -1):

            if grid[i][current_x] == "#":
                return False
            if grid[i][current_x] == ".":
                grid[i][current_x] = "O"
                grid[current_y - 1][current_x] = "."
                return True
    if direction == "v":
        for i in range(current_y + 1, len(grid)):

            if grid[i][current_x] == "#":
                return False
            if grid[i][current_x] == ".":
                grid[i][current_x] = "O"
                grid[current_y + 1][current_x] = "."
                return True
    if direction == ">":
        for i in range(current_x + 1, len(grid[current_y])):

            if grid[current_y][i] == "#":
                return False
            if grid[current_y][i] == ".":
                grid[current_y][i] = "O"
                grid[current_y][current_x + 1] = "."
                return True
    if direction == "<":
        for i in range(current_x - 1, 0, -1):

            if grid[current_y][i] == "#":
                return False
            if grid[current_y][i] == ".":
                grid[current_y][i] = "O"
                grid[current_y][current_x - 1] = "."
                return True



file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0

grid_i = []
moves_i = []
read_moves = False
for line in Lines:
    input_line= line.strip()
    if input_line == "":
        read_moves = True
        continue
    if read_moves == False:
        grid_i.append(list(input_line))
    else:
        moves_i += list(input_line)
    print("Line {}: {}".format(count, input_line))
    count += 1

#bounce(grid_i, 1, 4, "v")
print("TASK 1 - sol: {}".format(solve_part_one(grid_i, moves_i)))

print("TASK 2 - ")