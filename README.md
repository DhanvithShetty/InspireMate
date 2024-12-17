# Inspire Mate (Instagram Account Automation)

A Python project to automate the generation and uploading of inspirational quote images to Instagram. This project integrates image processing, text rendering, random quote fetching, and automated uploads using the several libraries.

---

## Features

1. **Dynamic Quote Fetching**

   - Fetches random quotes and authors using the [ZenQuotes API](https://zenquotes.io/).
   - Handles rate limit errors gracefully with a custom exception.

2. **Dynamic Instagram-Ready Post Creation**

   - Generates Instagram-ready posts by overlaying quotes on customizable backgrounds.
   - Automatically adjusts text size and positioning for a clean look.
   - Supports different font colors depending on the chosen background.

3. **Automated Hashtag Management**

   - Includes a pre-defined set of motivational hashtags for captions.
   - Randomly selects hashtags to make captions engaging and diverse.

4. **Automated Upload to Instagram**
   - Uses `instabot` to upload posts seamlessly.
   - Securely manages Instagram credentials using a `credentials.env` file.

---

## Project Structure

```plaintext
📂 ProjectRoot/
├── Designs.py    # Background images and font color mappings
├── Posts.py      # Generates the quote images
├── Upload.py     # Uploads images to Instagram
├── Quotes.py     # Fetches random quotes using ZenQuotes API
├── Main.py       # Main script to orchestrate the workflow
├── credentials.env   # Stores Instagram credentials (not shared)
└── Fonts/            # Font files used for text rendering
```

---

## Setup Instructions

### 1. Prerequisites

- **Python 3.x**
- Required Libraries:
  - `Pillow` (for image generation)
  - `instabot` (for uploading posts)
  - `requests` (for fetching quotes)
  - `python-dotenv` (to manage credentials)

Install dependencies using the requirements.txt file provided:

```bash
pip install requirements.txt
```

### 2. Folder Structure

Ensure your project directory includes the following:

- **Backgrounds**: Place background image files (e.g., `Black.png`, `Grey.png`) in a folder named `Backgrounds/`.
- **Fonts**: Include your chosen font files (e.g., `Anantason-Bold.ttf`) in a folder named `Fonts/`.
- **credentials.env**: Store your Instagram username and password.

Example `credentials.env`:

```env
INSTA_USERNAME=your_instagram_username
INSTA_PASSWORD=your_instagram_password
```

### 3. Run the Project

Use the `Main.py` script to run the entire workflow:

```bash
python Main.py
```

### Workflow

1. **Fetch a Quote**: Automatically fetches a random motivational quote and author.
2. **Create Post**: Generates a quote image with dynamic font color and backgrounds.
3. **Prepare Caption**:
   - Adds a motivational call-to-action (CTA).
   - Randomly selects hashtags from the predefined list.
4. **Upload to Instagram**: The generated post is uploaded with the caption.

---

## Example Caption Output

- **Quote**: "Believe in yourself and all that you are."
- **Author**: Christian D. Larson
- **Background**: `Backgrounds/Black.png`
- **Font Color**: `#E1C340`

**Caption Example**:

```plaintext
"Believe in yourself and all that you are." - Christian D. Larson

Tag/Share this to someone who needs to hear this!

#InspireMate #QuotesToLiveBy #BelieveInYourself #Motivation #GrowthMindset #DailyInspiration #SuccessQuotes #BeTheChange #InspirationalQuotes #Mindfulness
```

---

## Customization

- **Backgrounds**: Add more images in the `Backgrounds/` folder.
- **Fonts**: Use your preferred `.ttf` or `.otf` fonts.
- **Quotes**: Replace or enhance the quote source as needed.
- **Captions**: Modify the hashtags and call-to-action in `Designs.py` or `Main.py`.

---

## Error Handling

- **Rate Limit**: If the ZenQuotes API exceeds its request limit, the program stops execution with a clear error message.
- **Missing Credentials**: Ensures credentials are securely loaded via `credentials.env`.

---

## Future Enhancements

- Add dynamic hashtag generation.
- Support for scheduling posts.
- Enhance API error handling for other edge cases.

---

## License

This project is licensed under the MIT License.

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.
