import requests

def get_google_doc_content(doc_url):
    # Make sure the document URL is in the public format
    # Replace '/edit' with '/export?format=html'
    export_url = doc_url.replace('/pub', '/export?format=html')
    
    # Send a GET request to the export URL
    response = requests.get(export_url)

    if response.status_code == 200:
        # Return the HTML content of the document
        return response.text
    else:
        print(f"Failed to retrieve document. Status code: {response.status_code}")
        return None

# Example Google Docs link (publicly shared)
doc_url = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'
content = get_google_doc_content(doc_url)

if content:
    print(content)
