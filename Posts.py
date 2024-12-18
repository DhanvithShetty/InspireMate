from PIL import Image, ImageDraw, ImageFont
import textwrap

def CreatePost(Quote, BackgroundImagePath, FontColour, CreatedPostPath):
    try:
        # Open the background image
        BackgroundImage = Image.open(BackgroundImagePath)

        # Convert to RGB mode to ensure compatibility with JPEG format
        if BackgroundImage.mode != 'RGB':
            BackgroundImage = BackgroundImage.convert('RGB')

        # Load the required font
        font_path = "Fonts/Anantason-Bold.ttf"  # Ensure this is the correct path to your font
        font_size = 54
        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            raise Exception(f"Font not found at {font_path}. Please check the path.")

        # Create a drawing context for the image
        draw = ImageDraw.Draw(BackgroundImage)

        # Get the dimensions of the background image
        image_width, image_height = BackgroundImage.size
        side_margin = 100  # Margin from the sides of the image
        max_text_width = image_width - 2 * side_margin

        # Wrap the text to fit within the available width
        text_wrap_width = max_text_width // (font_size // 2)
        wrapped_text = textwrap.fill(Quote, width=text_wrap_width)

        # Calculate the bounding box of the wrapped text
        text_bbox = draw.textbbox((0, 0), wrapped_text, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

        # If the text exceeds the available vertical space, adjust font size
        if text_height > image_height - 2 * side_margin:
            font_size = int((image_height - 2 * side_margin) * 0.8 / (text_height / font_size))
            font = ImageFont.truetype(font_path, font_size)
            wrapped_text = textwrap.fill(Quote, width=text_wrap_width)
            text_bbox = draw.textbbox((0, 0), wrapped_text, font=font)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

        # Calculate the position for the text to be centered
        text_x_position = (image_width - text_width) / 2
        text_y_position = (image_height - text_height) / 2

        # Add the wrapped text to the image
        draw.text((text_x_position, text_y_position), wrapped_text, font=font, fill=FontColour)

        # Save the final image in JPEG format
        BackgroundImage.save(CreatedPostPath, format="JPEG")
        print(f"Post created successfully and saved to {CreatedPostPath}")

    except Exception as e:
        print(f"Error in CreatePost: {e}")
