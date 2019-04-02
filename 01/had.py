import pyglet
window = pyglet.window.Window()

label = pyglet.text.Label('Ahoj!', x=100, y=200)
snake = [(1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5)]

food = [(2, 0), (5, 1), (1, 4)]

TILE_SIZE = 64

green = pyglet.image.load('green.png')
apple = pyglet.image.load('apple.png')
left_bottom = pyglet.image.load('snake-tiles/left-bottom.png')

tile= {}
for start in ['bottom', 'end', 'left', 'right', 'top']:
    for end in ['bottom', 'dead', 'end', 'left', 'right', 'tongue', 'top']:
        image = pyglet.image.load('snake-tiles/' + start + '-' + 'end' + '.png' )
        tiles[start, end] = image
print(tiles)

@window.event
def on_text(text):
    print(text)
    print(label.x)
    label.x = 20
    label.text = label.text + text


@window.event
def on_key_press(key_code, modifier):
    print(key_code)
    if key_code == pyglet.window.key.BACKSPACE:
        label.text = label.text[:-1]

@window.event
def on_draw():
    window.clear()
    label.draw()
    for x, y in snake:
        green.blit(
        x * TILE_SIZE, y * TILE_SIZE,
        width=TILE_SIZE, height=TILE_SIZE,
        )
    for x, y in food:
        apple.blit(
        x * TILE_SIZE, y * TILE_SIZE,
        width=TILE_SIZE, height=TILE_SIZE,
        )

pyglet.app.run()
