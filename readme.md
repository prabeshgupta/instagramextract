# Instagram Post and Reel Downloader with OCR

This tool allows you to download posts and reels from an Instagram profile at once, extract text from images using OCR, and save the extracted text to an Excel file. Tagged posts are skipped to ensure only original posts and reels are processed.

## Features
- Download posts and reels from a specified Instagram profile.
- Skip tagged posts to focus on the profile's original content.
- Extract text from downloaded images using OCR (Tesseract).
- Save extracted text and corresponding image filenames to an Excel file.

---

## Requirements

### Python Dependencies
Make sure you have Python installed (version 3.8 or later) and the following packages:

```bash
pip install instaloader pillow pytesseract pandas
```

### Additional Software

1. **Tesseract OCR**
   - Download and install Tesseract OCR from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki) or your system's package manager.
   - Ensure "C:\Program Files\Tesseract-OCR" is added to your system's PATH environment variable.
   - Verify installation with:
     ```bash
     tesseract --version
     ```

   #### Configuring Tesseract Path
   - If Tesseract is not automatically recognized, specify its path explicitly in the script:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
     ```
   - Replace the path with the actual installation path of Tesseract on your system.

2. **Optional Cookies Management**
   - Cookies are saved to a `cookies.json` file to reduce frequent logins.

---

## How to Use

### 1. Clone or Download the Script
Download the script to your local machine.

### 3. Set Instagram Username

Update the `instagram_username` in the script that you want to download posts from:

```python
instagram_username = "username"  
```

### 3. Configure Instagram Credentials

Update the `login_username` and `login_password` variables in the script with your Instagram login credentials:

```python
login_username = "your_instagram_username"  
login_password = "your_instagram_password"  
```

Alternatively, you can use a session file (`cookies.json`) for automatic login without entering credentials repeatedly.

### 4. Run the Script

To execute the script:

```bash
python extract.py
```
Or on Windows:
```bash
py extract.py
```

### 4. Specify the Number of Posts

When prompted, enter the number of posts to download:
- `0` to download all available posts and reels.
- Any other number (e.g., `5`) to limit the download.

### 5. Output

The script will:
1. Download the specified posts and reels to the `downloads/` directory.
2. Extract text from downloaded images.
3. Save the extracted text to an Excel file named `output.xlsx`.

---

## Directory Structure

After running the script, the following structure is created:

```
project-directory/
├── cookies.json          # Stores login session (optional)
├── downloads/            # Contains downloaded posts and reels
├── extractor.py          # Main script
├── output.xlsx           # Excel file with extracted text
```

---

## Notes
- Ensure your Instagram account credentials are valid.
- Avoid running the script too frequently to prevent account lockout.
- Use the cookies feature to minimize login attempts.
- Tesseract must be correctly installed and added to your PATH.

---

## Future Enhancements
- Support for captions and metadata extraction.
- Additional filters for content (e.g., filtering by hashtags or date).
- Enhanced error handling for account bans or CAPTCHA challenges.