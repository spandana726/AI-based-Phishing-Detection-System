import pandas as pd

legitimate_urls = ["https://www.google.com", "https://www.amazon.com"]
phishing_urls = ["https://locker-monrelais.com/", "https://sweetwind.org/"]

data = [{"URL": url, "Label": 0} for url in legitimate_urls] + [{"URL": url, "Label": 1} for url in phishing_urls]

df = pd.DataFrame(data)
df.to_csv("phishing_data.csv", index=False)

print("Dataset saved as phishing_data.csv")

