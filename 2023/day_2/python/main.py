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


game_constraints = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

class Day2:
    filename = "input.txt"
    file_content = []
    result = 0

    def read_file(self):
        with open(self.filename) as f:
            self.file_content = f.read().splitlines()

    def is_game_possible(self, input):
        i = input.find(":")
        game_id = int(input[5:i])

        game_results = input[i+2:]
        for result in game_results.split("; "):
            for color_result in result.split(", "):
                space_index = color_result.find(" ")
                num = int(color_result[:space_index])
                color = color_result[space_index+1:]
                if num > game_constraints[color]:
                    return game_id, False

        return game_id, True

    def get_game_power(self, input):
        i = input.find(":")
        lowest_possible = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        game_results = input[i+2:]
        for result in game_results.split("; "):
            for color_result in result.split(", "):
                space_index = color_result.find(" ")
                num = int(color_result[:space_index])
                color = color_result[space_index+1:]
                if num > lowest_possible[color]:
                    lowest_possible[color] = num

        game_power = 1
        for color in lowest_possible.values():
            game_power *= color

        return game_power

    def task1(self):
        self.result = 0
        for game in self.file_content:
            game_id, result = self.is_game_possible(game)
            if result:
                self.result += game_id

    def task2(self):
        self.result = 0
        for game in self.file_content:
            self.result += self.get_game_power(game)


aoc = Day2()
aoc.read_file()
aoc.task1()
print("Result of task 1: {}".format(aoc.result))
aoc.task2()
print("Result of task 2: {}".format(aoc.result))
