from queue import PriorityQueue

N = 4


def moves(position):
    blank = position.index(0)
    i, j = divmod(blank, N)
    offsets = []
    if i > 0: offsets.append(-N)  # вниз
    if i < N - 1: offsets.append(N)  # вверх
    if j > 0: offsets.append(-1)  # вправо
    if j < N - 1: offsets.append(1)  # влево
    for offset in offsets:
        swap = blank + offset
        yield tuple(
            position[swap] if x == blank else position[blank] if x == swap else position[x] for x in range(N * N))


def parity(permutation):
    seen, cycles = set(), 0
    for i in permutation:
        if i not in seen:
            cycles += 1
            while i not in seen:
                seen.add(i)
                i = permutation[i]
    return (cycles + len(permutation)) % 2


class Position:
    def __init__(self, position, start_distance):
        self.position = position
        self.start_distance = start_distance

    def __lt__(self, other):
        return self.start_distance < other.start_distance

    def __str__(self):
        return '\n'.join((N * '{:3}').format(*[i % (N * N) for i in self.position[i:]]) for i in range(0, N * N, N))


SOLVED = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)

start = [1, 2, 3, 4, 5, 6, 7, 8, 13, 9, 11, 12, 10, 14, 15, 0]

if parity(start) == 0:
    # https://en.wikipedia.org/wiki/15_puzzle#Solvability
    print('Нерешаемо')
else:
    start = tuple(start)

    p = Position(start, 0)

    print(p)
    print()

    candidates = PriorityQueue()
    candidates.put(p)

    visited = set([p])

    came_from = {p.position: None}

    while p.position != SOLVED:
        p = candidates.get()
        for k in moves(p.position):
            if k not in visited:
                candidates.put(Position(k, p.start_distance + 1))
                came_from[k] = p
                visited.add(k)

    path = []
    prev = p
    while p.position != start:
        p = came_from[p.position]
        number = p.position[prev.position.index(0)]
        path.append(number)
        prev = p
    path.reverse()

    print(path)