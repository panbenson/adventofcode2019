from collections import defaultdict

def main():
  example = open("6.in", "r")

  # build the graph
  orbit = defaultdict(list)

  for line in example:
    a, b = line.strip().split(")")
    orbit[a].append(b)
    orbit[b].append(a)

  # part 1
  print(dfs(orbit, [], "COM", 1))

  # part 2


def dfs(orbit, closed, current, depth):
  return sum([depth + dfs(orbit, closed + [current], next, depth + 1) for next in orbit[current] if next not in closed])


main()
