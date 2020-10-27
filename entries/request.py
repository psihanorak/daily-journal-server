from models.entry import Entry
from models.mood import Mood

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
            e.moodId,
            m.id,
            m.label
        FROM entries e
        JOIN moods m
            ON m.id = e.moodId
        """)

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'],
                          row['date'], row['moodId'])

            mood = Mood(row['id'], row['label'])

            entry.mood = mood.__dict__
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
            e.moodId,
            m.id,
            m.label
        FROM entries e
        JOIN moods m
            ON m.id = e.moodId
        WHERE e.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        entry = Entry(data['id'], data['concept'], data['entry'], data['date'], data['moodId'])

        mood = Mood(data['id'], data['label'])

        entry.mood = mood.__dict__

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

def create_journal_entry(new_entry):
    with sqlite3.connect('./daily-journal.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO entries
            ( concept, entry, date, moodId )
        VALUES
            (?, ?, ?, ?)
        """, (new_entry['concept'], new_entry['entry'],
                new_entry['date'], new_entry['moodId'], ))
    
        id = db_cursor.lastrowid

        new_entry['id'] = id

    return json.dumps(new_entry)

def update_entry(id, entry):
    with sqlite3.connect("./daily-journal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE entries
            SET
                concept = ?,
                entry = ?,
                date = ?,
                moodId = ?
        WHERE id == ?
        """, (entry['concept'], entry['entry'], entry['date'], entry['moodId'], id,))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
