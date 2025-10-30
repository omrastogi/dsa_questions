def build_rows(root):
    """Return rows of nodes including None placeholders so that:
       rows[i][j] -> children are rows[i+1][2*j], rows[i+1][2*j+1]."""
    if not root:
        return []
    rows = [[root]]
    while True:
        prev = rows[-1]
        nxt, any_real = [], False
        for n in prev:
            if n is None:
                nxt.extend([None, None])
            else:
                nxt.append(n.left)
                nxt.append(n.right)
                any_real |= (n.left is not None or n.right is not None)
        if not any_real:
            break
        rows.append(nxt)
    return rows

def render_ascii_tree(root, gap_extra=2):
    rows = build_rows(root)
    if not rows:
        print("(empty)")
        return

    # labels & widths
    lbl = lambda n: "_" if n is None else str(n.key)
    labels = [[lbl(n) for n in row] for row in rows]
    max_label = max(len(s) for row in labels for s in row)
    depth = len(rows) - 1
    last_cnt = len(rows[-1])  # 2**depth

    # base spacing between centers on the last row
    GAP = max_label + gap_extra

    # center positions for every node (absolute char columns)
    pos = [[0]*len(row) for row in rows]
    for j in range(last_cnt):
        pos[-1][j] = j * GAP
    for i in range(depth-1, -1, -1):
        for j in range(len(rows[i])):
            lc = pos[i+1][2*j]
            rc = pos[i+1][2*j+1]
            pos[i][j] = (lc + rc) // 2

    width = pos[-1][-1] + max_label + 2

    out = []
    for i, row in enumerate(rows):
        # --- node line ---
        line = [" "] * width
        for j, n in enumerate(row):
            if n is None: 
                continue
            s = labels[i][j]
            c = pos[i][j]
            start = max(0, c - len(s)//2)
            end = min(width, start + len(s))
            for k, ch in enumerate(s[:end-start]):
                line[start + k] = ch
        out.append("".join(line).rstrip())

        if i == depth:
            break

        # --- connector 'bridge' line: _______|_______ under the parent ---
        bridge = [" "] * width
        for j, n in enumerate(row):
            if n is None:
                continue
            c = pos[i][j]
            L = rows[i+1][2*j]
            R = rows[i+1][2*j+1]
            # draw underscores from child centers to parent center (only if child exists)
            if L is not None:
                lc = pos[i+1][2*j]
                for x in range(lc, c):
                    if 0 <= x < width:
                        bridge[x] = "_" if bridge[x] == " " else bridge[x]
            if R is not None:
                rc = pos[i+1][2*j+1]
                for x in range(c+1, rc+1):
                    if 0 <= x < width:
                        bridge[x] = "_" if bridge[x] == " " else bridge[x]
            # vertical bar directly under parent if any child exists
            if L is not None or R is not None:
                if 0 <= c < width:
                    bridge[c] = "|"
        out.append("".join(bridge).rstrip())

        # --- connector 'arms' line: put '/' above left child and '\' above right child ---
        arms = [" "] * width
        for j, n in enumerate(row):
            if n is None:
                continue
            L = rows[i+1][2*j]
            R = rows[i+1][2*j+1]
            if L is not None:
                lc = pos[i+1][2*j]
                if 0 <= lc < width:
                    arms[lc] = "/"
            if R is not None:
                rc = pos[i+1][2*j+1]
                if 0 <= rc < width:
                    arms[rc] = "\\"
        out.append("".join(arms).rstrip())

    print("\n".join(out))
