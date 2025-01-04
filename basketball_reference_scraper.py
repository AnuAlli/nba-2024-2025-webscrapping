import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_basketball_reference():
    url = "https://www.basketball-reference.com/leagues/NBA_2025_standings.html"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find both conference tables
        east_table = soup.find('table', {'id': 'confs_standings_E'})
        west_table = soup.find('table', {'id': 'confs_standings_W'})
        
        def parse_table(table, conference):
            teams_data = []
            rows = table.find_all('tr')[1:]  # Skip header row
            
            for row in rows:
                cols = row.find_all(['td', 'th'])
                if len(cols) >= 7:  # Make sure row has enough columns
                    team_name = cols[0].find('a')
                    if team_name:  # Only process if team name exists
                        team_dict = {
                            'Conference': conference,
                            'Team': team_name.get_text(strip=True),
                            'W': cols[1].get_text(strip=True),
                            'L': cols[2].get_text(strip=True),
                            'W/L%': cols[3].get_text(strip=True),
                            'GB': cols[4].get_text(strip=True),
                            'PS/G': cols[5].get_text(strip=True),
                            'PA/G': cols[6].get_text(strip=True),
                            'SRS': cols[7].get_text(strip=True)
                        }
                        teams_data.append(team_dict)
            return teams_data
        
        # Parse both conferences
        east_data = parse_table(east_table, 'Eastern')
        west_data = parse_table(west_table, 'Western')
        
        # Combine data from both conferences
        all_teams_data = east_data + west_data
        
        if not all_teams_data:
            print("No team data was found.")
            return None
            
        # Create DataFrame and save to CSV
        df = pd.DataFrame(all_teams_data)
        df.to_csv('nba_standings_basketball_reference.csv', index=False)
        print(f"Successfully scraped {len(all_teams_data)} teams' data and saved to nba_standings_basketball_reference.csv")
        
        return df
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    standings_df = scrape_basketball_reference()
    if standings_df is not None:
        print("\nFirst few rows of the scraped data:")
        print(standings_df.head()) 