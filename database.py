import sqlite3
from typing import Optional, List, Dict

DB_PATH = "database.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Создаем таблицу пользователей, если ее нет
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        goal TEXT,
        photo_file_id TEXT,
        bio TEXT,
        language TEXT
    )
    """)
    
    # Таблица для лайков
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS likes (
        from_user INTEGER,
        to_user INTEGER,
        PRIMARY KEY (from_user, to_user)
    )
    """)
    
    # Таблица для просмотров анкет
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS views (
        viewer INTEGER,
        viewed INTEGER,
        PRIMARY KEY (viewer, viewed)
    )
    """)
    
    conn.commit()
    conn.close()

def get_user(user_id: int) -> Optional[Dict]:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        keys = ['user_id', 'username', 'name', 'age', 'gender', 'goal', 'photo_file_id', 'bio', 'language']
        return dict(zip(keys, row))
    return None

def create_user(user_id: int, username: str, name: str, age: int, gender: str, goal: str,
                photo_file_id: str, bio: str, language: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT OR REPLACE INTO users (user_id, username, name, age, gender, goal, photo_file_id, bio, language)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (user_id, username, name, age, gender, goal, photo_file_id, bio, language))
    conn.commit()
    conn.close()

def add_like(from_user: int, to_user: int) -> bool:
    """
    Добавляет лайк от from_user к to_user.
    Возвращает True, если это совпадение (то есть to_user тоже лайкнул from_user).
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Добавляем лайк
    cursor.execute("INSERT OR IGNORE INTO likes (from_user, to_user) VALUES (?, ?)", (from_user, to_user))
    
    # Проверяем взаимный лайк
    cursor.execute("SELECT 1 FROM likes WHERE from_user=? AND to_user=?", (to_user, from_user))
    match = cursor.fetchone()
    
    conn.commit()
    conn.close()
    
    return match is not None

def add_view(viewer: int, viewed: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO views (viewer, viewed) VALUES (?, ?)", (viewer, viewed))
    conn.commit()
    conn.close()

def get_next_profile(user_id: int) -> Optional[Dict]:
    """
    Возвращает следующий профиль, которого user_id ещё не видел и не лайкал.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Получаем список user_id, которых уже видел или лайкал этот пользователь
    cursor.execute("""
    SELECT viewed FROM views WHERE viewer=?
    UNION
    SELECT to_user FROM likes WHERE from_user=?
    """, (user_id, user_id))
    excluded_ids = [row[0] for row in cursor.fetchall()]
    excluded_ids.append(user_id)  # Исключаем себя
    
    placeholders = ",".join("?" for _ in excluded_ids)
    query = f"SELECT * FROM users WHERE user_id NOT IN ({placeholders}) LIMIT 1"
    
    cursor.execute(query, excluded_ids)
    row = cursor.fetchone()
    conn.close()
    
    if row:
        keys = ['user_id', 'username', 'name', 'age', 'gender', 'goal', 'photo_file_id', 'bio', 'language']
        return dict(zip(keys, row))
    return None

def get_matches(user_id: int) -> List[Dict]:
    """
    Возвращает список пользователей, которые взаимно лайкнули друг друга.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT u.* FROM users u
    JOIN likes l1 ON u.user_id = l1.to_user
    JOIN likes l2 ON u.user_id = l2.from_user
    WHERE l1.from_user = ? AND l2.to_user = ?
    """, (user_id, user_id))
   
    rows = cursor.fetchall()
    conn.close()
    
    keys = ['user_id', 'username', 'name', 'age', 'gender', 'goal', 'photo_file_id', 'bio', 'language']
    return [dict(zip(keys, row)) for row in rows]
