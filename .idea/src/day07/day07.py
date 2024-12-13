def solve_part_one(input_list):
    result = 0
    for line in input_list:
        goal_split = line.split(": ")
        goal = int(goal_split[0])
        values_split = goal_split[1].split(" ")
        values = [int(x) for x in values_split]
        if solve_equation(goal, values, "ADD", 0):
            result += goal
    return result

def solve_part_two(input_list):
    result = 0
    for line in input_list:
        goal_split = line.split(": ")
        goal = int(goal_split[0])
        values_split = goal_split[1].split(" ")
        values = [int(x) for x in values_split]
        if solve_equation_two(goal, values, "ADD", 0):
            result += goal
    return result

def solve_equation(goal, input_list, opp, cuurent_result):
    if len(input_list) == 1:
        if opp == "MUL":
            if cuurent_result * input_list[0] == goal:
                return True
            else:
                return False
        if opp == "ADD":
            if cuurent_result + input_list[0] == goal:
                return True
            else:
                return False
    else:
        if opp == "MUL":
            new_result = cuurent_result * input_list[0]
            new_list = input_list[1:]
            if solve_equation(goal, new_list, "MUL", new_result):
                return True
            else:
                return solve_equation(goal, new_list, "ADD", new_result)
        if opp == "ADD":
            new_result = cuurent_result + input_list[0]
            new_list = input_list[1:]
            if solve_equation(goal, new_list, "MUL", new_result):
                return True
            else:
                return solve_equation(goal, new_list, "ADD", new_result)

def solve_equation_two(goal, input_list, opp, cuurent_result):
    if len(input_list) == 1:
        if opp == "MUL":
            if cuurent_result * input_list[0] == goal:
                return True
            else:
                return False
        if opp == "ADD":
            if cuurent_result + input_list[0] == goal:
                return True
            else:
                return False
        if opp == "CON":
            if int("{}{}".format(cuurent_result, input_list[0])) == goal:
                return True
            else:
                return False
    else:
        if opp == "MUL":
            new_result = cuurent_result * input_list[0]
            new_list = input_list[1:]
            if solve_equation_two(goal, new_list, "MUL", new_result):
                return True
            elif solve_equation_two(goal, new_list, "ADD", new_result):
                return True
            else:
                return solve_equation_two(goal, new_list, "CON", new_result)
        if opp == "ADD":
            new_result = cuurent_result + input_list[0]
            new_list = input_list[1:]
            if solve_equation_two(goal, new_list, "MUL", new_result):
                return True
            elif solve_equation_two(goal, new_list, "ADD", new_result):
                return True
            else:
                return solve_equation_two(goal, new_list, "CON", new_result)
        if opp == "CON":
            new_result = int("{}{}".format(cuurent_result, input_list[0]))
            new_list = input_list[1:]
            if solve_equation_two(goal, new_list, "MUL", new_result):
                return True
            elif solve_equation_two(goal, new_list, "ADD", new_result):
                return True
            else:
                return solve_equation_two(goal, new_list, "CON", new_result)

file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0

test_lines = []

for line in Lines:
    input_line= line.strip()
    test_lines.append(input_line)
    print("Line {}: {}".format(count, input_line))
    count += 1


print("TASK 1 - sol: {}".format(solve_part_one(test_lines)))

print("TASK 2 - sol: {}".format(solve_part_two(test_lines)))
