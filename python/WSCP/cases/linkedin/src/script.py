import json
import re
import os
import urllib.parse
from seleniumbase import SB
from bs4 import BeautifulSoup

def normalize_number(phone):
    return re.sub(r'\D', '', phone)

def remove_duplicate_phones(phone_numbers):
    seen = set()
    unique = []

    for phone in phone_numbers:
        normalized = normalize_number(phone)[-8:]  
        if normalized not in seen:
            seen.add(normalized)
            unique.append(phone)

    return unique