# Pi from Pascal's triangle

num_third_terms = 10000000 # number of third terms to use (larger num = more accurate)
third_num = 0 # the current third number which will be worked on
increment = 1 # the amount by which to increment the third_num to get the next third_num
alternating_count = 0 # a number to help determine if the sign of the number should be + or -
end_sum = 0 # the end result 

for i in range(num_third_terms):
    # each third number can be represented as (previous third number) plus (counter + 1); 
    # the counter starts at 1 and increments each time, so it will be (prev) + 1, (prev) + 2, etc.

    third_num += increment # add the increment to the current third number
    increment += 1 # increment the increment by one

    copy_of_third = third_num
    copy_of_third = 1 / copy_of_third # take reciprocal of the current third number

    if alternating_count == 0:
        # third_num's sign is positive if count is 0 or 1
        end_sum += copy_of_third # add third_num to the result
        alternating_count += 1

    elif alternating_count == 1:
        end_sum += copy_of_third
        alternating_count += 1

    elif alternating_count == 2:
        copy_of_third *= -1 # change the sign of third_num is count is 2 oe 3
        end_sum += copy_of_third
        alternating_count += 1

    elif alternating_count == 3:
        copy_of_third *= -1
        end_sum += copy_of_third
        alternating_count = 0 # reset the count

    else:
        print("ERROR u fool you broke something")

end_sum += 2 # the final step! now it's (close to) pi

print(end_sum)