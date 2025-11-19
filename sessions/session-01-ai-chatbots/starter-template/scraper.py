import requests
from bs4 import BeautifulSoup
import json

def scrape_wcc_events():
    """Scrape upcoming events from WCC website"""
    # Replace with actual WCC website URL
    url = "https://womencoding.community/events"
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        events = []
        for event in soup.find_all('div', class_='event'):
            events.append({
                "title": event.find('h3').text,
                "date": event.find('span', class_='date').text,
                "description": event.find('p').text
            })
        
        return events
    except Exception as e:
        print(f"Error scraping: {e}")
        return []

# Use in chatbot
events = scrape_wcc_events()
events_text = "\n".join([
    f"- {e['title']} on {e['date']}: {e['description']}"
    for e in events
])

system_prompt = f"""You are a WCC assistant.
Upcoming events:
{events_text}
"""