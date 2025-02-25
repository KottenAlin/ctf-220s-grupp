from PIL import Image
import sys
import os

def convert_png_to_xpm(png_file, xpm_file):
    try:
        # Open the PNG image
        img = Image.open(png_file)

        # Convert the image to RGB if it's not already in that mode
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # Get image dimensions
        width, height = img.size

        # Create a dictionary to map unique colors to characters
        color_map = {}
        current_char = 33  # Start with ASCII 33 (!)
        max_char = 126    # End with ASCII 126 (~)

        # Generate the XPM header
        xpm_data = []
        xpm_data.append(f"/* XPM */")
        xpm_data.append(f"static char * image[] = {{")
        xpm_data.append(f'"{width} {height} {len(color_map)} 1",')

        # Iterate over each pixel to create the XPM data
        for y in range(height):
            row = []
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                color = (r, g, b)
                # Map the color to a character
                if color not in color_map:
                    if current_char > max_char:
                        raise Exception("Too many unique colors in the image")
                    char = chr(current_char)
                    color_map[color] = char
                    current_char += 1

                row.append(color_map[color])
                row.append(color_map[color])

            # Append the row to the XPM data
            xpm_data.append(f'"{"".join(row)}",')

        # Add the color definitions
        xpm_data.append("};")
        xpm_data.append("")
        xpm_data.append("static char * colors[] = {")
        for color, char in color_map.items():
            r, g, b = color
            xpm_data.append(f'"{char} c #{r:02x}{g:02x}{b:02x}",')
        # Write the XPM data to the output file
        with open(xpm_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(xpm_data))

        print(f"Successfully converted {png_file} to {xpm_file}")

    except Exception as e:
        print(f"Error: {e}")

def convert_png_to_pbm(input_path, output_path=None):
    """
    Converts a PNG image to PBM format.

    :param input_path: Path to the input PNG image.
    :param output_path: Path to save the converted PBM image. If None, saves in the same directory as the input.
    """
    try:
        # Open the PNG image
        img = Image.open(input_path).convert('1')  # Convert to black and white (1-bit)

        # Set the output path
        if output_path is None:
            base_name = os.path.splitext(input_path)[0]
            output_path = f"{base_name}.pbm"

        # Save the image in PBM format
        img.save(output_path, format='PPM')

        print(f"Image successfully converted and saved to: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

#example usage
if __name__ == "__main__":
    '''
    input_png = "c:/Users/22sebali/Desktop/Important/cybersäkerhet/ctf-220s-grupp/This/moose-alg-modified.png"
    output_xpm = "output.xpm"
        convert_png_to_xpm(input_png, output_xpm)
    '''
    input_file = "c:/Users/22sebali/Desktop/Important/cybersäkerhet/ctf-220s-grupp/This/output_with_metadata.png"  # Replace with your PNG file path
    convert_png_to_pbm(input_file)
    
        