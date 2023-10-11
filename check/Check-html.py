import requests
from bs4 import BeautifulSoup


def search_words_in_html(url, words):
    results = set()  # Use a set to store unique results
    try:
        response = requests.get(url)
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')
        for word in words:
            if word in soup.get_text():
                result = (word, url)
                results.add(result)
    except Exception as e:
        print(f"Skipping '{url}' due to an exception: {str(e)}")

    return results


# Live URLs of the HTML pages
  
html_urls= [
  "https://www.citibank.co.uk/personal/ec-paying-bills.do",
  
]








search_words = ['fx', 'foreign exchange','FX spot' ,'bill' ,'Deposit']  

results = set()  

# Search for words in each HTML page
for url in html_urls:
    search_results = search_words_in_html(url, search_words)
    results.update(search_results)  # Add new results to the set


print("{:<10} {:<50}".format("Word", "Location"))
print("-" * 60)
for result in results:
    print("{:<10} {:<50}".format(result[0], result[1]))
