class Screen:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self._buffer = [[' ' for _ in range(width)] for _ in range(height)]
    
    def clear(self):
        self._buffer = [[' ' for _ in range(self.width)] for _ in range(self.height)]

    def present(self):
        for row in self._buffer:
            print(''.join(row))
    
    def draw(self, x: int, y: int, char: str = '#'):
        if 0 <= x < self.width and 0 <= y < self.height:
            self._buffer[y][x] = char
    
    def _in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height
    
    def __str__(self) -> str:
        return '\n'.join(''.join(row) for row in self._buffer)