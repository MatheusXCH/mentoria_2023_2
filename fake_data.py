import random

import faker_commerce
import pandas as pd
from faker import Faker

NUM_PRODUTOS = 300000
NUM_LOJAS = 200000
NUM_VENDAS = 2000000
NUM_TEMPO = 2101

fake = Faker("pt_BR")
fake.add_provider(faker_commerce.Provider)

produtos = []
for _ in range(NUM_PRODUTOS):
    nome_produto = fake.ecommerce_name()
    categoria = fake.ecommerce_category()
    marca = fake.company()
    preco = round(random.uniform(10, 10000), 2)
    produtos.append([nome_produto, categoria, marca, preco])

lojas = []
for _ in range(NUM_LOJAS):
    nome_loja = fake.company()
    cidade = fake.city()
    estado = fake.state()
    pais = fake.current_country()
    lojas.append([nome_loja, cidade, estado, pais])

vendas = []
for _ in range(NUM_VENDAS):
    sk_d_tempo = int(random.uniform(1, NUM_TEMPO))
    sk_d_produto = int(random.uniform(1, NUM_PRODUTOS))
    sk_d_loja = int(random.uniform(1, NUM_LOJAS))
    quantidade_vendida = int(random.uniform(1, 1000000))
    total_vendas = round(random.uniform(1, 10000000), 2)
    vendas.append(
        [sk_d_tempo, sk_d_produto, sk_d_loja, quantidade_vendida, total_vendas]
    )

tempos = pd.DataFrame({"data": pd.date_range("2018-01-01", "2023-10-01")})
tempos["ano"] = tempos.data.dt.year
tempos["mes"] = tempos.data.dt.month
tempos["dia"] = tempos.data.dt.day
tempos["semana"] = tempos.data.dt.dayofweek
tempos["trimestre"] = tempos.data.dt.quarter
tempos["feriado"] = tempos.data.dt.is_quarter_start
tempos.insert(0, "sk_d_tempo", range(1, len(tempos) + 1))

d_produto = pd.DataFrame(
    produtos, columns=["nome_produto", "categoria", "marca", "preco"]
)
d_tempo = pd.DataFrame(
    tempos,
    columns=[
        "data",
        "ano",
        "mes",
        "dia",
        "semana",
        "trimestre",
        "feriado",
    ],
)
d_loja = pd.DataFrame(lojas, columns=["nome_loja", "cidade", "estado", "pais"])
f_vendas = pd.DataFrame(
    vendas,
    columns=[
        "sk_d_tempo",
        "sk_d_produto",
        "sk_d_loja",
        "quantidade_vendida",
        "total_vendas",
    ],
)

d_produto.to_csv("data/d_produto.csv", index=False)
d_tempo.to_csv("data/d_tempo.csv", index=False)
d_loja.to_csv("data/d_loja.csv", index=False)
f_vendas.to_csv("data/f_vendas.csv", index=False)
