import pygame
import sys

# 初始化
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("技能冷却模拟器 - 寒冰射手W技能")

# 加载资源
skill_icon = pygame.image.load('images/skill_w.png').convert_alpha()
skill_rect = skill_icon.get_rect(center=(400, 300))

# 状态变量
cooldown = 8  # 冷却8秒
is_cooldown = False
start_time = 0

# 主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and not is_cooldown:
                print("技能释放！")
                is_cooldown = True
                start_time = pygame.time.get_ticks()

    # 绘制背景
    screen.fill((30, 30, 30))
    screen.blit(skill_icon, skill_rect)

    # 冷却处理
    current_time = pygame.time.get_ticks()
    if is_cooldown:
        elapsed_time = (current_time - start_time) // 1000
        if elapsed_time >= cooldown:
            is_cooldown = False
        else:
            # 绘制遮罩
            mask = pygame.Surface((96, 96), pygame.SRCALPHA)
            mask.fill((0, 0, 0, 180))
            screen.blit(mask, (skill_rect.x, skill_rect.y))
            # 绘制倒计时
            font = pygame.font.Font(None, 36)
            text = font.render(str(cooldown - elapsed_time), True, (255, 255, 255))
            text_rect = text.get_rect(center=skill_rect.center)
            screen.blit(text, text_rect)
    # 在释放技能时播放音效
    sound = pygame.mixer.Sound('sound.wav')
    sound.play()
    pygame.display.flip()

pygame.quit()
sys.exit()