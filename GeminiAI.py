import requests
import json

# Replace with your actual API key
API_KEY = "
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent"

def send_to_gemini(prompt):
    headers = {
        'Content-Type': 'application/json',
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    try:
        # Make the POST request to the API
        response = requests.post(f"{API_URL}?key={API_KEY}", headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # This will raise an HTTPError for bad responses (4xx or 5xx)

        # Parse the JSON response
        response_data = response.json()
        
        # Extract the generated text
        if 'candidates' in response_data and response_data['candidates']:
            generated_text = response_data['candidates'][0]['content']['parts'][0]['text']
            return generated_text
        else:
            return "No content generated."

    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except Exception as err:
        return f"An error occurred: {err}"

