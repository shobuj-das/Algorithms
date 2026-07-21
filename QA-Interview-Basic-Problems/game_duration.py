# https://judge.beecrowd.com/en/problems/view/1047
    

def print_result(hour, minutes):
    print(f"O JOGO DUROU {hour} HORA(S) E {minutes} MINUTO(S)")


def count_duration_of_game(start_hour, start_min, finish_hour, finish_min):

    # if finish_hour < start_hour:
    #     finish_hour += 24
    
    minutes = (60-(start_hour-finish_hour)) if start_hour>=finish_hour else (60-(finish_hour-start_hour))

    if start_hour >= finish_hour:
        hour = 24 - start_hour - finish_hour
    else:
        hour = finish_hour - start_hour
    
    if finish_min < start_min:
        hour -= 1

    print_result(hour,minutes)



if __name__=="__main__":
    # take input
    count_duration_of_game(7,7,7,7)
