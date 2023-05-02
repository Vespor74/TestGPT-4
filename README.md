# Программа чат-бота на основе OpenAI и Telegram
___
Эта программа - чат-бот, использующий API OpenAI для генерации ответов на вопросы, заданные пользователем в чате Telegram. Она была создана на языке Python с использованием библиотеки aiogram.
## Использование
___
1. Установите необходимые библиотеки, выполнив команду:
```
pip install -r requirements.txt
```
2. Вставьте свой токен Telegram и ключ API OpenAI в соответствующие переменные в начале файла (6 и 7 строичка).
3. Запустите программу, выполните команду:
```
python main.py
```
4. Напишите сообщение боту в чате Telegram.
5. Бот сгенерирует ответ с помощью модели GPT-4 OpenAI и отправит его в ответ.
## Информация о файлах
___
**main.py** - основной файл программы.
**requirements.txt** - список необходимых библиотек для установки.
## Автор
___
Эта программа была создана Павлом Дзюбайло для тестирования возможностей GPT-4 и Telegram.
## Лицензия
___
Эта программа лицензируется под MIT License.