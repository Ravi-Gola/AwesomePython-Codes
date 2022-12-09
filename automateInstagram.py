from instabot import Bot
bot=Bot()
bot.login(username="awesome_code_for_you",password="@9997626161")
followers=bot.get_user_followers("awesome_code_for_you")
for follower in followers:
    print(bot.get_user_info(follower))