import os
import requests
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
weather_api_key = os.getenv("WEATHER_API_KEY")

client = Groq(api_key=groq_api_key)

llm_messages = [
    {
        "role": "system",
        "content": "You are a helpful weather assistant. Use the get_weather tool to answer weather queries."
    },
    {
        "role": "user",
        "content": "What's the weather in Hyderabad?"
    }
]

def get_weather(location):
    """
    Fetch current weather information for a given city/location using OpenWeather API.

    Args:
        location (str): Name of the city to get weather for.

    Returns:
        dict: Weather details (location, temperature, description) on success,
              or error message dict on failure.
    """
    api_key = weather_api_key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 and str(data.get("cod")) == "200":
        return {
            "location": location,
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    else:
        return {"error": "City not found"}

tools = [{
    "type": "function",
    "function":{
        "name": "get_weather",
        "description": "Get current weather for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "location" : {
                    "type": "string",
                    "description": "City Name"
                }
            },
            "required": ["location"]
        }
    }
}]

response = client.chat.completions.create(
    messages = llm_messages,
    model = "llama-3.3-70b-versatile",
    tools= tools,
    tool_choice = "auto"
)

response_message = response.choices[0].message
if response_message.tool_calls:
    tool_call = response_message.tool_calls[0]
    arguments = json.loads(tool_call.function.arguments)
    location = arguments["location"]
    weather_data = get_weather(location)

    llm_messages.append(response_message)
    llm_messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": json.dumps(weather_data)
    })

    final_response = client.chat.completions.create(
        messages = llm_messages,
        model = "llama-3.3-70b-versatile",
        tools = tools,
        tool_choice = "auto"
    )

    print(final_response.choices[0].message.content)