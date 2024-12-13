
def solve_part_one(input_list):
    i = 0
    result = 0
    while i + 4 < len(input_list) + 2:
        a_x, a_y  = parse_coordinates(input_list[i])
        b_x, b_y  = parse_coordinates(input_list[i + 1])
        coordinates_x, coordinates_y = parse_solution(input_list[i + 2])

        max_a = max(coordinates_x // a_x, coordinates_y // a_y)
        max_b = max(coordinates_x // b_x, coordinates_y // b_y)

        for k in range(0, max_a):
            for j in range(0, max_b):
                result_x = a_x * k + b_x * j
                result_y = a_y * k + b_y * j
                if result_x == coordinates_x and result_y == coordinates_y:
                    result += k * 3
                    result += j * 1
        i += 4

    return result

def parse_coordinates(input_line):
    value = input_line.split(": ")[1]
    value = value.replace("X", "")
    value = value.replace("Y", "")
    value = value.replace("+", "")
    value_x = int(value.split(", ")[0])
    value_y = int(value.split(", ")[1])
    return value_x, value_y

def parse_solution(input_line):
    coordinates = input_line.split(": ")[1]
    coordinates = coordinates.replace("X", "")
    coordinates = coordinates.replace("Y", "")
    coordinates = coordinates.replace("=", "")
    coordinates_split = coordinates.split(", ")
    coordinates_x = int(coordinates_split[0])
    coordinates_y = int(coordinates_split[1])
    return coordinates_x, coordinates_y

def solve_part_two(input_list):
    i = 0
    result = 0
    while i + 4 < len(input_list) + 2:
        a_x, a_y  = parse_coordinates(input_list[i])
        b_x, b_y  = parse_coordinates(input_list[i + 1])
        coordinates_x, coordinates_y = parse_solution(input_list[i + 2])
        coordinates_x += 10000000000000
        coordinates_y += 10000000000000


        a_x_mul = a_x * a_y
        b_x_mul = b_x * a_y
        a_y_mul = a_y * a_x
        b_y_mul = b_y * a_x
        new_b_y = b_y_mul - b_x_mul
        coordinates_x_mul = coordinates_x * a_y
        coordinates_y_mul = coordinates_y * a_x
        new_coordinates_y = coordinates_y_mul - coordinates_x_mul
        b_sol = new_coordinates_y // new_b_y
        if new_coordinates_y % new_b_y == 0:
            a_sol_1 = coordinates_x - (b_x * b_sol)

            a_sol = a_sol_1 // a_x

            if a_sol_1 % a_x == 0:

                result += (3 * a_sol + b_sol)

        i += 4

    return result

file1 = open('test.txt', 'r')
Lines = file1.readlines()

count = 0

input_l = []

for line in Lines:
    input_line= line.strip()
    input_l.append(input_line)


print("TASK 1 - sol: {}".format(solve_part_one(input_l)))

print("TASK 2 - sol: {}".format(solve_part_two(input_l)))
