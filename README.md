# Spotify Playlist Billboard 100 Maker

## Overview

Spotify Playlist Billboard 100 Maker is a Python tool that allows you to create a Spotify playlist featuring the top 100 Billboard songs for a specific date of your choice. Simply provide the date in the format `YYYY-MM-DD`, and this script will:

1. Scrape the Billboard Hot 100 songs from the Billboard website for that date.
2. Search for these songs on Spotify.
3. Create a new private playlist on your Spotify account with these songs.

This project is perfect for music enthusiasts who want to relive the hits of a particular time or explore the music from a specific period.

## Features

- Automate Spotify playlist creation for any date with Billboard Hot 100 songs.
- Utilize the Spotify Web API for seamless playlist generation.
- Relive the music of any week in history, dating back to when the Billboard Hot 100 chart was available.

## Prerequisites

- Python 3.x
- A Spotify developer account
- A Spotify application with Client ID and Client Secret
- `spotipy` library for interacting with the Spotify API
- `BeautifulSoup` for web scraping the Billboard website
- `.env` file for storing sensitive information securely


## Usage
1. Run the script:
   ```sh python main.py
3. Enter a date in the format YYYY-MM-DD to retrieve the Billboard Hot 100 for that week.
4.	Authenticate with Spotify to create a new playlist.
5.	The script will search for the top 100 songs on Spotify and add them to a newly created playlist in your account.

## Notes
- Due to Spotify’s song availability, some songs from the Billboard Hot 100 may not be found. The script will skip those songs if they cannot be found.
- 	Ensure that your Spotify Developer Application is correctly set up with redirect URIs for authentication.
