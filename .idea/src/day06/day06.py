from operator import index

import util.util


def solve_part_one(grid):
    result = 0
    step_list = []
    current_x = 0
    current_y = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                current_x = j
                current_y = i
                break
    direction = "N"
    while current_x >=0 and current_y >=0 and current_x < len(grid[0]) and current_y < len(grid):
        grid[current_y][current_x] = "X"
        step_list.append((current_y, current_x))
        try:
            if direction == "N" and grid[current_y -1][current_x] != "#":
                current_y -= 1
                continue
            elif direction == "N" and grid[current_y -1][current_x] == "#":
                direction = "E"
                continue
            if direction == "E" and grid[current_y ][current_x + 1] != "#":
                current_x += 1
                continue
            elif direction == "E" and grid[current_y][current_x +1] == "#":
                direction = "S"
                continue
            if direction == "S" and grid[current_y +1][current_x ] != "#":
                current_y += 1
                continue
            elif direction == "S" and grid[current_y +1][current_x] == "#":
                direction = "W"
                continue
            if direction == "W" and grid[current_y ][current_x - 1] != "#":
                current_x -= 1
                continue
            elif direction == "W" and grid[current_y][current_x -1] == "#":
                direction = "N"
                continue
        except:
            print("index error")
            break

    for row in grid:
        for char in row:
            if char == "X":
                result += 1
    return (result, step_list)

def solve_part_two2(grid):
    result = 0
    current_x = 0
    current_y = 0
    start_x = 0
    start_y = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                current_x = j
                current_y = i
                start_x = j
                start_y = i
                break
    direction = "N"
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == ".":
                grid[i][j] = "#"
            else:
                continue
            test_grid = []
            for row in grid:
                test_grid.append(row.copy())
            direction = "N"
            current_x = start_x
            current_y = start_y
            move = True
            steps = 0
            breaking = False
            while steps < 1000000:
                steps += 1
                test_grid[current_y][current_x] = "X"
                try:
                    if direction == "N" and test_grid[current_y -1][current_x] != "#":
                        current_y -= 1
                        move = True
                        continue
                    elif direction == "N" and test_grid[current_y -1][current_x] == "#":
                        direction = "E"
                        move = False
                        continue
                    if direction == "E" and test_grid[current_y ][current_x + 1] != "#":
                        current_x += 1
                        move = True
                        continue
                    elif direction == "E" and test_grid[current_y][current_x +1] == "#":
                        direction = "S"
                        move = False
                        continue
                    if direction == "S" and test_grid[current_y +1][current_x ] != "#":
                        current_y += 1
                        move = True
                        continue
                    elif direction == "S" and test_grid[current_y +1][current_x] == "#":
                        direction = "W"
                        move = False
                        continue
                    if direction == "W" and test_grid[current_y ][current_x - 1] != "#":
                        current_x -= 1
                        move = True
                        continue
                    elif direction == "W" and test_grid[current_y][current_x -1] == "#":
                        direction = "N"
                        move = False
                        continue
                    else:
                        print("else")
                except:
                    breaking  = True
                    break
            if not breaking:
                result += 1
            grid[i][j] = "."
    return result

def solve_part_two3(grid, step_list):
    result = 0
    current_x = 0
    current_y = 0
    start_x = 0
    start_y = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                current_x = j
                current_y = i
                start_x = j
                start_y = i
                break
    direction = "N"

    for step in step_list:

        if grid[step[0]][step[1]] == ".":
            grid[step[0]][step[1]] = "#"
        else:
            continue
        test_grid = []
        solution_grid = []
        for row in grid:
            test_grid.append(row.copy())
            solution_grid.append([[] for c in row])
        direction = "N"
        current_x = start_x
        current_y = start_y
        move = True
        steps = 0
        breaking = False
        move = True
        path = ""
        while steps < 10000:
            steps += 1
            test_grid[current_y][current_x] = "X"
            key = "{}.{}.{}".format(current_y, current_x, direction)
            path += "-"+key
            if key in solution_grid[current_y][current_x] and move:
                # print(path)
                # print(steps)
                test_grid[current_y][current_x] = "F"

                # for row in test_grid:
                #     print(row)
                # print(steps)
                # print(direction)
                result += 1
                if (step[0], step[1]) not in obsticle:
                    print("{}-{}".format(step[0], step[1]))
                break
            else:
                solution_grid[current_y][current_x].append(key)
            try:
                if direction == "N":
                    if current_y == 0:
                        breaking  = True
                        break
                    if test_grid[current_y -1][current_x] != "#":
                        current_y -= 1
                        move = True
                        continue
                    elif test_grid[current_y -1][current_x] == "#":
                        direction = "E"
                        move = False
                        continue
                    else:
                        print("else")
                if direction == "E":
                    if test_grid[current_y ][current_x + 1] != "#":
                        current_x += 1
                        move = True
                        continue
                    elif test_grid[current_y][current_x +1] == "#":
                        direction = "S"
                        move = False
                        continue
                    else:
                        print("else")
                if direction == "S":
                    if test_grid[current_y +1][current_x ] != "#":
                        current_y += 1
                        move = True
                        continue
                    elif test_grid[current_y +1][current_x] == "#":
                        direction = "W"
                        move = False
                        continue
                    else:
                        print("else")
                if direction == "W":
                    if current_x == 0:
                        breaking  = True
                        break
                    if test_grid[current_y ][current_x - 1] != "#":
                        current_x -= 1
                        move = True
                        continue
                    elif test_grid[current_y][current_x -1] == "#":
                        direction = "N"
                        move = False
                        continue
                    else:
                        print("else")
                else:
                    print("else")
            except:
                breaking  = True
                break

        grid[step[0]][step[1]] = "."

    return result

file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

file2 = open('obsticle.txt', 'r')
Lines2 = file2.readlines()

count = 0

input_grid = []
input_grid2 = []
obsticle = []
program_dict = dict()


for line in Lines:
    input_line= line.strip()
    row = list(input_line)
    input_grid.append(row)
    input_grid2.append(row.copy())
for line in Lines2:
    input_line= line.strip()
    obsticle.append(((int(input_line.split("-")[0])), (int(input_line.split("-")[1]))))


sol1 = solve_part_one(input_grid)


print("TASK 1 - sol: {}".format(sol1[0]))

print("TASK 2 - sol: {}".format(solve_part_two3(input_grid2, list(set(sol1[1])))))
# print("TASK 2 - sol: {}".format(solve_part_two3(input_grid2, [(44,70)])))

#<2065