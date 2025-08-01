# hugging_face_api.py
# This module provides a class for interacting with the Hugging Face API to fetch completions.
# Author: Vendel, GITHUB: jv813yh
# Date: 08/01/2025

from openai import OpenAI

HF_TOKEN = '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'

SYS_PROMPT = """
You are a financial summarization assistant.

Your task is to read structured records of daily market data and summarize them clearly and consistently. 

Instructions:
1. For each record, create one sentence that contains:
   - the date,
   - the opening price,
   - the maximum price,
   - the difference between the maximum and the opening price (both as an absolute value and as a percentage),
   - and explicitly mention the maximum value.
2. Present the summaries as a numbered list, one bullet point per day, in chronological order.
3. After listing the days, provide a short comparative summary across the days (e.g., differences between opening and closing, or variations in highs and lows).
4. Keep the style concise, factual, and use clear financial language.
5. Output only the summary, no explanations or additional text.\n\n"
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
                        "content": SYS_PROMPT
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

