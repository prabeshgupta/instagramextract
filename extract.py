import os
import instaloader
from PIL import Image
import pytesseract
import pandas as pd

# Step 1: Download posts and reels from Instagram
def download_posts_and_reels(username, download_dir="downloads", login_username=None, login_password=None, max_posts=0, cookies_file="cookies.json"):
    # Create the download directory if it doesn't exist
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    loader = instaloader.Instaloader()

    # Try to load cookies if they exist
    if os.path.exists(cookies_file):
        loader.load_session_from_file(login_username, cookies_file)
        print(f"Loaded session from {cookies_file}.")
    else:
        # Login if username and password are provided
        if login_username and login_password:
            try:
                loader.login(login_username, login_password)
                loader.save_session_to_file(cookies_file)
                print(f"Logged in and session saved to {cookies_file}.")
            except Exception as e:
                print(f"Error logging in: {e}")
                return None

    loader.dirname_pattern = download_dir  # Set the directory for downloads
    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        posts = profile.get_posts()
        
        # Download posts and reels
        count = 0
        for post in posts:
            # Skip tagged posts by checking if it's a reel or regular post
            if post.is_video or post.typename == 'GraphImage':  # Checking if it's a post or reel
                loader.download_post(post, target=download_dir)
                count += 1
                print(f"Downloaded post {count}.")
                if max_posts > 0 and count >= max_posts:
                    break
        if count == 0:
            print(f"No posts or reels found for {username}.")
    except Exception as e:
        print(f"Error downloading posts: {e}")
        return None
    return download_dir

# Step 2: Extract text from images using OCR
def extract_text_from_images(download_dir):
    text_data = []
    for root, _, files in os.walk(download_dir):
        for file in files:
            if file.endswith((".jpg", ".png")):
                image_path = os.path.join(root, file)
                try:
                    text = pytesseract.image_to_string(Image.open(image_path))
                    text_data.append({"image": file, "text": text.strip()})
                    print(f"Extracted text from {file}.")
                except Exception as e:
                    print(f"Error processing {file}: {e}")
    return text_data

# Step 3: Save extracted text to an Excel file
def save_to_excel(data, output_file="output.xlsx"):
    try:
        df = pd.DataFrame(data)
        df.to_excel(output_file, index=False)
        print(f"Data saved to {output_file}.")
    except Exception as e:
        print(f"Error saving data to Excel: {e}")

# Main function to integrate everything
if __name__ == "__main__":
    # Replace 'username' with the Instagram handle you want to download posts from
    instagram_username = "username"  # Instagram handle to download posts
    output_directory = "downloads"
    output_excel_file = "output.xlsx"

    # Instagram login credentials (fill in your username and password)
    login_username = "username"  
    login_password = "password"  

    # Ask the user how many posts to download
    try:
        max_posts = int(input("Enter the number of posts to download (0 for all): "))
        if max_posts < 0:
            print("Please enter a valid number (>= 0).")
            exit()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit()

    # Download posts and reels (but avoid tagged content)
    download_directory = download_posts_and_reels(instagram_username, output_directory, login_username, login_password, max_posts)
    if download_directory is None:
        print("Failed to download posts.")
    else:
        # Extract text from downloaded images
        extracted_data = extract_text_from_images(download_directory)

        # Save extracted text to an Excel file
        save_to_excel(extracted_data, output_excel_file)
