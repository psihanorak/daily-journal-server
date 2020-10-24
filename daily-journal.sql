CREATE TABLE 'Journal Entries' (
  'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  'concept' TEXT NOT NULL,
  'entry' TEXT NOT NULL,
  'mood_id' INTEGER NOT NULL,
  'date' INTEGER NOT NULL,
  FOREIGN KEY('mood_id') REFERENCES 'Mood'('id')
);

CREATE TABLE 'Mood' (
    'id' INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'label' TEXT NOT NULL
);

INSERT INTO 'Journal Entries' VALUES (null, 'First Date', 'I think she liked me!', 1, 6543132);
INSERT INTO 'Journal Entries' VALUES (null, 'New Car', 'I picked up my new car!', 2, 65432135);
INSERT INTO 'Journal Entries' VALUES (null, 'New House', 'I received the keys to my house!', 3, 979684);

INSERT INTO 'Mood' VALUES (null, 'Happy');
INSERT INTO 'Mood' VALUES (null, 'Ecstatic');
INSERT INTO 'Mood' VALUES (null, 'Sad');
INSERT INTO 'Mood' VALUES (null, 'Angry');
