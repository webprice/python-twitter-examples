def arithmetic_arranger(problems,state = "True"):
  operator = list()
  first_number = list()
  second_number = list()
  if len(problems) > 5:
    return print("Error: Too many problems.")
  for operators in problems:
    splitted=operators.split(" ")
    try:
      int(splitted[0])
      int(splitted[2])
    except ValueError:
      return  "Error: Numbers must only contain digits."
    if splitted[1] == '+' or splitted[1] == '-':
      pass
    else:
      return "Error: Operator must be '+' or '-'."
    if len(splitted[0]) > 4 or len(splitted[2]) >4:
      return "Error: Numbers cannot be more than four digits."
  i = 0
  Firstline = str()
  Secondline = str()
  Thirdline = str()
  Answerline = str()

  for _ in problems:
    #print(_)
    sortid = _.split(" ")
    z=first_number.append(sortid[0])
    mid=operator.append(sortid[1])
    y = second_number.append(sortid[2])
    #print(sortid[1])

    while i < len(first_number):
      diff=len(first_number[i]) -len(second_number[i])
      dash=str
      lspace=str
      answer = eval(_)
      #print(answer)
      if diff >0:
        lspace=' '*(diff+1)
        answerspace=' '* ((len(first_number[i])+2) - (len(str(answer))))
        dash='-' * (len(first_number[i])+2)
        Firstline = Firstline + f'  {first_number[i]}    '
        Secondline = Secondline + f'{operator[i]}{lspace}{second_number[i]}    '
        Thirdline = Thirdline + f'{dash}    '
        Answerline = Answerline + f'{answerspace}{answer}    '

      if diff < 0:
        lspace = ' ' * ((diff*-1) + 2)
        answerspace = ' ' * ((len(second_number[i]) + 2) - (len(str(answer))))
        dash = '-' * (len(second_number[i]) + 2)
        Firstline = Firstline + f'{lspace}{first_number[i]}    '
        Secondline = Secondline + f'{operator[i]} {second_number[i]}    '
        Thirdline = Thirdline + f'{dash}    '
        Answerline = Answerline + f'{answerspace}{answer}    '

      if diff == 0:
        lspace = '  '
        answerspace = ' ' * ((len(second_number[i]) + 2) - (len(str(answer))))
        dash = '-' * (len(second_number[i]) + 2)
        Firstline = Firstline + f'{lspace}{first_number[i]}    '
        Secondline = Secondline + f'{operator[i]} {second_number[i]}    '
        Thirdline = Thirdline + f'{dash}    '
        Answerline = Answerline + f'{answerspace}{answer}    '
      i = i+1

  if state == True:
    arranged_problems = f'{Firstline[:-4]}\n{Secondline[:-4]}\n{Thirdline[:-4]}\n{Answerline[:-4]}'

    return arranged_problems
  else:
    arranged_problems = f'{Firstline[:-4]}\n{Secondline[:-4]}\n{Thirdline[:-4]}'
    return arranged_problems


print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49',
          '888 + 40', '653 + 87'],True))
