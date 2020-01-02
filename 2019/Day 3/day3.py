w1, w2 = open('day3').read().split('\n')
w1, w2 = [x.split(',') for x in [w1,w2]]

dx = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
dy = {'L': 0, 'R': 0, 'U': 1, 'D': -1}

def get_points(A):
    x = 0
    y = 0
    length = 0
    points = {}
    for cmd in A:
        d = cmd[0]
        n = int(cmd[1:])
        assert d in ['L', 'R', 'U', 'D']
        for _ in range(n):
            x += dx[d]
            y += dy[d]
            length += 1
            if (x,y) not in points:
                points[(x,y)] = length
    return points

points_w1 = get_points(w1)
points_w2 = get_points(w2)

intersections = set(points_w1.keys())&set(points_w2.keys())

distances = [points_w1[p] + points_w2[p] for p in intersections]

ans = min(distances)

print(ans)
