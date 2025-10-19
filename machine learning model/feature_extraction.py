import re
import pandas as pd
from urllib.parse import urlparse

def extract_url_features(url):
    parsed_url = urlparse(url)
    return{
        "length"  : len(url),
        "num_didgit": sum(c.isdigit() for c in url),
        "num_special_chars": len(re.findall(r"[!@#$%^&*(),.?\":{}|<>]", url)),
        "num_subdomains": len(parsed_url.netloc.split(".")) - 1,
        "https": 1 if parsed_url.scheme == "https" else 0
    }
df = pd.read_csv("phishing_data.csv")
df_features = df["URL"].apply(lambda x: extract_url_features(x)).apply(pd.Series)
df = pd.concat([df, df_features], axis=1)
df.to_csv("phishing_data_with_features.csv", index=False)

print("Features extracted and saved.")