import cv2
import os
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

# Set up the Real-ESRGAN model
def setup_real_esrgan():
    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)
    model_path = 'weights/realesrgan-x4plus.pth'  # Path to the pre-trained weights
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
    output_path = os.path.join('static', os.path.basename(image_path).replace('.png', '_enhanced.png'))
    cv2.imwrite(output_path, output)
    return os.path.basename(output_path)
