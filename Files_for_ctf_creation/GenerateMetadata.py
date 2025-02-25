from PIL import Image
import piexif
import ffmpeg


def add_custom_metadata(image_path, output_path, custom_string):
    # Open the image
    img = Image.open(image_path)

    # Prepare EXIF metadata
    # Add metadata using UserComment tag
    exif_dict = {"Exif": {piexif.ExifIFD.UserComment: custom_string.encode()}}
    exif_bytes = piexif.dump(exif_dict)

    # Save the image with the new EXIF data
    img.save(output_path, exif=exif_bytes)
    print(f"Metadata added successfully! Saved as {output_path}")

# Paths and custom metadata
input_image = "c:/Users/22sebali/Desktop/Important/cybersäkerhet/ctf-220s-grupp/This/input.png"  # Full path to input image
output_image = "c:/Users/22sebali/Desktop/Important/cybersäkerhet/ctf-220s-grupp/This/output_with_metadata.png"  # Full path to output
custom_metadata = "CTF220s{älgarna_har_fått_nog}"  # Replace with your custom metadata



# Add metadata to the image
add_custom_metadata(input_image, output_image, custom_metadata)

def add_video_metadata(input_file, output_file, metadata):
        # Create an ffmpeg input stream
    stream = ffmpeg.input(input_file)

    # Create output stream with all metadata
    metadata_dict = {f"metadata:{k}": v for k, v in metadata.items()}
    stream = ffmpeg.output(stream, output_file, **metadata_dict)

    # Run the ffmpeg command
    ffmpeg.run(stream)

# Add metadata to the video
video_path = "hello.mp4"  # Replace with your actual video file path
output_path = "output_with_metadata.mp4"  # Replace with desired output file path
metadata = {
        "title": "My Awesome Video",
        "artist": "John Doe",
        "album": "Summer Vibes",
        "year": "2023",
        "comment": "This is a sample video with metadata.",
        "copyright": "Copyright 2023, All rights reserved."
    }



