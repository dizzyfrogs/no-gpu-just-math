class Screen:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self._buffer = [[' ' for _ in range(width)] for _ in range(height)]
    
    def clear(self):
        print("\033[H", end="")
        self._buffer = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def present(self):
        for row in self._buffer:
            print(''.join(row))
    
    def draw(self, x: int, y: int, char: str = '#'):
        if 0 <= x < self.width and 0 <= y < self.height:
            self._buffer[y][x] = char

    def set_pixel(self, x: int, y: int, char: str = "#"):
        if 0 <= x < self.width and 0 <= y < self.height:
            self._buffer[y][x] = char

    
    def draw_line(self, x0, y0, x1, y1, char="#"):
        dx = x1 - x0
        dy = y1 - y0

        steps = max(abs(dx), abs(dy))
        if steps == 0:
            self.set_pixel(x0, y0, char)
            return

        x_inc = dx / steps
        y_inc = dy / steps

        x = x0
        y = y0
        for _ in range(steps + 1):
            self.set_pixel(int(round(x)), int(round(y)), char)
            x += x_inc
            y += y_inc

    
    def _in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height
    
    def __str__(self) -> str:
        return '\n'.join(''.join(row) for row in self._buffer)