label chapter1_bolsa:
    $ player.condicoes.digitais_criminosas = True
    $ escolhas_feitas = 0  # Variável para controlar o número de escolhas
    $ opcoes_escolhidas = []  # Lista para registrar opções já escolhidas

    "Algo naquela bolsa te chama a atenção. Você se aproxima, a curiosidade pulsando em suas veias, e a pega."
    "Você pega a bolsa. O couro, frio e úmido, se molda à sua mão. Sente o peso suave do conteúdo, algo que não parece corresponder à aparência surrada da bolsa."
    "A textura do couro, lisa em alguns pontos e áspera em outros, revela anos de uso. Um leve aroma de couro e um vestígio de perfume feminino se misturam ao cheiro da chuva."
    "O fecho metálico, resistente à primeira tentativa, cede com um clique suave."
    "Você abre a bolsa e vê uma carteira de couro sintético, alguns papéis já manchados e borrados pela garoa, e um celular moderno, aparentemente desligado."

    while escolhas_feitas < 2:  # Enquanto o jogador não fizer duas escolhas
        menu:
            "Pegar os papéis" if "papéis" not in opcoes_escolhidas:
                $ opcoes_escolhidas.append("papéis")
                $ escolhas_feitas += 1
                "Você pega os papéis com cuidado. Estão úmidos e frios ao toque, grudando uns nos outros."
                "Ao tentar desdobrá-los, eles se rasgam e se desfazem nas suas mãos, a tinta borrando e tornando as palavras ilegíveis"
                "Uma onda de frustração te invade. A chuva destruiu qualquer informação útil que eles pudessem conter."

            "Pegar a carteira" if "carteira" not in opcoes_escolhidas:
                $ opcoes_escolhidas.append("carteira")
                $ player.item_chave.carteira = True
                $ player.pistas.nome_vitima_parque = True
                $ escolhas_feitas += 1
                "Você pega a carteira. O couro sintético, frio e úmido, está um pouco pegajoso ao toque."
                "Abrindo-a, você encontra uma identidade parcialmente borrada pela chuva."
                "O nome \"Julia Lynder\" ainda é legível, mas a foto está quase apagada, mostrando apenas o contorno borrado de um rosto jovem, possivelmente na casa dos 20 anos."
                "Algumas cédulas dobradas, úmidas e amassadas, completam o conteúdo da carteira."

            "Pegar o celular" if "celular" not in opcoes_escolhidas:
                $ opcoes_escolhidas.append("celular")
                $ player.item_chave.celular = True
                $ escolhas_feitas += 1
                "Você pega o celular. O metal frio e liso do aparelho contrasta com a textura úmida da bolsa. A tela está escura, refletindo vagamente o céu nublado."
                "Você pressiona o botão de ligar. Nada. Tenta novamente, segurando o botão por mais tempo. Silêncio. Sem bateria."
                if "carteira" in opcoes_escolhidas:
                    "Uma onda de frustração te percorre. O celular, que poderia conter alguma pista sobre o paradeiro de Julia Lynder, é inútil."

    return
