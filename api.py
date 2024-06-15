from flask import Flask, request, jsonify
import psycopg2
import psycopg2.extras
import config

app = Flask(__name__)

def get_database_connection():
    '''Функция для получения подключения к базе данных'''
    conn = psycopg2.connect(
        database=config.db_credentials['database'],
        user=config.db_credentials['user'],
        password=config.db_credentials['password'],
        host=config.db_credentials['host'],
        port=config.db_credentials['port'],
        options='-c client_encoding=utf8'  # Устанавливаем кодировку клиента UTF-8
    )
    return conn

@app.route('/logs', methods=['GET'])
def retrieve_logs():
    '''Эндпоинт для получения логов с фильтрацией'''
    # Получение параметров из запроса
    server_ip = request.args.get('ip', default=None)
    start_timestamp = request.args.get('start_date', default=None)
    end_timestamp = request.args.get('end_date', default=None)

    # Подключение к базе данных
    conn = get_database_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Формируем SQL запрос
    query = 'SELECT * FROM logs WHERE TRUE'
    if server_ip:
        query += f" AND server_ip = '{server_ip}'"
    if start_timestamp:
        query += f" AND date_time >= '{start_timestamp}'"
    if end_timestamp:
        query += f" AND date_time <= '{end_timestamp}'"

    cursor.execute(query)
    logs = cursor.fetchall()

    # Преобразуем результаты в JSON
    json_logs = [dict(log) for log in logs]

    cursor.close()
    conn.close()

    return jsonify(json_logs)

if __name__ == '__main__':
    app.run(debug=True)  # Запуск сервера Flask