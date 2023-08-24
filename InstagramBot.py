from instabot import Bot
bot=Bot()
bot.login(username="focus_in_facts",password="password",use_cookie=False)
#bot.follow('akshaykumar') 

#bot.upload_photo("C:/Users/INDIA/Downloads/the-legend-of-hanuman-wallpapers---the-legend-of-hanuman-4k-wallpaper.jpg",caption="The Biggest Protector of every human being is Lord Hanuman")
#bot.unfollow("akshaykumar")
#bot.send_message("Hey Dude Bhuppi Here",["the_diamond_hrt","mr._expert_810"])

# followers=bot.get_user_followers("focus_in_facts")
# for follower in followers:
    
#     print(bot.get_user_info(follower))

following=bot.get_user_following("focus_in_facts")
for Following in following:
    print(bot.get_user_info(Following))