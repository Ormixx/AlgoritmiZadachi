K = int(input().strip())
if 0 <= K <= 9:
    second_digit = 9
    third_digit = 9 - K
    result_number = int(f'{K}{second_digit}{third_digit}')
    print(result_number)
