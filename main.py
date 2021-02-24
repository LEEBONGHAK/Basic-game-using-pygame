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

# 프로그램이 종료되지 않도록 대기하도록 만듬
# 이벤트 루프
running = True  # 게임이 진행중인가?
while running:
    for event in pygame.event.get():
        # pygame을 쓰는데 무조건 필요 / 프로그램이 종료되지 않게하며 사용자의 동작을 확인
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트 발생?
            running = False  # 게임이 진행중이 아님

    # screen.fill((0, 0, 255)) # RGB를 이용해 배경 넣기
    screen.blit(background, (0, 0))  # 해당하는 좌표에 배경 그리기

    pygame.display.update()  # 게임 화면 다시 그리기
    # pygame에서는 매 프레임 마다 화면을 다시 그려줘야 하기 때문에

# pygame 종료
pygame.quit()
