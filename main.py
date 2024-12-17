import random
from Quotes import FetchQuote, RateLimitError
from Posts import CreatePost
from Upload import UploadPost
from Designs import Backgrounds_And_Font_Colours, Caption_Hashtags

def main():
    try:
        # Fetching a random quote and author
        Quote_Data = FetchQuote()

        Quote = Quote_Data['Quote']
        Author = Quote_Data['Author']

        # Randomly selecting a background and font color from Designs.py
        Background, FontColour = random.choice(list(Backgrounds_And_Font_Colours.items()))
        CreatedPostPath = "InstaPost.jpg"

        # Creating the post (image with quote)
        CreatePost(Quote, Background, FontColour, CreatedPostPath)

        # Preparing the caption with hashtags from Designs.py
        PostCaption = f'"{Quote}" - {Author}'
        
        CallToAction = "Tag/Share this to someone who needs to hear this!"
        
        # Mandatory Hashtags
        Hashtags = ["#InspireMate", "#QuotesToLiveBy"]
        
        # Randomly select additional 8 more hashtags from the Caption_Hashtags list
        Hashtags += random.sample(Caption_Hashtags, 8)  # Adjust the number for a total of 10-15 hashtags

        # Join the hashtags into a string with spaces between them
        PostHashtags = " ".join(Hashtags)

        # Complete the caption by adding the CTA and hashtags
        PostCaption += f"\n\n{CallToAction}\n\n{PostHashtags}"
        
        # Upload the post to Instagram
        UploadPost(CreatedPostPath, PostCaption)

    except RateLimitError as e:
        # If there's a rate limit error, print the error and stop execution
        print(f"Error: {e}")

    except Exception as e:
        # Catch any other exceptions (e.g., unexpected response)
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
