#! /usr/bin/env python3
"""
This script will allow us to find
out how many calls at once (within
the same second) are operating at
the reception
"""

class Simultaneous():

    def __init__(self):
        self.call_list = list()
        self.fresh_list = list()
        self.count = int()

    def read_call_list(self, file):
        """method to read the line in txt file, and 
        create a 2D str list"""

        with open(file, 'r') as f:
            self.call_list = [
                line.strip("\n").split(":")
                for line in f.readlines() if line.strip()]
            self.call_list = list(self.call_list)

        return self.call_list

    def transform_str_to_int_from_a_list(self, data):
        """method to transform 2D str list into a 
        2D int list"""

        self.fresh_list = [
            [int(call) for call in calls] for calls in data]

        return self.fresh_list

    def count_simultaneous_calls(self, clean_data):
        """method to count simultaneous call
        within the same second from all the
        different calls in the list"""

        self.count = 0

        for current_start, current_end in clean_data:
            for next_start, next_end in clean_data:
                if current_end < next_start:
                    self.count -= 1
                elif current_end == next_start:
                    self.count -= 1
                elif current_start == next_start and current_end > next_end:
                    self.count -= 1
                elif current_end > next_end:
                    continue
                elif current_start > next_start or current_end > next_end:
                    self.count += 1

        return self.count