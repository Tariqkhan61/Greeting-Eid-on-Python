import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import time

# Set page configuration
st.set_page_config(page_title="Eid Mubarak", layout="centered")

st.title("🎉 Eid Mubarak! 🎉")
st.subheader("🌙Afaq-Imran-Qamar-Munawwar-Zaheer-Khalid Saeed")
st.write("##### True Friends")
st.write("#### Wishing you a joyous and blessed Eid!")

# Add your image below the subheading with a new caption
image_path = "c:/Users/Glow Computers/Desktop/Album/Oldies-1.jpg"  # Ensure this path is correct
st.image(image_path, caption="🌙 Wishing You a Joyous and Blessed Eid 🌙", use_container_width=True)

# Create animated frames
def create_frame(text, color, font_path, font_size):
    img = Image.new("RGB", (600, 400), color)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)  # Load a font from a .ttf file
    w, h = draw.textbbox((0, 0), text, font=font)[2:]  # Using textbbox to get text dimensions
    draw.text(((600 - w) // 2, (400 - h) // 2), text, fill="red", font=font)
    return img

# Define font path (update this if you don't have arial.ttf)
font_path = "arial.ttf"  # Ensure this font file exists in your environment
colors = ["blue", "green", "purple", "orange", "gold"]
frames = [create_frame("Eid Mubarak!", color, font_path, 60) for color in colors]

# Display animation
placeholder = st.empty()

for i in range(5):  # Loop the animation 5 times
    for frame in frames:
        placeholder.image(np.array(frame), use_container_width=True)  # Updated to use use_container_width
        time.sleep(0.5)

# Display a static message after the animation
st.success("#### 🤩May your Eid be filled with love, and happiness🤩!")



