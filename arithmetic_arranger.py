def arithmetic_arranger(problems, answer=False):

    if len(problems) > 5:
        return "Error: Too many problems"

    for problem in problems:
        if "*" in problem:
            return "Error: Operator must be " + " or " - ""
        if "/" in problem:
            return "Error: Operator must be " + " or " - ""

    for problem in problems:
        for item in problem.split():
            if item == "+":
                continue
            if item == "-":
                continue
            if item.isdigit() == True:
                continue
            else:
                return "Error: Numbers must only contain digits"

    for problem in problems:
        for item in problem.split():
            if item == "+":
                continue
            if item == "-":
                continue
            if item.isdigit() == True:
                if len(item) > 4:
                    return "Error: Numbers cannot be more than four digits"
            else:
                continue

    problem_num = len(problems)
    i = 0
    first_line = ""

    while i < problem_num:
        if i <= problem_num - 2:
            first_line += str((
                f"{problems[i].split()[0]:>{len(max((problems[i].split()), key=len)) + 2}}"
            )) + "    "
        else:
            first_line += str((
                f"{problems[i].split()[0]:>{len(max((problems[i].split()), key=len)) + 2}}"
            ))
        i += 1

    i = 0
    second_line = ""
    while i < problem_num:
      if i <= problem_num - 2:
        second_line += str((f"{problems[i].split()[1].ljust ((len(max((problems[i].split()), key=len)) + 2) - (len(problems[i].split()[2]))) + problems[i].split()[2]:>{len(max((problems[i].split()), key=len)) + 2}}")) + "    "
      else:
        second_line += str((f"{problems[i].split()[1].ljust ((len(max((problems[i].split()), key=len)) + 2) - (len(problems[i].split()[2]))) + problems[i].split()[2]:>{len(max((problems[i].split()), key=len)) +2}}"))
      i += 1

    i = 0
    third_line = ""
    while i < problem_num:
      if i <= problem_num - 2:
        third_line += str(("-" * (len(max((problems[i].split()), key=len)) + 2) + "    "))
      else:
        third_line += str(("-" * (len(max((problems[i].split()), key=len)) + 2) + "    "))
      i += 1

    if answer == True:
      problem_num = len(problems)
      i = 0
      fourth_line = ""
      while i < problem_num:
        if problems[i].split()[1] == "+":
          result = int(problems[i].split()[0]) + int(problems[i].split()[2])
          if i <= problem_num - 2:
            fourth_line += str((str(result).rjust(len(max((problems[i].split()), key=len)) + 2))) + "    "
          else:
            fourth_line += str((str(result).rjust(len(max((problems[i].split()), key=len)) + 2)))
        if problems[i].split()[1] == "-":
          result = int(problems[i].split()[0]) - int(problems[i].split()[2])
          if i <= problem_num - 2:
            fourth_line += str((str(result).rjust(len(max((problems[i].split()), key=len)) + 2))) + "   "
          else:
            fourth_line += str((str(result).rjust(len(max((problems[i].split()), key=len)) + 2)))
        i += 1

      return first_line + "\n" + second_line + "\n" + third_line + "\n" + fourth_line
    else:
      return first_line + "\n" + second_line + "\n" + third_line
