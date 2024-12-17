import requests

class RateLimitError(Exception):
    """Custom exception to indicate rate limit errors."""
    pass

def FetchQuote():
    # API URL
    ZenQuotesAPIUrl = "https://zenquotes.io/api/random/"

    # Get API Response
    APIResponse = requests.get(ZenQuotesAPIUrl)
    JSONData = APIResponse.json()

    # Check if the response contains the expected quote or an error message
    if JSONData and 'q' in JSONData[0] and 'a' in JSONData[0]:
        Quote = JSONData[0].get('q', "No quote found")
        Author = JSONData[0].get('a', "No author found")

        # Check if the quote indicates an error (e.g., rate limit)
        if 'Too many requests' in Quote:
            raise RateLimitError("Rate limit reached: Too many requests. Please try again later.")
        else:
            return {"Quote": Quote, "Author": Author}
    else:
        # Return a generic error if expected keys are missing
        raise Exception("Unexpected response format.")

