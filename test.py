import requests
from bs4 import BeautifulSoup

def get_google_doc_content(doc_url):
    # Simply request the document content by using the provided 'pub' link
    response = requests.get(doc_url)
    
    if response.status_code == 200:
        # Return the raw content (HTML)
        return response.text
    else:
        print(f"Failed to retrieve document. Status code: {response.status_code}")
        return None


def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Get all text within the HTML document
    text = soup.get_text(separator=' ', strip=True)
    return text

def to_grid(data_array):
    split_array = [[data_array[i], data_array[i+1], data_array[i+2]] for i in range(0, len(data_array)-2) if (i % 3) == 0]
    return split_array

def add_until_index(lst, value, target_index):
    # Add the value until the list has the target_index length
    return lst + [value] * (target_index - len(lst))

def write_out(grid):
    string = []
    
    for block in grid:
        x_ind = int(block[0])  # x-coordinate
        y_ind = int(block[2])  # y-coordinate
        
        # Ensure the list has enough rows for y_ind
        if len(string) <= y_ind:
            string = add_until_index(string, [], y_ind + 1)  # add rows up to y_ind
        
        # Ensure each row has enough columns for x_ind
        if len(string[y_ind]) <= x_ind:
            string[y_ind] = add_until_index(string[y_ind], " ", x_ind + 1)  # add columns up to x_ind
        
        # Set the value at the specified x_ind, y_ind location
        string[y_ind][x_ind] = block[1]

    return string[::-1]

def array_to_string(array):
    string = ""
    for line in array:
        string += "".join(line)+"\n"
    return string

# Your provided public Google Docs link
doc_url = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'

# Fetch the content
content = get_google_doc_content(doc_url)

# Fetch and parse the content
if content:
    text = extract_text_from_html(content)
    split_text = text.split(" ")
    data = split_text[split_text.index("y-coordinate")+1:len(split_text)]
    # print(data)
    split_up = to_grid(data)
    print(split_up)
    final_array = write_out(split_up)
    print(final_array)
    print(array_to_string(final_array))
