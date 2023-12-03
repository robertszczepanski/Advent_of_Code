#include <iostream>
#include <fstream>
#include <map>
#include <string>

std::map<std::string, int> game_constraints = {
    {"red", 12},
    {"green", 13},
    {"blue", 14},
};

std::pair<int, bool> isGamePossible(std::string game_line) {
    int i = game_line.find(":");
    int game_id = std::stoi(game_line.substr(5, i-5));
    std::string game_results = game_line.substr(i+2);
    size_t pos;

    do {
        pos = game_results.find("; ");
        std::string token = game_results.substr(0, pos);
        game_results.erase(0, pos + 2);

        size_t inner_pos;
        do {
            inner_pos = token.find(", ");
            std::string color_result = token.substr(0, inner_pos);
            token.erase(0, inner_pos + 2);

            int space_index = color_result.find(" ");
            int num = std::stoi(color_result.substr(0, space_index));
            std::string color = color_result.substr(space_index + 1);

            if(num > game_constraints[color]) {
                std::pair<int, bool> result{game_id, false};
                return result;
            }
        } while(inner_pos != std::string::npos);

    } while(pos != std::string::npos);

    std::pair<int, bool> result{game_id, true};
    return result;
}

void solveTask1(const std::string *filename) {
    std::ifstream input_stream;

    try {
        input_stream.open(*filename);
    }
    catch (std::ifstream::failure e) {
        std::cerr << "Exception opening a file\n";
    }

    std::string line;
    int result = 0;
    while(std::getline(input_stream, line)) {
        std::pair<int, bool> game_possibility = isGamePossible(line);
        if(game_possibility.second) {
            result += game_possibility.first;
        }
    }

    std::cout << "Result of task 1: " << result << std::endl;
}

int main() {
    const std::string filename = "../../input.txt";

    solveTask1(&filename);

    return 0;
}
