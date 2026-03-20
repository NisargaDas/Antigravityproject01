# Google Cloud Tech Conference - 1-Day Schedule Website

A lightweight, responsive web application built with Python Flask, vanilla JavaScript, and CSS to showcase a 1-day technical conference schedule.

## Features
- **Dynamic Schedule**: Displays a timetable of 8 tech talks and 1 lunch break.
- **Search Functionality**: Users can search by talk title, speaker name, or category seamlessly.
- **Modern UI**: Clean, aesthetic design featuring Google Cloud colors.
- **Responsive**: Fully functional on mobile and desktop devices.

## Prerequisites
- Python 3.8+
- `pip` package manager

## Setup Instructions

1. **Navigate to the project directory**
   ```bash
   cd path/to/gcp_conf
   ```

2. **Install dependencies**
   Install the required Flask framework using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   Launch the Flask server:
   ```bash
   python app.py
   ```

4. **Access the web app**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## Making Changes
- **Add/Modify Talks**: Open `app.py` and modify the `talks` list. The data structure is straightforward JSON/dict format.
- **Modify Styles**: Open `static/css/style.css` to tweak colors or layout elements.
- **Update UI Structure**: Edit the `templates/index.html` file to change the core HTML structure.
