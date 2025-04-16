from openai import OpenAI
import sys


class AIConsultantDeepSeek:
    def __init__(self, api_key):
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

    def get_ai_response(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Ошибка: {str(e)}"

class AIConsultant:
    def __init__(self, api_key):
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

    def get_ai_response(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model="google/gemini-2.5-pro-exp-03-25:free",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Ошибка: {str(e)}"

def main():
    print("=== Консультант пользователя (ИИ-помощник) ===")
    print("Для выхода введите 'exit' или 'quit'\n")

    # Укажите ваш API-ключ
    flag = input('1 - Google  or 2 - deepseek')
    if flag:
        api_key = "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"
        consultant = AIConsultant(api_key)
    else:
        api_key_ds = "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"
        consultant = AIConsultantDeepSeek(api_key_ds)

    while True:
        user_input = input("Вы: ")

        if user_input.lower() in ('exit', 'quit'):
            print("До свидания!")
            break

        response = consultant.get_ai_response(user_input)
        print("\nКонсультант:", response, "\n")


if __name__ == "__main__":
    main()