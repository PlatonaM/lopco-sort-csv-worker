"""
   Copyright 2021 InfAI (CC SES)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""


import datetime
import sys
import os


delimiter = os.getenv("delimiter")
time_format = os.getenv("time_format")
time_col = os.getenv("time_column")


def get_microseconds(timestamp: str) -> int:
    dt = datetime.datetime.strptime(timestamp, time_format)
    return int(dt.timestamp() * 1000000)


with open(sys.argv[1], "r") as in_file:
    with open(sys.argv[2], "w") as out_file:
        first_line = in_file.readline().strip()
        out_file.write(first_line + delimiter + "0" + "\n")
        first_line = first_line.split(delimiter)
        time_col_num = first_line.index(time_col)
        for line in in_file:
            line = line.strip().split(delimiter)
            line.append(str(get_microseconds(line[time_col_num])))
            out_file.write(delimiter.join(line) + "\n")
