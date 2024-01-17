# Validando E-mails com Expressões Regulares

## Introdução:

A validação de e-mails é uma tarefa essencial em muitos projetos, e as expressões regulares (regex) são uma ferramenta 
poderosa para realizar essa verificação de forma eficiente. No Python 3, podemos utilizar a biblioteca `re` para trabalhar 
com expressões regulares.

## Exemplo de Códigos:

Aqui estão três exemplos de expressões regulares para validar e-mails:

### 1. Básica
```python
^\w+(?:[.\-+!%]\w+)*@\w+(?:[.\-]\w+)+$
```
[Ver no regex101](https://regex101.com/r/9s4bgv/1/)

### 2. Básica 2
```python
^[^\s@<>\(\)[\]\.]+(?:\.[^\s@<>\(\)\[\]\.]+)*@\w+(?:[\.\-_]\w+)*$
```
[Ver no regex101](https://regex101.com/r/mH4ChC/2/)

### 3. RFC 5322
```python
^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$
```
[Ver no regex101](https://regex101.com/r/fkxI15/1/)

## Exemplos de E-mails:

Aqui estão alguns exemplos de e-mails que podem ser usados para testar as expressões regulares:

### E-mails Válidos:
- o-que_vai.te+dar+dor-de.cabeca@gmail-com-traco.com.br
- simple@example.com
- very.common@example.com
- disposable.style.email.with+symbol@example.com
- ...

### E-mails Inválidos:
- Abc.example.com
- <aqui-te-um@email-pra-validar.com.br>
- A@b@c@example.com
- a"b(c)d,e:f;g<h>i[j\k]l@example.com
- ...

## Conclusão:

As expressões regulares fornecem uma ferramenta poderosa para validar e-mails de forma precisa. No entanto, 
é importante entender as nuances e limitações de cada regex. 

