from internet_speed_bot import InternetSpeedBot

bot = InternetSpeedBot()
print(f"down: {bot.down}")
print(f"up: {bot.up}")
bot.sina_at_provider()
