import argparse
import sys
import os
import csv
import traceback
from datetime import datetime
from Bio import Entrez

def fetch_ncbi_records(database, term, number, download_folder):
    Entrez.email = "thea.meimoun@weizmann.ac.il"

    # Search the term in NCBI selected database
    search_handle = Entrez.esearch(db=database, term=term, idtype="acc", retmax=number)
    search_results = Entrez.read(search_handle)
    search_handle.close()

    ids = search_results["IdList"]
    total = search_results["Count"]

    file_names = []

    # Create a directory to save the files if it doesn't exist
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Fetch each record and save to file
    for index, record_id in enumerate(ids):
        fetch_handle = Entrez.efetch(db=database, id=record_id, rettype="gb", retmode="text")
        record = fetch_handle.read()
        fetch_handle.close()

        file_name = f"{download_folder}/{term.replace(' ', '_')}_{index + 1}.gb"
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
    parser = argparse.ArgumentParser()
    parser.add_argument('--database', help="nucleotide|protein", required=True)
    #database = parser.add_mutually_exclusive_group(required=True)
    #database.add_argument('--protein', action='store_true')
    #database.add_argument('--nucleotide', action='store_true')

    #parser.add_argument('--protein', action='store_true')
    #parser.add_argument('--nucleotide', action='store_true')
    parser.add_argument('--term', required=True)
    #parser.add_argument('number', type=int)
    parser.add_argument('--number', type=int, default=1)
    parser.add_argument('--download_folder', default="downloads")
    parser.add_argument('--silent', '-s', action='store_true')
    args = parser.parse_args()

    term = args.term
    database = args.database
    number = args.number
    #download_folder = args.download_folder if args.download_folder else "downloads"
    download_folder = args.download_folder


    #if len(sys.argv) != 4 and len(sys.argv) != 5:
    #    print("Usage: python ncbi.py DATABASE TERM NUMBER [DOWNLOAD_FOLDER=downloads]")
    #    print("DATABASE: nucleotide|protein")
    #    sys.exit(1)

    #database = sys.argv[1]
    #term = sys.argv[2]
    #number = int(sys.argv[3])
    #download_folder = sys.argv[4] if len(sys.argv) == 5 else "downloads"

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not args.silent:
        print(f"Searching NCBI for term '{term}' and downloading up to {number} items...")

    try:
        file_names, total = fetch_ncbi_records(database, term, number, download_folder)
        log_search_details(current_date, term, number, total)

        if not args.silent:
            print("Downloaded files:")
            for file_name in file_names:
                print(file_name)

    except Exception as e:
        print(f"An error occurred: {e}")
        #print(traceback.format_exc())
        sys.exit(1)

if __name__ == "__main__":
    main()
