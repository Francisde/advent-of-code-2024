def solve_part_one(pages, updates):
    result = 0
    for update in updates:
        update_correct = True
        for page_order in pages:
            split_pages = page_order.split("|")
            if split_pages[0] in update and split_pages[1] in update:
                if update.index(split_pages[0]) > update.index(split_pages[1]):
                    update_correct = False
        if update_correct:
            split_update = update.split(",")
            result += int(split_update[len(split_update) // 2])
    return result

def solve_part_two(pages, updates):
    result = 0
    incorrt_updates = []
    for update in updates:
        update_correct = True
        for page_order in pages:
            split_pages = page_order.split("|")
            if split_pages[0] in update and split_pages[1] in update:
                if update.index(split_pages[0]) > update.index(split_pages[1]):
                    update_correct = False
        if update_correct:
            pass
        else:
            incorrt_updates.append(update)
    for update in incorrt_updates:
        correct = False
        while not correct:
            correct = True
            for page_order in pages:
                split_pages = page_order.split("|")
                if split_pages[0] in update and split_pages[1] in update:
                    if update.index(split_pages[0]) > update.index(split_pages[1]):
                        correct = False
                        update = "{}{}{}{}{}".format(update[0:update.index(split_pages[1])],
                                                     split_pages[0],
                                                     update[update.index(split_pages[1]) + 2: update.index(split_pages[0])],
                                                     split_pages[1],
                                                     update[update.index(split_pages[0]) + 2:])

            if correct:
                split_update = update.split(",")
                result += int(split_update[len(split_update) // 2])
    return result



file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0

page_orders = []
update_order = []
updates = False

for line in Lines:
    input_line= line.strip()
    if updates:
        update_order.append(input_line)
    else:
        if input_line == "":
            updates = True
        else:
            page_orders.append(input_line)
    print("Line {}: {}".format(count, input_line))
    count += 1


print("TASK 1 - sol: {}".format(solve_part_one(page_orders, update_order)))

print("TASK 2 - sol: {}".format(solve_part_two(page_orders, update_order)))
