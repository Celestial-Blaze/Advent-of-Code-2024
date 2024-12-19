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

safe_reports = 0  # counter for how many reports are safe

# okay so for part 2 I'm going with the greedy approach and removing the first problem I encounter instead of
# checking all configurations of the sequence with one less element to see which ones are safe because that
# would be a factorial scale problem -- and I know that based on the size of the data, Python won't even complain
# and execute it just fine, but I really don't want to write such terrifying code unless I really have to
for report in reports:
    print(f"checking for report: {report}")
    safe_flag = True
    level_index = 0
    pop_count = 0
    # choose increasing or decreasing sequence constraint
    if int(report[0]) < int(report[1]):  # increasing sequence route
        print("it might be an increasing sequence, let's find out")
        while level_index < len(report) - 1:
            # 1 <= difference between consecutive levels <= 3 constraint
            if (not (1 <= abs(int(report[level_index]) - int(report[level_index + 1])) <= 3)) \
                    or int(report[level_index]) >= int(report[level_index + 1]):
                if pop_count < 1:  # if we can fix the problem, fix it!
                    print("first error! fixing now")
                    report.pop(level_index)  # pop the current item, the one causing the issue and then...
                    pop_count += 1  # increment pop_count
                    continue
                else:  # if we can't, then oh well
                    print(f"BROKE RULES AFTER {report[level_index]}")
                    safe_flag = False
                    break
            else:
                print(f"so far so good... we're at {report[level_index]}")
                level_index += 1

    elif int(report[0]) > int(report[1]):  # decreasing sequence route
        print("it might be a decreasing sequence, let's find out")
        while level_index < len(report) - 1:
            # 1 <= difference between consecutive levels <= 3 constraint
            if (not (1 <= abs(int(report[level_index]) - int(report[level_index + 1])) <= 3)) \
                    or int(report[level_index]) <= int(report[level_index + 1]):
                if pop_count < 1:  # if we can fix the problem, fix it!
                    print("first error! fixing now")
                    report.pop(level_index)  # pop the current item, the one causing the issue and then...
                    pop_count += 1  # increment pop_count
                    continue
                else:  # if we can't, then oh well
                    print(f"BROKE RULES AFTER {report[level_index]}")
                    safe_flag = False
                    break
            else:
                print(f"so far so good... we're at {report[level_index]}")
                level_index += 1

    else:
        # case when first two elements are equal
        print("first two elements match so I'm deleting the second one")
        report.pop(level_index + 1)  # pop the next item, the one causing the issue and then...
        pop_count += 1  # not that it matters here
        # choose increasing or decreasing sequence constraint
        if int(report[0]) < int(report[1]):  # increasing sequence route
            print("it might be an increasing sequence now, let's find out")
            while level_index < len(report) - 1:
                # 1 <= difference between consecutive levels <= 3 constraint
                if (not (1 <= abs(int(report[level_index]) - int(report[level_index + 1])) <= 3)) \
                        or int(report[level_index]) >= int(report[level_index + 1]):
                    print(f"BROKE RULES AFTER {report[level_index]}")
                    safe_flag = False
                    break
                else:
                    print(f"so far so good... we're at {report[level_index]}")
                    level_index += 1
        elif int(report[0]) > int(report[1]):  # decreasing sequence route
            print("it might be a decreasing sequence now, let's find out")
            while level_index < len(report) - 1:
                # 1 <= difference between consecutive levels <= 3 constraint
                if (not (1 <= abs(int(report[level_index]) - int(report[level_index + 1])) <= 3)) \
                        or int(report[level_index]) <= int(report[level_index + 1]):
                    print(f"BROKE RULES AFTER {report[level_index]}")
                    safe_flag = False
                    break
                else:
                    print(f"so far so good... we're at {report[level_index]}")
                    level_index += 1
        else:
            # wow, same issue again? what...? more doubles? FINE, NOT SAFE
            safe_flag = False
    # outcome
    if safe_flag:
        print("SAFE")
        safe_reports += 1
    print("----------------------------------------------------------------------------------------------")

print(safe_reports)

# AAAAAAHHHHHHHHHH I DON'T WANNA BRUTE FORCE (┬┬﹏┬┬)
