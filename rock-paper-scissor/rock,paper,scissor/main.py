import random
from datetime import timedelta, datetime
from config import GAME_CHOICES, RULES, score_bord
from decorators import log_time


def get_user_choice():
    """
    user choice from GAME_CONFIG
    """
    user_input = input('ENTER your choice (r,p,s): '
                       )
    if user_input not in GAME_CHOICES:
        print("Ooops!! wrong choice")
        return get_user_choice()
    return user_input

def get_user_play_again_choice():
    """
    does your user want play again?
    :return:
    """
    play_again = input("Do you want play again? (y/n)")
    if play_again == 'y':
        play_one_hand()
    elif play_again == 'n':
        pass
    else:
        return get_user_play_again_choice()

def get_system_choice():
    """
    choice random from GAME_CONFIG
    """
    return random.choice(GAME_CHOICES)

def find_winner(user, system):
    """
    receive user and system choice, sort them and compare with game rules
    :param user:
    :param system:
    :return: winner
    """
    match = {user, system}
     
    if len(match) == 1:
        return None

    return RULES[tuple(sorted(match))]

def update_scorboard(result):
    """
    each 3 score add +1 to that user scoreborad
    :param result:
    :return: scoreboard
    """
    if result['user'] == 3:
        score_bord['user'] +=1
        msg = 'you win'
    else:
        score_bord['system'] +=1
        msg = 'you lose'

    print('#'* 30)
    print("##", f'user: {score_bord["user"]}'.ljust(24),"##")
    print("##", f'system: {score_bord["system"]}'.ljust(24),"##")
    print("##", f'last_game: {msg}'.ljust(24),"##")
    print('#' * 30)


def play_one_hand():
    """
    main play handler
    """
    result = {'user':0, 'system':0}
    while result['user'] < 3 and result['system'] < 3:
        user_choice = get_user_choice()
        system_choice = get_system_choice()
        winner = find_winner(user_choice, system_choice)
        if winner == user_choice:
            msg = "you win"
            result['user'] +=1
        elif winner == system_choice:
            msg = "you lose"
            result['system'] +=1
        else:
            msg = "draw"
        print(f"your choice: {user_choice}\t system: {system_choice}\t result: {msg}")
        print(result)

    update_scorboard(result)
    get_user_play_again_choice()


@log_time
def play():
    play_one_hand()

if __name__ == '__main__':
    # start_time = datetime.now()
    play()
    # end_time = datetime.now()
    # duration = end_time - start_time
    # print("total time: ", str(end_time-start_time)[:7])
    # print(
    #     f"total time:  {duration} : {duration.seconds} : {duration.seconds // 3600} :{duration.seconds // 60}"
    #     f" :{duration.seconds % 60}",
    # )

