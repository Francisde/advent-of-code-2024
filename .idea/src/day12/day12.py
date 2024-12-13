import util.util

def solve_part_one(grid):
    result = 0
    regions, region_list = get_regions(grid)
    util.util.print2D(regions)
    print(region_list)
    for region in region_list:
        area = get_area(regions, region)
        perimeter = get_perimeter(regions, region)
        price = area * perimeter
        print("area: {}, perimeter: {}, price: {}".format(area, perimeter, price))
        result += price
    return result

def solve_part_two(grid):
    result = 0
    regions, region_list = get_regions(grid)
    util.util.print2D(regions)
    print(region_list)
    for region in region_list:
        area = get_area(regions, region)
        corners = get_corners(regions, region)
        price = area * corners
        print("region {} : area: {}, corners: {}, price: {}".format(region, area, corners, price))
        result += price
    return result

def get_regions(grid):
    regions = []
    region_list = []
    for row in grid:
        regions.append(row.copy())

    region = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == regions[y][x]:
                mark_region(grid, regions, region, y, x)
                region_list.append(region)
                region += 1
    return regions, region_list

def mark_region(grid, regions, marker, y, x):
    if regions[y][x] == marker:
        return
    regions[y][x] = marker
    if x > 0:
        if grid[y][x-1] == grid[y][x]:
            mark_region(grid, regions, marker, y, x-1)
    if x < len(grid[y]) - 1:
        if grid[y][x+1] == grid[y][x]:
            mark_region(grid, regions, marker, y, x+1)
    if y > 0:
        if grid[y - 1][x] == grid[y][x]:
            mark_region(grid, regions, marker, y - 1, x)
    if y < len(grid) - 1:
        if grid[y + 1][x] == grid[y][x]:
            mark_region(grid, regions, marker, y + 1, x)

def get_area(regions, region):
    result = 0
    for row in regions:
        for value in row:
            if value == region:
                result += 1
    return result

def get_perimeter(regions, region):
    result = 0
    for y in range(len(regions)):
        for x in range(len(regions[y])):
            if regions[y][x] == region:
                if x > 0:
                    if regions[y][x -1] != region:
                        result += 1
                else:
                    result += 1
                if x < len(regions[y]) - 1:
                    if regions[y][x + 1] != region:
                        result += 1
                else:
                    result += 1
                if y > 0:
                    if regions[y - 1][x] != region:
                        result += 1
                else:
                    result += 1
                if y < len(regions) - 1:
                    if regions[y + 1][x] != region:
                        result += 1
                else:
                    result += 1
    return result

def get_corners(regions, region):
    result = 0
    for y in range(len(regions)):
        for x in range(len(regions[y])):
            if regions[y][x] == region:
                # check left up
                if x > 0:
                    if y > 0:
                        if regions[y - 1][x] != region and regions[y][x - 1] != region:
                            result += 1
                    elif regions[y][x - 1] != region:
                        result += 1
                elif y > 0:
                    if regions[y - 1][x] != region:
                        result += 1
                else:
                    result += 1

                # check left down
                if x > 0:
                    if y < len(regions) - 1:
                        if regions[y + 1][x] != region and regions[y][x - 1] != region:
                            result += 1
                    elif regions[y][x - 1] != region:
                        result += 1
                elif y < len(regions) - 1:
                    if regions[y + 1][x] != region:
                        result += 1
                else:
                    result += 1

                # check right up
                if x < len(regions[y]) - 1:
                    if y > 0:
                        if regions[y - 1][x] != region and regions[y][x + 1] != region:
                            result += 1
                    elif regions[y][x + 1] != region:
                        result += 1
                elif y > 0:
                    if regions[y - 1][x] != region:
                        result += 1
                else:
                    result += 1

                # check right down
                if x < len(regions[y]) - 1:
                    if y < len(regions) - 1:
                        if regions[y + 1][x] != region and regions[y][x + 1] != region:
                            result += 1
                    elif regions[y][x + 1] != region:
                        result += 1
                elif y < len(regions) - 1:
                    if regions[y + 1][x] != region:
                        result += 1
                else:
                    result += 1

                # check left up inner corner
                if x > 0 and y > 0:
                    if regions[y - 1][x] == region and regions[y][x - 1] == region and regions[y - 1][x - 1] != region:
                        result += 1

                # check left down inner corner
                if x > 0 and y < len(regions) - 1:
                    if regions[y + 1][x] == region and regions[y][x - 1] == region and regions[y + 1][x - 1] != region:
                        result += 1

                # check right up inner corner
                if x < len(regions[y]) - 1 and y > 0:
                    if regions[y - 1][x] == region and regions[y][x + 1] == region and regions[y - 1][x + 1] != region:
                        result += 1

                # check right down inner corner
                if x < len(regions[y]) - 1 and y < len(regions) - 1:
                    if regions[y + 1][x] == region and regions[y][x + 1] == region and regions[y + 1][x + 1] != region:
                        result += 1

    return result



file1 = open('puzzle.txt', 'r')
Lines = file1.readlines()

count = 0

garden = []

for line in Lines:
    input_line= line.strip()
    garden.append(list(input_line))
    print("Line {}: {}".format(count, input_line))
    count += 1


print("TASK 1 - sol: {}".format(solve_part_one(garden)))

print("TASK 2 - sol: {}".format(solve_part_two(garden)))
