import sqlite3

# Устанавливаем соединение с базой данных
conn = sqlite3.connect('database.db')

# Создаем курсор
cursor = conn.cursor()

# Добавляем первый пост
cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('Первый пост', 'Содержание первого поста'))

# Добавляем второй пост
cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", ('Второй пост', 'Содержание второго поста'))

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()