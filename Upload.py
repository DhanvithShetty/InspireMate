from instabot import Bot
import os
import shutil

def UploadPost(image_path, caption):
    # Remove the 'config' folder if it exists
    if os.path.exists("config"):
        shutil.rmtree("config")
        print("Old config folder deleted.")

    # Ensure no conflicts with the 'REMOVE_ME' file
    remove_me_file = f"{image_path}.REMOVE_ME"
    if os.path.exists(remove_me_file):
        os.remove(remove_me_file)
        print(f"Removed existing file: {remove_me_file}")
    
    # Initialize the bot
    bot = Bot()

    # Login to Instagram (replace with your credentials)
    bot.login(username="your_username", password="your_password")

    # Upload an image to Instagram (provide the path to your image)
    bot.upload_photo(image_path, caption=caption)
