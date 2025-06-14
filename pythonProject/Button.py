# class Button:
#     def __init__(self, x, y, width, height, text, function):
#         self.rect = pygame.Rect(x, y, width, height)
#         self.text = text
#         self.function = function
#
#     def draw(self, screen):
#         pygame.draw.rect(screen, (100, 100, 100), self.rect)
#         font = pygame.font.SysFont(None, 36)
#         text_surf = font.render(self.text, True, (255, 255, 255))
#         screen.blit(text_surf, (self.rect.x + 10, self.rect.y + 10))
#
#     def handle_click(self, pos):
#         if self.rect.collidepoint(pos):
#             if self.function:
#                 self.function()