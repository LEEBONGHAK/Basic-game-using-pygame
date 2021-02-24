import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Bong Hak Game")  # 게임 이름

# FPS (frame per second)
clock = pygame.time.Clock()

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

# 캐릭터 이동 속도
character_speed = 0.6

# 적 enemy 캐릭터
enemy = pygame.image.load(
    "C:/Users/이봉학/Desktop/코딩/python 나도코딩/pygame/Basic-game-using-pygame/images/enemy.png")
enemy_size = enemy.get_rect().size  # 이미지의 크기를 구해옴
enemy_width = enemy_size[0]  # 캐릭터의 가로 크기
enemy_height = enemy_size[1]  # 캐릭터의 세로 크기
enemy_x_pos = screen_width / 2 - enemy_width / \
    2  # 화면 가로의 절반 크기에 해당하는 곳에 위치(가로)
enemy_y_pos = screen_height / 2 - enemy_height / \
    2  # 화면 세로의 절반 크기에 해당하는 곳에 위치(세로)

# 폰트 정의
game_font = pygame.font.Font(None, 40)  # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks()  # 시작 tick 을 받아옴

# 프로그램이 종료되지 않도록 대기하도록 만듬
# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(60)  # 게임화면의 초당 프레임 수 설정

    # 캐릭터가 1초 동안 100 만큼 이동을 해야함
    # 10 fps : 1초 동안 10번 동작 -> 1번에 몇 만큼 이동? 10만큼! 10 * 10 = 100
    # 20 fps : 1초 동안 20번 동작 -> 1번에 몇 만큼 이동? 5만큼! 5 * 20 = 100

    # print("fps : " + str(clock.get_fps())) # 설정된 프레임 확인

    for event in pygame.event.get():
        # pygame을 쓰는데 무조건 필요 / 프로그램이 종료되지 않게하며 사용자의 동작을 확인
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트 발생?
            running = False  # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            # 눌러졌다면 각 방향으로 character speed만큼 이동
            if event.key == pygame.K_LEFT:
                to_x_left -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x_right += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:  # 방향키 떼면 멈춤
            if event.key == pygame.K_LEFT:
                to_x_left = 0
            elif event.key == pygame.K_RIGHT:
                to_x_right = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += (to_x_left + to_x_right) * \
        dt  # 프레임이 변화해도 속도를 일정하게 만들어 주기 위해서
    character_y_pos += to_y * dt  # 프레임이 변화해도 속도를 일정하게 만들어 주기 위해서

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

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()  # 위치가 변화하여도 자체 이미지의 rect 정보는 바뀌지 않았음
    character_rect.left = character_x_pos  # 실제 위치의 rect 정보로 업데이트 해줌
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌 했어요")
        running = False

    # screen.fill((0, 0, 255)) # RGB를 이용해 배경 넣기
    screen.blit(background, (0, 0))  # 해당하는 좌표에 배경 그리기

    # 캐릭터 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    # 적 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # ms 기준임 / 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시

    timer = game_font.render(
        str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 출력할 글자, True, 글자 색상(RGB)
    screen.blit(timer, (10, 10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임 아웃")
        running = False

    pygame.display.update()  # 게임 화면 다시 그리기
    # pygame에서는 매 프레임 마다 화면을 다시 그려줘야 하기 때문에

# 잠시 대기
pygame.time.delay(2000)  # 2초 정도 대기(ms)

# pygame 종료
pygame.quit()
