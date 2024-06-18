import os
import json
from tsidpy import TSID, TSIDGenerator
from datetime import datetime
from flask import request

directory_path = 'roles/'

EEA = ["AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE", "IS", "LI", "NO"]

EU = ["AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE"]

def get_country_codes():
    country_code = request.headers.get('cf-ipcountry')
    return country_code

def is_eea(country_code):
    if country_code in EEA and country_code in EU:
        value = {
            "eea": True,
            "eu": True
            }
    elif country_code in EEA and country_code not in EU:
        value = {
            "eea": True,
            "eu": False
            }
    else:
        value = {
            "eea": False,
            "eu": False
            }
    return json.dumps(value)

def get_tsid():
    tsid = str(TSID.create())
    return tsid

def get_specific_roles(prefix):
    specific_roles = []

    # Get the list of files in the specified directory
    file_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # Iterate through each file and extract data
    matching_files = [file for file in file_list if file.startswith(prefix)]

    for filename in matching_files:
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'r') as file:
            data = json.load(file)
            specific_roles.append(data)

    return specific_roles


def get_roles_data():
    roles_data = []

    # Get the list of files in the specified directory
    file_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # Iterate through each file and extract data
    for filename in file_list:
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'r') as file:
            data = json.load(file)
            roles_data.append(data)

    roles_data = sorted(roles_data, key=lambda x: x.get('title', '').lower())

    return roles_data

def get_iam_categories():
    """
    Retrieve a list of words before the period in the filenames of JSON files
    in the specified directory.

    Returns:
    - A list of words before the period in the filenames.
    """
    words_before_period = []
    deduplicated_list = []

    # Get the list of files in the specified directory
    file_list = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # Iterate through each file and extract the word before the period
    for filename in file_list:
        word = filename.split('.')[0]
        words_before_period.append(word)

    # Deduplicate the list
    for word in words_before_period:
        if word not in deduplicated_list:
            deduplicated_list.append(word)

    deduplicated_list.sort()
    return deduplicated_list
