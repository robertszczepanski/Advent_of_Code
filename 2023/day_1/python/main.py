# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class Day1:
    digits = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    filename = "../input.txt"
    file_content = []
    result = 0

    def read_file(self):
        with open(self.filename) as f:
            self.file_content = f.read().splitlines()

    def get_digit_str(self, word, placement, consider_words=False):
        assert placement in ["first", "last"]
        multiplier = 10
        treshold_index = len(word)
        found_digit = -1

        if not consider_words:
            digits = self.digits[0:10]
        else:
            digits = self.digits

        if placement == "last":
            treshold_index = -1
            multiplier = 1

        for i, digit in enumerate(digits):
            if placement == "first":
                occurence = word.find(digit)
            else:
                occurence = word.rfind(digit)

            if occurence != -1 and (
                (placement == "first" and occurence < treshold_index)
                or (placement == "last" and occurence > treshold_index)
            ):
                treshold_index = occurence
                found_digit = i

            if found_digit > 9:
                found_digit -= 10

        if found_digit != -1:
            return found_digit * multiplier
        else:
            return 0

    def task1(self):
        self.result = 0
        for line in self.file_content:
            self.result += self.get_digit_str(line, "first")
            self.result += self.get_digit_str(line, "last")

    def task2(self):
        self.result = 0
        for line in self.file_content:
            self.result += self.get_digit_str(line, "first", True)
            self.result += self.get_digit_str(line, "last", True)


aoc = Day1()
aoc.read_file()
aoc.task1()
print("Result of task 1: {}".format(aoc.result))
aoc.task2()
print("Result of task 2: {}".format(aoc.result))
