"""
Date: 2024-05-25
Author: Dragan :)

IN PROGRESS
The utility for changing times in a subtitle file.

Input:

offset - time in seconds for shifting each time codes. Make sure that the first character is a "+" (adding) or "-" 
    (subtracting). For example, +1.20 means adding 1 second and 200 milliseconds to every timecode.

stretch - time that should be added for each minute from the offset time.

Example:

start = 00:02:22,630
offset = 3200 (3.2 seconds)
stretch = 60 (5 milliseconds per 1 min)

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
import re
import argparse


def get_timecode_parts(timecode: str) -> (int, int, int, int):
    """
    timecode format: 'hh:mm:ss,ttt'
    return (hh, mm, ss, ttt)
    """
    pattern = r'^(\d\d):(\d\d):(\d\d),(\d\d\d)$'

    match = re.match(pattern, timecode)

    if match:
        return [int(x) for x in match.groups()]
    else:
        raise Exception(f'Invalid timecode {timecode}! Expected format is: "hh:mm:ss,ttt"')


def timecode_to_millis(timecode):
    timecode_parts = get_timecode_parts(timecode)
    return (timecode_parts[2] + 60*(timecode_parts[1] + 60*timecode_parts[0]))*1000 + timecode_parts[3]


def process_command_line():
    parser = argparse.ArgumentParser(description='subtitle sync app')

    parser.add_argument('subtitle', action="store")
    parser.add_argument('--start', action="store", type=str, default='00:00:00,000', help='start time in milliseconds')
    parser.add_argument('--offset', action="store", type=int, default=0, help='offest in milliseconds')
    parser.add_argument('--stretch', action="store", type=int, default=0, help='stretch in milliseconds')

    return parser.parse_args()


class SubtitleShifter:
    def __init__(self, subtitle: str, start: str, offset: int, stretch: int) -> None:
        start = start.strip(" '")
        self.start_in_millis: int = SubtitleShifter.timeline_code_to_millis(start)
        self.offset: int = offset
        self.stretch: float = stretch / 60000

        self.subtitle = subtitle

    def new_subtitle(self):
        return self.subtitle + '.new'
    
    @staticmethod
    def get_timeline(line):
        """
        If 'line' represent timeline returns the pair of time_codes in a timeline
        Otherwise returns None

        timeline format: 'hh:mm:ss,ttt --> hh:mm:ss,ttt'
        return: (hh:mm:ss,ttt, hh:mm:ss,ttt)
        """
        timecode_pattern = r'\d\d:\d\d:\d\d,\d\d\d'
        print(f'check if "{line.strip()}" is timecode')
        timeline_pattern: str = f'^({timecode_pattern}) --> ({timecode_pattern})$'
        match = re.match(timeline_pattern, line.strip())
        print(match)

        if match:
            return match.groups()

        return None

    def process_timeline(self, timeline_codes: list[str]) -> str:
        """
        timeline_codes: original timeline codes (timeline_code_begin, timeline_code_end)
        return: shifted timeline 'hh:mm:ss,ttt --> hh:mm:ss,ttt'
        """
        print(f'timeline_codes: {timeline_codes}')
        shifted_timeline_codes = [
            self.shift_timeline_code(timeline_codes[0]),
            self.shift_timeline_code(timeline_codes[1])
        ]

        return ' --> '.join(shifted_timeline_codes) + '\n'

    def shift_timeline_code(self, timeline_code: str) -> str:
        timeline_millis = self.timeline_code_to_millis(timeline_code)
        shifted_timeline_millis = timeline_millis + self.offset + self.stretch_from_start(timeline_millis)
        return self.timeline_millis_to_code(shifted_timeline_millis)

    def process_subtitle(self):
        original_subtitle = open(self.subtitle, 'r')
        new_subtitle = open(self.new_subtitle(), 'w')

        while True:
            line = original_subtitle.readline()
            if not line:
                break

            timeline_codes = SubtitleShifter.get_timeline(line)
            if timeline_codes:
                line = self.process_timeline(timeline_codes)

            new_subtitle.write(line)

        new_subtitle.close()

    @staticmethod
    def timeline_code_to_millis(timeline_code):
        timecode_parts = get_timecode_parts(timeline_code)
        return timecode_parts[3] + 1000 * (timecode_parts[2] + 60 * (timecode_parts[1] + 60 * timecode_parts[0]))

    def stretch_from_start(self, timeline_millis):
        return (timeline_millis - self.start_in_millis) * self.stretch

    @staticmethod
    def timeline_millis_to_code(shifted_timeline_millis):
        ttt = int(shifted_timeline_millis % 1000)
        seconds = int(shifted_timeline_millis / 1000)
        ss = seconds % 60
        minutes = int(seconds / 60)
        mm = minutes % 60
        hh = int(minutes / 60)
        return f'{hh:02d}:{mm:02d}:{ss:02d},{ttt:03d}'


args = process_command_line()
processor = SubtitleShifter(args.subtitle, args.start, args.offset, args.stretch)
processor.process_subtitle()
