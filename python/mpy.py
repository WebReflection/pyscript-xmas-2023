from pyscript import window, document
from pyscript.js_modules import snow_flakes

SnowFlakes = snow_flakes.default

card = document.getElementById("card")
image = document.getElementById("image")

flakes = None

def show_flakes(event):
    global flakes
    if flakes:
        flakes.stop()

    flakes = SnowFlakes.new(card).start().write("Marry Mpy Xmas")

show_flakes(None)
window.addEventListener("resize", show_flakes)

def change_background(event):
    files = event.target.files
    if files:
        # note: won't work via worker
        bg = window.URL.createObjectURL(files[0])
        card.style.backgroundImage = f"url({bg})"

image.addEventListener("change", change_background)
