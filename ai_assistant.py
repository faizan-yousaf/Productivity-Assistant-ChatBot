class AIAssistant:
    def get_response(self, question):
        # This is a placeholder for a more sophisticated AI model
        responses = {
            "time management": "Try the Pomodoro Technique: Work for 25 minutes, then take a 5-minute break.",
            "productivity": "Set clear, achievable goals for each day and prioritize your tasks.",
            "remote work": "Establish a dedicated workspace and stick to a regular schedule.",
            "default": "I'm sorry, I don't have specific advice for that. Can you try asking about time management, productivity, or remote work?"
        }
        
        for key in responses:
            if key in question.lower():
                return responses[key]
        return responses["default"]