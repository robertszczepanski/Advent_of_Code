#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>
#include <complex>
// Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53

int isWinningNumber(int number, std::vector<int> &winning_numbers, bool checking_winning) {
    if (checking_winning) {
        winning_numbers.push_back(number);
    } else {
        auto it = std::find(winning_numbers.begin(), winning_numbers.end(), number);
        if (*it != 0) {
            return 1;
        }
    }

    return 0;
}

int getNumberOfWinningNumbers(std::string line) {
    int colon_index = line.find(":");
    int game_id = std::stoi(line.substr(5, colon_index - 5));
    std::vector<int> winning_numbers;
    int result = 0;

    std::string number("");
    bool checking_winning = true;
    for (int i = colon_index + 1; i < line.length(); i++) {
        if (std::isdigit(line.at(i))) {
            number += line.at(i);
            if (i == line.length() - 1) {
                result += isWinningNumber(std::stoi(number), winning_numbers, checking_winning);
            }
        } else if (line.at(i) == '|') {
            checking_winning = false;
        } else if (number != "") {
            result += isWinningNumber(std::stoi(number), winning_numbers, checking_winning);
            number = "";
        }
    }

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
        int game_result = getNumberOfWinningNumbers(line);
        result += game_result ? std::pow(2, game_result - 1) : 0;
    }

    std::cout << "Result of task 1: " << result << std::endl;
    input_stream.close();
}

void solveTask2(const std::string *filename) {
    std::ifstream input_stream;
    std::vector<std::pair<int, std::string>> games;
    std::string line;
    int result = 0;
    int wins = 0;

    try {
        input_stream.open(*filename);
    }
    catch (std::ifstream::failure e) {
        std::cerr << "Exception opening a file\n";
    }

    while(std::getline(input_stream, line)) {
        std::pair<int, std::string> game(1, line);
        games.push_back(game);
    }

    for (int i = 0; i < games.size(); i++) {
        int game_result = getNumberOfWinningNumbers(games.at(i).second);

        for (int j = 1; j <= game_result; j++) {
            games.at(i + j).first += games.at(i).first;
        }

        result += games.at(i).first;
    }

    std::cout << "Result of task 2: " << result << std::endl;
    input_stream.close();
}

int main() {
    const std::string filename = "../../input.txt";

    solveTask1(&filename);
    solveTask2(&filename);

    return 0;
}
