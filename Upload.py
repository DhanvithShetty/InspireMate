from instabot import Bot
import os
import shutil
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv("credentials.env")

def UploadPost(image_path, caption):
    # Get Instagram credentials from environment variables
    username = os.getenv("INSTA_USERNAME")
    password = os.getenv("INSTA_PASSWORD")

    print(username, password)

    """

    # Ensure the credentials exist
    if not username or not password:
        raise ValueError("Instagram username or password is missing")

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

    # Login to Instagram (using environment variables)
    bot.login(username=username, password=password)

    # Upload an image to Instagram (provide the path to your image)
    bot.upload_photo(image_path, caption=caption)
    """
