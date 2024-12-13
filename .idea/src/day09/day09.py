def solve_part_one(file_system):
    id = 0
    queue = []
    file = True
    for char in file_system:
        length = int(char)
        for i in range(length):
            if file:
                queue.append("{}".format(id))
            else:
                queue.append("{}".format("."))
        if file:
            file = False
            id += 1
        else:
            file = True
    while True:

        breaking = False
        for char in queue:
            if char == ".":
                breaking = True
            if breaking and char != ".":
                breaking = False
                break
        if breaking:
            break
        last_file = ""
        last_index = 0
        for i in range(len(queue)):
            if queue[i] != ".":
                last_file = queue[i]
                last_index = i
        new_queue = []
        first_free = True
        for char in range(len(queue)):
            if queue[char] == "." and first_free:
                new_queue.append(last_file)
                first_free = False
            elif char == last_index:
                new_queue.append(".")
            else:
                new_queue.append(queue[char])

        queue = new_queue[:-1]
    print(queue)
    checksum = 0
    for i in range(len(queue)):
        if queue[i] == ".":
            break
        checksum += (i * int(queue[i]))
    return checksum

def solve_part_two(file_system):
    id = 0
    queue = []
    id_length_dict = dict()
    file = True
    for char in file_system:
        length = int(char)
        if file:
            id_length_dict["{}".format(id)] = length
        for i in range(length):
            if file:
                queue.append("{}".format(id))
            else:
                queue.append("{}".format("."))
        if file:
            file = False
            id += 1
        else:
            file = True

    id -= 1
    while id > 0:
        needed_length = id_length_dict["{}".format(id)]
        left_most_gap_length = 0
        left_most_gap_start = 0
        gap_start = False
        for i in range(len(queue)):
            if queue[i] == "." and not gap_start:
                gap_start = True
                left_most_gap_start = i
            if queue[i] != "." and gap_start:
                left_most_gap_length = i - left_most_gap_start
                gap_start = False
                if left_most_gap_length >= needed_length:
                    break
        if needed_length <= left_most_gap_length:
            start_index = queue.index("{}".format(id))
            if start_index > left_most_gap_start:
                for i in range(needed_length):
                    queue[i + start_index] = "."
                    queue[i + left_most_gap_start] = "{}".format(id)

        id -= 1
    checksum = 0
    for i in range(len(queue)):
        if queue[i] == ".":
            continue
        checksum += (i * int(queue[i]))
    return checksum


file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0

compressed_input = ""

for line in Lines:
    input_line= line.strip()
    compressed_input = input_line
    print("Line {}: {}".format(count, input_line))
    count += 1


print("TASK 1 - sol: {}".format(solve_part_one(compressed_input)))

print("TASK 2 - sol: {}".format(solve_part_two(compressed_input)))
