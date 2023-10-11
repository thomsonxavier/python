import requests
import PyPDF2
import webbrowser
import os

def download_file(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)

def search_words_in_pdf(file_path, words):
    results = set()  # Use a set to store unique results
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()  
                for word in words:
                    if word in page_text:
                        result = (word, file_path, page_num + 1)
                        results.add(result)
    except Exception as e:
        if 'EOF marker not found' in str(e):
            print(f"Skipping '{file_path}' due to EOF marker not found.")
        else:
            print(f"Skipping '{file_path}' due to an exception: {str(e)}")

    return results

# Live link to the PDF files

pdf_links = [
    "https://www.citibank.co.uk/static/documents/FID_UKC_CGCA.pdf",
    "https://www.citibank.co.uk/static/documents/FID_UKC_EuroCA_Staff.pdf",
    "https://www.citibank.co.uk/static/documents/FID_UKC_FlexibleSaver_Staff.pdf",
    "https://www.citibank.co.uk/static/documents/FID_UKC_DollarRewardSaver_Staff.pdf",
    "https://www.citibank.co.uk/static/documents/travel_insurance_policy.pdf",
    "https://www.citibank.co.uk/static/documents/overdraft-charges.pdf",
    "https://www.citibank.co.uk/static/documents/FID_UKC_EuroCA.pdf",
    "https://www.citibank.co.uk/static/documents/Specificterms.pdf",
    "https://www.citibank.co.uk/static/documents/FID_UKC_FlexibleSaver.pdf",
    "https://www.citibank.co.uk/static/documents/FID_UKC_DollarRewardSaver.pdf",
    "https://www.citibank.co.uk/static/documents/staff-rates_new.pdf",
    "https://www.citibank.co.uk/static/documents/Chubb_insurance_product_information_document.pdf",
    "https://www.citibank.co.uk/static/documents/FID_UKC_CACA.pdf",
    "https://www.citibank.co.uk/static/documents/FID_UKC_DollarCA_Staff.pdf",
    "https://www.citibank.co.uk/static/documents/FID_UKC_CPCA.pdf",
    "https://www.citibank.co.uk/static/documents/FID_UKC_CCA_Staff.pdf",
    "https://www.citibank.co.uk/static/documents/FID_UKC_CGCA_Staff.pdf",
    "https://www.citibank.co.uk/static/documents/FID_UKC_RewardSaver_Staff.pdf",
    "https://www.citibank.co.uk/static/documents/FID_UKC_DollarCA.pdf",
    "https://www.citibank.co.uk/static/documents/overdraft-precontract.pdf",
    "https://www.citibank.co.uk/static/documents/Staff-Terms-Conditions.pdf",
    "https://www.citibank.co.uk/static/documents/comparison-rates.pdf",
    "https://www.citibank.co.uk/static/documents/Glossary.pdf",
    "https://www.citibank.co.uk/static/documents/FID_UKC_RewardSaver.pdf",
    "https://www.citibank.co.uk/static/documents/fscs.pdf",
    "https://www.citibank.co.uk/static/documents/protecting-your-money.pdf",
    "https://www.citibank.co.uk/static/documents/overdraft-charges-b.pdf",
    "https://www.citibank.co.uk/static/documents/CECA-Terms-Conditions.pdf",
    "https://www.citibank.co.uk/static/documents/depositor-guarantee-information-cukl.pdf",
    "https://www.citibank.co.uk/static/documents/CECA-FID.pdf",
    "https://www.citibank.co.uk/static/documents/terms.pdf",
    "https://www.ipb.citibank.co.uk/ipb/europe/pdfs/fscs_brochure.pdf",
    "https://www.ipb.citibank.co.uk/ipb/europe/pdfs/glossary.pdf",

    "https://www.ipb.citibank.co.uk/ipb/europe/pdfs/Important_information_Jersey.pdf",
    https://www.citibank.co.uk/static/documents/terms.pdf",


    "https://www.ipb.citibank.co.uk/ipb/europe/pdfs/TransferringFunds_Jersey.pdf",
    "https://www.ipb.citibank.co.uk/ipb/europe/pdfs/TransferringFunds_NA.pdf",
    "https://www.ipb.citibank.co.uk/ipb/europe/pdfs/fscs_awareness.pdf",
    "https://www.ipb.citibank.co.uk/pdfs/TransferringFunds_Jersey_new.pdf",
    "https://www.ipb.citibank.co.uk/international-banking/pdf/tranferring-funds-jersey.pdf"
]




directory = './pdf/'  # Replace './pdf/' with the desired local directory path
search_words = ['fx', 'foreign exchange'] # Add or modify the words as needed

results = set()  # Use a set to store unique results

# Download and process each PDF file
for link in pdf_links:
    file_name = link.split('/')[-1]
    file_path = os.path.join(directory, file_name)
    download_file(link, file_path)
    search_results = search_words_in_pdf(file_path, search_words)
    results.update(search_results)  

# Display results in a table
print("{:<10} {:<50} {:<10}".format("Word", "File", "Page"))
print("-" * 80)
for result in results:
    print("{:<10} {:<50} {:<10}".format(result[0], result[1], result[2]))


