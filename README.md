# 🖼️ Image Base64 Encoder/Decoder

A powerful Streamlit web application for converting images to base64 strings and decoding base64 strings back to images. Perfect for developers, designers, and anyone working with image data encoding.

## ✨ Features

### 📤 Image to Base64 Encoder
- **Multi-format Support**: Upload PNG, JPG, JPEG, GIF, and BMP images
- **Live Preview**: Instantly displays uploaded images
- **Base64 Generation**: Converts images to base64 strings automatically
- **Copy & Download**: Easy copying of base64 strings or download as .txt files
- **Clean Interface**: User-friendly upload interface with drag-and-drop support

### 📥 Base64 to Image Decoder
- **Smart Validation**: Automatically detects and validates base64 strings
- **Format Detection**: Recognizes various image formats within base64 data
- **Data URL Support**: Handles base64 strings with data URL prefixes
- **Error Handling**: Robust handling of truncated or corrupted data
- **Image Preview**: Displays decoded images with size information
- **Download Ready**: Save decoded images as PNG files

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd image-base64-encoder-decoder
   ```

2. **Install required packages**
   ```bash
   pip install streamlit pillow
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, navigate to the URL shown in your terminal

## 💻 Usage Guide

### Encoding Images to Base64

1. **Upload an Image**
   - Click "Choose an image file" or drag and drop
   - Supported formats: PNG, JPG, JPEG, GIF, BMP

2. **View Results**
   - Your image appears immediately
   - Base64 string is generated below the image

3. **Copy or Download**
   - Copy the base64 string from the text area
   - Or click "Download Base64 as .txt file"

### Decoding Base64 to Images

1. **Paste Base64 String**
   - Paste your base64 data into the text area
   - Supports both raw base64 and data URLs

2. **Automatic Validation**
   - App validates the base64 format
   - Shows success/error messages

3. **View and Download**
   - Decoded image displays automatically
   - Download as PNG file with one click
   - View image dimensions and details

## 🔧 Technical Features

### Robust Error Handling
- **Truncated Image Support**: Handles incomplete image data gracefully
- **Format Normalization**: Converts various image formats to ensure compatibility
- **Memory Management**: Efficient handling of large images and data

### Smart Validation
- **File Signature Detection**: Identifies image types by binary signatures
- **Data URL Processing**: Automatically strips data URL prefixes
- **Padding Correction**: Auto-corrects base64 padding issues

### User Experience
- **Responsive Design**: Two-column layout for efficient workflow
- **Visual Feedback**: Clear status messages and progress indicators
- **Accessibility**: Proper contrast and semantic markup

## 📁 File Structure

```
image-base64-encoder-decoder/
├── app.py                 # Main Streamlit application
├── README.md             # This file
└── requirements.txt      # Python dependencies (optional)
```

## 🛠️ Dependencies

```
streamlit>=1.28.0
Pillow>=9.0.0
```

## 🎯 Use Cases

- **Web Development**: Embedding images directly in HTML/CSS
- **API Development**: Sending images through REST APIs
- **Data Processing**: Converting images for database storage
- **Email Templates**: Embedding images in email HTML
- **Documentation**: Including images in markdown or documentation
- **Testing**: Creating test data with encoded images

## 🔍 Supported Formats

### Input Formats (Encoding)
- PNG (Portable Network Graphics)
- JPEG/JPG (Joint Photographic Experts Group)
- GIF (Graphics Interchange Format)
- BMP (Bitmap)

### Output Format (Decoding)
- PNG (recommended for best compatibility)

## 🚨 Troubleshooting

### Common Issues

**"Image file is truncated" Error**
- The app now handles this automatically
- Ensure your base64 string is complete
- Try re-copying the base64 data

**"Invalid base64 string" Error**
- Check for missing characters or extra spaces
- Ensure the string is properly formatted
- Remove any non-base64 characters

**Large File Issues**
- Very large images may take time to process
- Consider resizing images before encoding
- Browser memory limits may apply

### Performance Tips
- Use PNG format for best quality-to-size ratio
- Compress images before encoding when possible
- Clear browser cache if experiencing slowdowns

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Create an issue in the repository
3. Ensure you're using the latest version

---

**Built with ❤️ using Streamlit and PIL**

*Perfect for developers, designers, and anyone working with image data encoding!*
