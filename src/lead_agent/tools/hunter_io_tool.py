# src/<project_name>/tools/hunter_email_tool.py

from typing import Dict
import requests
import os
from crewai.tools import tool

# HUNTER_API_KEY = os.getenv("HUNTER_API_KEY")
HUNTER_API_KEY = "0a6c8bd916805e2c1972318fbb5284f2b596d640"

@tool("hunter_email_lookup_tool")
def hunter_email_lookup(input: Dict[str, str]) -> str:
    """
    Uses Hunter.io API to find email addresses for a given person's name and domain.
    Input format: {'data': 'full_name=John Doe;domain=company.com'}
    Returns: A string with email, confidence score, and LinkedIn URL (if available)
    """
    data = input.get("data")
    try:
        fields = dict(item.split("=") for item in data.split(";"))
        full_name = fields.get("full_name")
        domain = fields.get("domain")

        if not full_name or not domain:
            return "Missing full_name or domain"

        first_name, last_name = full_name.strip().split(" ", 1)
        url = "https://api.hunter.io/v2/email-finder"
        params = {
            "domain": domain,
            "first_name": first_name,
            "last_name": last_name,
            "api_key": HUNTER_API_KEY
        }

        response = requests.get(url, params=params)
        if response.status_code != 200:
            return f"API error: {response.status_code} - {response.text}"

        result = response.json().get("data", {})
        email = result.get("email", "Not found")
        score = result.get("score", "N/A")
        linkedin = result.get("linkedin_url", "Not found")

        return f"Email: {email}\nConfidence: {score}\nLinkedIn: {linkedin}"

    except Exception as e:
        return f"Error during lookup: {str(e)}"
