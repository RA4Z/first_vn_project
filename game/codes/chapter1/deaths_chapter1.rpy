label chapter1_atacar:
    "Cautelosamente você se aproxima dele para tentar atacá-lo"
    "Conforme você se aproxima dele, a tensão aumenta"
    "Você está tão concentrado na figura à sua frente que se distrai do mundo à sua volta"
    "Que acaba por tropeçar em um buraco no chão, torcendo o tornozelo e fazendo um barulho"
    "Lentamente ele olha em sua direção e sorri"
    "Ele se aproxima de você com uma faca grande nas mãos"
    "Você percebe que esse é o fim de sua vida"
    $ player.condicoes.vivo = False
    return

label chapter1_esconder_atras_arvore:
    "Você corre rapidamente até a árvore mais próxima, pressionando-se contra o tronco enquanto tenta se manter o mais quieto possível."
    "Cada passo do assassino é agora mais próximo, seus pés esmagando a vegetação com uma precisão calma."
    "Você segura a respiração, tentando controlar a aceleração do coração, mas sabe que ele já o viu."
    "Os passos do assassino desaceleram, como se ele estivesse avaliando o espaço ao redor, decidindo com precisão onde procurar."
    "Ele para a poucos metros de onde você se esconde, e você consegue ouvir seu movimento mais uma vez, agora com mais atenção."
    "Ele começa a se aproximar da árvore, os olhos fixos em sua direção."
    "O sorriso cruel que se forma em seu rosto é o último sinal de que sua tentativa de fuga foi em vão."
    $ player.condicoes.vivo = False
    return

label chapter1_ficar_imovel:
    "O som de passos ecoa em sua direção, cada vez mais próximo."
    "Você permanece completamente imóvel, tentando não fazer um único movimento, sem emitir um som"
    "Talvez, se não fizer nenhum som, ele desista."
    "O silêncio é absoluto, e você sente o tempo se arrastar, cada segundo se tornando mais longo."
    "O assassino olha ao redor, seus olhos percorrendo as árvores com precisão."
    "Ele finalmente se volta, fixando os olhos em você."
    "O sorriso que surge em seu rosto é lento e cruel, como se estivesse se divertindo com a cena."
    "Ele dá um passo final em sua direção, e a lâmina brilha enquanto o golpe vem sem aviso."
    $ player.condicoes.vivo = False
    return

label chapter1_implorar:
    "As palavras escapam de sua boca antes que você consiga controlá-las."
    player_name "Por favor, não..."
    "Sua voz soa tremida, quase engasgada"
    "Enquanto o assassino continua avançando, sua expressão tão imutável quanto uma máscara de mármore."
    "Ele para a poucos passos de distância, inclinando a cabeça como se estivesse avaliando sua súplica"
    "Por um momento, o silêncio é ensurdecedor, e uma centelha de esperança se insinua"
    "Mas logo é esmagada.\nSem uma palavra, ele ergue a lâmina, e o brilho frio do aço é a última coisa que você vê."
    $ player.condicoes.vivo = False
    return
