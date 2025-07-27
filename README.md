# JPEG to PNG Converter

A simple Python script that converts all `.jpg` and `.jpeg` images in the `INPUT` folder to `.png` format and saves them in the `OUTPUT` folder.

The script uses the [Pillow](https://pillow.readthedocs.io/) library for image processing and **automatically creates the `OUTPUT` folder** if it doesn’t exist.

---

## Features
- Converts `.jpg` and `.jpeg` files to `.png`.
- Automatically creates the `OUTPUT` folder (no manual setup needed).
- Keeps the same filenames (only the extension changes).
- Skips non-image files.

---

## How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/jpeg-to-png-converter.git
   cd jpeg-to-png-converter
   ```

2. **Install dependencies (Pillow):**
   ```bash
   pip install pillow
   ```

3. **Place your images** inside the `INPUT` folder.

4. **Run the script:**
   ```bash
   python "PNG to JPEG.py"
   ```

5. **Check the converted `.png` files** in the `OUTPUT` folder.

---

## Folder Structure
```
project/
├── INPUT/          # Place JPEG images here
├── OUTPUT/         # Converted PNG files will be saved here (ignored by Git)
├── PNG to JPEG.py  # Conversion script
└── README.md
```

---

## Requirements
- Python 3.7+
- Pillow (`pip install pillow`)

---

## Notes
- The `OUTPUT` folder is ignored in Git (via `.gitignore`) to keep the repo clean.
- Add your own sample images to `INPUT` for testing.

---

## License
Feel free to use, modify, and share this project for any purpose.
