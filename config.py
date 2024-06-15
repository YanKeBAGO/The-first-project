# Пути к лог-файлам
file_paths = [
    (r'/Users/yankebago/Desktop/proekt1/Pars_Apache_Logs/logs1', '%h,%t,%r,%>s,%b'),
    (r'/Users/yankebago/Desktop/proekt1/Pars_Apache_Logs/logs2', '%r,%>s')
]

# Информация для подключения к базе данных
db_info = {
    'database': 'apache_logs',
    'user': 'postgres',
    'password': '1234',
    'host': '127.0.0.1',
    'port': '5433'
}
