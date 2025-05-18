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
     export OPENAI_API_KEY="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"
     ```
   - Or edit `config.json` with your key:
     ```json
     {
       "openai_api_key": "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"
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
