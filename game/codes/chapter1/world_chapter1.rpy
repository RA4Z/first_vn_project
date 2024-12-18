label chapter1_introduction:
    "Hoje, como sempre, ele caminhava pelas trilhas familiares, buscando a serenidade que só a natureza podia oferecer."
    "O ar fresco e úmido do parque preencheu seus pulmões. A garoa fina, quase imperceptível, acariciava seu rosto enquanto ele caminhava sob as árvores imponentes."
    "A luz do sol poente, filtrada pela folhagem, criava um mosaico de sombras e tons dourados no chão coberto de folhas úmidas."
    "O cheiro de terra molhada e o farfalhar suave das folhas sob seus pés eram os únicos sons, criando uma atmosfera de tranquilidade quase irreal."
    "À beira da trilha, meio escondida sob a sombra de um arbusto, uma forma escura contrastava com o verde úmido da vegetação. Você parou, intrigado." 
    "O fecho de metal, embora um pouco oxidado, estava firmemente fechado. Parecia ter sido simplesmente deixada ali, esquecida sob a chuva incessante."
    "Era uma bolsa de couro marrom, pequena e desgastada, com a alça jogada sobre o corpo da bolsa. A chuva fina umedecia o couro, escurecendo-o e realçando sua textura enrugada."

    menu:
        "O fecho de metal, embora um pouco oxidado, estava firmemente fechado. Parecia ter sido simplesmente deixada ali, esquecida sob a chuva incessante."
        "Verificar a bolsa":
            call chapter1_bolsa

        "Ignorar e voltar à caminhada":
            "Você ignorou a bolsa e retornou à sua caminhada"

    jump chapter1_grito


label chapter1_grito:
    "Um grito dilacerante corta o ar, carregado de dor e desespero. É um som humano, cru e visceral, que te faz estremecer."
    "Os pássaros, que cantavam até então, emudecem instantaneamente."

    menu:
        "O grito ecoa entre as árvores, vindo de algum lugar além da trilha, e se extingue abruptamente, deixando um silêncio pesado e opressivo."
        "Seguir em direção ao grito":
            jump chapter1_seguir_grito

        "Seguir o caminho que estava indo":
            "bla bla bla"   # ESPERAR AVANÇO NO FLUXOGRAMA

        "Voltar de onde veio":
            "De forma rápida, você volta de onde estava vindo"  # ESPERAR AVANÇO NO FLUXOGRAMA


label chapter1_seguir_grito:
    "Você se embrenha na mata, seguindo na direção do grito. As árvores se fecham ao seu redor como uma parede verde-escura, bloqueando a pouca luz que ainda filtrava pelas folhas."
    "O ar, denso, úmido e frio, carrega o cheiro de terra molhada e folhas em decomposição"

    menu:
        "A trilha some sob o tapete espesso de folhas e galhos úmidos. O silêncio é absoluto, quebrado apenas pelo som da sua própria respiração e o farfalhar das folhas sob seus pés."
        "Seguir o caminho silenciosamente":
            jump chapter1_encontro_assassino

        "Chamar a pessoa que estava gritando":
            "bla bla bla"   # ESPERAR AVANÇO NO FLUXOGRAMA


label chapter1_encontro_assassino:
    "Você decide prosseguir em silêncio, tentando não fazer barulho."
    "Você avança lentamente, os sentidos em alerta. O ar está pesado, carregado de um odor metálico que te faz prender a respiração. "
    "Através da densa folhagem, você vislumbra uma clareira. O chão está escuro, lamacento. No centro, uma figura curvada sobre algo que você não consegue distinguir. Um brilho metálico pisca na penumbra."
    "Você se aproxima mais alguns passos, o coração batendo forte no peito. O odor metálico se intensifica, misturando-se ao cheiro de terra molhada e algo mais... algo doce e enjoativo."
    "Então, você vê. Um homem ajoelhado sobre o corpo de uma mulher. A lâmina em sua mão, longa e afiada, reflete a luz fraca que atravessa as árvores."
    "O som úmido e ritmado da carne sendo cortada te causa náuseas. As roupas da mulher, encharcadas de um vermelho escuro, quase se confundem com a terra úmida."
    "Você recua instintivamente, um passo silencioso para trás. Suas mãos tremem. A respiração fica presa na garganta. O homem, alheio à sua presença, continua seu trabalho macabro."
    "A postura do homem impede que você veja seu rosto. Mas você nota um movimento quase imperceptível – uma leve inclinação da cabeça, um sorriso cruel que se insinua no canto de seus lábios."

    menu:
        "Ele parece estar imerso em um ritual macabro, alheio ao mundo ao seu redor."
        "Atacar":
            jump chapter1_atacar    # MORTE

        "Recuar":
            "Você dá um passo para trás, com cuidado para não fazer barulho. Mas o peso do seu corpo faz um galho seco estalar sob seu pé. O som ressoa alto no silêncio da mata."
            jump chapter1_encarar

        "Desmaiar":
            jump chapter1_desmaiar  # MORTE

        "Gritar":
            "O grito escapa de sua garganta antes que você consiga detê-lo, ecoando alto e claro pelo bosque. Por um breve momento, o som parece congelar o tempo."
            jump chapter1_encarar

        "Se Esconder":
            "bla bla bla"   # ESPERAR AVANÇO NO FLUXOGRAMA

    return

label chapter1_encarar:
    "O assassino, que estava absorto em seu macabro \"trabalho\", interrompe o movimento da lâmina e ergue a cabeça lentamente, como um animal que detecta um predador."
    "Ele para por um segundo, os ombros tensos, e vira a cabeça na sua direção. Você vê o momento exato em que ele percebe sua presença. Não há dúvida; ele te viu."
    "O sorriso que antes curvava seus lábios se desmancha, substituído por uma expressão fria e predatória."
    
    menu:
        "Ele se ergue devagar, a faca pingando sangue em sua mão firme. Cada passo que ele dá em sua direção é medido, metódico, como um caçador encurralando sua presa."
        "Correr":
            jump chapter1_correr

        "Se esconder atrás de uma árvore":
            jump chapter1_esconder_atras_arvore  # MORTE
        
        "Ficar Imóvel":
            jump chapter1_ficar_imovel  # MORTE
        
        "Implorar":
            jump chapter1_implorar      # MORTE


label chapter1_correr:
    "Seus pés se movem antes mesmo de sua mente compreender completamente o que está fazendo."
    "O som das folhas secas e galhos quebrando sob seus passos reverbera pelo ar, ecoando mais alto do que você gostaria."
    "Atrás de você, o homem reage ao movimento, uma mudança sutil em sua postura que revela que ele agora está focado em você."
    "A adrenalina domina seu corpo, impulsionando seus movimentos. O bosque que antes parecia um refúgio agora se transforma em um labirinto sufocante."
    "Cada tronco e cada sombra parecem querer barrar sua fuga, enquanto os sons atrás de você se tornam mais claros  — passos firmes, constantes, metódicos."
    "Ele não corre como você, mas avança com uma confiança perturbadora, como se já tivesse decidido o desfecho dessa perseguição."
    "A trilha começa a desaparecer à medida que você avança, e a vegetação mais densa obriga decisões rápidas."
    "Cada escolha parece um divisor de águas, com o instinto de sobrevivência guiando cada passo enquanto o perseguidor implacável se mantém em seu encalço."
    "A trilha estreita se fecha à frente, e uma árvore caída bloqueia o caminho como um obstáculo natural."
    "O tronco é grosso, coberto de musgo, e galhos quebrados se espalham ao redor, tornando difícil saber por onde passar."
    
    menu:
        "Os passos atrás de você soam mais próximos, forçando uma decisão rápida."
        "Pular por cima da árvore":
            "bla bla bla"   # ESPERAR AVANÇO NO FLUXOGRAMA

        "Desviar pelo lado":
            "bla bla bla"   # ESPERAR AVANÇO NO FLUXOGRAMA

