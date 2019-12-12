from collections import defaultdict
def main():
  image = ""
  code = open("8.in", "r")
  for line in code:
    image = line.strip()

  layers = []
  layer_num = 0
  data_frame = 25 * 6
  while layer_num*data_frame < len(image):
    m = defaultdict(int)
    layers.append()

main()
