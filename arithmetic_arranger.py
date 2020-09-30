
def exception_handler(num_1, num_2, sign):
    result = None

    if not (sign in ['+', '-']):
        return "Error: Operator must be '+' or '-'."
        # raise Exception("Error: Operator must be '+' or '-'.")

    if(len(num_1) > 4 or len(num_2) > 4):
        return "Error: Numbers cannot be more than four digits."
        # raise Exception('Error: Numbers cannot be more than four digits.')
    
    try:
        int(num_1)
    except:
        return "Error: Numbers must only contain digits." 

    try:
        int(num_2)
    except:
        return "Error: Numbers must only contain digits." 

    return result

def arithmetic_arranger(problems, display=False):
    arranged_problems = None
    line_start = True
    side_space = "    "
    line_1 = line_2 = line_3 = line_4 = ""

    if len(problems) > 5:
        arranged_problems = "Error: Too many problems."
        return arranged_problems


    for prob in problems:
        num_1, sign, num_2 = prob.split()
        arranged_problems = exception_handler(num_1, num_2, sign)
        if arranged_problems is not None:
            return arranged_problems

        # space contains the max no. os spaces required.
        space = max(len(num_1), len(num_2))
        
        nm_1 = int(num_1)
        nm_2 = int(num_2)

        # For first arithmetic arragement
        if line_start:
            line_1 += num_1.rjust(space + 2)
            line_2 += sign + ' ' + num_2.rjust(space)
            line_3 += '-' * (space + 2)
            if display == True:
                if sign == '+':
                    line_4 += str(nm_1 + nm_2).rjust(space + 2)
                else:
                    line_4 += str(nm_1 - nm_2).rjust(space + 2)
            line_start = False
        # Other than first arithmetic arragement
        else:
            line_1 += num_1.rjust(space + 6)
            line_2 += sign.rjust(5) + ' ' + num_2.rjust(space)
            line_3 += side_space + '-' * (space + 2)
            if display == True:
                if sign == '+':
                    line_4 += side_space + str(nm_1 + nm_2).rjust(space + 2)
                else:
                    line_4 += side_space + str(nm_1 - nm_2).rjust(space + 2)
    
    if display == True:
        arranged_problems = line_1 + '\n' + line_2 + '\n' + line_3 + '\n' + line_4
        return arranged_problems

    arranged_problems = line_1 + '\n' + line_2 + '\n' + line_3
    return arranged_problems 