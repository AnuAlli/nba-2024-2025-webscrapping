import schedule
import time
from datetime import datetime
import logging
from basketball_reference_scraper import scrape_basketball_reference

# Set up logging
logging.basicConfig(
    filename='nba_standings_scraper.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def job():
    try:
        logging.info("Starting NBA standings scraping job")
        
        # Run the scraper
        standings_df = scrape_basketball_reference()
        
        if standings_df is not None:
            # Add timestamp to filename
            timestamp = datetime.now().strftime("%Y%m%d")
            filename = f'nba_standings_{timestamp}.csv'
            
            # Save with timestamp
            standings_df.to_csv(filename, index=False)
            
            # Also save as latest version
            standings_df.to_csv('nba_standings_latest.csv', index=False)
            
            logging.info(f"Successfully scraped and saved data to {filename}")
        else:
            logging.error("Failed to scrape NBA standings")
            
    except Exception as e:
        logging.error(f"Error in scraping job: {e}")

def run_scheduler():
    # Schedule job to run at midnight (00:00)
    schedule.every().day.at("00:00").do(job)
    
    # Run job immediately when script starts
    job()
    
    logging.info("Scheduler started - will run every day at 00:00")
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    try:
        run_scheduler()
    except KeyboardInterrupt:
        logging.info("Scheduler stopped by user")
    except Exception as e:
        logging.error(f"Scheduler crashed: {e}") 