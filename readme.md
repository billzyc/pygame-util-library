# Pygame Tools
1) Input Box

2) Text Box

3) Draw Pixel

# Pygame InputBox

## 1) import module:

place import at top of the file
"from pygame-util-library import InputBox"

## 2) create a new instance of InputBox:

"text = InputBox(40, 100, 200, 50, 'enter text here')"

parameters:
TextBox( x-position, y-position ,width, height, instruction text on of input, fontSize, input field color (optional), active input field color (optional),text color)

## 3) call "runInputBox(event)" in the mainloop and pygame.event.get() loop:

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    text.runInputBox(event)

## 4) add draw into end of main loop or draw function with window parameter

"text.draw(window)"


# Pygame TextBox

## 1) import module:

place import at top of the file
"from pygame-util-library import TextBox"

## 2) create a new instance of TextBox:

"text = InputBox(40, 100, 200, 50, 'enter text here')"

parameters:
TextBox( x-position, y-position ,width, height, text, fontSize, fontsize (optional), bgColor (optional), textColor (optional))

## 3) add draw into end of main loop or draw function with window parameter

"text.draw(window)"



# Pygame TextBox

## 1) import module:

place import at top of the file
"from pygame-util-library import drawPixel"

## 2) create a new instance of TextBox:

add to draw "drawPixel(window, x, y, color = (255,0,0))"

parameters:
drawPixel(window, x, y, color (optional)))


