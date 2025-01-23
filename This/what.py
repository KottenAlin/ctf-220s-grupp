from PIL import Image
from PIL.ExifTags import TAGS
from PIL import ExifTags
from PIL.PngImagePlugin import PngInfo

# Create a new 1x1 pixel image with white background
img = Image.new('RGB', (1, 1), color='white')

# Create info object for metadata
meta = PngInfo()
meta.add_text("gemigflaggan", "gemigflaggan")

# Save the image with metadata
img.save('empty_with_metadata.jpg', pnginfo=meta)