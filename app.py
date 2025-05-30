import streamlit as st
import base64
import io
from PIL import Image
import re

def encode_image_to_base64(image):
    """Convert PIL Image to base64 string"""
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

def is_valid_base64(s):
    """Check if string is valid base64"""
    try:
        # Remove whitespace and any data URL prefixes
        s = re.sub(r'\s+', '', s)
        # Remove data URL prefix if present
        if ',' in s and s.startswith('data:'):
            s = s.split(',', 1)[1]
        
        # Check if length is valid for base64
        if len(s) % 4 != 0:
            # Add padding if needed
            s += '=' * (4 - len(s) % 4)
        
        # Validate base64
        decoded = base64.b64decode(s, validate=True)
        
        # Additional check: try to identify if it's image data
        # Check for common image file signatures
        if len(decoded) > 10:
            # PNG signature
            if decoded.startswith(b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'):
                return True
            # JPEG signature
            elif decoded.startswith(b'\xFF\xD8\xFF'):
                return True
            # GIF signature
            elif decoded.startswith(b'GIF87a') or decoded.startswith(b'GIF89a'):
                return True
            # BMP signature
            elif decoded.startswith(b'BM'):
                return True
            # WebP signature
            elif b'WEBP' in decoded[:12]:
                return True
            # Try to open as image to be sure
            else:
                try:
                    test_img = Image.open(io.BytesIO(decoded))
                    test_img.verify()
                    return True
                except:
                    return False
        return False
    except Exception:
        return False

def decode_base64_to_image(base64_string):
    """Convert base64 string to PIL Image"""
    try:
        # Remove whitespace and any data URL prefixes
        base64_string = re.sub(r'\s+', '', base64_string)
        # Remove data URL prefix if present (e.g., "data:image/png;base64,")
        if ',' in base64_string and base64_string.startswith('data:'):
            base64_string = base64_string.split(',', 1)[1]
        
        img_data = base64.b64decode(base64_string)
        
        # Use BytesIO and load the image with truncation handling
        img_buffer = io.BytesIO(img_data)
        
        # Enable truncated image loading
        from PIL import ImageFile
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        
        image = Image.open(img_buffer)
        
        # Force load the image data to catch truncation issues early
        image.load()
        
        # Convert to RGB if necessary to avoid issues with certain formats
        if image.mode in ('RGBA', 'LA', 'P'):
            # Convert to RGB for consistent handling
            rgb_image = Image.new('RGB', image.size, (255, 255, 255))
            if image.mode == 'P':
                image = image.convert('RGBA')
            rgb_image.paste(image, mask=image.split()[-1] if image.mode in ('RGBA', 'LA') else None)
            image = rgb_image
        elif image.mode not in ('RGB', 'L'):
            image = image.convert('RGB')
            
        return image
    except Exception as e:
        st.error(f"Error decoding base64: {str(e)}")
        return None

def create_download_link(data, filename, link_text):
    """Create a download link for data"""
    b64 = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}">{link_text}</a>'
    return href

# Streamlit App
st.set_page_config(page_title="Image Base64 Encoder/Decoder", layout="wide")

st.title("🖼️ Image Base64 Encoder/Decoder")
st.markdown("Convert images to base64 strings and decode base64 strings back to images")

# Create two columns for the two main functions
col1, col2 = st.columns(2)

with col1:
    st.header("📤 Image to Base64 Encoder")
    
    uploaded_file = st.file_uploader(
        "Choose an image file", 
        type=['png', 'jpg', 'jpeg', 'gif', 'bmp'],
        key="encoder_upload"
    )
    
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Convert to base64
        base64_string = encode_image_to_base64(image)
        
        st.subheader("Base64 String:")
        st.text_area(
            "Copy this base64 string:",
            value=base64_string,
            height=100,
            key="base64_output"
        )
        
        # Create download button for base64 string
        st.download_button(
            label="📥 Download Base64 as .txt file",
            data=base64_string,
            file_name=f"{uploaded_file.name.split('.')[0]}_base64.txt",
            mime="text/plain"
        )

with col2:
    st.header("📥 Base64 to Image Decoder")
    
    base64_input = st.text_area(
        "Paste your base64 string here:",
        height=100,
        key="base64_input"
    )
    
    if base64_input:
        # Check if it's valid base64
        if is_valid_base64(base64_input):
            st.success("✅ Valid base64 string detected!")
            
            # Decode to image
            decoded_image = decode_base64_to_image(base64_input)
            
            if decoded_image is not None:
                # Create a copy of the image to avoid display issues
                display_image = decoded_image.copy()
                
                st.image(display_image, caption="Decoded Image", use_column_width=True)
                
                # Convert image to bytes for download
                img_buffer = io.BytesIO()
                # Save as PNG to ensure compatibility
                decoded_image.save(img_buffer, format='PNG')
                img_bytes = img_buffer.getvalue()
                
                # Create download button for the decoded image
                st.download_button(
                    label="📥 Download Decoded Image",
                    data=img_bytes,
                    file_name="decoded_image.png",
                    mime="image/png"
                )
                
                # Show image info
                st.info(f"Image size: {decoded_image.size[0]} x {decoded_image.size[1]} pixels")
            else:
                st.error("Failed to decode the image. Please check if the base64 string is complete and valid.")
        else:
            st.error("❌ Invalid base64 string. Please check your input.")

# Instructions
st.markdown("---")
st.markdown("## 📋 Instructions")
st.markdown("""
### Encoding Images:
1. Upload an image file using the file uploader on the left
2. The image will be displayed and converted to a base64 string
3. Copy the base64 string or download it as a text file

### Decoding Base64:
1. Paste a base64 string into the text area on the right
2. The app will validate if it's a proper base64 string
3. If valid, the decoded image will be displayed
4. Download the decoded image as a PNG file

**Supported formats:** PNG, JPG, JPEG, GIF, BMP
""")

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit and PIL*")