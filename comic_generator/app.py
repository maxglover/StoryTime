from flask import Flask, request, render_template
from textAnalysis import analyze_text
from imageGeneration import generate_image
from imageComposition import add_speech_bubble
import os
from dotenv import load_dotenv

# Load environment variables from key.env file
load_dotenv('key.env')

app = Flask(__name__)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # Fetch the API key from environment variables

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        story_text = request.form['story_text']
        entities, sentiment = analyze_text(story_text)
        
        # Generate a prompt for the image based on the analyzed text
        prompt = "A dark forest with a scared man walking through it."
        image_url = generate_image(prompt, OPENAI_API_KEY)
        
        # Add speech bubble to the image
        image = add_speech_bubble(image_url, "I'm scared!")
        
        # Save the image
        image_path = os.path.join('static', 'images', 'output.png')
        image.save(image_path)
        
        return render_template('index.html', image_url=image_path)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
