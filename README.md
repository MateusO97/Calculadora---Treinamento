  <h3 align="center">Calculadora</h3>

  <p align="center">
    <i>Treinamento Sprint</i>
    <br>
</p>


<br></br>

## Introdução

Neste treinamento estaremos aplicando todos os conceitos estudados até o momento, desde o funcionamento das metologias ágeis explicadas, até o desenvolvimento em Django utilizando Docker e seguindo o Gitflow para subirem as alterações feitas.

## Instalação
Para este projeto será necessário possuir Git, e realizar a instalação do Docker e Docker Compose.

### Pré-Requisitos
* [Git](https://git-scm.com/)
* [Docker](https://www.docker.com/community-edition#/download)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Clonar
Clonar o repositório deste projeto.

```bash
$ git clone https://github.com/MateusO97/Calculadora---Treinamento
```

### Docker Compose
Hora de rodar o projeto. Navegue no diretório no qual você clonou o projeto e rode o Docker Compose

```bash
$ cd diretorio-do-seu-clone
$ docker-compose up
```

E está pronto! Agora você consegue rodar a aplicação, navegue até `http://localhost:3000/` no seu navegador!
Caso os comandos acima não tenham funcionado, rode como sudo:

```bash
$ sudo docker-compose up
```


## Scrum City of Code

O desafio deste treinamento é finalizar as issues apresentadas neste repositório, mas seguindo o passo a passo do Scrum e utilizando dos conceitos aprendidos até o momento no tempo delimitado, acompanhe as intruções a seguir.

### Planejamento da Sprint [10 Minutos]

A primeira fase do projeto será planejar a Sprint que irão executar, nesta etapa vocês terão um prazo de <b>10 Minutos</b> para concluir e estes passos são:

  - Planning Poke: Pontuar as issues do backlog(Sugestão, em virtude do tempo realizem a votação e decidam rapidamente pela maioria dos votos)
  - Alocar Histórias: Decidam quantas e quais issues serão feitas nesta Sprint, levem em consideração que teremos somente 2 Sprints.
  - Definir Pareamentos: Montem as duplas, levando em consideração a passagem de conhecimento e aloquem as histórias de cada dupla
  
  
### Execução [1 hora]

Depois de definidos os pareamentos é hora de colocar a mão no código! Nessa etapa vocês terão um prazo de <b>30 minutos</b>, levem em consideração os seguintes pontos:

  - Esquema Dojo: Dentro da dupla o desenvolvimento vai funcionar da seguinte forma: Um dos membros começara como Piloto enquanto o outro irá sentar do seu lado sendo o Co-Piloto. O Piloto é o único que poderá tocar no código neste tempo, e enquanto ele estiver progamando seu dever é falar em voz alta para o Co-Piloto tudo que ele estiver fazendo. O Co-Piloto não poderá programar, mas pode falar para o Piloto o que ele deve fazer e guia-lo caso necessário.
  - Daily: Após <b>15 Minutos</b> iremos parar as atividades e realizar um Stand Up, todos irão dizer rapidamente o que fizeram neste tempo. Após o Daily os Pilotos e Co-Pilotos inverterão os papéis.
  - Commits: Os commits devem ser atômicos(1 funcionalidade por commit) e devem seguir o esquema de branches do Gitflow, o nome das Branches criadas deve ser: <b>issue_x_nome_issue</b> sendo "x" o número da Issue. 
  - Pull Request: Ao finalizar sua Issue, a dupla deve solicitar um Pull Request e solicitar outra dupla para revisar e aceita-lo.
  
 ### Revisão da Sprint [10 Minutos]

  - O que foi feito ?: Listar as Issues que foram finalizadas(Pull Requests aceitos)
  - O que não foi feito ?: Listar as issues que não foram finalizadas.
  - Porque não foi feito ?: Listar os problemas e dificuldades que impidiram de finalizar as Issues
  
 ### Retrospectiva da Sprint [10 Minutos]

  - O que deu certo ?: Quais foram os pontos fortes da equipe nesta sprint ? O que funcionou melhor ?
  - O que deu errado ?: O que deu errado do que foi planejado ? Quais fases menos funcionaram ?
  - Como melhorar ?: Para uma próxima Sprint, o que poderia ser feito melhor ? Quais medidas seriam interessantes ? (Listar 3, uma que precisaria ocorrer imediatamente, uma que seria interessante mas não fundamental e uma que poderia um dia ocorrer)

