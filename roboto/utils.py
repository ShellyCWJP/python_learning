def input_handling():
    """ユーザーの入力を受け取る

    Returns:
        str: ユーザーの入力
    """
    try:
        answer = input(">> ")
    except KeyboardInterrupt:
        print('\n')
        exit()

    return answer


def ask_name():
    """ユーザーに名前を尋ねる

    Returns:
        str: ユーザーの名前
    """
    name = None

    while True:
        if name is not None and name != '':
            break
        print('こんにちは！私はRobokoです。あなたのお名前は何ですか？')
        name = input_handling()

    return name


def say_goodbye(name):
    """ユーザーに別れを告げる

    Args:
        name (str): ユーザーの名前

    Returuns:
        None
    """
    print(f'{name}さん。ありがとうございました。\n良い一日を！さようなら。')


def ask_yes_or_no():
    """YesかNoで答えてもらう

    Returns:
        bool: Yes は True を返す
    """
    is_valid_answer = False

    while is_valid_answer is False:
        try:
            answer = input_handling()
            answer = answer.lower()

            if answer[0] == 'y':
                is_valid_answer = True
                return True
            elif answer[0] == 'n':
                is_valid_answer = True
                return False
            else:
                print('YesかNoで答えてください。')
                continue
        except KeyboardInterrupt:
            print('\n')
            exit()


def ask_favorite_restaurant_name(name):
    """ユーザーに好きなレストランを書いてもらう

    Args:
        name (str): ユーザーの名前

    Returns:
        str: 好きなレストランの名前
    """
    restaurant = None

    while True:
        if restaurant is not None and restaurant != '':
            break
        print(f"{name}さん。どこのレストランが好きですか？")
        restaurant = input_handling()

    return restaurant


def ask_favorite_restaurant(name, ranking):
    """ユーザーに好きなレストランを尋ねる

    Args:
        name (str): ユーザーの名前
        ranking (list): レストランのランキングリスト

    Returns:
        str: 好きなレストランの名前
    """
    restaurant = None

    for row in ranking:
        print(f'私のオススメのレストランは、{row[0]}です。\n'
              'このレストランは好きですか？[Yes/No]')

        answer = ask_yes_or_no()
        restaurant = row[0] if answer is True else False

        if answer is True and restaurant is not None:
            break
    else:
        restaurant = ask_favorite_restaurant_name(name)

    return restaurant
