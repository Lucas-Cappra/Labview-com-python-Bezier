Como é relacionado as bibliotecas de python em relação ao LabVIEW?

Quando se começa a estudar a intepretação e integração entre Python e LabView, a questão das bibliotecas levanta dúvidas, entretanto, a relação entre os dois são independentes, as bibiliotecas utilizadas nos códigos de arquivos .py trabalham de maneira isoladas.
Mas como podem ser utilizadas no LabVIEW?

Primeiramente segue um exemplo de diagrama de blocos:
 - O código rodado em python, dentro do diagrama de blocos, recebe 3 pontos dentro de uma função "function", faz a interpolação linear, salva como uma imagem e retorna como uma string.

A SEGUIR O CÓDIGO:

![imagem_2022-10-14_155110101](https://user-images.githubusercontent.com/108031562/195919820-71a6e54c-07c2-4521-83e8-72d64c9e98d9.png)

Fonte: Feito por Lucas Cappra


Nota-se que ocorre uma conversão dos pontos x,y,z para inteiros. Para trabalham com números, relacionando LabVIEW com um código de função python, a maneira que trabalha de forma mais acessível é:
 - Trabalhar com o LabVIEW enviando os parâmetros em formato de String, texto propriamente dito. Desta forma, necessita-se dentro da função que ocorra uma conversão de STR para INT, e então segue-se trabalhando com estes valores.
 - Continuamente, para retornar a função para o front panel, como os parâmetros enviados foram em formato STR, retorna-se do mesmo formato.

A SEGUIR O DIAGRAMA DE BLOCOS NO LABVIEW:

![imagem_2022-10-14_155726788](https://user-images.githubusercontent.com/108031562/195920813-54a609ec-d269-428d-940c-f6ed57901ec8.png)

Fonte: Feito por Lucas Cappra


A SEGUIR O FRONT PANEL NO LABVIEW:

![imagem_2022-10-14_155810999](https://user-images.githubusercontent.com/108031562/195920940-35071aff-6833-4018-88fc-2a50703c1a85.png)

Fonte: Feito por Lucas Cappra
