
# ========================================== MAIN LOOP ========================================================================

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen = Screen(screen)
pygame.display.set_caption(TITLE)

while True:
    # На hub баг, который хранит все предыдущие нажатия клавиш, и из-за этого некоторые евенты
    # происходят больше 1 раза. Временный фикс
    happend = [False, False, False, False]
    dt = pygame.time.get_ticks() / 1000 - clock.t
    clock.tick(dt)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN or pygame.mouse.istouchin():
            if not happend[0]:
                on_mouse_down(pygame.mouse.get_pressed(), pos)
                happend[0] = True

        if event.type == pygame.MOUSEMOTION:
            on_mouse_move(pos)

        if event.type == pygame.MOUSEBUTTONUP:
            if not happend[1]:
                on_mouse_up(event.button, pos)
                happend[1] = True

        if event.type == pygame.KEYDOWN:
            keyboard._press(event.key)
            if not happend[2]:
                on_key_down(event.key)
                happend[2] = True

        if event.type == pygame.KEYUP:
            keyboard._release(event.key)
            if not happend[3]:
                on_key_up(event.key)
                happend[3] = True

    update(dt)
    draw()
    pygame.display.update()
    clock_pg.tick(FPS)