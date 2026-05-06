from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyDtwdtgct2kI0t0gLW-ChBkcHU6_x0IRtc")

prompt = """
Professional LinkedIn headshot of a young man in his mid-20s,
voluminous wavy dark brown hair with natural texture,
hazel green-brown eyes, olive tan skin tone,
strong defined jawline and high cheekbones, light stubble,
athletic build, confident natural expression with a slight smile,
wearing a well-fitted navy blue blazer over a white dress shirt,
clean light gray studio background,
soft professional studio lighting from the front,
sharp focus, photorealistic, high quality portrait photography
"""

result = client.models.generate_images(
    model="imagen-4.0-generate-001",
    prompt=prompt,
    config=types.GenerateImagesConfig(
        number_of_images=1,
        aspect_ratio="1:1",
    ),
)

image = result.generated_images[0]
image_bytes = image.image.image_bytes

with open("headshot.png", "wb") as f:
    f.write(image_bytes)

print("Saved headshot.png")
