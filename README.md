# PyScript Xmas Card

To run this demo simply clone this folder and, once entered into it, type `python3 -m http.server` to then reach [http://0.0.0.0:8080/](http://0.0.0.0:8080/) and enjoy the snow over an Xmas wish!

To test in a worker use correct headers or try `npx static-handler --port 8000 --coi .` instead.

## How does it work?

  * to change picture (*mpy* only) click the input and chose any picture you like from your hard drive
  * to see the result in a different layout (size) just change your browser's window size
  * to test *mpy* VS *py* change the `index.html` file so that `TYPE` points at **py** instead of **mpy**
    * if your card is live feel free to also change the `config/remote.toml` to point at such live location

To change the default image simply replace the `assets/snow.jpg` with your own Xmas image and spread the wishes all over 🎄

## Credits

  * the **MerryChristmasFlake** *CSS font* is under the [dafont](https://www.dafont.com/merry-christmas.font) license constraints
  * the **snow** effect has been fully rewritten from [this codepen](https://codepen.io/oklai/pen/njQVxV) to change the following:
    * the width and height are not browser size dependent (canvas size dependent in here)
    * there is no need to loop each flake twice (updates within the same loop)
    * both flakes and logic are classes (for portability and simplicity sake)
    * there is a resize event that updates the logic (no stretches over resizes)
    * most operations have been optimized for speed and logic (most operations are more accurate)
    * a text, if provided, is drawn underneath the flaks
    * `requestAnimationFrame` has been used for a smoother "snow storm"

About the latest credit, it's still not clear the real source of the *sin* / *cos* update, or the heuristic to have a more snow-ish effect while flakes are disappearing, so that any credits are left to the original publisher of the very same logic that many out there are using to replicate this lovely effect based on an incremental, forever waving, angle.

## Goal

This demo is to simply demonstrate how latest `js_modules` works in *PyScript*. The demo simply uses a main world JS library (created ad-hoc for this use case, but any other use case would do) from either `py` or an `mpy` tag, where the latter shows roughly instantly without any delay in the making.

See the [**live demo**](https://webreflection.github.io/pyscript-xmas-2023/) to understand what this is all about.
