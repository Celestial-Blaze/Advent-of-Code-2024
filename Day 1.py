# we're going to 50 places to get 50 stars and the missing Chief Historian will have to be at one of those
# DAY 1:
# list of locations to check is currently empty --> someone decides to look in the Chief Historian's office
# assortment of historically significant locations found - listed using a number called "Location ID"
# our input is provided as the two lists the elves compiled
# the two lists don't match exactly...
# sort and pair up so that the smallest number on the left pairs with the smallest on the right and so on
# sum up all the distances between the left and the right number pairs

day_1_input = open("Day 1 Input", "r")
day_1_input_list = day_1_input.readlines()
day_1_input.close()

left_list = []
right_list = []

for line in day_1_input_list:
    both_lists = line.strip("\n").split("   ")
    left_list.append(int(both_lists[0]))
    right_list.append(int(both_lists[1]))

left_list.sort()
right_list.sort()

sum_of_distances = 0
for x in range(len(left_list)):
    dist = abs(left_list[x] - right_list[x])
    sum_of_distances += dist

print(sum_of_distances)
# yay! solved correctly!

# now, solve part 2 with presort mode style algorithm (n log n) where our sort was also Tim Sort (n log n)
# find the sum of all similarity scores, where similarity_score = left_list[x] * freq_of_llx_in_rl

similarity_score_sum = 0
right_index = 0

for value in left_list:  # only checking a few values for now
    # print(f"checking value: {value} in this for loop iteration")
    right_frequency = 0  # number of occurrences of the left value in the right list
    # skip left values that can't be in the sorted right_list (freq = 0)
    if right_list[right_index] <= value:
        # print(f"because {right_list[right_index]} is less than or equal to {value}...")
        # get to a point in the sorted right_list where the value matches
        while right_list[right_index] < value and right_index < len(right_list)-1:
            # print("since the values don't match yet...")
            # print(f"incrementing the right index until we get to a value that matches...{right_index}")
            right_index += 1
        # at this point, the right_index is at a position where the value either matches or is the last element
        while right_index < len(right_list) and right_list[right_index] == value:
            # print(f"here, the index is not out of bounds and the right_list value matches so")
            right_frequency += 1  # seen once in the right_list
            # print(f"adding one to the frequency, it is now {right_frequency}")
            right_index += 1  # check next value
            # print("incrementing the right index to check the next value")

    similarity_score = value * right_frequency  # calculate similarity score
    # print(f"the similarity score for {value} is {similarity_score}")
    similarity_score_sum += similarity_score  # add the similarity score to the total

print(similarity_score_sum)  # YESSSSSSS FINALLY
