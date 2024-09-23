from flask import Flask, render_template, request
import requests

# импортируем объект класса Flask
app = Flask(__name__)

# формируем путь и методы GET и POST
@app.route('/', methods=['GET', 'POST'])
# создаем функцию с переменной weather, где мы будем сохранять погоду
def index():
    weather = None
    news = None
    # формируем условия для проверки метода. Форму мы пока не создавали, но нам из неё необходимо будет взять только город.
    if request.method == 'POST':
        # этот определенный город мы будем брать для запроса API
        city = request.form['city']
        weather = get_weather(city)
        news = get_news()
    return render_template("index.html", weather=weather, news=news)

def get_weather(city):
    api_key = "c8ad1be9db9052b37ba20a64ef2c625e"
    # адрес, по которому мы будем отправлять запрос. Не забываем указывать f строку.
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}&units=metric"
    response = requests.get(url)
    return response.json()
def get_news():
    api_key = "81ab77d589114f83a6d7b593abb0e48d"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"

    # для получения результата нам понадобится модуль requests
    response = requests.get(url)
    return response.json().get('articles', [])

if __name__ == '__main__':
    app.run(debug=True)

#Временная сложность для разных частей этого кода:

#1. Функция index:
#В основном обрабатывает запросы и выполняет шаблонизацию.
#При POST-запросе:
#Выполняется функция get_weather(city) и get_news(), которые оба делают сетевые запросы.
#Временная сложность самой функции index по сути зависит от сложности вызова внешних функций
# get_weather() и get_news().
#2. Функция get_weather(city):
#Формирует URL и отправляет запрос к API погоды.
#Основное время выполнения этой функции — это выполнение HTTP-запроса через requests.get(),
# которое зависит от задержек сети, но с точки зрения алгоритмической оценки на уровне
# кода можно считать выполнение функции как O(1), так как сложность выполнения запроса
# не зависит от размера данных (городов).
#3. Функция get_news():
#Аналогично get_weather(), формируется URL и выполняется HTTP-запрос через requests.get().
#Хотя возвращаемый JSON с новостями может быть большим, сложность самого запроса также
# не зависит от размера данных, так как запрос ограничен определенным количеством новостей
# (например, 20).
#Поэтому сложность запроса также считается O(1).

#Общая сложность:

#Основная работа в коде связана с выполнением двух HTTP-запросов к внешним API в функциях
# get_weather() и get_news(). С точки зрения оценки сложности выполнения этих запросов,
# они оба считаются операциями с константной сложностью O(1), так как не зависят от входных
# данных (размеры ответа API фиксированы, например, список новостей ограничен 20 статьями).

#Таким образом:

#Временная сложность работы алгоритма в функции index — O(1).
#Основное время выполнения кода будет зависеть от задержек сети при выполнении
# HTTP-запросов к API погоды и новостей.





