# we're going to 50 places to get 50 stars and the missing Chief Historian will have to be at one of those
# DAY 1:
# list of locations to check is currently empty --> someone decides to look in the Chief Historian's office
# assortment of historically significant locations found - listed using a number called "Location ID"
# our input is provided as the two lists the elves compiled
# the two lists don't match exactly...
# sort and pair up so that the smallest number on the left pairs with the smallest on the right and so on
# sum up all the distances between the left and the right number pairs

day_1_input = open("Day 1 Input", "r")
day_1_input = day_1_input.readlines()
left_list = []
right_list = []

for line in day_1_input:
    both_lists = line.strip("\n").split("   ")
    left_list.append(int(both_lists[0]))
    right_list.append(int(both_lists[1]))

left_list.sort()
right_list.sort()

# sum_of_distances = 0
# for x in range(len(left_list)):
#     dist = abs(left_list[x] - right_list[x])
#     sum_of_distances += dist
#
# print(sum_of_distances)
# yay! solved correctly!

# now, solve part 2 with presort mode algorithm (n log n) where our sort was also Tim Sort (n log n)
# find the sum of all similarity scores, where similarity_score = left_list[x] * freq_of_llx_in_rl

similarity_score_sum = 0
x_iter = 0
i = 0
while i < len(left_list):
    run_length = 1
    run_value = left_list[i]  # calculate runs & frequencies for each value in left_list
    while run_length + i < len(right_list) and right_list[run_length + i] == run_value:
        run_length += 1
        x_iter += 1
    similarity_score_sum += run_length * run_value
    i += 1

print(f"I just did {x_iter} iterations")
print(similarity_score_sum)
