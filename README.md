# GoContact Reports Downloader (Python)

This Python application connects to the *GoContact API* to generate and download campaign reports automatically.  
It authenticates using your GoContact credentials, requests a report for the current month, and saves it as a CSV file (report.csv) locally.

---

## 🚀 Features
- Connects securely to GoContact via API.
- Automatically generates a campaign report using a predefined template.
- Downloads and saves the report as a *CSV file*.
- Calculates the date range: *first day of the current month → today*.
- Uses *environment variables* for credentials and domain.

---

## ⚙ Requirements
- Python *3.8+*
- pip
- python-dotenv

---

## 🔑 Environment Variables
Create a .env file in the same directory as main.py based on .env.example:  

USERNAME="your_gocontact_username"  
PASSWORD="your_gocontact_password"  
DOMAIN="your_gocontact_domain.com"  

- USERNAME: Your GoContact API username  
- PASSWORD: Your GoContact API password (will be hashed automatically)  
- DOMAIN: GoContact domain (e.g., api.gocontact.com)  

---

## ⚙ Installation, ▶ Usage & ✅ Expected Output

1. Clone the repository or download the script:  
   git clone https://github.com/yourusername/gocontact-reports-downloader.git  
   cd gocontact-reports-downloader  

2. (Optional) Create a virtual environment:  
   python -m venv venv  
   source venv/bin/activate   # On Mac/Linux  
   venv\Scripts\activate      # On Windows  

3. Install dependencies:  
   pip install python-dotenv  

4. Copy .env.example to .env and edit with your GoContact credentials:  
   cp .env.example .env  

5. Run the script:  
   python main.py  

6. Expected output:  
   📅 Date range: 2025-10-01 00:00:00 → 2025-10-02 23:59:59  
   Requesting report...  
   ✅ Report generated: report_123456789.csv  
   Downloading report...  
   ✅ Report saved as report.csv  

---

## 💡 Notes
- The script uses a predefined report template ID (90) and campaign owner type.  
  You can modify templateId or ownerType in the code if needed.  
- Reports are saved in the same directory as main.py under the name report.csv.  
- Ensure your API user has permissions in GoContact to generate and download reports.  
- If the script fails to generate a filename, check your credentials, domain, and template ID.  

---

## 📄 License
This project is licensed under the MIT License.  
Feel free to use and modify it within your organization.