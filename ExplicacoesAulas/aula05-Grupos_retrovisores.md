# Grupos e Retrovisores em Expressões Regulares (Regex) em Python 3

As expressões regulares (regex) são uma poderosa ferramenta em Python para manipulação de padrões em strings. 
Grupos e retrovisores são conceitos essenciais nesse contexto, permitindo a identificação e manipulação de partes 
específicas dos padrões.

**Meta Caracteres: ^ $ () \1 \2 \3**

**^ e $ :** Representam o início e o final da linha, respectivamente.

**() :** Define um grupo de captura, permitindo extrair partes específicas do texto correspondente.

**\1 \2 \3 :** São retrovisores que se referem aos grupos de captura. Permitem reutilizar o texto correspondente aos 
grupos na substituição ou em outras partes da expressão.

**1. Grupos:**

Os parênteses `( )` são utilizados para criar grupos em expressões regulares. Um grupo permite que você aplique 
quantificadores a partes específicas do padrão e facilite a manipulação dessa informação. No exemplo:

```python
re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', texto)
```

- `<([dpiv]{1,3})>`: Grupo para identificar tags como 'd', 'p', 'i' ou 'v'.
- `(.+?)`: Grupo para capturar o conteúdo dentro da tag de forma não-greedy.

**2. Retrovisores:**

Os retrovisores `\1`, `\2`, etc., são usados para referenciar grupos já definidos na expressão. No exemplo:

```python
re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS \3 COISAS \4', texto)
```

- `(<(.+?)>)`: Grupo para a tag de abertura.
- `(.+?)`: Grupo para o conteúdo da tag.
- `(<\/\2>)`: Grupo referente à tag de fechamento, utilizando retrovisor `\2`.

**Exemplo Prático:**

Considere a substituição no exemplo acima:

```python
<p MAIS Frase 1 COISAS </p> <p MAIS Eita COISAS </p> <p MAIS Qualquer frase COISAS </p> <div MAIS 1 COISAS </div>
```

A utilização de grupos e retrovisores torna possível aplicar modificações específicas apenas em partes desejadas do padrão.

**Dica Extra:**

No exemplo do CPF, a expressão `((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})` utiliza grupos não capturadores `(?: ... )` 
para evitar a criação de grupos desnecessários para a aplicação de quantificadores.

Ao utilizar grupos e retrovisores em conjunto, você ganha flexibilidade para manipular padrões complexos e extrair 
informações específicas de suas strings.