# Validando Endereços IP (IPv4) com Expressões Regulares em Python 3

**Introdução:**
A validação de endereços IP (IPv4) é uma tarefa comum em programação, e uma maneira eficiente de
realizar essa validação é através do uso de expressões regulares em Python 3. Expressões regulares
são padrões de busca em strings, permitindo a validação de formatos específicos.

**Código de Exemplo:**
```python
import re

cpf = '025.258.963-10'
cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', flags=0)

ip_reg_exp = re.compile(
    r'^'
    r'(?:'
    r'(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.'
    r'){3}'
    r'(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])'
    r'$',
    flags=0
)

for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_reg_exp.findall(ip))
```

**Explicação:**
1. **CPF:**
   - A expressão regular para o CPF (`cpf_reg_exp`) valida um formato específico de CPF, garantindo três dígitos
   seguidos de um ponto, repetido três vezes, seguido de dois dígitos após um traço.

2. **Endereço IP (IPv4):**
   - A expressão regular para o endereço IP (`ip_reg_exp`) valida o formato de um endereço IPv4.
   - `25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9]`: Esta parte valida cada octeto do endereço IP, garantindo que esteja dentro do intervalo válido (0 a 255).
   - `(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.`: Esta parte valida os três primeiros octetos, cada um seguido por um ponto.
   - `{3}`: Garante que os três primeiros octetos se repitam exatamente três vezes.
   - A última parte valida o último octeto, sem ponto no final.

3. **Loop de Teste:**
   - O loop `for` gera 300 endereços IP fictícios e os valida usando a expressão regular. Os resultados são impressos no console.

**Conclusão:**
Utilizando expressões regulares em Python 3, podemos criar padrões de validação poderosos para garantir que os dados,
como CPF e endereços IP, estejam no formato desejado.