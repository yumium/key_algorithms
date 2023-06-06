# My solutions to algorithmic puzzles book by Levitin A. and Levitin M.

# Q50
'''
This one is simple.
Simply add up all the numbers given, the missing number is the difference to sum(1..100) = 5050

A cool trick is realising that the sum will be contiguous numbers, and since there are 100 of them, the mod 100 will spread across [0..99].
This means instead of tracking the sum, we just need to track the last 2 digits of the sum (taking mod 100 of the sum).
Then with that, we can find out the missing number.
'''

# Q51
'''




'''
