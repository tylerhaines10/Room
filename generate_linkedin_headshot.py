import google.generativeai as genai
from PIL import Image
import io

genai.configure(api_key="YOUR_GOOGLE_API_KEY")

# Use Imagen 3
imagen = genai.ImageGenerationModel("imagen-3.0-generate-002")

prompt = """
Professional LinkedIn headshot of a person,
business casual attire, neutral background,
soft studio lighting, friendly smile,
sharp focus, high quality portrait photography
"""

result = imagen.generate_images(
    prompt=prompt,
    number_of_images=1,
    aspect_ratio="1:1",
)

# Save the image
image = result.images[0]
image._pil_image.save("headshot.png")
print("Saved headshot.png")
