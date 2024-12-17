import random
from Quotes import FetchQuote, RateLimitError
from Posts import CreatePost
from Upload import UploadPost
from Designs import Backgrounds_And_Font_Colours

def main():
    try:
        # Step 1: Fetch a random quote and author
        Quote_Data = FetchQuote()

        Quote = Quote_Data['Quote']
        Author = Quote_Data['Author']

        print(f"Quote: {Quote}")
        print(f"Author: {Author}")

        # Step 2: Randomly select a background and font color
        Background, FontColour = random.choice(list(Backgrounds_And_Font_Colours.items()))

        print(f"Selected Background: {Background}")
        print(f"Selected Font Color: {FontColour}")

        # Step 3: Prepare the output path
        CreatedPostPath = "InstaPost.jpg"

        # Step 3: Create the post (image with quote)
        CreatePost(Quote, Background, FontColour, CreatedPostPath)

        # Step 4: Upload the post to Instagram
        #caption = f'"{Quote}" - {Author}'  # Prepare the caption
        #UploadPost(created_post_path, caption)

    except RateLimitError as e:
        # If there's a rate limit error, print the error and stop execution
        print(f"Error: {e}")

    except Exception as e:
        # Catch any other exceptions (e.g., unexpected response)
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
