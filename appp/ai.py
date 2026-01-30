from groq import Groq
from decouple import config

#initialize client
client = Groq(api_key=config("GROQ_API_KEY"))



def generate_ai_description(name, price):
    """
    Generates an attractive product description using Groq API.
    """

    prompt = (
        "You are an expert ecommerce copywriter. "
        "Write a short, attractive, positive product description "
        "that makes the customer feel they must buy it.\n\n"
        f"Product Name: {name}\n"
        f"Price: ₹{price}\n"
    )

    # Use a currently supported model
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # <--- UPDATED MODEL
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=120
    )

    # Extract the generated text
    return response.choices[0].message.content.strip()


def groq_analyze(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are an expert e-commerce data analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=200
    )
    return response.choices[0].message.content.strip()
