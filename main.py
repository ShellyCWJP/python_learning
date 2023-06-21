import roboto.utils
import ranking.utils

# ユーザーが設定した名前
name = None

# 名前を尋ねる
name = roboto.utils.ask_name()

# レストランのランキングリストを取得する
ranking_list = ranking.utils.read_ranking_csv()

# ユーザーに好きなレストランを尋ねる
favorite_restaurant = roboto.utils.ask_favorite_restaurant(name, ranking_list)

# 回答を元にランキングリストを更新する
ranking.utils.write_ranking_csv(favorite_restaurant)

# 別れの挨拶をする
roboto.utils.say_goodbye(name)
