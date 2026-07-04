"""
Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
"""

intervals = []

n = int(input("no of intervals: "))

for i in range(n):
    start = int(input("Start: "))
    end = int(input("End: "))

    intervals.append([start, end])

intervals.sort()
print(intervals)


# store = []
# for i in range(len(intervals)-1):
#     start = intervals[i][0]
#     if intervals[i][1] >= intervals[i+1][0]:
#         if intervals[i][1] > intervals[i+1][1]:
#             end = intervals[i][1]
#         else:
#             end = intervals[i+1][1]
#         store.append([start, end])
#
# store.append(intervals[-1])
# print(store)


store = []
for i in range(len(intervals) - 1):
    if intervals[i+1][0] > intervals[i][1]:
        start = intervals[i][0]
        # end = intervals[i+1][1]
        # start = intervals[i][0]
        if intervals[i][1] >= intervals[i + 1][0]:
            if intervals[i][1] > intervals[i + 1][1]:
                end = intervals[i][1]
            else:
                end = intervals[i + 1][1]
            store.append([start, end])

store.append(intervals[-1])
print(store)
