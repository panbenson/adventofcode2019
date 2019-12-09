def int_code_computer(prog):
  ins = 0
  line_width = 4

  while ins * line_width < len(prog):
    print(prog[ins*line_width:ins*line_width+line_width])
    if prog[ins * line_width] == 1:
      # addition
      prog[prog[ins * line_width + 3]] = prog[prog[ins * line_width + 2]] + prog[prog[ins * line_width + 1]]
    elif prog[ins * line_width] == 2:
      # multiplication
      prog[prog[ins * line_width + 3]] = prog[prog[ins * line_width + 2]] * prog[prog[ins * line_width + 1]]
    elif prog[ins * line_width] == 99:
      break
    else:
      print("error in program!")
    
    print(prog)
    ins += 1

  
def main():
  code = open("example.in", "r")
  copy = []
  for line in code:
    copy += map(int, line.strip().split(","))
  print(copy)
  
  int_code_computer(copy)
  print(copy)


main()
