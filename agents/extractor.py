import requests

def extractor_agent(url):
    raw = requests.post("http://localhost:8001/tool/fetch_url", json={"url": url}).json()
    clean = requests.post("http://localhost:8001/tool/clean_extract", json={"raw_text": raw}).json()
    entities = requests.post("http://localhost:8001/tool/extract_entities", json={"text": clean}).json()
    return entities