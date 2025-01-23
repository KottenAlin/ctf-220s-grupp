from PIL import Image
import piexif

def add_custom_metadata(image_path, output_path, custom_string):
    # Open the image
    img = Image.open(image_path)

    # Prepare EXIF metadata
    exif_dict = {"0th": {piexif.ImageIFD.ImageDescription: custom_string.encode("utf-8")}}
    exif_bytes = piexif.dump(exif_dict)

    # Save the image with the new EXIF data
    img.save(output_path, exif=exif_bytes)
    print(f"Metadata added successfully! Saved as {output_path}")

# Paths and custom metadata
input_image = "input.png"  # Replace with your input image file name
output_image = "output_with_metadata.png"  # Replace with desired output file name
custom_metadata = "gemigflaggan"

# Add metadata to the image
add_custom_metadata(input_image, output_image, custom_metadata)
