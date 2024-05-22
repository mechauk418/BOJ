from collections import deque
import copy


def solution(maze):
    m, n = len(maze), len(maze[0])

    red, blue = [], []
    for i in range(m):
        for j in range(n):
            if maze[i][j] == 1:
                red = [i, j]
            elif maze[i][j] == 2:
                blue = [i, j]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    red_reached, blue_reached = False, False
    vr_, vb_ = [[[False for _ in range(n)] for _ in range(m)] for _ in range(2)]

    path = deque()
    path.append(red + blue + [vr_] + [vb_] + [0])

    while path:
        rr, rc, br, bc, vr_temp, vb_temp, count = path.popleft()

        vr = copy.deepcopy(vr_temp)
        vb = copy.deepcopy(vb_temp)
        vr[rr][rc] = True
        vb[br][bc] = True

        if maze[rr][rc] == 3 and maze[br][bc] == 4:
            return count
            break
            
        else:
            if maze[rr][rc] == 3:
                red_reached = True
                blue_reached = False
            elif maze[br][bc] == 4:
                red_reached = False
                blue_reached = True
            else:
                red_reached = False
                blue_reached = False

        for i in range(4):
            if blue_reached:
                r = [rr + dr[i], rc + dc[i]]
                if is_bounded(r, m, n):
                    if not (is_overlapped(r, (br, bc)) or is_wall(r, maze) or is_visited(r, vr)):
                        path.append([r[0], r[1], br, bc, vr, vb, count + 1])
            elif red_reached:
                b = [br + dr[i], bc + dc[i]]
                if is_bounded(b, m, n):
                    if not (is_overlapped(b, (rr, rc)) or is_wall(b, maze) or is_visited(b, vb)):
                        path.append([rr, rc, b[0], b[1], vr, vb, count + 1])
            else:
                r = [rr + dr[i], rc + dc[i]]
                if is_bounded(r, m, n):
                    if not (is_wall(r, maze) or is_visited(r, vr)):
                        for j in range(4):
                            b = [br + dr[j], bc + dc[j]]
                            if is_bounded(b, m, n):
                                if not (is_overlapped(r, b) or is_switched(r, (br, bc), b, (rr, rc)) or is_wall(b,maze) or is_visited(b, vb)):
                                    path.append([r[0], r[1], b[0], b[1], vr, vb, count + 1])
    return 0


def is_bounded(x, m, n):
    return 0 <= x[0] < m and 0 <= x[1] < n


def is_wall(x, map):
    return map[x[0]][x[1]] == 5


def is_overlapped(x, y):
    return (x[0], x[1]) == (y[0], y[1])


def is_switched(x, y, z, w):
    return (x[0], x[1]) == (y[0], y[1]) and (z[0], z[1]) == (w[0], w[1])


def is_visited(n, v):
    return v[n[0]][n[1]]