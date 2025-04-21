**AI-Based Image Enhancer**  
*Enhance and upscale images using deep learning for sharper, clearer results.*

---

## **Features**  
🖼️ **Image Super-Resolution**: 2x/4x upscaling without quality loss  
✨ **Noise Reduction**: Clean up grainy/blurry images  
🎨 **Color Correction**: Automatic color enhancement  
📁 **Batch Processing**: Enhance multiple images at once  
⚡ **Fast Processing**: GPU-accelerated performance  

---

## **Tech Stack**  
- **Deep Learning**: ESRGAN  
- **Backend**: Python
- **Frontend**: Streamlit  
- **Computer Vision**: OpenCV, PIL  

---

## **Installation**  
1. **Clone the repo**:  
   ```bash  
   git clone https://github.com/saivignesh-balne/AI-Based_Image_Enhancer.git  
   cd AI-Based_Image_Enhancer  
   ```  

2. **Set up environment**:  
   ```bash  
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate # Linux/Mac
   ```  

3. **Install dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```
   if that doesn't work try
   ```bash
   pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html
   pip install basicsr==1.3.4.9
   pip install opencv-python streamlit Pillow numpy
   ```

---

## **Usage**  
1. **Run the app**:  
   ```bash  
   streamlit run app.py  
   ```  
2. **Enhance images**:  
   - Upload an image and it gives the enhanced image which can be downloaded

---

## **Development**  
To contribute:  
1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/new-model`)  
3. Commit changes (`git commit -m "Add SwinIR support"`)  
4. Push to branch (`git push origin feature/new-model`)  
5. Open a Pull Request  
