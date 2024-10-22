#https://acmp.ru/index.asp?main=task&id_task=92
with open('INPUT.TXT') as f:
    S = int(f.readline().strip())
     
if S % 6 == 0:
    P = S // 6
    K = 4 * P
     
    with open('OUTPUT.TXT', 'w') as f_out:
        f_out.write(f"{P} {K} {P}\n")
