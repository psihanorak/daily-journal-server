from models.entry import Entry

import sqlite3
import json

def get_all_entries():
    with sqlite3.connect("./daily-journal.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.moodId
        FROM entries e
        """)

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'],
                          row['date'], row['moodId'])
            
            entries.append(entry.__dict__)

    return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("./daily-journal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.moodId
        FROM entries e
        WHERE e.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        entry = Entry(data['id'], data['concept'], data['entry'], data['date'], data['moodId'])

        return json.dumps(entry.__dict__)

def delete_entry(id):
    with sqlite3.connect('./daily-journal.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM entries
        WHERE id = ?
        """, (id, ))

def search_entry(entry):
    with sqlite3.connect('./daily-journal.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(f"""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.moodId
        FROM entries e
        WHERE e.entry LIKE '%{entry}%'
        """)

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'],
                          row['date'], row['moodId'],
                                )
            entries.append(entry.__dict__)

        return json.dumps(entries)
