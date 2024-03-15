 URL Scanner

URL Scanner is a simple tool for scanning URLs to determine if they are classified as good or bad.

Features

URL Classification**: Input any URL and get it classified as either good or bad.
Sanitization: The tool sanitizes the input URL to improve classification accuracy.
Machine Learning Model: Uses a logistic regression model trained on a dataset of labeled URLs.
Graphical User Interface: Provides a user-friendly interface for easy interaction.

Requirements

Python 3.x
Flask
pandas
scikit-learn
Jinja2

Installation

1. Clone the repository:

  bash
    git clone https://github.com/your-username/url-scanner.git


2. Install the required Python packages:

    bash
    pip install -r requirements.txt
    

 Usage

1. Run the Flask application:

    bash
    python app.py
    

2. Open your web browser and navigate to `http://localhost:5000`.
3. Paste the URL you want to scan into the input field and click the "Scan" button.
4. View the classification result displayed on the screen.

Dataset

The project uses a dataset of labeled URLs for training the machine learning model. The dataset contains two columns: `url` and `label`.

Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.
contact me at (alimuzzammil180@gmail.com)
