def area (lgc, cmp):
    areatotal = lgc * cmp
    print(f'A area total entre {lgc}x{cmp} é igual a {areatotal}m²')

lgc = int(input('Qual o largura do espaço em (m)?  '))
cmp = int(input('Qual o comprimento em (m)? '))
area(lgc, cmp)