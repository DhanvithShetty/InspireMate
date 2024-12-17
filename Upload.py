from instabot import Bot

def UploadPost(image_path, caption):
    # Initialize the bot
    bot = Bot()

    # Login to Instagram (replace with your credentials)
    bot.login(username="your_username", password="your_password")

    # Upload an image to Instagram (provide the path to your image)
    bot.upload_photo(image_path, caption=caption)
