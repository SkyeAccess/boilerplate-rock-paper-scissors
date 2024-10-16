import random

def player(prev_play, opponent_history=[], play_order={}, abbey_wins=0):
    if not prev_play:
        prev_play = 'R'

    opponent_history.append(prev_play)
    
    # Count the number of wins for Abbey
    if prev_play == 'R':
        abbey_wins += 1 if prev_play == 'P' else 0
    elif prev_play == 'P':
        abbey_wins += 1 if prev_play == 'S' else 0
    elif prev_play == 'S':
        abbey_wins += 1 if prev_play == 'R' else 0

    prediction = 'P'  # Default prediction

    # Analyze the last 5 moves
    if len(opponent_history) > 5:
        last_five = "".join(opponent_history[-5:])
        play_order[last_five] = play_order.get(last_five, 0) + 1
        
        potential_plays = [
            "".join([*opponent_history[-4:], v]) 
            for v in ['R', 'P', 'S']
        ]

        sub_order = {
            k: play_order[k]
            for k in potential_plays if k in play_order
        }

        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1:]

    response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    # Introduce dynamic randomness based on Abbey's win rate
    win_rate_threshold = 3  # Threshold of winning rounds
    if abbey_wins > win_rate_threshold:  # If Abbey wins too often
        if random.random() < 0.2:  # 20% chance to pick a random choice
            return random.choice(['R', 'P', 'S'])

    return response[prediction]
