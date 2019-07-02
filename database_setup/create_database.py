import sqlite3

DBNAME = 'alum_message.db'

def init_alum_message_db():
    try:
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()
        conn.close()
    except:
        print("Unable to create or connect to alum_messages.db database.")

def create_alum_table():
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    table_name = "alum"
    drop_statement = '''
        DROP TABLE IF EXISTS '{}';
    '''.format(table_name)
    cur.execute(drop_statement)
    conn.commit()
    alum_statement = '''
        CREATE TABLE '{}' (
            'alum_id' INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            'uniqname' TEXT NOT NULL UNIQUE,
            'display_name' TEXT NOT NULL,
            'family_name' TEXT NOT NULL,
            'given_name' TEXT NOT NULL
            );
    '''.format(table_name)
    conn.execute(alum_statement)

def create_message_table():
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    table_name = "message"
    drop_statement = '''
        DROP TABLE IF EXISTS '{}';
    '''.format(table_name)
    cur.execute(drop_statement)
    conn.commit()
    message_statement = '''
        CREATE TABLE '{}' (
            'message_id' INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            'subject' TEXT NOT NULL,
            'message_text' TEXT NOT NULL,
            'timestamp' TEXT NOT NULL,
            'sender_alum_id' INTEGER NOT NULL,
            FOREIGN KEY(sender_alum_id) REFERENCES alum(alum_id)
            );
    '''.format(table_name)
    conn.execute(message_statement)

def create_receipt_table():
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()
    table_name = "receipt"
    drop_statement = '''
        DROP TABLE IF EXISTS '{}';
    '''.format(table_name)
    cur.execute(drop_statement)
    conn.commit()
    receipt_statement = '''
        CREATE TABLE '{}' (
            'receipt_id' INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            'message_id' INTEGER NOT NULL,
            'alum_id' INTEGER NOT NULL,
            FOREIGN KEY(alum_id) REFERENCES alum(alum_id),
            FOREIGN KEY(message_id) REFERENCES message(message_id)
            );
    '''.format(table_name)
    conn.execute(receipt_statement)

## Main Program

if __name__=="__main__":
    # Calling functions to create and populate database tables
    init_alum_message_db()
    create_alum_table()
    create_message_table()
    create_receipt_table()