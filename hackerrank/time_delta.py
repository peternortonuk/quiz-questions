"""
https://www.hackerrank.com/challenges/python-time-delta/problem

When users post an update on social media,such as a URL, image, status update etc., other users in their network are
able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many
hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two
timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format

The first line contains , the number of testcases.
Each testcase contains  lines, representing time  and time .

Constraints

Input contains only valid timestamps
.
Output Format

Print the absolute difference  in seconds.

Sample Input 0

2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
Sample Output 0

25200
88200
"""

import math
import os
import random
import re
import sys
from datetime import datetime as dt
from test_time_delta import test_cases

fmt = '%a %d %b %Y %H:%M:%S %z'


# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = dt.strptime(t1, fmt)
    t2 = dt.strptime(t2, fmt)
    naive_diff = t1.replace(tzinfo=None) - t2.replace(tzinfo=None)
    tzone_diff = t1.utcoffset() - t2.utcoffset()
    diff = naive_diff.total_seconds() + tzone_diff.total_seconds()
    diff = abs(diff)
    return naive_diff, tzone_diff, abs(diff)


if __name__ == '__main__':
    results = []
    for pair, answer in test_cases:
        t1, t2 = pair
        naive_diff, tzone_diff, delta = time_delta(t1, t2)
        print(t1, '\n', t2, '\n', naive_diff.seconds, '\n', tzone_diff.seconds, '\n', delta, '\n', answer, '\n\n\n')
        if delta == answer:
            results.append(1)
        else:
            results.append(0)
    pass