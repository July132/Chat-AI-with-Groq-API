from groq import Groq

# Initialize Groq API client
client = Groq(
    api_key='YOUR API KEY',  # Replace with your own API key
)

# Function to get chat completion from Groq API
def get_ai_response(user_input):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_input}
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# Main loop for user input
while True:
    user_input = input("You: ")
    print()
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye! 👋")
        break
    response = get_ai_response(user_input)
    if len(response) > 50:
        for i in range(100, len(response), 100):
            counter = i
            while True:
                if counter >= len(response):
                    break
                if response[counter] == " ":
                    before_i = response[:counter]
                    after_i = response[counter + 1:]
                    response = before_i + '\n' + after_i
                    break
                counter += 1

    print(f"AI: {response}")
    print()
    with open("chat_history.txt", "w") as f:
        f.write(f"You: {user_input}\n\n")
        f.write(f"AI: {response}\n\n")
