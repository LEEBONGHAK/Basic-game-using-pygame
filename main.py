import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Bong Hak Game")  # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load(
    "C:/Users/이봉학/Desktop/코딩/python 나도코딩/pygame/Basic-game-using-pygame/images/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(
    "C:\\Users\\이봉학\\Desktop\\코딩\\python 나도코딩\\pygame\\Basic-game-using-pygame\\images\\character.png")
character_size = character.get_rect().size  # 이미지의 크기 구하기
character_width = character_size[0]  # 캐릭터의 가로 크기
character_height = character_size[1]  # 캐릭터의 세로 크기
character_x_pos = screen_width / 2 - \
    character_width / 2  # 화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
character_y_pos = screen_height - \
    character_height  # 화면 세로 크기 가장 아래에 해당하느 곳에 위치(세로)

# 캐릭터가 이동할 좌표
to_x_left = 0
to_x_right = 0
to_y = 0

# 프로그램이 종료되지 않도록 대기하도록 만듬
# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():
        # pygame을 쓰는데 무조건 필요 / 프로그램이 종료되지 않게하며 사용자의 동작을 확인
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트 발생?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            # 눌러졌다면 각 방향으로 5px씩 이동
            if event.key == pygame.K_LEFT:
                to_x_left -= 5
            elif event.key == pygame.K_RIGHT:
                to_x_right += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_DOWN:
                to_y += 5

        if event.type == pygame.KEYUP:  # 방향키 때면 멈춤
            if event.key == pygame.K_LEFT:
                to_x_left = 0
            elif event.key == pygame.K_RIGHT:
                to_x_right = 0
            elif event.key == pygame.K_UP or event.type == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x_left + to_x_right
    character_y_pos += to_y

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # screen.fill((0, 0, 255)) # RGB를 이용해 배경 넣기
    screen.blit(background, (0, 0))  # 해당하는 좌표에 배경 그리기

    # 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()  # 게임 화면 다시 그리기
    # pygame에서는 매 프레임 마다 화면을 다시 그려줘야 하기 때문에

# pygame 종료
pygame.quit()
