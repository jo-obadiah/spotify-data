
🎧 Spotify Data ETL Pipeline

 📌 Project Overview
This project extracts music data from Spotify using their public API and loads it for potential analysis. The script uses the `Spotipy` library to collect track metadata and can be expanded into a full ETL pipeline.

🛠️ Tools Used
- Python
- Spotipy (Spotify API wrapper)
- Pandas
- JSON handling
- Git

 📊 Pipeline Steps
1. **Extract** – Connect to Spotify API using access tokens and fetch track/playlist data.
2. **Transform** – Flatten nested JSONs, extract relevant features.
3. **Load** – Currently prints to console; can be extended to CSV or database.

 🚀 How to Run
```bash
# Clone the repository
git clone https://github.com/jo-obadiah/spotify-data.git
cd spotify-data

# Install required libraries
pip install spotipy pandas

# Run the ETL script
python etl.py
