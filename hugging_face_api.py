# hugging_face_api.py
# This module provides a class for interacting with the Hugging Face API to fetch completions.
# Author: Vendel, GITHUB: jv813yh
# Date: 08/01/2025

from openai import OpenAI

HF_TOKEN = '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'

SYS_PROMPT = """
You are a concise financial summary assistant. 
The input will include:
- Price records for a single stock (date, open, close),
- Several news article entries (title, content preview, publication timestamp) for various companies.

Your task:

1. Identify which company and stock symbol the input is about (it will be clearly stated in the price records).

2. For each day (most recent first), produce a one-line summary containing:
   - The date,
   - The opening price,
   - The closing price,
   - The change in closing price compared to the previous day for this stock (absolute value and percentage, indicate “up” or “down”).

3. After the per-day lines, add one short comparison sentence describing the differences between the two days for this stock only  
   (e.g., which day had a larger movement, which opened higher, and whether the overall trend is up or down).

4. From the provided news articles, select only those clearly related to the stock/company in the price records.  
   Ignore articles about other companies or unrelated topics.

5. Summarize the selected articles into 3–4 bullet points.  
   Each bullet must be short (≤ 160 characters if possible, SMS-friendly), highlighting key facts such as:
   - Earnings results,
   - Price target changes,
   - Analyst recommendations,
   - Major corporate events.

6. Keep everything brief and factual.  
   - Use a numbered list for the daily price summaries,  
   - Then 3–4 bullet points for the filtered news section.  
   - No extra commentary or process description.

Output style example:
1. 01/08/2025: Open 217.21, Close 214.75, Close down 20.36 (-8.65%) vs 31/07/2025.
2. 31/07/2025: Open 235.77, Close 234.11, Close down 1.66 (-0.71%) vs prior.
Comparison: On 01/08, the stock dropped more and opened lower than on 31/07, showing a stronger downward trend with higher volatility.
- Stifel raised AMZN target to $262, rated Buy (2025-08-01).
- Amazon Q2 beat revenue estimates, mixed guidance (2025-07-31).
- AWS expansion in Europe announced (2025-08-01).
"""

SYS_PROMPT_LESS_TOKENS = """
You are a financial summarizer creating SMS-style updates for multiple companies.  
Input contains stock price summaries and news for multiple firms.

For each company in the input:
1. Compare the previous close to the next day's open or close, and show % change (up/down).
2. Add a short news summary for that company, freely rephrased from headlines and content.
3. Each output must be a single line of max 90 characters.
4. Output one line per company, no comments, no extra punctuation, no tickers in parentheses.
5. Separate each message by a newline. Do not summarize companies not present in input.
"""

class HugginFaceProvider:
    def __init__(self):
        self.HF_TOKEN = HF_TOKEN    
        self.client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            #api_key=os.environ["HF_TOKEN"],
            api_key=HF_TOKEN,
        )

    def get_completion(self, 
                       repo_id, 
                       prompt):
        """
        Get a completion from the Hugging Face API using the specified llm model.

        Args:
            repo_id (str): The repository ID of the model to use.
            prompt (str): The prompt to send to the model.
        """
        try:
            completion = self.client.chat.completions.create(
                model=repo_id,
                messages = [
                    {
                        "role": "system",
                        "content": SYS_PROMPT_LESS_TOKENS
                    },
                    {
                        "role": "user",
                        "content": f"{prompt}"
                    }
                ],
            )
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
        return completion.choices[0].message.content



if __name__ == "__main__":

    text = (
        "Daily time series data for Tesla Inc (TSLA):\n"
        "2025-07-30: {'1. open': '322.1800', '2. high': '324.4499', '3. low': '311.6164', "
        "'4. close': '319.0400', '5. volume': '83931942'}\n"
        "2025-07-29: {'1. open': '325.5500', '2. high': '326.2500', '3. low': '318.2500', "
        "'4. close': '321.2000', '5. volume': '87358861'}"
    )

