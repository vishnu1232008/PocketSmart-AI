import json
from google import genai
from PIL import Image
import io
from app.config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)
MODEL_NAME = "gemini-1.5-flash"

def clean_json_response(text: str) -> str:
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()

def generate_home_recommendations(budget: float, functionality: str):
    prompt = f"""
    You are an AI budget planner. The user has a budget of ₹{budget} for Home Interior functionality: {functionality}.
    Allocate this budget across categories like furniture, lighting, and decor. Provide specific vendor links (e.g., IKEA, Amazon).
    Return ONLY a valid JSON array of objects with keys: "item", "category", "estimated_cost", "vendor_link", "reasoning".
    """
    response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
    return clean_json_response(response.text)

def generate_party_recommendations(budget: float, event_type: str, guests: int):
    prompt = f"""
    You are a party planner. Budget: ₹{budget}, Event: {event_type}, Guests: {guests}.
    Allocate budget across catering, decoration, and entertainment using platforms like Swiggy, Zomato, and OYO.
    Return ONLY a valid JSON array of objects with keys: "category", "suggestion", "estimated_cost", "vendor", "reasoning".
    """
    response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
    return clean_json_response(response.text)

def generate_jewelry_recommendations(budget: float, occasion: str, style: str, image_bytes: bytes = None):
    contents = [f"""
    You are a jewelry stylist. Budget: ₹{budget}, Occasion: {occasion}, Style: {style}.
    If an outfit image is provided, match the jewelry aesthetics. Source from Amazon or Flipkart.
    Return ONLY a valid JSON array of objects with keys: "jewelry_type", "suggestion", "estimated_cost", "vendor", "match_reasoning".
    """]
    if image_bytes:
        img = Image.open(io.BytesIO(image_bytes))
        contents.append(img)
        
    response = client.models.generate_content(model=MODEL_NAME, contents=contents)
    return clean_json_response(response.text)