from typing import Any
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

talks: list[dict[str, Any]] = [
    {
        "id": "T1",
        "title": "Scaling AI Workloads on GKE",
        "speakers": [{"firstName": "Jane", "lastName": "Doe", "linkedIn": "https://linkedin.com/in/janedoe"}],
        "categories": ["AI/ML", "Infrastructure"],
        "description": "Learn how to efficiently run and scale large language models using Google Kubernetes Engine.",
        "time": "09:00 AM - 09:45 AM",
        "is_break": False
    },
    {
        "id": "T2",
        "title": "Serverless Data Pipelines with Cloud Run",
        "speakers": [{"firstName": "John", "lastName": "Smith", "linkedIn": "https://linkedin.com/in/johnsmith"},
                     {"firstName": "Alice", "lastName": "Johnson", "linkedIn": "https://linkedin.com/in/alicej"}],
        "categories": ["Data Analytics"],
        "description": "Building resilient and cost-effective data processing workflows using Cloud Run and Pub/Sub.",
        "time": "10:00 AM - 10:45 AM",
        "is_break": False
    },
    {
        "id": "T3",
        "title": "Zero Trust Security on Google Cloud",
        "speakers": [{"firstName": "Miguel", "lastName": "Hernandez", "linkedIn": "https://linkedin.com/in/miguelh"}],
        "categories": ["Security"],
        "description": "Implementing BeyondCorp principles to secure your enterprise infrastructure on GCP.",
        "time": "11:00 AM - 11:45 AM",
        "is_break": False
    },
    {
        "id": "T4",
        "title": "Modernizing Apps with Anthos",
        "speakers": [{"firstName": "Sarah", "lastName": "Connor", "linkedIn": "https://linkedin.com/in/sarahc"}],
        "categories": ["Infrastructure"],
        "description": "Strategies for hybrid and multi-cloud environments using Google Anthos.",
        "time": "12:00 PM - 12:45 PM",
        "is_break": False
    },
    {
        "id": "B1",
        "title": "Lunch Break",
        "speakers": [],
        "categories": ["Break"],
        "description": "60 minutes lunch break. Enjoy networking and excellent food!",
        "time": "12:45 PM - 01:45 PM",
        "is_break": True
    },
    {
        "id": "T5",
        "title": "Vertex AI: From Jupyter to Production",
        "speakers": [{"firstName": "David", "lastName": "Lee", "linkedIn": "https://linkedin.com/in/davidl"}],
        "categories": ["AI/ML"],
        "description": "An end-to-end guide on moving your machine learning models from experimentation to production with Vertex AI.",
        "time": "01:45 PM - 02:30 PM",
        "is_break": False
    },
    {
        "id": "T6",
        "title": "Demystifying BigQuery Storage",
        "speakers": [{"firstName": "Emily", "lastName": "Chen", "linkedIn": "https://linkedin.com/in/emilyc"}],
        "categories": ["Data Analytics"],
        "description": "Deep dive into how BigQuery stores and manages petabytes of data efficiently.",
        "time": "02:45 PM - 03:30 PM",
        "is_break": False
    },
    {
        "id": "T7",
        "title": "Cloud IAM Best Practices",
        "speakers": [{"firstName": "Robert", "lastName": "Brown", "linkedIn": "https://linkedin.com/in/robertb"},
                     {"firstName": "Lisa", "lastName": "Wang", "linkedIn": "https://linkedin.com/in/lisaw"}],
        "categories": ["Security", "Infrastructure"],
        "description": "How to structure your Identity and Access Management policies for minimum privilege.",
        "time": "03:45 PM - 04:30 PM",
        "is_break": False
    },
    {
        "id": "T8",
        "title": "The Future of Generative AI at Google",
        "speakers": [{"firstName": "Sundar", "lastName": "Pichai", "linkedIn": "https://linkedin.com/in/sundar"}],
        "categories": ["AI/ML"],
        "description": "Exploring upcoming Generative AI capabilities and Gemini models coming to Google Cloud.",
        "time": "04:45 PM - 05:30 PM",
        "is_break": False
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/api/talks')
def api_talks():
    search = request.args.get('search', '').lower()
    
    if not search:
        return jsonify(talks)

    filtered_talks = []
    for talk in talks:
        if talk["is_break"]:
            filtered_talks.append(talk)
            continue
            
        # Check title
        if search in talk["title"].lower():
            filtered_talks.append(talk)
            continue
            
        # Check categories
        cat_match = any(search in cat.lower() for cat in talk["categories"])
        if cat_match:
            filtered_talks.append(talk)
            continue
            
        # Check speakers
        speaker_match = False
        for speaker in talk["speakers"]:
            full_name = f"{speaker['firstName']} {speaker['lastName']}".lower()
            if search in full_name:
                speaker_match = True
                break
        
        if speaker_match:
            filtered_talks.append(talk)
            continue

    return jsonify(filtered_talks)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
