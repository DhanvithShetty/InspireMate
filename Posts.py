from PIL import Image, ImageDraw, ImageFont
import textwrap

def CreatePost(Quote, BackgroundImagePath, CreatedPostPath):
    
    # Open the background image
    BackgroundImage = Image.open(BackgroundImagePath)
    
    # Convert to RGB if the image has an alpha channel (RGBA)
    if BackgroundImage.mode == 'RGBA':
        BackgroundImage = BackgroundImage.convert('RGB')
    
    # Load the required font
    font_path = "Fonts/Newyear Goo.ttf"  # Ensure this is the correct path to your font
    font_size = 54
    font = ImageFont.truetype(font_path, font_size)
    
    # Create a drawing context for the image
    draw = ImageDraw.Draw(BackgroundImage)
    
    # Get the dimensions of the background image
    image_width, image_height = BackgroundImage.size
    side_margin = 100  # Margin from the sides of the image
    max_text_width = image_width - 2 * side_margin
    
    # Wrap the text to fit within the available width
    text_wrap_width = max_text_width // (font_size // 2)
    wrapped_text = textwrap.fill(Quote, width=text_wrap_width)
    
    # Calculate the bounding box of the wrapped text (to get the actual size of the text)
    text_bbox = draw.textbbox((0, 0), wrapped_text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    
    # If the text exceeds the available vertical space, reduce the font size
    if text_height > image_height - 2 * side_margin:
        font_size = int((image_height - 2 * side_margin) * 0.8 / (text_height / font_size))
        font = ImageFont.truetype(font_path, font_size)
        wrapped_text = textwrap.fill(Quote, width=text_wrap_width)
        text_bbox = draw.textbbox((0, 0), wrapped_text, font=font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    
    # Calculate the position for the text to be centered within the image
    text_x_position = (image_width - text_width) / 2
    text_y_position = (image_height - text_height) / 2
    
    # Add the wrapped text to the image at the calculated position
    draw.text((text_x_position, text_y_position), wrapped_text, font=font, fill="black")
    
    # Save the final image to the specified output path
    BackgroundImage.save(CreatedPostPath)
    print(f"Post created successfully and saved to {CreatedPostPath}")
