import pygame
import sys

# 初始化Pygame
pygame.init()

# 设置屏幕尺寸
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("用Radius参数画一只羊")


# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# 定义半径参数
Radius = 50

# 设置背景颜色
screen.fill(WHITE)




# 绘制羊的身体（椭圆，用半径来控制大小）
body_width = 3 * Radius
body_height = 2 * Radius
pygame.draw.ellipse(screen, BLACK, [200 - body_width // 2, 200 - body_height // 2, body_width, body_height], 3)

# 绘制羊的头部（圆）
head_radius = Radius // 2
pygame.draw.circle(screen, BLACK, (200 + body_width // 2 - head_radius, 200 - head_radius), head_radius, 3)

# 绘制羊的眼睛（两个小圆）
eye_radius = Radius // 8
pygame.draw.circle(screen, BLACK, (200 + body_width // 2 - head_radius - eye_radius, 200 - head_radius // 2), eye_radius)
pygame.draw.circle(screen, BLACK, (200 + body_width // 2 - head_radius + eye_radius, 200 - head_radius // 2), eye_radius)

# 绘制羊的耳朵（两个小椭圆）
ear_width = Radius // 3
ear_height = Radius // 2
pygame.draw.ellipse(screen, BLACK, [200 + body_width // 2 - head_radius - ear_width, 200 - head_radius, ear_width, ear_height], 3)
pygame.draw.ellipse(screen, BLACK, [200 + body_width // 2 - head_radius, 200 - head_radius, ear_width, ear_height], 3)

# 绘制羊的腿（矩形）
leg_width = Radius // 4
leg_height = Radius // 2
pygame.draw.rect(screen, BLACK, [200 - body_width // 4 - leg_width // 2, 200 + body_height // 2 - 5, leg_width, leg_height])
pygame.draw.rect(screen, BLACK, [200 + body_width // 4 - leg_width // 2, 200 + body_height // 2 - 5, leg_width, leg_height])

# 刷新屏幕以显示图像
pygame.display.flip()

# 退出事件处理
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
