def Read(name):
    with open(name) as f:
        lines = f.readlines()
        return "\n".join(lines)