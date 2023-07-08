# Movie Recommendation System
* Link to youtube demo: [click here](https://www.youtube.com/watch?v=34JFKU5L4zc&t=2s)
* Link to the website deployed on PythonAnywhere: [click here](http://leoleopython.pythonanywhere.com/)

### Overview
* Used: Django, HTML, CSS, JavaScript, Bootstrap, Python, Scikit-learn, BeautifulSoup
* Used content-based filtering techniques to recommend the most relevant movies based on user’s past activity
* Scraped over 5000 film details, cast information, and movie reviews using BeautifulSoup and Python
* Incorporated a pre-trained RoBERTa model to analyze the sentiments of the movie reviews as positive, neutral, or negative

### How to run the project?
1. Clone or download this repository to your local machine.
2. Install all the libraries mentioned in the `requirements.txt` file with the command `pip install -r requirements.txt`
3. Open your terminal/command prompt from your project directory and run the file `app.py` by executing the command `streamlit run app.py`.
4. As soon as you run the command as shown above, a local Streamlit server will spin up and your app will open in a new tab in your default web browser.
