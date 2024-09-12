from transformers import pipeline


class AIAssistant:
    def __init__(self):
        # Load a pre-trained language model for text generation (formerly conversational)
        self.model = pipeline('text-generation', model='gpt2')
        self.responses = {
            "time management": "Try the Pomodoro Technique: Work for 25 minutes, then take a 5-minute break.",
            "productivity": "Set clear, achievable goals for each day and prioritize your tasks.",
            "remote work": "Establish a dedicated workspace and stick to a regular schedule.",
            "goal setting": "Use the SMART criteria to set specific, measurable, achievable, relevant, and time-bound goals.",
            "report generation": "I can help you summarize your weekly tasks and achievements. Please provide the details.",
            "default": "I'm sorry, I don't have specific advice for that. Can you try asking about time management, productivity, or remote work?"
        }

    def get_response(self, question):
        question = question.lower()
        
        # Check for specific keywords in the user's question
        for key in self.responses:
            if key in question:
                return self.responses[key]

        # If no specific keyword found, generate a response using the text-generation model
        generated_response = self.model(question, max_length=100, num_return_sequences=1)
        return generated_response[0]['generated_text']

    def add_custom_response(self, topic, response):
        """Allows the addition of custom responses for specific topics."""
        self.responses[topic.lower()] = response

    def get_productivity_report(self, tasks):
        """Generates a simple productivity report based on completed tasks."""
        completed_tasks = [task for task in tasks if task['completed']]
        report = f"You completed {len(completed_tasks)} out of {len(tasks)} tasks this week."
        return report