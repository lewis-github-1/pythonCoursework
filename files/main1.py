def main():
  write_to_file = open('scores.txt', 'w')

  for i in range(3):
    score = get_input(0, 100, "\nEnter a score between 0 and 100: ")
    write_to_file.write(str(score) + "\n")

  write_to_file.close()

  # read from file:
  read_from_file = open('scores.txt', 'r')
  scores = []
  for line in read_from_file:
    # line = line.replace("\n", "")
    scores.append(int(line))

  read_from_file.close()
  print(scores)
  print("Average:", sum(scores) / len(scores))


def get_input(min, max, prompt):
  while True:
    user = int(input(prompt))
    if user < min or user > max:
      print("Invalid entry. Please re-enter: ")
      continue
    else:
      break
  return user

main()





