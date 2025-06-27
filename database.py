import aiosqlite

DB_PATH = "users.db"

async def create_user(user_id, username, name, age, gender, goal, photo_file_id, bio, language):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute('''
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
        ''')
        await db.execute('''
            INSERT OR REPLACE INTO users (user_id, username, name, age, gender, goal, photo_file_id, bio, language)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (user_id, username, name, age, gender, goal, photo_file_id, bio, language))
        await db.commit()

async def get_user(user_id):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
        row = await cursor.fetchone()
        if row:
            return {
                'user_id': row[0],
                'username': row[1],
                'name': row[2],
                'age': row[3],
                'gender': row[4],
                'goal': row[5],
                'photo_file_id': row[6],
                'bio': row[7],
                'language': row[8]
            }
        return None
