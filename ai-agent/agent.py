import requests

from prompts import SYSTEM_PROMPT


OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "qwen3:4b"


class StudyHubAgent:
    """
    Study Hub AI Agent.

    Qwen provides the language-model capability.
    This class controls the Study Hub-specific behavior,
    instructions, and future integration with the backend.
    """

    def __init__(self):
        self.model = MODEL_NAME

    def answer(self, question):
        """
        Send a teacher's question to the Study Hub AI.
        """

        if not question or not question.strip():
            return "Please enter a question."

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question.strip()
            }
        ]

        try:
            response = requests.post(
                OLLAMA_URL,
                json={
                    "model": self.model,
                    "messages": messages,
                    "stream": False
                },
                timeout=120
            )

            response.raise_for_status()

            result = response.json()

            return result["message"]["content"].strip()

        except requests.exceptions.ConnectionError:
            return (
                "Study Hub AI is currently unavailable. "
                "Please make sure the AI service is running."
            )

        except requests.exceptions.Timeout:
            return (
                "Study Hub AI took too long to respond. "
                "Please try again."
            )

        except requests.exceptions.RequestException:
            return (
                "Study Hub AI encountered a connection problem. "
                "Please try again."
            )

        except (KeyError, TypeError, ValueError):
            return (
                "Study Hub AI received an unexpected response. "
                "Please try again."
            )