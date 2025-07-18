#!/usr/bin/env python3
# Student ID: 103921235
# Date: 2025-07-18
# Lab 7 – OPS445

from lab7a import Time

t_valid = Time(12, 30, 30)
t_invalid = Time(25, 70, 90)

print("Testing valid_time():")
print(t_valid.format_time(), "is valid?", t_valid.valid_time())
print(t_invalid.format_time(), "is valid?", t_invalid.valid_time())

t4 = Time(23, 59, 59)
t5 = Time(0, 0, 2)
t6 = t4.sum_times(t5)

print("Testing sum_times():")
print(f"{t4.format_time()} + {t5.format_time()} = {t6.format_time()}")
