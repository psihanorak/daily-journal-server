from models.journal_entries import Journal_Entries

import sqlite3
import json

ENTRIES = [{
                "id": 1,
                "concept": "1235",
                "entry": "123",
                "date": 1598458543321,
                "moodId": 1
            }, {
                "id": 2,
                "concept": "abc",
                "entry": "123",
                "date": 1598458548239,
                "moodId": 2
            }, {
                "id": 3,
                "concept": "Delete",
                "entry": "Now Deleting",
                "date": 1598458559152,
                "moodId": 1
            }, {
                "id": 4,
                "concept": "ANGRY",
                "entry": "jlj",
                "date": 1598557358781,
                "moodId": 3
            }, {
                "id": 5,
                "concept": "678",
                "entry": "Now Deleting",
                "date": 1598557373697,
                "moodId": 4
            }]

def get_all_entries():
    return ENTRIES

    # with sqlite3.connect("./daily-journal.db") as conn:
    #    conn.row_factory = sqlite3.Row
    #    db_cursor = conn.cursor()

    #    db_cursor.execute("""
    #    SELECT
    #        e.id,
    #        e.concept,
    #        e.entry,
    #        e.moodId,
    #        e.date,
    #        m.id id,
    #        m.label mood
    #    FROM JournalEntries e
    #    JOIN Moods m
    #        ON m.id = e.moodId
    #    """)

    #    entries = []

    #    dataset = db_cursor.fetchall()

    #    for row in dataset:
    #       entry = Journal_Entries(row['id'], row['concept'], row['entry'],
    #                        row['moodId'], row['date'])
            
    #        entries.append(entry.__dict__)

    # return json.dumps(entries)
