# DAY 2:
# we're at the red-nosed reindeer nuclear fission/fusion plant (the first location we're checking)
# engineers there need help figuring out patterns in their reports which contain a list of numbers called levels
# the reports are considered *safe* if
# the levels are all increasing or all decreasing
# AND any two adjacent levels differ by at least one and at most three
# figure out how many reports are safe

day_2_input = open("Day 2 Input", "r")
day_2_input_list = day_2_input.readlines()
day_2_input.close()
reports = []

for line in day_2_input_list:
    reports.append(line.strip().split(" "))
    # TODO: make sure you turn values to ints before processing

safe_reports = 0  # counter for how many reports are safe

for report in reports:
    report.sort()  # all hail the mighty TimSort
    safe_flag = True
    level_index = 0
    while safe_flag and level_index < len(report):
        # increasing or decreasing sequence constraint
        # 1 <= difference between consecutive levels <= 3 constraint
        if report[level_index] == report[level_index + 1]:
            safe_flag = False