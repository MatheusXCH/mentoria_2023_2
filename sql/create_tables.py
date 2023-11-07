drop_tables_mentoria = """
    DROP TABLE IF EXISTS f_vendas, d_tempo, d_produto, d_loja
"""

create_table_d_tempo = """
    CREATE TABLE d_tempo (
        sk_d_tempo INT AUTO_INCREMENT PRIMARY KEY,
        data DATE NOT NULL,
        ano INT NOT NULL,
        mes INT NOT NULL,
        dia INT NOT NULL,
        trimestre INT NOT NULL,
        semana INT NOT NULL,
        feriado BOOLEAN NOT NULL
    );
"""

create_table_d_produto = """
    CREATE TABLE d_produto (
        sk_d_produto INT AUTO_INCREMENT PRIMARY KEY,
        nome_produto VARCHAR(255) NOT NULL,
        categoria VARCHAR(255),
        marca VARCHAR(255),
        preco DECIMAL(10,2)
    );
"""

create_table_d_loja = """
    CREATE TABLE d_loja (
        sk_d_loja INT AUTO_INCREMENT PRIMARY KEY,
        nome_loja VARCHAR(255) NOT NULL,
        cidade VARCHAR(255) NOT NULL,
        estado VARCHAR(255) NOT NULL,
        pais VARCHAR(255) NOT NULL
    );
"""

create_table_f_vendas = """
    CREATE TABLE f_vendas (
        sk_f_vendas INT AUTO_INCREMENT PRIMARY KEY,
        sk_d_tempo INT NOT NULL,
        sk_d_produto INT NOT NULL,
        sk_d_loja INT NOT NULL,
        quantidade_vendida INT,
        total_vendas DECIMAL(10,2),
    FOREIGN KEY (sk_d_tempo) REFERENCES d_tempo(sk_d_tempo),
    FOREIGN KEY (sk_d_produto) REFERENCES d_produto(sk_d_produto),
    FOREIGN KEY (sk_d_loja) REFERENCES d_loja(sk_d_loja)
    );
"""
