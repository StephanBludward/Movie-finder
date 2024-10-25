# Installation Guide

Follow these steps to install and run the Classic Movie Recommender app on your machine.

## Prerequisites
- **Python 3.7 or higher**: Check your Python version:
  ```bash
  python --version
  ```
- **pip**: Should be included with Python. If not, install it from [pip's official website](https://pip.pypa.io/en/stable/installation/).

## Step-by-Step Setup

1. **Clone the Repository**:
   ```bash
   git clone  https://stephanbludward.github.io/Movie-finder/
   cd classic-movie-recommender
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the App in Your Browser**:
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser.
