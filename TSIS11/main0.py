# CREATE OR REPLACE PROCEDURE public.many1(
#   )
# LANGUAGE 'plpgsql'
# AS $BODY$
# declare
# nums varchar(30);
# begin
# for nums in select phone from list
# loop
# if(length(nums) <= 15 and length(nums) >= 11) then
# raise notice 'correct nums=%', nums;
# else
# DELETE from list where phone = nums;
# end if;
# end loop;
# end
# $BODY$;
# ALTER PROCEDURE public.many1()
#     OWNER TO postgres;



# CREATE OR REPLACE FUNCTION public.get_info1(
#   )
#     RETURNS TABLE(name character varying, number character varying)
#     LANGUAGE 'plpgsql'
#     COST 100
#     VOLATILE PARALLEL UNSAFE
#     ROWS 1000
#
# AS $BODY$
# BEGIN
# RETURN QUERY
#
# SELECT user_name, phone FROM list order by id limit 3 offset 2;
#
# END;
# $BODY$;
#
# ALTER FUNCTION public.get_info1()
#     OWNER TO postgres;


#
# -- PROCEDURE: public.insert_user(character varying, character varying)
#
# -- DROP PROCEDURE IF EXISTS public.insert_user(character varying, character varying);
#
# CREATE OR REPLACE PROCEDURE public.insert_user(
#   IN name character varying,
#   IN number character varying)
# LANGUAGE 'plpgsql'
# AS $BODY$
# BEGIN
# INSERT INTO list(user_name, phone)
# VALUES(name, number);
# END;
# $BODY$;
# ALTER PROCEDURE public.insert_user(character varying, character varying)
#     OWNER TO postgres;
#
#
# insert user
#
#
# -- PROCEDURE: public.delete_user(character varying)
#
# -- DROP PROCEDURE IF EXISTS public.delete_user(character varying);
#
# CREATE OR REPLACE PROCEDURE public.delete_user(
#   IN name character varying)
# LANGUAGE 'plpgsql'
# AS $BODY$
# BEGIN
# DELETE from list where user_name = name;
# END;
# $BODY$;
# ALTER PROCEDURE public.delete_user(character varying)
#     OWNER TO postgres;
#
#
# delete user
#
#
# CREATE OR REPLACE PROCEDURE public.update_user(
#   IN name character varying,
#   IN number character varying)
# LANGUAGE 'plpgsql'
# AS $BODY$
# BEGIN
# UPDATE list SET phone = number WHERE user_name = name;
# END;
# $BODY$;
# ALTER PROCEDURE public.update_user(character varying, character varying)
#     OWNER TO postgres;
#
#
# update user
#
#
# CREATE OR REPLACE PROCEDURE public.get_many(
#   )
# LANGUAGE 'plpgsql'
# AS $BODY$
# declare
# nums text;
# begin
# for nums in select phone from list
# loop
# if(length(nums) <= 15 and length(nums) >= 11) then
# raise notice 'correct nums=%', nums;
# else
# raise notice 'uncorrect nums=%', nums;
# end if;
# end loop;
# end
# $BODY$;
# ALTER PROCEDURE public.get_many()
#     OWNER TO postgres;
#
#
# задание с корректностью номеров и вводом большого количества значений
#
#
#
#
#
# create or replace function get_info (
#   n_pattern varchar
# )
# returns table (
#   name varchar,
#   number varchar
# )
# language plpgsql
# as $$
# begin
#   return query
#     select
#       user_name,
#       phone::varchar
#     from
#       list
#     where
#       user_name ilike n_pattern;
# end; $$
#
#
# функция с получением информации по паттерну
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="nn22913705"
)
cur = conn.cursor()


def info():  # 1
    word = input("Enter word: ")
    word += '%'
    cur.execute("SELECT * from get_info(%s);", (word,))  # 1
    row = cur.fetchall()
    print(row)
    conn.commit()


def update(name, number):  # 2
    check_user = ("SELECT 1 FROM list WHERE user_name = '%s'" % (name,))
    cur.execute(check_user)
    row = cur.fetchone()
    if row != None:
        cur.execute('CALL update_user(%s, %s)', (name, number))
    else:
        cur.execute('CALL insert_user(%s, %s)', (name, number))
    conn.commit()


def many1():   # 3
    l = [['Lolter', '+77018260248'], ['Kyle', '+9213890484'], ['Bot', '21930344'], ['Proos', '23847853']]
    for i in l:
        cur.execute("CALL insert_user(%s, %s)", (i[0], i[1],))
    cur.execute("select * from many3();")
    cur.execute("select * from list2;")
    row = cur.fetchall()
    print(row)



def offset():  # 4
    cur.execute("select * from get_info1();")
    row = cur.fetchall()
    print(row)


def delete(name):  # 5
    cur.execute('CALL delete_user(%s)', (name,))
    conn.commit()

many1()
conn.commit()
cur.close()
conn.close()