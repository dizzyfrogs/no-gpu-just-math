# no-gpu-just-math

A spinning 3D wireframe cube rendered in your terminal, with no graphics library and no GPU. Just matrix math and ASCII characters.

Pure Python, standard library only.

## Running it

```bash
python main.py
```

Needs a terminal that supports ANSI escape codes (most do). Press `Ctrl+C` to quit.

## Files

| File | What it does |
| --- | --- |
| `linalg.py` | `Vec3` and `Mat4` implementation. Rotation, translation, and perspective matrices |
| `screen.py` | An ASCII framebuffer: clear, draw lines, print a frame |
| `main.py` | Defines the cube, runs the render loop |

## How it works

Same pipeline a real graphics card uses, just done by hand and very slowly:

1. Build a model-view-projection matrix each frame, rotate the cube, push it back from the camera, apply perspective.
2. Multiply each of the cube's 8 vertices through it to get normalized device coordinates.
3. Map those to character cells in an 80×40 grid.
4. Draw the 12 edges between them and print the whole grid.

Repeat about 30 times a second, bumping the rotation angle a little each pass.

## Why

Two reasons. I wanted to use what I learned in linear algebra on something interesting. Rotation and projection matrices are a lot cooler when you can watch a cube spin. And I'd always wondered how those ASCII renderers people post actually worked, so I built one to find out.
