import http.client
import hashlib
import os
from urllib.parse import urlencode
from typing import Optional, Tuple
from datetime import datetime, timedelta
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

DOMAIN = os.getenv("DOMAIN")

def get_credentials() -> dict:
    """Read credentials from .env and return them with hashed password."""
    username = os.getenv("USERNAME")
    password_plain = os.getenv("PASSWORD")

    if not username or not password_plain:
        raise ValueError("❌ Missing USERNAME or PASSWORD in .env file")

    # Hash password using sha512 and return hex string
    password_hashed = hashlib.sha512(password_plain.encode("utf-8")).hexdigest()

    return {
        "domain": "be23a282-f840-4cb5-a678-cce9f046dd4a",
        "username": username,
        "password": password_hashed,
    }


def get_date_range() -> Tuple[str, str]:
    """Return first day of current month and end of today."""
    now = datetime.now()

    # First day of this month at 00:00:00
    start_date = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    # End of today at 23:59:59
    end_date = now.replace(hour=23, minute=59, second=59, microsecond=0)

    return (
        start_date.strftime("%Y-%m-%d %H:%M:%S"),
        end_date.strftime("%Y-%m-%d %H:%M:%S"),
    )


def request_report(credentials: dict, start_date: str, end_date: str) -> Optional[str]:
    """Send request to generate report and return filename."""
    payload = {
        **credentials,
        "api_download": "true",
        "action": "downloadReport",
        "ownerType": "campaign",
        "ownerId": "allOwners",
        "startDate": start_date,
        "endDate": end_date,
        "dataType": "0",
        "templateId": "90",
        "includeALLOwners": "true",
    }

    conn = http.client.HTTPSConnection(DOMAIN)
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    conn.request(
        "POST",
        "/fs/modules/report-builder/php/reportBuilderRequests.php",
        urlencode(payload),
        headers,
    )
    res = conn.getresponse()
    data = res.read().decode("utf-8").strip('"')

    return data if data else None


def download_report(credentials: dict, filename: str) -> str:
    """Download the report file given a filename."""
    payload = {
        **credentials,
        "api_download": "true",
        "action": "getCsvReportFile",
        "file": filename,
    }

    conn = http.client.HTTPSConnection(DOMAIN)
    conn.request(
        "GET",
        "/fs/modules/report-builder/php/reportBuilderRequests.php?" + urlencode(payload)
    )

    res = conn.getresponse()
    return res.read().decode("utf-8")


def main():
    credentials = get_credentials()
    start_date, end_date = get_date_range()

    print(f"📅 Date range: {start_date} → {end_date}")

    print("Requesting report...")
    filename = request_report(credentials, start_date, end_date)

    if not filename:
        print("❌ Failed to get report filename")
        return

    print(f"✅ Report generated: {filename}")

    print("Downloading report...")
    csv_data = download_report(credentials, filename)

    with open("report.csv", "w", encoding="utf-8") as f:
        f.write(csv_data)

    print("✅ Report saved as report.csv")


if __name__ == "__main__":
    main()
