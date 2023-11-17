import re
import random

# Sample dictionary for intention recognition using regular expressions
intentions_dict = {
    "go_to": [r"go to the (\w+)", r"head to the (\w+)"],
    "take_me_to": [r"take me to the (\w+)"]
}

# Dictionary to map intentions to actions
actions_dict = {
    "go_to": lambda place: f"Robot is moving to {place}",
    "take_me_to": lambda place: f"Robot is taking you to {place}"
}

def recognize_intention(command):
    """
    Recognizes the user's intention from the command.
    """
    for intention, patterns in intentions_dict.items():
        for pattern in patterns:
            match = re.search(pattern, command, re.IGNORECASE)
            if match:
                return intention, match.group(1)
    return None, None

def execute_action(intention, place):
    """
    Executes the action based on the recognized intention.
    """
    if intention in actions_dict:
        action = actions_dict[intention](place)
        return action
    else:
        return "I don't understand that command."

def chatbot_command(command):
    """
    Processes the command and provides user feedback.
    """
    intention, place = recognize_intention(command)
    if intention:
        response = execute_action(intention, place)
    else:
        response = "Sorry, I didn't understand that. Can you rephrase?"
    
    return response

# Example usage
if __name__ == "__main__":
    user_command = input("Enter your command: ")
    response = chatbot_command(user_command)
    print(response)

