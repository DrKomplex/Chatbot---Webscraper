import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Funktion zur Extraktion der Subdomain
def extract_subdomain(url):
    parsed_url = urlparse(url)
    subdomain = parsed_url.hostname.split('.')[0]
    return subdomain

# Funktion zum Scrapen einer Webseite und Extrahieren des Inhalts des mainContent-Elements
def scrape_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            main_content = soup.find("div", {"id": "mainContent"})
            if main_content:
                # Fachbereich
                subdomain = extract_subdomain(url)
                # Titel
                title = soup.find("h1").get_text() if soup.find("h1") else "No Title"
                # Link
                link = url
                # Inhalt
                content = f"<{main_content.get_text()}>"
                return f"({subdomain}). [{title}]. %{link}%. {content}"
            else:
                print(f"Das Element mit der ID 'mainContent' wurde nicht auf der Webseite {url} gefunden.")
                return None
        else:
            print(f"Fehler beim Abrufen der Webseite {url}: Statuscode {response.status_code}")
            return None
    except Exception as e:
        print(f"Fehler beim Scrapen der Webseite {url}: {e}")
        return None

# Hauptfunktion zum Scrapen aller Webseiten und Schreiben in die Datei
def main():
    try:
        with open("url_data.txt", "r", encoding="utf-8") as file:
            urls = file.readlines()
            urls = [url.strip() for url in urls]

        with open("chatbot_data.txt", "w", encoding="utf-8") as file:
            for url in urls:
                content = scrape_website(url)
                if content:
                    file.write(content + "\n\n")  # Trennung zwischen den Inhalten der einzelnen Webseiten
            print("Scraping abgeschlossen. Daten wurden in chatbot_data.txt gespeichert.")
    except Exception as e:
        print(f"Fehler beim Schreiben der Daten in die Datei: {e}")

if __name__ == "__main__":
    main()
