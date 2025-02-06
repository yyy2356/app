import requests
from bs4 import BeautifulSoup

def get_google_doc_content(doc_url):
    response = requests.get(doc_url)
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve document. Status code: {response.status_code}")
        return None


def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    text = soup.get_text(separator=' ', strip=True)
    return text

def to_grid(data_array):
    split_array = [[data_array[i], data_array[i+1], data_array[i+2]] for i in range(0, len(data_array)-2) if (i % 3) == 0]
    return split_array

def add_until_index(lst, value, target_index):
    return lst + [value] * (target_index - len(lst))

def write_out(grid):
    string = []
    
    for block in grid:
        x_ind = int(block[0])  
        y_ind = int(block[2]) 
        
        if len(string) <= y_ind:
            string = add_until_index(string, [], y_ind + 1)  
        
        if len(string[y_ind]) <= x_ind:
            string[y_ind] = add_until_index(string[y_ind], " ", x_ind + 1)  
        
        # Set the value at the specified x_ind, y_ind location
        string[y_ind][x_ind] = block[1]

    return string[::-1]

def array_to_string(array):
    string = ""
    for line in array:
        string += "".join(line)+"\n"
    return string

#link to document
doc_url = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'


# Fetch and parse the content
def parse_and_print(link):
    # Fetch the content
    content = get_google_doc_content(link)
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

parse_and_print(doc_url)
