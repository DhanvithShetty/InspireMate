from instagrapi import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv("credentials.env")

def UploadPost(image_path, caption):
    # Get Instagram credentials from environment variables
    username = os.getenv("INSTA_USERNAME")
    password = os.getenv("INSTA_PASSWORD")

    # Ensure the credentials exist
    if not username or not password:
        raise ValueError("Instagram username or password is missing")
    
    cl = Client()
    cl.login(username, password)
    print("Instagram Login successful")

    cl.photo_upload(image_path, caption)
    print("Post uploaded successfully")