
class ClickButton:
    def __init__(
        self,
        x,
        y,
        width,
        height,
        promptText="",
        fontSize=20,
        bgColor=(255, 255, 255),
        textColor=(0, 0, 0),
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.fontSize = fontSize
        self.bgColor = bgColor
        self.textColor = textColor
        self.promptText = promptText
        self.font = pygame.font.SysFont("arial", 15)

    def draw(self, window):
        self.image.fill(self.bgColor)
        window.blit(self.image, (self.x, self.y))
        if self.promptText:
            instructions = self.font.render(self.promptText, 1, self.textColor)
            window.blit(
                instructions, (self.x, self.y - round(self.y / 50) - self.fontSize)
            )

    def runInputBox(self, event, action):
        if event.type == pygame.MOUSEBUTTONDOWN and self.checkClicked(
            pygame.mouse.get_pos()
        ):
            action()

    def checkClicked(self, clickedPos):
        if clickedPos[0] > self.x and clickedPos[0] < self.x + self.width:
            if clickedPos[1] > self.y and clickedPos[1] < self.y + self.height:
                return True
        return False
