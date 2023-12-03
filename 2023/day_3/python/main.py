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



class Day3:
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
    ]

    filename = "../input.txt"
    file_content = []
    result = 0

    def read_file(self):
        with open(self.filename) as f:
            self.file_content = f.read().splitlines()

    def get_symbol_matrix(self):
        symbol_matrix = []
        for i, line in enumerate(self.file_content):
            symbol_matrix.append([])
            for c in line:
                if c in self.digits + ["."]:
                    symbol_matrix[i].append(False)
                else:
                    symbol_matrix[i].append(True)
        return symbol_matrix

    def has_symbol_neighbour(self, line_index, pos):
        non_symbol_list = self.digits + ["."]
        line_length = len(self.file_content[line_index])
        line_count = len(self.file_content)
        i = line_index
        j = pos
        found_symbol = False

        if j != 0: # Left
            found_symbol |= self.file_content[i][j-1] not in non_symbol_list
        if j != (line_length - 1): # Right
            found_symbol |= self.file_content[i][j+1] not in non_symbol_list

        if i != 0: # Top
            found_symbol |= self.file_content[i-1][j] not in non_symbol_list
            if j != 0: # Top left
                found_symbol |= self.file_content[i-1][j-1] not in non_symbol_list
            if j != (line_length - 1): # Top right
                found_symbol |= self.file_content[i-1][j+1] not in non_symbol_list

        if i != line_count - 1: # Bottom
            found_symbol |= self.file_content[i+1][j] not in non_symbol_list
            if j != 0: # Bottom left
                found_symbol |= self.file_content[i+1][j-1] not in non_symbol_list
            if j != (line_length - 1): # Bottom right
                found_symbol |= self.file_content[i+1][j+1] not in non_symbol_list

        return found_symbol

    def get_gear_pos(self, line_index, pos):
        line_length = len(self.file_content[line_index])
        line_count = len(self.file_content)
        i = line_index
        j = pos
        gear_pos = (-1, -1)

        if j != 0: # Left
            gear_pos = (i, j-1) if self.file_content[i][j-1] == "*" else gear_pos
        if j != (line_length - 1): # Right
            gear_pos = (i, j+1) if self.file_content[i][j+1] == "*" else gear_pos

        if i != 0: # Top
            gear_pos = (i-1, j) if self.file_content[i-1][j] == "*" else gear_pos
            if j != 0: # Top left
                gear_pos = (i-1, j-1) if self.file_content[i-1][j-1] == "*" else gear_pos
            if j != (line_length - 1): # Top right
                gear_pos = (i-1, j+1) if self.file_content[i-1][j+1] == "*" else gear_pos

        if i != line_count - 1: # Bottom
            gear_pos = (i+1, j) if self.file_content[i+1][j] == "*" else gear_pos
            if j != 0: # Bottom left
                gear_pos = (i+1, j-1) if self.file_content[i+1][j-1] == "*" else gear_pos
            if j != (line_length - 1): # Bottom right
                gear_pos = (i+1, j+1) if self.file_content[i+1][j+1] == "*" else gear_pos

        return gear_pos

    def get_valid_numbers(self):
        valid_numbers = []
        for i, line in enumerate(self.file_content):
            number = ""
            is_valid = False
            for j, c in enumerate(line):
                if c in self.digits:
                    is_valid |= self.has_symbol_neighbour(i, j)
                    number += c
                    # print("Checking: {}, is_valid: {}".format(number[-1], is_valid))
                elif number != "":
                    if is_valid:
                        valid_numbers.append(int(number))
                    is_valid = False
                    number = ""
                else:
                    number = ""
            if number != "" and is_valid:
                valid_numbers.append(int(number))

        return valid_numbers

    def get_numbers_with_gear(self):
        numbers_with_gear = []
        for i, line in enumerate(self.file_content):
            number = ""
            gear_pos = (-1, -1)
            for j, c in enumerate(line):
                if c in self.digits:
                    gear_pos = self.get_gear_pos(i, j) if gear_pos == (-1, -1) else gear_pos
                    number += c
                    # print("Checking: {}, is_valid: {}".format(number[-1], is_valid))
                elif number != "":
                    if gear_pos != (-1, -1):
                        numbers_with_gear.append((int(number), gear_pos))
                    gear_pos = (-1, -1)
                    number = ""
                else:
                    number = ""
            if number != "" and (gear_pos != (-1, -1)):
                numbers_with_gear.append((int(number), gear_pos))

        return numbers_with_gear

    def get_gear_pairs(self, numbers_with_gear):
        gear_pairs = []
        for i, (n, n_gear_pos) in enumerate(numbers_with_gear):
            pair = [n]
            for m, m_gear_pos in numbers_with_gear[i:]:
                if n_gear_pos == m_gear_pos and n != m:
                    pair.append(m)
            if len(pair) == 2:
                gear_pairs.append(pair)
        return gear_pairs

    def task1(self):
        self.result = 0
        valid_numbers = self.get_valid_numbers()

        for n in valid_numbers:
            self.result += n

    def task2(self):
        self.result = 0
        numbers_with_gear = self.get_numbers_with_gear()
        gear_pairs = self.get_gear_pairs(numbers_with_gear)

        for pair in gear_pairs:
            self.result += pair[0] * pair[1]

aoc = Day3()
aoc.read_file()
aoc.task1()
print("Result of task 1: {}".format(aoc.result))
aoc.task2()
print("Result of task 2: {}".format(aoc.result))
