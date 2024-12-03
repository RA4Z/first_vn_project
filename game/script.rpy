label start:
    $ texto_do_jogador = renpy.input("Escolha o nome do protagonista", default='Gabriel')
    $ player_name = Character(texto_do_jogador)
    $ player = Player(texto_do_jogador)

    "[player.nome] sempre valorizou o silêncio. Não o tipo desconfortável que paira entre estranhos, mas aquele que só a natureza pode oferecer."
    "Era um homem comum, introvertido por escolha, que encontrava na solitude sua verdadeira paz."
    "Como designer gráfico freelancer, passava longas horas diante da tela do computador, entre prazos apertados e clientes exigentes."
    "Mas quando a pressão do trabalho se tornava insuportável, ele tinha um refúgio: o parque."
    call chapter1_introduction from _call_chapter1_introduction

    if player.condicoes.vivo:   # Verificar se o jogador está vivo para continuar a história
        "Bem-vindo ao capítulo 2"

    "Obrigado por jogar nosso jogo, [player.nome]!"
    return
