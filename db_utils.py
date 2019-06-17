import sqlite3
from sqlite3 import Error

import configparser

config = configparser.ConfigParser()
config.read('config.ini')
db_file = config['FILE_PATHS']['DB_FILE']


def get_db_connection():
    """ create a database connection to a SQLite database """
    db_connection = sqlite3.connect(db_file)
    return db_connection

def create_db_table():
    create_table_stmt = '''CREATE TABLE IF NOT EXISTS annotations (
                                            id text PRIMARY KEY,
                                            comment_id text NOT NULL,
                                            department text,
                                            survey_id integer,
                                            aos_typ text,
                                            code text,
                                            question text,
                                            comment text,
                                            sentence text,
                                            comment_created text,
                                            feedback_categories text,
                                            sentiment_category text,
                                            is_multi_label boolean,
                                            annotator_name text
                                        );'''
    db_connection = get_db_connection()
    try:
        cursor = db_connection.cursor()
        cursor.execute(create_table_stmt)
    except Error as e:
        print(e)

def get_visited_comments():
    db_connection = get_db_connection()
    visited_comment_ids = []
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM annotations")

    rows = cur.fetchall()

    for row in rows:
        visited_comment_ids.append(row[1])
    return visited_comment_ids


def insert_db_record(df,
                     username,
                     current_sentence_idx,
                     current_sentences,
                     comment_idx,
                     feedback_categories,
                     sentiment_category):
    db_connection = get_db_connection()
    sql = ''' INSERT INTO annotations(id,
                                      comment_id,
                                      department,
                                      survey_id,
                                      aos_typ,
                                      code,
                                      question,
                                      comment,
                                      sentence,
                                      comment_created,
                                      feedback_categories,
                                      sentiment_category,
                                      is_multi_label,
                                      annotator_name)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''

    str_feedback_categories = ''
    is_multi_label = False
    if len(feedback_categories) != 1:
        is_multi_label = True

    for index, feedback_category in enumerate(feedback_categories):
        if index == len(feedback_categories)-1:
            str_feedback_categories = str_feedback_categories+feedback_category
        else:
            str_feedback_categories = str_feedback_categories+feedback_category+'||' \
                                                                                ''
    record = (str(username)+'_'+str(current_sentence_idx)+'_'+str(df.index.values[comment_idx]),
              str(df.index.values[comment_idx]),
              df['DEPARTMENT'].values[comment_idx],
              int(df['SURVEY_ID'].values[comment_idx]),
              str(df['AOS_TYPE'].values[comment_idx]),
              df['CODE'].values[comment_idx],
              df['QUESTION_PROMPT'].values[comment_idx],
              df['QUESTION_RESPONSE'].values[comment_idx],
              current_sentences[current_sentence_idx],
              df['QUESTION_RESPONDED'].values[comment_idx],
              str_feedback_categories,
              sentiment_category,
              is_multi_label,
              username)

    cursor = db_connection.cursor()
    cursor.execute(sql, record)
    db_connection.commit()

def get_num_annotated_comments(username):
    db_connection = get_db_connection()
    visited_comment_ids = []
    cur = db_connection.cursor()
    cur.execute("SELECT comment_id,annotator_name FROM annotations group by comment_id having annotator_name='"+username+"'")

    rows = cur.fetchall()
    return len(rows)

if __name__ == "__main__":
    print(get_num_annotated_comments(username='george'))