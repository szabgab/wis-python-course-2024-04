import sys
import os
import csv
from datetime import datetime
from Bio import Entrez

def fetch_ncbi_records(term, number):
    Entrez.email = "thea.meimoun@weizmann.ac.il"

    # Search the term in NCBI protein database
    search_handle = Entrez.esearch(db="protein", term=term, idtype="acc", retmax=number)
    search_results = Entrez.read(search_handle)
    search_handle.close()

    ids = search_results["IdList"]
    total = search_results["Count"]

    file_names = []

    # Create a directory to save the files if it doesn't exist
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    # Fetch each record and save to file
    for index, record_id in enumerate(ids):
        fetch_handle = Entrez.efetch(db="protein", id=record_id, rettype="gb", retmode="text")
        record = fetch_handle.read()
        fetch_handle.close()

        file_name = f"downloads/{term.replace(' ', '_')}_{index + 1}.gb"
        with open(file_name, 'w') as file:
            file.write(record)
        file_names.append(file_name)

    return file_names, total

def log_search_details(date, term, number, total):
    log_file = 'search_log.csv'
    log_exists = os.path.isfile(log_file)

    with open(log_file, 'a', newline='') as csvfile:
        log_writer = csv.writer(csvfile)
        if not log_exists:
            log_writer.writerow(["date", "term", "max", "total"])
        log_writer.writerow([date, term, number, total])

def main():
    if len(sys.argv) != 3:
        print("Usage: python ncbi_protein_downloader.py TERM NUMBER")
        sys.exit(1)

    term = sys.argv[1]
    number = int(sys.argv[2])

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"Searching NCBI for term '{term}' and downloading up to {number} items...")

    try:
        file_names, total = fetch_ncbi_records(term, number)
        log_search_details(current_date, term, number, total)

        print("Downloaded files:")
        for file_name in file_names:
            print(file_name)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
