import streamlit as st
import subprocess
import os

def download_mp3(url):
    download_dir = ''
    os.chdir(download_dir)  # Change cwd to the desired directory
    command = f"yt-dlp -x --audio-format mp3 {url}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode == 0:
        print("Download complete!")
    else:
        print("Download failed.")   

def main():
    st.title("YouTube MP3 Downloader")
    url = st.text_input("Enter YouTube URL")
    if st.button("Download"):
        download_mp3(url)

if __name__ == "__main__":
    main()