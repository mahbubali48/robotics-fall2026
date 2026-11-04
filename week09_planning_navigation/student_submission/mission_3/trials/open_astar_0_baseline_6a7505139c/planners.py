
from collections import deque
from heapq import heappush, heappop
from planning.core import reconstruct


# Check whether a grid cell is free.
def is_free(ctx, cell):
    row, col = cell
    return (
        0 <= row < len(ctx.grid)
        and 0 <= col < len(ctx.grid[row])
        and ctx.grid[row][col] == 0
    )


# 1. Breadth-First Search (BFS)
def bfs(ctx):
    start, goal = ctx.start, ctx.goal

    if not is_free(ctx, start) or not is_free(ctx, goal):
        return []

    if start == goal:
        return [start]

    frontier = deque([start])
    visited = {start}
    parent = {start: None}

    while frontier:
        current = frontier.popleft()

        if current == goal:
            return reconstruct(parent, goal)

        neighbors = ctx.expand(current, len(frontier) + 1)

        for nxt in neighbors:
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = current
                frontier.append(nxt)

    return []


# 2. Depth-First Search (DFS)
def dfs(ctx):
    start, goal = ctx.start, ctx.goal

    if not is_free(ctx, start) or not is_free(ctx, goal):
        return []

    if start == goal:
        return [start]

    stack = [start]
    visited = {start}
    parent = {start: None}

    while stack:
        current = stack.pop()

        if current == goal:
            return reconstruct(parent, goal)

        neighbors = ctx.expand(current, len(stack) + 1)

        # Reverse insertion preserves the preferred
        # neighbor order when popping from the stack.
        for nxt in reversed(neighbors):
            if nxt not in visited:
                visited.add(nxt)
                parent[nxt] = current
                stack.append(nxt)

    return []


# 3. Iterative Deepening DFS (IDDFS)
def iddfs(ctx):
    start, goal = ctx.start, ctx.goal

    if not is_free(ctx, start) or not is_free(ctx, goal):
        return []

    if start == goal:
        return [start]

    def depth_limited(current, depth, limit,
                      path, on_path, pending):
        if current == goal:
            return list(path), False

        neighbors = ctx.expand(current, pending + 1)
        available = [n for n in neighbors if n not in on_path]

        if depth == limit:
            return None, bool(available)

        had_cutoff = False

        for index, nxt in enumerate(available):
            path.append(nxt)
            on_path.add(nxt)

            remaining = len(available) - index - 1

            result, cutoff = depth_limited(
                nxt,
                depth + 1,
                limit,
                path,
                on_path,
                pending + remaining
            )

            if result is not None:
                return result, False

            had_cutoff = had_cutoff or cutoff
            on_path.remove(nxt)
            path.pop()

        return None, had_cutoff

    limit = 0

    while True:
        path = [start]
        on_path = {start}

        result, cutoff = depth_limited(
            start, 0, limit, path, on_path, 0
        )

        if result is not None:
            return result

        # All reachable paths have been exhausted.
        if not cutoff:
            return []

        limit += 1


# 4. A* Search
def astar(ctx):
    start, goal = ctx.start, ctx.goal

    if not is_free(ctx, start) or not is_free(ctx, goal):
        return []

    if start == goal:
        return [start]

    frontier = []
    parent = {start: None}
    g_cost = {start: 0}

    heappush(
        frontier,
        (ctx.heuristic(start), 0, start)
    )

    while frontier:
        f, g, current = heappop(frontier)

        # Ignore outdated queue entries.
        if g != g_cost[current]:
            continue

        if current == goal:
            return reconstruct(parent, goal)

        neighbors = ctx.expand(current, len(frontier) + 1)

        for nxt in neighbors:
            new_g = g + 1

            if new_g < g_cost.get(nxt, float("inf")):
                g_cost[nxt] = new_g
                parent[nxt] = current

                new_f = new_g + ctx.heuristic(nxt)

                heappush(
                    frontier,
                    (new_f, new_g, nxt)
                )

    return []
