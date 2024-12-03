label chapter1_bolsa:
    $ player.condicoes.digitais_criminosas = True
    $ escolhas_feitas = 0  # Variável para controlar o número de escolhas
    $ opcoes_escolhidas = []  # Lista para registrar opções já escolhidas

    "A bolsa estava levemente úmida ao toque, com o couro desgastado."
    "Ao abri-la, você encontra um interior simples: uma carteira, papéis manchados de garoa e, no fundo, um celular."

    while escolhas_feitas < 2:  # Enquanto o jogador não fizer duas escolhas
        menu:
            "Pegar os papéis" if "papéis" not in opcoes_escolhidas:
                $ opcoes_escolhidas.append("papéis")
                $ escolhas_feitas += 1
                "Você pega os papéis com cuidado, mas eles estão úmidos e frágeis."
                "Assim que tenta desdobrá-los, eles começam a se desfazer em pedaços."
                "As palavras restantes são completamente ilegíveis,"
                "Deixando você apenas com resíduos em suas mãos."

            "Pegar a carteira" if "carteira" not in opcoes_escolhidas:
                $ opcoes_escolhidas.append("carteira")
                $ player.item_chave.carteira = True
                $ player.pistas.nome_vitima_parque = True
                $ escolhas_feitas += 1
                "Uma carteira de couro escuro, bem usada, mas ainda firme."
                "Ao abrir, percebe que contém uma identidade parcialmente borrada e cédulas dobradas."
                "Você consegue ver nome \"Julia Lynder\" mas a foto está um pouco borrada e difícil de identificar"
                "Mas o documento sugere que pertence a alguém jovem, talvez na casa dos 20 anos."

            "Pegar o celular" if "celular" not in opcoes_escolhidas:
                $ opcoes_escolhidas.append("celular")
                $ player.item_chave.celular = True
                $ escolhas_feitas += 1
                "Você pega o celular, percebendo que ele está limpo, mas desligado."
                "Tentando pressionar o botão de energia, descobre que a bateria está completamente descarregada."
                "Não há sinais aparentes de danos, mas o aparelho não oferece qualquer resposta."

    return
