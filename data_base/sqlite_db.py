import sqlite3 as sq

def sqlStart():
    global db, cur
    db = sq.connect('botyara.db')
    cur = db.cursor()
    if db: print('DB connected')
    db.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY,description TEXT, price TEXT)')
    db.execute('CREATE TABLE IF NOT EXISTS users(id TEXT PRIMARY KEY, nickname TEXT)')
    #base.execute('CREATE TABLE IF NOT EXISTS backed(id TEXT, nickname TEXT)')
    db.commit()

async def sql_add_menu(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?,?,?,?)', tuple(data.values()))
        db.commit()