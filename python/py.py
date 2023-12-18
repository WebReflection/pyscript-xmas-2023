from pyscript import window, document
from pyscript.js_modules import snow_flakes
from pyodide.ffi import create_proxy

SnowFlakes = snow_flakes.default

card = document.getElementById("card")
image = document.getElementById("image")

flakes = None

def show_flakes(event):
    global flakes
    if flakes:
        flakes.stop()

    flakes = SnowFlakes.new(card).start().write("Marry Py Xmas")

show_flakes(None)
window.addEventListener("resize", create_proxy(show_flakes))

image.style.display = "none";
