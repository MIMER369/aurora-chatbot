# Aurora - E-Commerce AI Chatbot

**Aurora** is a Matrix-themed e-commerce chatbot built with Streamlit and OpenAI.

## Setup

1. Clone or download this repo.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key:
   - Via environment variable:
     ```
     export OPENAI_API_KEY="your_key_here"
     ```
   - Or edit `config.json` with your key:
     ```json
     {
       "openai_api_key": "your_key_here"
     }
     ```
4. Run the app:
   ```
   streamlit run streamlit_app.py
   ```

## Files

- `streamlit_app.py`: Main Streamlit application.
- `utils.py`: Helpers for loading API key and products.
- `products.json`: Sample product catalog.
- `config.json`: Template for your API key.
- `requirements.txt`: Python dependencies.
- `.gitignore`: Git ignore rules.
- `README.md`: This documentation.
