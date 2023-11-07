import logging
import os

import pandas as pd

from classes.database_info import DatabaseInfo
from sql.create_tables import *
from utils.instancias import INSTANCIA_GERENCIADA, INSTANCIA_VM

CHUNK = 10000

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logging.getLogger().setLevel(logging.INFO)

# db_info = DatabaseInfo(**INSTANCIA_GERENCIADA)
db_info = DatabaseInfo(**INSTANCIA_VM)


def create_database_schema(db_info):
    logging.info(f"Recriando tabelas no banco...")
    database = (
        db_info.connect()
        .execute(drop_tables_mentoria)
        .execute(create_table_d_tempo)
        .execute(create_table_d_loja)
        .execute(create_table_d_produto)
        .execute(create_table_f_vendas)
        .disconnect()
    )
    logging.info(f"Tabelas criadas com sucesso!")
    return database


def load_tempo(db_info):
    logging.info(f"Carregando D_TEMPO...")
    df_d_tempo = pd.read_csv("data/d_tempo.csv")
    df_d_tempo.to_sql(
        "d_tempo",
        con=db_info.engine,
        if_exists="append",
        index=False,
        chunksize=CHUNK,
    )
    logging.info("D_TEMPO carregada com sucesso!")
    return


def load_produto(db_info):
    logging.info(f"Carregando D_PRODUTO...")
    df_d_produto = pd.read_csv("data/d_produto.csv")
    df_d_produto.to_sql(
        "d_produto",
        con=db_info.engine,
        if_exists="append",
        index=False,
        chunksize=CHUNK,
    )
    logging.info("D_PRODUTO carregada com sucesso!")
    return


def load_loja(db_info):
    logging.info(f"Carregando D_LOJA...")
    df_d_loja = pd.read_csv("data/d_loja.csv")
    df_d_loja.to_sql(
        "d_loja",
        con=db_info.engine,
        if_exists="append",
        index=False,
        chunksize=CHUNK,
    )
    logging.info("D_LOJA carregada com sucesso!")
    return


def load_vendas(db_info):
    logging.info(f"Carregando F_VENDAS...")
    df_f_vendas = pd.read_csv("data/f_vendas.csv")
    df_f_vendas.to_sql(
        "f_vendas",
        con=db_info.engine,
        if_exists="append",
        index=False,
        chunksize=CHUNK,
    )
    logging.info("F_VENDAS carregada com sucesso!")
    return


create_database_schema(db_info=db_info)
load_tempo(db_info=db_info)
load_produto(db_info=db_info)
load_loja(db_info=db_info)
load_vendas(db_info=db_info)
