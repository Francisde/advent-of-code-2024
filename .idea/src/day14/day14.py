from curses import start_color


class Robot:

    def __init__(self, start_x, start_y, v_x, v_y, x_bound, y_bound):
        self.start_x = start_x
        self.current_x = start_x
        self.start_y = start_y
        self.current_y = start_y
        self.v_x = v_x
        self.v_y = v_y
        self.x_bound = x_bound
        self.y_bound = y_bound

    def simulate_one_step(self):
        self.current_x = (self.current_x + self.v_x) % self.x_bound
        self.current_y = (self.current_y + self.v_y) % self.y_bound

    def reset(self):
        self.current_x = self.start_x
        self.current_y = self.start_y
    def get_quadrant(self):
        if self.current_x == self.x_bound // 2 or self.current_y == self.y_bound // 2:
            return None
        if self.current_x < self.x_bound // 2:
            if self.current_y < self.y_bound // 2:
                return 1
            else:
                return 2
        else:
            if self.current_y < self.y_bound // 2:
                return 3
            else:
                return 4

    def __repr__(self):
        return "current x: {}, y: {}".format(self.current_x, self.current_y)

def solve_part_one(robots_list, sim_sec):
    for i in range(sim_sec):
        # print("simulation second {}".format(i))
        for robot in robots_list:
            robot.simulate_one_step()

    res_1 = 0
    res_2 = 0
    res_3 = 0
    res_4 = 0
    for robot in robots_list:
        if robot.get_quadrant() == 1:
            res_1 += 1
        elif robot.get_quadrant() == 2:
            res_2 += 1
        elif robot.get_quadrant() == 3:
            res_3 += 1
        elif robot.get_quadrant() == 4:
            res_4 += 1
    return res_1 * res_2 * res_3 * res_4

def solve_part_two(robots_list, sim_sec):
    for i in range(sim_sec):
        # print("simulation second {}".format(i))
        for robot in robots_list:
            robot.simulate_one_step()
        print_robots(robots_list, i)


def print_robots(robots_list, i):
    grid = [["." for i in range(101)] for j in range(103)]
    for robot in robots_list:
        grid[robot.current_y][robot.current_x] = 'X'
    found = False
    for row in grid:
        line = ""
        for char in row:
            line += char
            #print(char, end='')
        if "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" in line:
            found = True
        print(line)
    print()
    if found:
        print(i + 1)
        input("next?")


file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()
robots = []
x_max = 101
y_max = 103

for line in Lines:
    input_line= line.strip()
    split_line = input_line.split(" ")
    remove_pos = split_line[0].replace("p=", "")
    x = int(remove_pos.split(",")[0])
    y = int(remove_pos.split(",")[1])
    remove_vel = split_line[1].replace("v=", "")
    v_x = int(remove_vel.split(",")[0])
    v_y = int(remove_vel.split(",")[1])
    robots.append(Robot(x, y, v_x, v_y, x_max, y_max))


print("TASK 1 - sol: {}".format(solve_part_one(robots, 100)))
for robot in robots:
    robot.reset()


print("TASK 2 - sol: {}".format(solve_part_two(robots, 100000)))