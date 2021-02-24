import pygame

pygame.init()  # 초기화 (반드시 필요)

# 화면크기 설정
screen_width = 480  # 가로 크기
screen_height = 640  # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Bong Hak Game")  # 게임 이름

# 프로그램이 종료되지 않도록 대기하도록 만듬
# 이벤트 루프
running = True
while running:
    for event in pygame.event.get():
        # pygame을 쓰는데 무조건 필요 / 프로그램이 종료되지 않게하며 사용자의 동작을 확인
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트 발생?
            running == False  # 게임 종료


# pygame 종료
pygame.quit()
