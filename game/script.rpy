label start:
    $ texto_do_jogador = renpy.input("Escolha o nome do protagonista", default='Gabriel')
    $ player_name = Character(texto_do_jogador)
    $ player = Player(texto_do_jogador)

    "O zumbido constante da tela do computador era a trilha sonora da vida de [player.nome]. Designer gráfico freelancer, ele se afogava em prazos apertados e clientes exigentes."
    "A interação humana era um fardo, um teatro de máscaras que ele evitava sempre que possível."
    "Sua verdadeira paz estava no silêncio sussurrante das árvores do parque, seu único refúgio."
    call chapter1_introduction

    if player.condicoes.vivo:   # Verificar se o jogador está vivo para continuar a história
        "Bem-vindo ao capítulo 2"

    "Obrigado por jogar nosso jogo, [player.nome]!"
    return
