# Expressões Regulares, Shorthands e Flags em Python 3

As expressões regulares (regex) em Python são poderosas ferramentas para busca, manipulação e validação de padrões em 
textos.

1. **\w (Word Character):**
   - Representa qualquer caractere alfanumérico (letras, números e underscore).
   - Equivalente a [a-zA-Z0-9_].
   - Pode ser modificado com a flag `re.A` para considerar também caracteres acentuados.

2. **\W (Non-Word Character):**
   - Representa qualquer caractere que não seja alfanumérico.
   - Equivalente a [^a-zA-Z0-9_].
   - A flag `re.A` amplia a correspondência para caracteres não alfanuméricos acentuados.

3. **\d (Digit):**
   - Corresponde a qualquer dígito numérico [0-9].

4. **\D (Non-Digit):**
   - Corresponde a qualquer caractere que não seja um dígito.

5. **\s (Whitespace):**
   - Corresponde a qualquer caractere de espaço em branco, como espaço, tabulação, quebra de linha, etc.

6. **\S (Non-Whitespace):**
   - Corresponde a qualquer caractere que não seja um espaço em branco.

7. **\b (Word Boundary):**
   - Indica uma borda de palavra.
   - Pode ser usado para encontrar palavras específicas, como `\b\w{4}\b` que encontra palavras de exatamente 4 letras.

8. **\B (Non-Word Boundary):**
   - Indica uma posição que não é uma borda de palavra.

**Exemplos de Uso:**
   - `re.findall(r'\w+', texto, flags=re.I)`: Encontra todas as palavras alfanuméricas no texto.
   - `re.findall(r'\W+', texto, flags=re.I)`: Encontra sequências de caracteres não alfanuméricos.
   - `re.findall(r'\d+', texto, flags=re.I)`: Encontra todos os números no texto.
   - `re.findall(r'\S+', texto, flags=re.I)`: Encontra todas as sequências não vazias.
