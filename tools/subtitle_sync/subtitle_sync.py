"""
Date: 2024-05-25
Author: Dragan :)

IN PROGRESS
The utility for changing times in a subtitle file.

Input:

offset - time in seconds for shifting each time codes. Make sure that the first character is a "+" (adding) or "-" 
    (subtracting). For example, +1.20 means adding 1 second and 200 milliseconds to every timecode.

stretch - time that should be added for each second frrom the offset time.

Example:

start = 00:02:22,630
offset = 3200 (3.2 seconds)
stretch = 5 (5 miliseconds per 1 sec)

1
00:02:22,630 --> 00:02:26,835
00:02:25,830
stretch: 0

10
00:03:03,981 --> 00:03:08,287
00:03:07,181
stretch: 03:03,981 - 02:22,630 = 41,351 -> 206ms
00:03:07,387
"""
import os
import sys
import re
import argparse


def process_command_line():
    parser = argparse.ArgumentParser(description='subtitle sync app')

    parser.add_argument('subtitle', action="store")
    parser.add_argument('--start', action="store", type=int, default=0, help='start time in milliseconds')
    parser.add_argument('--offset', action="store", type=int, help='offest in milliseconds')
    parser.add_argument('--stretch', action="store", type=int, help='stretch in milliseconds')

    return parser.parse_args()

class SubtitleShifter:
    def __init__(self, subtitle, start, offset, stretch) -> None:
        self.start = start
        self.offset = offset
        self.stretch = stretch

        self.subtitle = subtitle

    def new_subtitle(self):
        return self.subtitle + '.new'
    
    @staticmethod
    def is_timecode(line):
        print(f'check if "{line.strip()}" is timecode')
        pattern = re.compile("^\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d$")
        result = pattern.match(line.strip())
        print(result)
        return result is not None
        # 00:02:22,630 --> 00:02:26,835

    def process_time_code(self, timecode):
        return timecode.strip() + " HAHAHA\n"

    def process_subtitle(self):
        original_subtitle = open(self.subtitle, 'r')
        new_subtitle = open(self.new_subtitle(), 'w')

        while True:
            line = original_subtitle.readline()
            if not line:
                break

            if SubtitleShifter.is_timecode(line):
                line = self.process_time_code(line)

            new_subtitle.write(line)

        new_subtitle.close()

args = process_command_line()
processor = SubtitleShifter(args.subtitle, args.start, args.offset, args.stretch)
processor.process_subtitle()
