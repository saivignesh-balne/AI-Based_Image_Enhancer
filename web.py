import streamlit as st
import cv2
import torch
import os
from PIL import Image
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

# Set up the Real-ESRGAN model
def setup_real_esrgan():
    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)
    model_path = 'realesrgan-x4plus.pth'  # Path to the pre-trained weights
    upsampler = RealESRGANer(
        scale=4,
        model_path=model_path,
        model=model,
        tile=0,  # Tile size (0 for no tiling)
        tile_pad=10,
        pre_pad=0,
        half=False  # Use FP16 for faster inference (set to True if your GPU supports it)
    )
    return upsampler

# Enhance image quality and resolution
def enhance_image(image_path, upsampler):
    # Read the input image
    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        raise ValueError(f"Failed to read image: {image_path}")

    # Enhance the image
    output, _ = upsampler.enhance(img, outscale=4)  # Upscale by 4x

    # Save the enhanced image
    output_path = os.path.splitext(image_path)[0] + '_enhanced.png'
    cv2.imwrite(output_path, output)
    return output_path

# Streamlit app
def main():
    st.title("Real-ESRGAN Image Enhancement")
    st.write("Upload a low-resolution or blurred image, and this app will enhance its quality and resolution using Real-ESRGAN.")

    # Upload image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True, width=800)

        # Save the uploaded image temporarily
        temp_image_path = "temp_input_image.png"
        image.save(temp_image_path)

        # Set up the Real-ESRGAN model
        upsampler = setup_real_esrgan()

        # Enhance the image
        st.write("Enhancing image...")
        enhanced_image_path = enhance_image(temp_image_path, upsampler)

        # Display the enhanced image
        enhanced_image = Image.open(enhanced_image_path)
        st.image(enhanced_image, caption="Enhanced Image", use_column_width=True, width=800)

        # Provide a download link for the enhanced image
        with open(enhanced_image_path, "rb") as file:
            btn = st.download_button(
                label="Download Enhanced Image",
                data=file,
                file_name="enhanced_image.png",
                mime="image/png"
            )

        # Clean up temporary files
        os.remove(temp_image_path)
        os.remove(enhanced_image_path)

if __name__ == "__main__":
    main()