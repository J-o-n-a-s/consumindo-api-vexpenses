[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

[contributors-shield]: https://img.shields.io/github/contributors/J-o-n-a-s/consumindo-api-vexpenses.svg?style=for-the-badge
[contributors-url]: https://github.com/J-o-n-a-s/consumindo-api-vexpenses/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/J-o-n-a-s/consumindo-api-vexpenses.svg?style=for-the-badge
[forks-url]: https://github.com/J-o-n-a-s/consumindo-api-vexpenses/network/members
[stars-shield]: https://img.shields.io/github/stars/J-o-n-a-s/consumindo-api-vexpenses.svg?style=for-the-badge
[stars-url]: https://github.com/J-o-n-a-s/consumindo-api-vexpenses/stargazers
[issues-shield]: https://img.shields.io/github/issues/J-o-n-a-s/consumindo-api-vexpenses.svg?style=for-the-badge
[issues-url]: https://github.com/J-o-n-a-s/consumindo-api-vexpenses/issues
[license-shield]: https://img.shields.io/github/license/J-o-n-a-s/consumindo-api-vexpenses.svg?style=for-the-badge
[license-url]: https://github.com/J-o-n-a-s/consumindo-api-vexpenses/blob/master/LICENSE

# Consumindo API do VExpenses

**SEJA BEM-VINDO A ESTE REPOSITÓRIO!!!**

-------------

**Instruções**

 - *Fork* este repositório;
 - Clone seu repositório *forked*;
 - Adicione seus scripts;
 - *Commit & Push*;
 - Crie um *pull request*;
 - Dê uma estrela para este repositório;
 - Aguarde que o seu *pull request* solicitado vire um *merge*;
 - Comemore, seu primeiro passo para o mundo de código aberto e continue contribuindo.

## Introdução

Projeto para manipular as informações do VExpenses atráves da API disponibilizada pela empresa. Importa salientar que para ter acesso ao *```token público```* para autenticação é necessário ter uma conta VExpenses (*não estou fazendo propaganda e não recebi patrocínio para esses desenvolvimento*), cada empresa possui um *```token público```* diferente.

O intuito do projeto é realizar consultas simples sem interface gráfica para automatizar as atividades repetitivas, tediosas e evitar erros humanos durante essas coletas. Porém posteriormente posso pensar em realizar algumas melhorias no software facilitando ainda mais a sua utilização e agregando funcionalidades facilitadoras.

## Motivação

Atualmente, em nossa empresa, nós utilizamos o VExpenses para fazer toda a gestão de todos os gastos, adiantamentos e reembolsos dos funcionários/sócios. Com o intuito de facilitar a interação com o VExpenses, sem a necessidade de acessar o site para buscar e coletar as informações manualmente, decidi estudar a API e verificar as informações disponíveis e como trabalhar com elas para facilitar a nossa vida no dia-a-dia e otimizar o nosso tempo realizando a automação desta atividade.

## Descrição do projeto

O projeto foi desenvolvido em Python 3.12 realizando o código em arquivos separados como boa prática para facilitar a localização das funções. Está sendo utilizado formatadores de código para garantir a padronização da maneira de escrever os códigos.

Nesta primeira versão, toda a interação com o software é realizada sem interface gráfica. A ideia é o usuário interagir com um menu para selecionar as opções necessária para receber a informação que precisa.

### Bibliotecas e recursos utilizados

 - OS -> Biblioteca para funções do sistema operacional;
 - Time -> Para adição de tempo e registro do início, fim e duração do processo;
 - Tkinter -> Para utilização da caixa de diálogo de seleção de diretório para exportação de arquivo;
 - Datetime -> Para pegar a data atual do sistema;
 - Requests -> Para realizar o acesso a API do VExpenses;
 - Openpyxl -> Para criação/escrita de arquivo XLSX;
 - Pyinstaller -> Para criação do arquivo executável. Facilitando a utilização do programa mesmo em máquinas que não possuem o Python instalado.

### Funcionamento do programa

![Apresentação e menu de seleção inicial](img/menu_geral.png)

### Amostra do resultado da execução do programa

...

## Instalação e execução do projeto

 - `pip install poetry` para instalar o gerenciador de pacotes
 - `poetry install` para que o poetry instale os pacotes usados no projeto
 - `poetry shell` para que o poetry crie um ambiente virtual
 - `python src/main.py` para executar o projeto

## Licença

MIT License
 
