def ramji():
    import pygame
    import time
    from colorama import Fore, Style, init

    init(autoreset=True)

    lyrics = [
        "तन मोरा राम, मन मोरा राम..........",
        "तन मोरा राम, मन मोरा राम",
        "मोरा कण कण हो..., राम ही राम........",
        "राम ही पार लगावेंगे"
    ]

    delays = [1,.80,0.5,1]

    pygame.mixer.init()
    pygame.mixer.music.load("ram.mp3")
    pygame.mixer.music.play()

    time.sleep(1)

    for i, line in enumerate(lyrics):

        for char in line:
            print(Fore.YELLOW + char, end='', flush=True)
            time.sleep(0.12)

        time.sleep(delays[i])
        print(Style.RESET_ALL)

ramji()
