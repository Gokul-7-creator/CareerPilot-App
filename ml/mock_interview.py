import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def evaluate_answer(question, answer):

    prompt = f"""
You are a Senior Technical Interviewer.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate under these headings:

1. Technical Knowledge (Score /10)
2. Communication (Score /10)
3. Confidence (Score /10)
4. Strengths
5. Weaknesses
6. Better Answer

Keep it concise.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content