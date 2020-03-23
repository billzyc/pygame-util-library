# Pygame Tools
Input Box

# Pygame InputBox

## 1) import module:

place import at top of the file
"from input_box import InputBox"

## 2) create a new instance of textbox:

"text = InputBox(40, 100, 200, 50, 'enter text here')"

parameters:
TextBox( x-position, y-position ,width, height, instruction text on of input, fontSize, input field color (optional), active input field color (optional),text color)

## 3) call "runInputBox(event)" in the mainloop and pygame.event.get() loop:

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    testTextBox.runInputBox(event)

