for T in range(int(input())):
    A, B, C, D = map(int, input().split())
    if B == 0 and C == 0 and A != 0 and D != 0:
        result = 'impossible'
    elif abs(B - C) > 1:
        result = 'impossible'
    else:
        if B == 0 and C == 0:
            if A != 0:
                result = '0' * (A + 1)
            else:
                result = '1' * (D + 1)
        elif B < C:
            result = '1' * D + '10' * C + '0' * A
        elif B > C:
            result = '0' * A + '01' * B + '1' * D
        else:
            result = '0' * A + '01' * B + '1' * D + '0'
    print('#{} {}'.format(T+1, result))