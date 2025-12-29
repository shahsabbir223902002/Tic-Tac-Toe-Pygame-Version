import pygame
import sys

pygame.init()

# ---------------- CONSTANTS ---------------- #
WIDTH, HEIGHT = 400, 500
BOARD_SIZE = 300
ROWS = COLS = 3
SQUARE_SIZE = BOARD_SIZE // 3
LINE_WIDTH = 6

TOP_MARGIN = 120
LEFT_MARGIN = (WIDTH - BOARD_SIZE) // 2

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (200, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 100, 255)
ORANGE = (255, 140, 0)

# ---------------- SCREEN ---------------- #
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic_Tac_Toe_By_SABBIR223902002")

font = pygame.font.SysFont(None, 36)
mark_font = pygame.font.SysFont(None, 80)
win_font = pygame.font.SysFont(None, 45)

# ---------------- GAME STATE ---------------- #
START_SCREEN = True
player1_name = ""
player2_name = ""
active_input = 1

board = [[0]*3 for _ in range(3)]
player = 1
game_over = False
win_line = None

# ---------------- INPUT BOXES ---------------- #
p1_box = pygame.Rect(80, 180, 240, 40)
p2_box = pygame.Rect(80, 240, 240, 40)

# ---------------- BUTTONS ---------------- #
restart_btn = pygame.Rect(20, 420, 110, 50)
newgame_btn = pygame.Rect(135, 420, 142, 50)
exit_btn = pygame.Rect(285, 420, 110, 50)

# ---------------- FUNCTIONS ---------------- #
def draw_start_screen():
    screen.fill(WHITE)
    screen.blit(font.render("Enter Player Names", True, BLACK), (90, 100))

    pygame.draw.rect(screen, BLUE if active_input == 1 else GRAY, p1_box, 2)
    pygame.draw.rect(screen, BLUE if active_input == 2 else GRAY, p2_box, 2)

    screen.blit(font.render("Player X:", True, BLACK), (80, 155))
    screen.blit(font.render("Player O:", True, BLACK), (80, 215))

    screen.blit(font.render(player1_name, True, BLACK), (90, 188))
    screen.blit(font.render(player2_name, True, BLACK), (90, 248))

    screen.blit(font.render("Press ENTER to start", True, GREEN), (90, 300))

def draw_board():
    screen.fill(WHITE)
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK,
            (LEFT_MARGIN, TOP_MARGIN + i*SQUARE_SIZE),
            (LEFT_MARGIN + BOARD_SIZE, TOP_MARGIN + i*SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, BLACK,
            (LEFT_MARGIN + i*SQUARE_SIZE, TOP_MARGIN),
            (LEFT_MARGIN + i*SQUARE_SIZE, TOP_MARGIN + BOARD_SIZE), LINE_WIDTH)

def draw_player_info():
    screen.blit(font.render(f"X: {player1_name}", True, BLACK), (20, 60))
    screen.blit(font.render(f"O: {player2_name}", True, RED), (220, 60))

def draw_marks():
    for r in range(3):
        for c in range(3):
            x = LEFT_MARGIN + c*SQUARE_SIZE + 35
            y = TOP_MARGIN + r*SQUARE_SIZE + 15
            if board[r][c] == 1:
                screen.blit(mark_font.render("X", True, BLACK), (x, y))
            elif board[r][c] == 2:
                screen.blit(mark_font.render("O", True, RED), (x, y))

def draw_buttons():
    pygame.draw.rect(screen, GREEN, restart_btn)
    pygame.draw.rect(screen, ORANGE, newgame_btn)
    pygame.draw.rect(screen, RED, exit_btn)

    screen.blit(font.render("Restart", True, WHITE), (28, 435))
    screen.blit(font.render("New Game", True, WHITE), (152, 435))
    screen.blit(font.render("Exit", True, WHITE), (300, 435))

def check_win(p):
    for i in range(3):
        if all(board[i][j] == p for j in range(3)): return ("row", i)
        if all(board[j][i] == p for j in range(3)): return ("col", i)
    if all(board[i][i] == p for i in range(3)): return ("diag", 0)
    if all(board[i][2-i] == p for i in range(3)): return ("diag", 1)
    return None

def animate_win(line_type, index):
    for i in range(0, BOARD_SIZE + 30, 20):
        draw_board()
        draw_player_info()
        draw_marks()
        draw_buttons()

        if line_type == "row":
            y = TOP_MARGIN + index*SQUARE_SIZE + SQUARE_SIZE//2
            pygame.draw.line(screen, BLUE, (LEFT_MARGIN, y), (LEFT_MARGIN+i, y), 8)
        elif line_type == "col":
            x = LEFT_MARGIN + index*SQUARE_SIZE + SQUARE_SIZE//2
            pygame.draw.line(screen, BLUE, (x, TOP_MARGIN), (x, TOP_MARGIN+i), 8)
        elif line_type == "diag":
            if index == 0:
                pygame.draw.line(screen, BLUE,
                    (LEFT_MARGIN, TOP_MARGIN),
                    (LEFT_MARGIN+i, TOP_MARGIN+i), 8)
            else:
                pygame.draw.line(screen, BLUE,
                    (LEFT_MARGIN+BOARD_SIZE, TOP_MARGIN),
                    (LEFT_MARGIN+BOARD_SIZE-i, TOP_MARGIN+i), 8)

        pygame.display.update()
        pygame.time.delay(25)

def reset_board():
    global board, player, game_over, win_line
    board = [[0]*3 for _ in range(3)]
    player = 1
    game_over = False
    win_line = None

def new_game():
    global START_SCREEN, player1_name, player2_name, active_input
    reset_board()
    player1_name = ""
    player2_name = ""
    active_input = 1
    START_SCREEN = True

# ---------------- MAIN LOOP ---------------- #
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if START_SCREEN:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if p1_box.collidepoint(event.pos): active_input = 1
                elif p2_box.collidepoint(event.pos): active_input = 2

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and player1_name and player2_name:
                    START_SCREEN = False
                elif event.key == pygame.K_BACKSPACE:
                    if active_input == 1:
                        player1_name = player1_name[:-1]
                    else:
                        player2_name = player2_name[:-1]
                else:
                    if active_input == 1 and len(player1_name) < 10:
                        player1_name += event.unicode
                    elif active_input == 2 and len(player2_name) < 10:
                        player2_name += event.unicode

        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if not game_over and LEFT_MARGIN < x < LEFT_MARGIN+BOARD_SIZE and TOP_MARGIN < y < TOP_MARGIN+BOARD_SIZE:
                    r = (y-TOP_MARGIN)//SQUARE_SIZE
                    c = (x-LEFT_MARGIN)//SQUARE_SIZE
                    if board[r][c] == 0:
                        board[r][c] = player
                        win_line = check_win(player)
                        if win_line:
                            game_over = True
                            animate_win(*win_line)
                        else:
                            player = 2 if player == 1 else 1

                if restart_btn.collidepoint(x, y):
                    reset_board()
                if newgame_btn.collidepoint(x, y):
                    new_game()
                if exit_btn.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()

    if START_SCREEN:
        draw_start_screen()
    else:
        draw_board()
        draw_player_info()
        draw_marks()
        draw_buttons()
        if game_over:
            winner = player1_name if player == 1 else player2_name
            screen.blit(win_font.render(f"{winner} Wins!", True, BLUE), (80, 20))

    pygame.display.update()
