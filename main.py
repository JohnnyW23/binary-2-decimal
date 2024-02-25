while True:
    while True:
        binary = input('''
Enter your binary value: ''')  # It begins as a string
        try:
            int(binary)  # Since binaries are integer numbers
            v = 0
            for n in binary:
                if n == '0' or n == '1':
                    v += 1
            if v != len(binary):  # Means it validated all binary digits
                print('\033[31mOnly 0 and 1 allowed!\033[m')
            else:
                break
        except ValueError:
            print('\033[31mINVALID ENTRY!\033[m')
    bin = binary  # Saves the binary string before it's reversed
    binary = binary[::-1]  # Reversed string so the formula works more clearly
    bin2dec = 0
    for i, n in enumerate(binary):  # Since 0 powered to any value is still 0,
        if n == '1':                # I only counted the 1 in the string and
            bin2dec += (1 * 2 ** i) # multiplied it by 2 powered to the index
    print(f'''
Binary: {bin}
Decimal: \033[33m{bin2dec}\033[m
''')
    while True:
        answer = input('Do you wish to calculate again? [Y/N]: ').upper().strip()
        if answer != 'Y' and answer != 'N':
            print('\033[31mINVALID ANSWER!\033[m')
        else:
            if answer == 'N':
                answer = False
            break
    if not answer:
        print()
        break
    print('''
\033[36m=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=~=\033[m''')
