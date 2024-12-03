label chapter1_introduction:
    "O parque era um recanto de tranquilidade, envolvido por árvores altas que filtravam a luz do final da tarde em suaves tons dourados."
    "Uma garoa leve caía, quase imperceptível, criando um brilho delicado nas folhas e no chão coberto por um tapete de tons outonais."
    "O som distante de pássaros e o farfalhar das folhas eram os únicos ruídos, e os caminhos serpenteavam calmamente pela vegetação densa, convidando à exploração."
    "Tudo parecia sereno, como se o parque tivesse sido feito para momentos como esse — de completa solitude e paz."
    "Enquanto caminhava, seus olhos captaram algo fora do lugar: uma bolsa caída ao lado do caminho, próxima a um arbusto."

    menu:
        "Era uma peça de couro, marrom e desgastada, como algo que já tivesse sido usado por anos."
        "Verificar a bolsa":
            call chapter1_bolsa

        "Ignorar e voltar à caminhada":
            "Você ignorou a bolsa e retornou à sua caminhada"

    jump chapter1_grito
    return


label chapter1_grito:
    "De repente, um grito agudo rompe o ar, tão alto e inesperado que faz você parar imediatamente."
    "Ele ecoa pelas árvores como um alerta, carregado de medo e desespero."
    "Os pássaros, que antes pareciam responder ao vento, ficam em silêncio."
    "Seus olhos se voltam instintivamente para o som, vindo de um trecho mais denso da mata"
    "Onde as árvores crescem próximas umas das outras, criando um emaranhado de sombras e folhas."
    menu:
        "Seguir em direção ao grito":
            jump chapter1_seguir_grito

        "Seguir o caminho que estava indo":
            "bla bla bla"   # ESPERAR AVANÇO NO FLUXOGRAMA

        "Voltar de onde veio":
            "De forma rápida, você volta de onde estava vindo"  # ESPERAR AVANÇO NO FLUXOGRAMA


label chapter1_seguir_grito:
    "Você toma a decisão de seguir o som, atravessando a trilha que leva à área mais densa da mata."
    "As árvores se fecham ao seu redor, tornando o ambiente mais escuro e o caminho menos visível."
    "Cada passo sobre a folhagem molhada soa alto no silêncio."
    menu:
        "Seguir o caminho silenciosamente":
            jump chapter1_encontro_assassino

        "Chamar a pessoa que estava gritando":
            "bla bla bla"   # ESPERAR AVANÇO NO FLUXOGRAMA


label chapter1_encontro_assassino:
    "Entre as árvores, uma pequena clareira surge."
    "O chão ali parece mais escuro, quase encharcado."
    "No centro, um homem está ajoelhado, o corpo inclinado sobre algo"
    "A lâmina em sua mão reflete um brilho pálido, os movimentos precisos, cortantes, repetidos com uma cadência que beira o ritual."
    "O ar parece mais denso aqui, carregado por um odor metálico que não deixa dúvidas sobre o que está acontecendo."
    "O corpo de uma mulher está estendido, as roupas encharcadas de vermelho, quase indistinguíveis na terra úmida."
    "O silêncio que acompanha os movimentos do homem é quebrado apenas pelo som macabro de carne sendo cortada, úmido e abafado"
    "O homem, alto e de ombros largos, usa roupas simples e escuras."
    "Sua postura bloqueia uma visão clara de seu rosto, mas há um movimento inquietante"
    "Uma leve inclinação da cabeça, seguida por um sorriso quase imperceptível."
    "Ele parece estar contemplando sua obra, como um artista diante de uma pintura finalizada."
    menu:
        "Atacar":
            jump chapter1_atacar    # MORTE

        "Recuar":
            "Você dá um passo para trás, com cuidado para não fazer barulho"
            "Mas o galho seco sob seus pés decide o contrário. Um estalo seco ressoa no silêncio do bosque."
            jump chapter1_encarar

        "Desmaiar":
            "bla bla bla"   # ESPERAR AVANÇO NO FLUXOGRAMA

        "Gritar":
            jump chapter1_encarar

        "Se Esconder":
            "bla bla bla"   # ESPERAR AVANÇO NO FLUXOGRAMA

    return

label chapter1_encarar:
    "O assassino para imediatamente, seus movimentos interrompidos no meio do ato."
    "Sua cabeça se ergue lentamente, como a de um predador captando um som distante."
    "Ele vira em sua direção, seus olhos fixos no lugar de onde ouviu o barulho."
    "Sem pressa, ele larga o que está segurando e se endireita."
    "Sua postura relaxada contrasta com o brilho afiado em sua mão."
    "Ele dá o primeiro passo na sua direção, os pés esmagando a vegetação com uma calma inquietante, como se tivesse todo o tempo do mundo."
    menu:
        "Correr":
            "bla bla bla"   # ESPERAR AVANÇO NO FLUXOGRAMA

        "Se esconder atrás de uma árvore":
            jump chapter1_esconder_atras_arvore
        
        "Ficar Imóvel":
            jump chapter1_ficar_imovel  # MORTE
        
        "Implorar":
            jump chapter1_implorar      # MORTE
