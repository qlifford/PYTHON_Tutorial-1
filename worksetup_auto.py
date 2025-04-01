import webbrowser as wb

def setupauto():
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    URLS = (
        "gmail.com",
        "stackoverflow.com",
        "github.com",
        "youtube.com",
    )
    for url in URLS:
        wb.get(chrome_path).open(url)
setupauto()