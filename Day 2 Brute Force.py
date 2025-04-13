def safe_report(report):
    safe_flag = True
    level_index = 0
    if int(report[0]) < int(report[1]):  # increasing sequence route
        while level_index < len(report) - 1:
            # 1 <= difference between consecutive levels <= 3 constraint
            if (not (1 <= abs(int(report[level_index]) - int(report[level_index + 1])) <= 3)) \
                    or int(report[level_index]) >= int(report[level_index + 1]):
                safe_flag = False
                break
            else:
                level_index += 1
    elif int(report[0]) > int(report[1]):  # decreasing sequence route
        while level_index < len(report) - 1:
            # 1 <= difference between consecutive levels <= 3 constraint
            if (not (1 <= abs(int(report[level_index]) - int(report[level_index + 1])) <= 3)) \
                    or int(report[level_index]) <= int(report[level_index + 1]):
                safe_flag = False
                break
            else:
                level_index += 1
    else:
        # same two first values
        safe_flag = False
    return safe_flag

def permute_report(report):



def main():
    day_2_input = open("Day 2 Input", "r")
    day_2_input_list = day_2_input.readlines()
    day_2_input.close()
    reports = []

    for line in day_2_input_list:
        reports.append(line.strip().split(" "))

    safe_reports = 0

    for report_x in reports:
        print("x")
