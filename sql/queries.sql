SELECT *
FROM mentoria.f_vendas fv
    JOIN mentoria.d_loja dl ON fv.sk_d_loja = dl.sk_d_loja
    JOIN mentoria.d_produto dp ON fv.sk_d_produto = dp.sk_d_produto
    JOIN mentoria.d_tempo dt ON fv.sk_d_tempo = dt.sk_d_tempo
ORDER BY fv.sk_f_vendas DESC;

SELECT
    dl.nome_loja,
    sum(fv.quantidade_vendida) as sum_quantidade_vendida,
    sum(fv.total_vendas) as sum_total_vendas
FROM mentoria.f_vendas fv
    JOIN mentoria.d_loja dl ON fv.sk_d_loja = dl.sk_d_loja
    JOIN mentoria.d_produto dp ON fv.sk_d_produto = dp.sk_d_produto
    JOIN mentoria.d_tempo dt ON fv.sk_d_tempo = dt.sk_d_tempo
WHERE
    dp.categoria IN ('Kids', 'Grocery', 'Toys')
GROUP BY dl.nome_loja
ORDER BY sum_total_vendas DESC;

SELECT
    dl.nome_loja,
    SUM(
        CASE
            WHEN dp.categoria = 'Kids' THEN fv.total_vendas
            ELSE 0
        END
    ) AS kids,
    SUM(
        CASE
            WHEN dp.categoria = 'Grocery' THEN fv.total_vendas
            ELSE 0
        END
    ) AS grocery,
    SUM(
        CASE
            WHEN dp.categoria = 'Toys' THEN fv.total_vendas
            ELSE 0
        END
    ) AS toys
FROM d_loja dl
    JOIN f_vendas fv ON fv.sk_d_loja = dl.sk_d_loja
    JOIN d_produto dp ON fv.sk_d_produto = dp.sk_d_produto
GROUP BY dl.nome_loja;