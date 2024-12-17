from Quotes import FetchQuote, RateLimitError
from Posts import CreatePost
from Upload import UploadPost

def main():
    try:
        # Step 1: Fetch a random quote and author
        quote_data = FetchQuote()

        quote = quote_data['Quote']
        author = quote_data['Author']

        print(f"Quote: {quote}")
        print(f"Author: {author}")

        # Step 2: Prepare the background image and output path
        background_image_path = "Backgrounds/Grey_Sheet.png"
        created_post_path = "CreatedPost.jpg"

        # Step 3: Create the post (image with quote)
        CreatePost(quote, background_image_path, created_post_path)

        # Step 4: Upload the post to Instagram (if necessary)
        #caption = f'"{quote}" - {author}'  # Prepare the caption
        #UploadPost(created_post_path, caption)

    except RateLimitError as e:
        # If there's a rate limit error, print the error and stop execution
        print(f"Error: {e}")

    except Exception as e:
        # Catch any other exceptions (e.g., unexpected response)
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
