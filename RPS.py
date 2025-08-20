# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    guess = "R"  # default

    # Chỉ chạy Markov chain nếu đủ dữ liệu
    n = 3  # độ dài context
    if len(opponent_history) > n:
        # lấy n moves gần nhất làm key
        pattern = "".join(opponent_history[-n:])
        possible = {}

        # duyệt qua toàn bộ lịch sử để đếm tần suất
        for i in range(len(opponent_history) - n):
            key = "".join(opponent_history[i:i+n])
            if key == pattern:
                next_move = opponent_history[i+n]
                possible[next_move] = possible.get(next_move, 0) + 1

        if possible:
            # chọn move có xác suất cao nhất
            predicted = max(possible, key=possible.get)
            guess = counter_move(predicted)

    return guess


def counter_move(move):
    """Trả về chiêu thắng move"""
    if move == "R":
        return "P"
    if move == "P":
        return "S"
    if move == "S":
        return "R"
