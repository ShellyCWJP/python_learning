import os
import csv
import operator

import constants


def read_ranking_csv():
    """ランキングCSVファイルの読み込みを行う

    Returns:
        list: ソートしたランキングの内容を格納したリスト
    """
    ranking = []

    if os.path.exists(constants.RANKING_FILE_PATH):
        with open(constants.RANKING_FILE_PATH, 'r') as file:
            reader = csv.reader(file)
            reader = sorted(reader, key=operator.itemgetter(1), reverse=True)
            ranking = reader[1:]

    return ranking


def touch_ranking_csv():
    """ランキングCSVファイルがなければ作成する
    """
    with open(constants.RANKING_FILE_PATH, 'w') as file:
        writer = csv.DictWriter(
            file,
            fieldnames=constants.RANKING_FILE_HEADER
        )
        writer.writeheader()


def write_ranking_csv(restaurant):
    """ランキングCSVファイルの書き込みを行う

    Args:
        restaurant (str): ユーザーが選択したレストラン名
    """
    current_ranking = []

    if os.path.exists(constants.RANKING_FILE_PATH):
        current_ranking_raw = read_ranking_csv()
        for row in current_ranking_raw:
            current_ranking.append(row[0])
    else:
        touch_ranking_csv()

    is_exists_restaurant = current_ranking.index(restaurant) \
        if restaurant in current_ranking else None

    if is_exists_restaurant is None:
        with open(constants.RANKING_FILE_PATH, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([restaurant, 1])
    else:
        with open(constants.RANKING_FILE_PATH, 'w') as file:
            writer = csv.DictWriter(
                file,
                fieldnames=constants.RANKING_FILE_HEADER
            )
            writer.writeheader()
            for row in current_ranking_raw:
                if row[0] == restaurant:
                    row[1] = int(row[1]) + 1
                writer.writerow({'Name': row[0], 'Count': row[1]})
