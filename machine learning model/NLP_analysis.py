import requests
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
import pandas as pd
import warnings


warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

def extract_html_features(url):
    """Extracts HTML-based features from a webpage."""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return 0, 0, 0  # Return zero values if page fails to load

        soup = BeautifulSoup(response.text, "html.parser")
        return len(soup.get_text()), len(soup.find_all("a")), len(soup.find_all("script"))

    except requests.RequestException:
        return 0, 0, 0  

def process_html_features(input_csv, output_csv):
    """Extracts HTML features for URLs in a dataset."""
    df = pd.read_csv(input_csv)
    
    
    df = df[df["URL"].str.startswith(("http://", "https://"))].copy()

    df[["text_length", "num_links", "num_scripts"]] = df["URL"].apply(
        lambda x: extract_html_features(x)
    ).apply(pd.Series)

    df.to_csv(output_csv, index=False)
    print(f"✅ HTML features extracted and saved to {output_csv}")


if __name__ == "__main__":
    process_html_features("phishing_data.csv", "phishing_data_with_html_features.csv")
