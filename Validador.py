# #Autenticador de CPF**

set = input("Você Gostaria de : \n 1- Verificar um CPF \n 2- Gerar um CPF \n")


def valida_cpf(cpf):

  # Remove caracteres não numéricos
  cpf = ''.join(filter(str.isdigit, cpf))

  if len(cpf) != 11 or cpf == cpf[0] * 11:
    return False

  # Validação do primeiro dígito verificador
  soma = 0
  for i in range(9):
    soma += int(cpf[i]) * (10 - i)
  resto = 11 - (soma % 11)
  if resto == 10 or resto == 11:
    resto = 0
  if resto != int(cpf[9]):
    return False

  # Validação do segundo dígito verificador
  soma = 0
  for i in range(10):
    soma += int(cpf[i]) * (11 - i)
  resto = 11 - (soma % 11)
  if resto == 10 or resto == 11:
    resto = 0
  if resto != int(cpf[10]):
    return False

  return True


def gera_cpf():
  cpf = [random.randint(0, 9) for _ in range(9)]

  # Calcula o primeiro dígito verificador
  soma = 0
  for i in range(9):
    soma += cpf[i] * (10 - i)
  resto = 11 - (soma % 11)
  if resto == 10 or resto == 11:
    resto = 0
  cpf.append(resto)

  # Calcula o segundo dígito verificador
  soma = 0
  for i in range(10):
    soma += cpf[i] * (11 - i)
  resto = 11 - (soma % 11)
  if resto == 10 or resto == 11:
    resto = 0
  cpf.append(resto)

  return ''.join(map(str, cpf))


## Opção de digitar CPF

if set == "1":
  cpf = input("Digite o CPF: ")

  print(f'CPF: {cpf}')

  if valida_cpf(cpf):
    print('CPF válido!')
  else:
    print('CPF inválido!')

## Opção de Gerar CPF
if set == "2":
  cpf = gera_cpf()
  print(f'CPF gerado: {cpf}')

  if valida_cpf(cpf):
    print('CPF válido!')

  else:
    print('CPF inválido!')