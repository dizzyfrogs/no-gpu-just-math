class Vec3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other: 'Vec3') -> 'Vec3':
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other: 'Vec3') -> 'Vec3':
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar: float) -> 'Vec3':
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def dot(self, other: 'Vec3') -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def length(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5
    
    def normalize(self) -> 'Vec3':
        len = self.length()
        if len == 0:
            return Vec3(0, 0, 0)
        return Vec3(self.x / len, self.y / len, self.z / len)
    
class Mat4:
    def __init__(self, elements: list):
        self.elements = elements # 4x4 matrix, 16 elements in column-major order
    
    def __matmul__(self, other: 'Mat4') -> 'Mat4':
        result = [0.0] * 16

        for col in range(4):
            for row in range(4):
                result[col * 4 + row] = (
                    self.elements[0 * 4 + row] * other.elements[col * 4 + 0] +
                    self.elements[1 * 4 + row] * other.elements[col * 4 + 1] +
                    self.elements[2 * 4 + row] * other.elements[col * 4 + 2] +
                    self.elements[3 * 4 + row] * other.elements[col * 4 + 3]
                )

        return Mat4(result)

    
    def __mul__(self, vec: Vec3) -> Vec3:
        x = vec.x * self.elements[0] + vec.y * self.elements[4] + vec.z * self.elements[8] + self.elements[12]
        y = vec.x * self.elements[1] + vec.y * self.elements[5] + vec.z * self.elements[9] + self.elements[13]
        z = vec.x * self.elements[2] + vec.y * self.elements[6] + vec.z * self.elements[10] + self.elements[14]
        w = vec.x * self.elements[3] + vec.y * self.elements[7] + vec.z * self.elements[11] + self.elements[15]
        if w != 0:
            return Vec3(x / w, y / w, z / w)
        return Vec3(x, y, z)
    
    def transpose(self) -> 'Mat4':
        transposed = [0.0] * 16
        for col in range(4):
            for row in range(4):
                transposed[col * 4 + row] = self.elements[row * 4 + col]
        return Mat4(transposed)
