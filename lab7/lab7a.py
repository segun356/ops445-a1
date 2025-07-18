#!/usr/bin/env python3
# Student ID: 103921235
# Date: 2025-07-18
# Lab 7 – OPS445

class Time:
    """Simple object type for time of the day."""

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def format_time(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        sum_hour = self.hour + t2.hour
        sum_minute = self.minute + t2.minute
        sum_second = self.second + t2.second

        if sum_second >= 60:
            extra_min = sum_second // 60
            sum_second = sum_second % 60
            sum_minute += extra_min

        if sum_minute >= 60:
            extra_hr = sum_minute // 60
            sum_minute = sum_minute % 60
            sum_hour += extra_hr

        return Time(sum_hour, sum_minute, sum_second)

    def valid_time(self):
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True
