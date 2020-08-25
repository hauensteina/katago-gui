
from pdb import set_trace as BP
from katago_gui import bcrypt

def create_tables(db):
    create_t_user(db)
    create_t_game(db)

def create_t_user(db):
    if db.table_exists( 't_user'):
        return
    sql = '''
    create table t_user (
    id bigserial not null primary key
    ,username text
    ,email text
    ,password text
    ,fname text
    ,lname text
    ,ts_created timestamptz
    ,ts_last_seen timestamptz
    ,email_verified boolean
    ,lang text
    ,game_hash text
    ,move_count integer not null default 0
    ,self_move_count integer not null default 0
    ,watch_game_hash text
    ) '''
    db.run( sql)

def create_t_game(db):
    if db.table_exists( 't_game'):
        return
    sql = '''
    create table t_game (
    game_hash text not null primary key
    ,username text
    ,handicap integer
    ,komi real
    ,ts_started timestamptz
    ,ts_latest_move timestamptz
    ,game_record text
    ) '''
    db.run( sql)
