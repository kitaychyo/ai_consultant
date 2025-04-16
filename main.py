from openai import OpenAI
import sys


class AIConsultantDeepSeek:
    def __init__(self, api_key):
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com/v1"
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
            base_url="https://api.proxyapi.ru/openai/v1"
        )

    def get_ai_response(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Ошибка: {str(e)}"

def main():
    print("=== Консультант пользователя (ИИ-помощник) ===")
    print("Для выхода введите 'exit' или 'quit'\n")

    # Укажите ваш API-ключ
    flag = input('1 - gpt\ 2 - deepseek')
    if flag:
        api_key = "sk-eojihWMYuwlwO4oNjNMX8DbkkkBtLg7I"
        consultant = AIConsultant(api_key)
    else:
        api_key_ds = "sk-1d99cfa9db714d5083eb5394cf64f54d"
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