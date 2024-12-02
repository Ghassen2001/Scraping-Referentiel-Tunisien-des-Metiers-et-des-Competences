# Tunisian Reference of Professions and Skills Scraper  

This repository contains a web scraping script to extract and structure information from the [Tunisian Reference of Professions and Skills (RTMC)](http://rtmc.emploi.nat.tn). The script scrapes detailed information about professions, including appellations, identity, and required skills, and organizes it into structured JSON files for analysis and integration.

---

## 🚀 Features  
- **Automated Scraping**: Extracts data for all professions categorized by alphabetical sections (A to N).  
- **Structured Output**: Saves data for each section into separate JSON files, and then combines them into a single file.  
- **Scalable & Reusable**: Modular design for scalability and future customization.  

---

## 🛠️ Installation  

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/yourusername/tunisian-professions-scraper.git
   cd tunisian-professions-scraper
   ```

2. **Install Dependencies**:  
   Ensure you have Python installed, then run:  
   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver**:  
   - Download the [ChromeDriver](https://chromedriver.chromium.org/downloads) version matching your installed Chrome browser.  
   - Place it in your system's PATH or the project directory.  

---

## 📋 How to Use  

1. **Run the Script**:  
   Execute the script to start scraping:  
   ```bash
   python scraper.py
   ```  

2. **Output**:  
   - Separate JSON files for each alphabetical section (e.g., `all_jobs_data_A.json`, `all_jobs_data_B.json`, etc.).  
   - A final combined JSON file: `all_jobs_data_combined.json`.  

3. **Modify Scraping Range**:  
   To adjust the range of letters, modify the following section in the script:  
   ```python
   for letter in range(ord('A'), ord('N') + 1):  # Adjust range as needed
   ```

---

## 📂 Project Structure  

```
├── scraper.py               # Main scraping script
├── all_jobs_data_A.json      # Scraped data for section A
├── all_jobs_data_combined.json # Combined JSON file (final output)
└── README.md                # Project documentation
```

---

## ⚠️ Notes  

- **Page Selectors**: Ensure the CSS selectors in the script match the structure of the target website. Update them if the website changes.  
- **Internet Connection**: Requires a stable internet connection to scrape the data.  
- **Data Storage**: Make sure you have enough storage space for the JSON files.  

---

## 📧 Contact  

For questions or suggestions, please reach out to:  
**Your Name**: [ghassen.elabed@gmail.com]  
GitHub: [Your GitHub Profile](https://github.com/Ghassen2001)
