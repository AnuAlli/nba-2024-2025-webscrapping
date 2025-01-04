# NBA Standings Scraper 2024-2025 🏀

## Overview
This project automatically scrapes and updates NBA standings data for the 2024-2025 season. The data is collected from Basketball Reference and updates daily at midnight.

## Features
- 🔄 Daily automatic updates at 12:00 AM
- 📊 Comprehensive NBA standings statistics
- 📅 Historical data tracking with dated files
- 📈 Latest standings always available

## Data Points Collected
The scraper collects the following statistics for each team:
- Team Name
- Wins (W)
- Losses (L)
- Win Percentage (W/L%)
- Games Behind (GB)
- Points Scored Per Game (PS/G)
- Points Allowed Per Game (PA/G)
- Simple Rating System (SRS)
- Conference Standing
- Home Record
- Away Record

## File Structure
- `nba_standings_latest.csv` - Most recent standings data
- `nba_standings_YYYYMMDD.csv` - Historical data files with timestamps
- `nba_standings_scraper.log` - Log file tracking all updates

## Last Updated
The data in this repository was last updated on: ${timestamp}

## Requirements
- Python 3.x
- Required packages:
  - requests
  - beautifulsoup4
  - pandas
  - schedule

## Installation 
