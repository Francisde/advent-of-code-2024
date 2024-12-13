def solve_part_one(stones_list, max):
    result = 0
    steps = 0
    # print(stones_list)
    while steps < max:
        steps += 1
        new_stones = []
        for stone in stones_list:
            string_repr = "{}".format(stone)
            if stone == 0:
                new_stones.append(1)
                continue
            elif len(string_repr) % 2 == 0:
                half = len(string_repr) // 2
                left = string_repr[0:half]
                right = string_repr[half:]
                new_stones.append(int(left))
                new_stones.append(int(right))
                continue
            else:
                new_stones.append(stone * 2024)
        stones_list = new_stones
    return len(stones_list), stones_list

def solve_part_two(stones_list):

    stone_set_dict = dict()
    stone_ocuurence = dict()
    stone_dict = dict()
    round_2_stones = []
    for i in range(len(stones_list)):
        # print("index {}, stone {}".format(i, stones_list[i]))
        solution = solve_part_one([stones_list[i]], 25)[1]
        # stone_dict["{}".format(stones_list[i])] = solution
        solution_set = set(solution)
        stone_set_dict["{}".format(stones_list[i])] = solution_set
        round_2_stones += list(solution_set)
        for key in list(solution_set):
            stone_ocuurence["{}-{}".format(stones_list[i], key)] = solution.count(key)


    # round 2
    round_2_stones = list(set(round_2_stones))
    round_3_stones = []
    for i in range(len(round_2_stones)):
        # print("index {}, stone {}".format(i, round_2_stones[i]))
        solution = solve_part_one([round_2_stones[i]], 25)[1]
        # stone_dict["{}".format(round_2_stones[i])] = solution
        solution_set = set(solution)
        stone_set_dict["{}".format(round_2_stones[i])] = solution_set
        round_3_stones += list(solution_set)
        for key in list(solution_set):
            stone_ocuurence["{}-{}".format(round_2_stones[i], key)] = solution.count(key)

    # # round 3
    round_3_stones = list(set(round_3_stones))
    for i in range(len(round_3_stones)):
        # print("index {}, stone {}".format(i, round_3_stones[i]))
        solution = solve_part_one([round_3_stones[i]], 25)[1]
        # stone_dict["{}".format(round_3_stones[i])] = solution
        solution_set = set(solution)
        stone_set_dict["{}".format(round_3_stones[i])] = solution_set
        for key in list(solution_set):
            stone_ocuurence["{}-{}".format(round_3_stones[i], key)] = solution.count(key)

    final_result = 0
    for stone in stones_list:
        for stage1_stone in list(stone_set_dict["{}".format(stone)]):
            # final_result += stone_ocuurence["{}-{}".format(stone, stage1_stone)]
            for stage2_stone in list(stone_set_dict["{}".format(stage1_stone)]):
                # final_result += (stone_ocuurence["{}-{}".format(stage1_stone, stage2_stone)] * stone_ocuurence["{}-{}".format(stone, stage1_stone)])
                for stage3_stone in list(stone_set_dict["{}".format(stage2_stone)]):
                    final_result += (stone_ocuurence["{}-{}".format(stage1_stone, stage2_stone)] * stone_ocuurence["{}-{}".format(stone, stage1_stone)] * stone_ocuurence["{}-{}".format(stage2_stone, stage3_stone)])
                    # final_result += stone_ocuurence["{}-{}".format(stage2_stone, stage3_stone)]
                #     pass
    return final_result



file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0

stones = []

for line in Lines:
    input_line= line.strip()
    stones = [int(x) for x in input_line.split(" ")]
    print("Line {}: {}".format(count, input_line))
    count += 1



print("TASK 1 - sol: {}".format(solve_part_one(stones, 25)[0]))
print("TASK 2 - sol: {}".format(solve_part_two(stones)))
