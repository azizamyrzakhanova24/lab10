

conn = psycopg2.connect(
    host="localhost",
    dbname="lab10",
    user="postgres",
    password="Almaty250505",
    port=5432
)
cur = conn.cursor()
conn.set_session(autocommit=True)

# Пайдаланушылар таблицасы
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);
""")

# Ұпай таблицасы
cur.execute("""
CREATE TABLE IF NOT EXISTS user_scores (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    level INTEGER,
    score INTEGER,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

print("Tables created successfully.")
cur.close()
conn.close()
