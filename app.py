import streamlit as st
import zipfile
import os
from PIL import Image
#set app name

# Set favicon
st.set_page_config(
        page_title="Video_frame_predictor",
        page_icon="chart_with_upwards_trend"
    )
#link the fontawsome 
css_example = '''
<!-- Import Font Awesome CSS -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<!-- Use Font Awesome icons -->
<i class="fa-solid fa-square"></i>
<i class="fa-solid fa-dragon"></i>
<i class="fa-solid fa-paw"></i>
'''
st.write(css_example, unsafe_allow_html=True)
st.markdown("""
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" integrity="sha512-vNtQSlSCF83C5NcQklm8CwYiuPAxnqSmrMtVfu2TrS+duYq37D8tMbAoqx/MbLV58gVz2lPGTlBKHpxWrnM3dQ==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    </head>
""", unsafe_allow_html=True)
st.markdown("""
        <style>
               .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-right : 0.2rem;
                    
                }
        </style>
        """, unsafe_allow_html=True)

st.markdown('<div class="custom-container"><p style="font-size:30px; color:purple;"><b>Welcome to the app!</b></p></div>', unsafe_allow_html=True)
def main():
    col1 = st.sidebar
    with col1:

        st.markdown('<h1><i class="fas fa-question-circle" style="color:green;"></i> How to Use</h1>', unsafe_allow_html=True)
        st.markdown("""
            <ol>
                <li>Upload videos/video using the file uploader below.</li>
                <li>Click the link '<a href="./uploaded_videos.zip">Download the predicted frames</a>' to download the predicted frames.</li>
            </ol>
            """, unsafe_allow_html=True)
        st.markdown('''<p style="font-size:30px;"><b>Note:</b></p>''' ,unsafe_allow_html=True )
        st.markdown('''<p style="font-size:20px;">If uploading multiple videos, compress them into a zip file before uploading</p>''' ,unsafe_allow_html=True )
    st.write('The model takes in videos as input and returns the predicted frames by learning using sequence-to-sequence learning.')
    st.image('second.png', width=400)
    st.markdown('''<p style=font-size:20px;">Upload your Videos</p>''' , unsafe_allow_html=True )
    uploaded_file = st.file_uploader("Upload Video(s)", type=["mp4", "avi", "mov"], accept_multiple_files=True)
    if uploaded_file is not None:
        with st.spinner("Uploading..."):
            # Create a temporary directory to store uploaded files
            temp_dir = "temp_videos"
            os.makedirs(temp_dir, exist_ok=True)
            for i, file in enumerate(uploaded_file):
                with open(os.path.join(temp_dir, f"video_{i}.mp4"), "wb") as f:
                    f.write(file.getbuffer())
            with zipfile.ZipFile("uploaded_videos.zip", "w") as zipf:
                for file in os.listdir(temp_dir):
                    zipf.write(os.path.join(temp_dir, file), arcname=file)
            st.markdown(
                """
                [Download the predicted frames](./uploaded_videos.zip)
                """
            )
            st.markdown('<p id="footer" style="text-align: right; color:#8B4000;"><b>Developed at Murthy Labs</b></p>', unsafe_allow_html=True)
if __name__ == "__main__":
    main()
