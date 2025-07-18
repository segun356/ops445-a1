#!/usr/bin/env python3
# Student ID: 103921235
# Date: 2025-07-18
# Lab 7 – OPS445

from lab7a import Time

t1 = Time(8, 0, 0)
t2 = Time(8, 55, 0)
t3 = Time(9, 50, 0)
td = Time(0, 50, 0)

tsum1 = t1.sum_times(td)
tsum2 = t2.sum_times(td)
tsum3 = t3.sum_times(td)

ft = Time.format_time

print(ft(t1), '+', ft(td), '=', ft(tsum1))
print(ft(t2), '+', ft(td), '=', ft(tsum2))
print(ft(t3), '+', ft(td), '=', ft(tsum3))
