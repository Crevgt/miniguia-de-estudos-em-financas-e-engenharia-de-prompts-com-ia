# 📚 Miniguia de Estudos e Engenharia de Prompts com IA

Este repositório reúne atividades práticas de aprendizagem ativa com Inteligência Artificial, utilizando ferramentas como NotebookLM, engenharia de prompts e análise estruturada de informações.

O projeto está dividido em três desafios práticos:

* **Desafio 1:** Miniguia de Estudos em Finanças Introdutórias;
* **Desafio 2:** Extraindo Insights do Feedback de Clientes Bancários.
* **Desafio 3:** Detecção de Fraudes com Machine Learning.

---

# 💰 Desafio 1 — Miniguia de Estudos em Finanças Introdutórias

## 🎯 Contexto e Objetivos

Este projeto nasceu de um desafio de aprendizagem ativa com Inteligência Artificial. O objetivo é criar um caderno temático sobre finanças introdutórias no NotebookLM, reunindo fontes abertas e confiáveis, explorando perguntas estratégicas, testando diferentes prompts e consolidando os principais aprendizados em um miniguia de estudo.

A proposta busca utilizar a IA não apenas para obter respostas prontas, mas como uma ferramenta de apoio à aprendizagem ativa, à organização do conhecimento e ao desenvolvimento do pensamento crítico.

### Objetivos principais

* Entender os fundamentos do orçamento doméstico;
* Diferenciar poupança de investimento;
* Compreender crédito, juros e endividamento;
* Entender os impactos da inflação no poder de compra;
* Explorar práticas internacionais de alfabetização financeira;
* Desenvolver prompts reutilizáveis para futuras revisões.

---

## 📚 Curadoria de Fontes

Foram selecionadas cinco fontes abertas e confiáveis, priorizando instituições oficiais e materiais educacionais relacionados à educação financeira e à alfabetização financeira.

| Fonte                                                           | Tipo       | Link                                                                                                                                     |
| --------------------------------------------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Caderno de Educação Financeira – Banco Central                  | PDF/Página | [Banco Central](https://www.bcb.gov.br/cidadaniafinanceira)                                                                   |
| Guia de Planejamento Financeiro – CVM                           | PDF        | [Guia CVM](https://www.gov.br/investidor/pt-br/educacional/publicacoes-educacionais/guias/guia-de-planejamento-financeiro/guia-planejamento-financeiro.pdf)       |
| TOP Planejamento Financeiro Pessoal – CVM                       | Página     | [CVM](https://www.gov.br/cvm/pt-br/assuntos/noticias/2025/cvm-lanca-2a-edicao-do-livro-top-planejamento-financeiro-pessoal)   |
| Entendendo a Inflação – IBGE                                    | Página     | [IBGE](https://educa.ibge.gov.br/jovens/materias-especiais/23189-entendendo-a-inflacao.html)                                  |
| OECD/INFE 2023 International Survey of Adult Financial Literacy | PDF        | [OECD Report](https://www.oecd.org/content/dam/oecd/en/publications/reports/2023/12/oecd-infe-2023-international-survey-of-adult-financial-literacy_8ce94e2c/56003a32-en.pdf) |

### Critérios de seleção

As fontes foram escolhidas considerando:

* Confiabilidade das instituições responsáveis;
* Disponibilidade pública e gratuita;
* Relação direta com o tema estudado;
* Conteúdo adequado para estudantes iniciantes;
* Diversidade de perspectivas sobre educação financeira;
* Possibilidade de utilização no NotebookLM.

---

## ❓ Perguntas Estratégicas

As perguntas foram elaboradas para explorar diferentes níveis de aprendizagem.

### Compreensão

* Quais são os passos para elaborar um orçamento pessoal?
* Qual é a diferença entre receita e despesa?
* Como os juros influenciam empréstimos e investimentos?

### Comparação

* Explique a diferença entre poupança e investimento com exemplos práticos.
* Compare orçamento pessoal e planejamento financeiro.
* Quais são as diferenças entre as abordagens brasileiras e internacionais sobre alfabetização financeira?

### Análise

* Como a falta de planejamento financeiro pode contribuir para o endividamento?
* Como a inflação interfere no poder de compra?
* Quais comportamentos financeiros diferenciam países segundo a OECD?

### Aplicação prática

* Como uma pessoa pode organizar suas finanças mensais?
* Crie um exemplo de orçamento doméstico para uma pessoa que deseja reduzir gastos.
* Como os conceitos estudados podem ajudar uma pessoa a evitar o endividamento?

---

## 🤖 Engenharia de Prompts

Durante o projeto, foram testadas diferentes formas de formular perguntas para observar como a estrutura do prompt influencia a qualidade das respostas.

### Prompt inicial

> Quais os passos para elaborar um orçamento pessoal?

### Prompt melhorado

> Com base exclusivamente nas fontes disponíveis no NotebookLM, explique os passos para elaborar um orçamento pessoal e apresente um exemplo prático de organização mensal.

**Aprendizado:** adicionar contexto, limitar as fontes e solicitar exemplos práticos torna a resposta mais específica e útil.

---

### Prompt de comparação

> Explique a diferença entre poupança e investimento com exemplos práticos.

### Prompt melhorado

> Compare poupança e investimento com base nas fontes disponíveis, considerando objetivo, risco, liquidez e prazo.

**Aprendizado:** definir critérios de comparação melhora a organização da resposta.

---

### Prompt de análise internacional

> Quais comportamentos financeiros diferenciam países segundo a OECD?

### Prompt melhorado

> Com base no relatório OECD/INFE e nas fontes brasileiras selecionadas, compare os principais conhecimentos, comportamentos e atitudes relacionados à alfabetização financeira.

**Aprendizado:** combinar fontes permite construir uma visão mais ampla e comparativa sobre o tema.

---

## 🩹 Cicatrizes e Troubleshooting

Durante a utilização do NotebookLM, algumas dificuldades foram encontradas.

### Respostas muito genéricas

**Problema:** perguntas muito amplas geravam respostas pouco específicas.

**Solução:** adicionar contexto e solicitar exemplos práticos.

**Aprendizado:** a qualidade da pergunta influencia diretamente a qualidade da resposta.

---

### Glossário incompleto

**Problema:** alguns conceitos importantes não apareciam no primeiro resultado.

**Solução:** solicitar explicitamente uma lista de termos com definições curtas e linguagem adequada para iniciantes.

**Aprendizado:** definir formato e critérios melhora a qualidade do resultado.

---

### Falha no processamento de fonte

**Problema:** a página "Entendendo a Inflação", do IBGE, apresentou falha ao ser adicionada diretamente ao NotebookLM.

**Solução:** testar alternativas, como utilizar o conteúdo em formato PDF ou selecionar outra fonte compatível.

**Aprendizado:** diferentes formatos e páginas podem apresentar comportamentos diferentes em ferramentas de IA.

---

## 🧪 Teste — O que é Educação Financeira?

### Prompt utilizado

> O que é educação financeira?

### Resposta obtida

A educação financeira foi definida como um meio de promover comportamentos que contribuem para melhorar o bem-estar financeiro e o exercício da cidadania financeira.

A resposta também apresentou a educação financeira como uma combinação de:

* Conscientização;
* Conhecimento;
* Habilidades;
* Atitudes;
* Comportamentos.

Além disso, foram destacados aspectos relacionados a:

* Planejamento financeiro;
* Consumo;
* Poupança;
* Investimentos;
* Prevenção de riscos;
* Proteção do patrimônio.

A resposta também indicou que decisões financeiras não dependem apenas de conhecimentos matemáticos, mas podem estar relacionadas ao comportamento, às emoções, aos impulsos e às escolhas de consumo.

### Resultado observado

Mesmo utilizando um prompt curto e genérico, a resposta apresentou uma visão ampla sobre educação financeira.

A resposta não se limitou a uma definição simples e relacionou o tema ao bem-estar financeiro, à cidadania financeira, ao comportamento e ao desenvolvimento econômico.

### Cicatriz identificada

Um possível ponto de atenção é que uma resposta ampla pode apresentar muitos conceitos ao mesmo tempo, dificultando a utilização como material de revisão rápida.

### Possível melhoria do prompt

> Com base nas fontes deste notebook, explique o que é educação financeira em linguagem simples e apresente apenas os três conceitos mais importantes para um estudante iniciante.

### Aprendizado

Este teste demonstrou que um prompt simples pode gerar uma resposta rica, mas nem sempre apresenta o conteúdo no formato mais adequado para revisão.

O refinamento do prompt pode ajudar a controlar a profundidade, o tamanho e a organização da resposta.

---

## 📖 Miniguia de Estudo

### 💰 Orçamento

O orçamento é uma ferramenta utilizada para organizar receitas e despesas.

Ele permite:

* Conhecer quanto dinheiro é recebido;
* Identificar os principais gastos;
* Reduzir desperdícios;
* Planejar objetivos financeiros;
* Tomar decisões mais conscientes.

---

### 💳 Crédito

O crédito permite utilizar recursos financeiros antes de possuir o dinheiro necessário.

Pode ser útil em determinadas situações, mas exige atenção aos:

* Juros;
* Prazos;
* Condições de pagamento;
* Risco de endividamento.

---

### 📈 Investimentos e Poupança

A poupança está relacionada à reserva de dinheiro para utilização futura.

Os investimentos envolvem diferentes alternativas para aplicação de recursos, considerando fatores como:

* Risco;
* Rentabilidade;
* Liquidez;
* Prazo.

---

### 📉 Inflação

A inflação representa o aumento generalizado dos preços de produtos e serviços.

Um dos seus principais efeitos é a redução do poder de compra do dinheiro ao longo do tempo.

---

### 🌎 Alfabetização Financeira

A alfabetização financeira envolve conhecimentos, comportamentos e atitudes que ajudam as pessoas a tomar decisões financeiras mais conscientes.

A análise da OECD permite observar o tema também em uma perspectiva internacional.

---

## 📘 Glossário

| Conceito        | Definição                                                                                 |
| --------------- | ----------------------------------------------------------------------------------------- |
| Liquidez        | Facilidade de converter um ativo em dinheiro                                              |
| Juros compostos | Juros calculados sobre o valor inicial e sobre os juros acumulados                        |
| Endividamento   | Situação relacionada ao acúmulo de compromissos financeiros e dívidas                     |
| Inflação        | Aumento generalizado dos preços                                                           |
| Poder de compra | Quantidade de bens e serviços que determinada quantia de dinheiro consegue adquirir       |
| Crédito         | Possibilidade de utilizar recursos financeiros antes de possuir o dinheiro correspondente |
| Orçamento       | Organização das receitas e despesas                                                       |
| Investimento    | Aplicação de recursos com objetivos financeiros futuros                                   |

---

## ♻️ Prompts Reutilizáveis

### Para resumo

> Resuma em cinco linhas o módulo sobre crédito presente nas fontes disponíveis.

### Para criação de glossário

> Monte um glossário com 10 termos financeiros básicos presentes nas fontes e apresente definições curtas para iniciantes.

### Para comparação

> Compare a visão da OECD com as fontes brasileiras sobre alfabetização financeira.

### Para revisão

> Crie cinco perguntas sobre os principais conceitos estudados. Não apresente as respostas imediatamente.

### Para aplicação prática

> Crie uma situação fictícia de uma pessoa com dificuldades financeiras e explique como os conceitos presentes nas fontes podem ajudá-la.

---

## 🎓 Principais Aprendizados

O desenvolvimento deste projeto demonstrou que a Inteligência Artificial pode apoiar significativamente a organização e a revisão de conteúdos.

Entretanto, a qualidade dos resultados depende de fatores como:

* Qualidade das fontes selecionadas;
* Clareza dos objetivos;
* Formulação das perguntas;
* Estrutura dos prompts;
* Verificação das referências;
* Capacidade crítica do estudante.

A principal conclusão do projeto é que a IA pode acelerar a organização da informação, mas o pensamento crítico continua sendo essencial para transformar informação em conhecimento.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# 🎯 Desafio 2 — Extraindo Insights do Feedback de Clientes Bancários

## 🎯 Contexto e Objetivo

Este desafio tem como objetivo explorar o uso de Inteligência Artificial para analisar feedbacks de clientes sobre a experiência de uso de um aplicativo bancário.

A proposta é construir e refinar um prompt capaz de transformar comentários de clientes em informações organizadas e úteis para apoiar decisões relacionadas à experiência do cliente e à melhoria do aplicativo.

---

## 1. 🎯 Definição da Intenção

### Tipo de feedback

Feedbacks de clientes relacionados à experiência de uso de um aplicativo bancário, incluindo acesso à conta, navegação e utilização das funcionalidades disponíveis.

### Usuários do resultado

As informações serão utilizadas pelas equipes de experiência do cliente e desenvolvimento digital.

### Decisões apoiadas

O resultado deverá apoiar decisões relacionadas à melhoria da usabilidade, da experiência dos usuários e do funcionamento do aplicativo.

### Formato esperado

A entrega deverá conter:

* Resumo executivo;
* Principais temas identificados;
* Classificação dos feedbacks;
* Principais prioridades;
* Recomendações de possíveis ações;
* Limitações da análise.

### Critério de qualidade

O resultado será considerado adequado quando apresentar informações claras, organizadas, baseadas exclusivamente nos feedbacks fornecidos e úteis para identificar as principais prioridades de melhoria.

---

## 2. 🧩 Contexto e Restrições

### Contexto

Trabalho com a análise de feedbacks de clientes relacionados à experiência de uso de um aplicativo bancário, incluindo aspectos como acesso à conta, navegação e utilização das funcionalidades disponíveis.

### Dados disponíveis

* Data do feedback;
* Texto do comentário;
* Funcionalidade mencionada;
* Nota de satisfação.

Esses dados serão considerados conforme sua disponibilidade na base fornecida.

### Critérios de análise

A IA deve classificar os feedbacks por:

* Tema;
* Sentimento;
* Nível de urgência;
* Tipo de manifestação.

O tipo de manifestação deverá indicar se o comentário representa:

* Reclamação;
* Elogio;
* Sugestão;
* Dúvida.

### Cuidados e restrições

* Use apenas os dados fornecidos para realizar a análise.
* Não invente informações, números, causas ou conclusões.
* Não exponha ou reproduza dados pessoais ou sensíveis dos clientes.
* Caso existam informações pessoais nos comentários, ignore esses dados durante a análise.
* Não apresente suposições como se fossem fatos.
* Caso não existam informações suficientes para uma conclusão, informe essa limitação.
* Considere tanto os feedbacks positivos quanto os negativos.
* Use linguagem simples, clara e objetiva, voltada para a tomada de decisão.

---

## 3. 🛠️ Construção e Refinamento do Prompt

O prompt foi estruturado utilizando os seguintes elementos:

* Papel da IA;
* Objetivo da análise;
* Contexto;
* Dados disponíveis;
* Critérios de classificação;
* Formato da resposta;
* Restrições e cuidados.

Durante o refinamento, foi identificada a necessidade de tornar o conceito de urgência mais objetivo.

### Critérios de urgência adicionados

**Baixa:** elogios, dúvidas simples ou sugestões sem impacto imediato na utilização do serviço.

**Média:** problemas que dificultam determinada funcionalidade ou experiência, mas não impedem completamente sua utilização.

**Alta:** problemas que impedem ou comprometem significativamente o acesso à conta, a realização de transações ou a utilização de funcionalidades essenciais.

Também foi incluída uma orientação para diferenciar fatos, interpretações e recomendações.

---

## 4. 🧪 Teste do Prompt

Para testar o funcionamento do prompt, foi utilizada uma base fictícia de feedbacks de clientes.

| ID | Data       | Funcionalidade | Nota | Feedback                                                                                |
| -- | ---------- | -------------- | ---: | --------------------------------------------------------------------------------------- |
| 01 | 01/09/2026 | Login          |    2 | O aplicativo demora muito para abrir e algumas vezes não consigo acessar minha conta.   |
| 02 | 01/09/2026 | Pix            |    1 | Tentei fazer um Pix várias vezes, mas o aplicativo apresentou erro.                     |
| 03 | 02/09/2026 | Navegação      |    5 | Gostei da nova versão. Agora ficou muito mais fácil encontrar as opções que procuro.    |
| 04 | 02/09/2026 | Cartão         |    3 | Seria interessante conseguir visualizar meus gastos do cartão de forma mais organizada. |
| 05 | 02/09/2026 | Pix            |    2 | Fiz uma transferência e tive dificuldade para encontrar o comprovante.                  |
| 06 | 02/09/2026 | Segurança      |    4 | Gostei da confirmação por biometria, ficou mais fácil e rápido acessar minha conta.     |

### Resultado observado

O teste permitiu identificar:

* Problemas relacionados ao Pix;
* Dificuldades de acesso e desempenho;
* Problemas de localização de informações;
* Sugestões relacionadas à organização dos gastos do cartão;
* Avaliações positivas da navegação;
* Avaliações positivas relacionadas à autenticação biométrica.

### Aprendizado do teste

O teste demonstrou que a estrutura do prompt permite organizar os feedbacks de acordo com diferentes critérios e transformar comentários individuais em informações mais estruturadas para análise.

Também foi possível perceber que critérios subjetivos, como nível de urgência, precisam ser definidos explicitamente para reduzir interpretações diferentes pela IA.

---

## 5. 📌 Prompt Final Refinado

### Papel

Atue como um analista de experiência do cliente especializado em serviços bancários digitais.

### Objetivo

Analise os feedbacks fornecidos por clientes sobre a experiência de uso de um aplicativo bancário, com o objetivo de identificar os principais problemas, elogios, padrões recorrentes e oportunidades de melhoria relacionados ao acesso à conta, navegação e utilização das funcionalidades disponíveis.

A análise será utilizada pelas equipes de experiência do cliente e desenvolvimento digital para apoiar decisões relacionadas à melhoria da experiência dos usuários e do aplicativo bancário.

### Dados disponíveis

A base poderá conter:

* Data do feedback;
* Texto do comentário;
* Funcionalidade mencionada;
* Nota de satisfação.

Considere cada informação conforme sua disponibilidade na base fornecida. Não presuma a existência de dados que não estejam disponíveis.

### Instruções de análise

1. Classifique o tema principal, considerando, quando aplicável, categorias como login e acesso, navegação, Pix, cartão, segurança, desempenho ou outras funcionalidades.
2. Classifique o sentimento como positivo, negativo ou neutro.
3. Identifique o tipo de manifestação como reclamação, elogio, sugestão ou dúvida.
4. Classifique o nível de urgência como baixo, médio ou alto, utilizando:

   * Baixa: elogios, dúvidas simples ou sugestões que não indiquem impacto imediato na utilização do serviço.
   * Média: problemas que dificultem determinada funcionalidade ou experiência, mas não impeçam completamente sua utilização.
   * Alta: problemas que impeçam ou comprometam significativamente o acesso à conta, a realização de transações ou a utilização de funcionalidades essenciais.
5. Identifique os principais problemas, elogios, padrões recorrentes e oportunidades de melhoria.
6. Apresente evidências baseadas nos feedbacks fornecidos.
7. Sugira ações práticas relacionadas aos problemas e oportunidades identificados.
8. Diferencie claramente:

   * Fato: informação diretamente observada nos feedbacks;
   * Interpretação: entendimento possível a partir das evidências;
   * Recomendação: ação sugerida com base na análise.
9. Quando houver informações insuficientes para realizar uma classificação ou chegar a uma conclusão, indique explicitamente essa limitação.

### Formato da resposta

#### 1. Resumo executivo

Síntese objetiva dos principais insights.

#### 2. Tabela de análise

| ID | Tema | Sentimento | Urgência | Tipo de manifestação | Evidência | Ação sugerida |
| -- | ---- | ---------- | -------- | -------------------- | --------- | ------------- |

#### 3. Principais insights

Apresente os principais problemas, elogios, padrões recorrentes e oportunidades.

#### 4. Principais prioridades

Apresente até três prioridades, considerando relevância, impacto aparente e urgência.

#### 5. Limitações da análise

Informe limitações e conclusões que não podem ser obtidas com segurança.

### Cuidados e restrições

* Utilize exclusivamente os dados fornecidos.
* Não invente informações, números, estatísticas, causas ou conclusões.
* Não atribua causas técnicas aos problemas quando elas não estiverem explicitamente presentes nos feedbacks.
* Não apresente suposições ou interpretações como fatos.
* Não exponha, reproduza ou destaque dados pessoais ou sensíveis dos clientes.
* Caso existam informações pessoais nos comentários, ignore essas informações durante a análise.
* Considere tanto os feedbacks positivos quanto os negativos.
* Não determine a frequência ou representatividade de um problema sem dados suficientes.
* Caso a quantidade de feedbacks seja insuficiente para generalizar os resultados, informe essa limitação.
* Use linguagem simples, clara, objetiva e voltada para tomada de decisão.

---

## 6. 🎓 Principais Aprendizados

Este desafio demonstrou que um bom prompt não depende apenas de uma pergunta bem formulada.

A qualidade da análise também depende da definição clara de:

* Objetivo;
* Contexto;
* Dados disponíveis;
* Critérios de classificação;
* Formato da resposta;
* Restrições;
* Limitações.

Outro aprendizado importante foi perceber que critérios subjetivos precisam ser definidos de maneira explícita. Neste caso, a definição dos níveis de urgência tornou a classificação mais consistente.

O desafio também reforçou a importância de evitar que a IA transforme interpretações em fatos ou atribua causas que não estejam presentes nos dados.

Por fim, o exercício mostrou como a engenharia de prompts pode ser utilizada para transformar dados textuais não estruturados em informações organizadas para apoiar processos de análise e tomada de decisão.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


📊 Desafio 3 — Detecção de Fraudes com Machine Learning
📌 Sobre o projeto

Este desafio consiste na aplicação de técnicas de Machine Learning para identificar possíveis transações fraudulentas em um conjunto de dados de operações com cartão de crédito.

O projeto foi desenvolvido com Python e bibliotecas voltadas para análise de dados, aprendizado de máquina e interpretação de modelos.

Foram utilizados dois modelos de classificação:

Regressão Logística;
Random Forest.

Além da comparação entre os modelos, também foram analisados diferentes limiares de classificação e técnicas de interpretação das variáveis utilizadas pelos modelos.

📚 Base de dados

Foi utilizado um conjunto de dados público de transações com cartão de crédito.

O conjunto possui:

284.807 transações
31 colunas
492 transações fraudulentas
284.315 transações normais

A variável Class representa o resultado da transação:

0 — transação normal
1 — transação fraudulenta

As variáveis V1 a V28 são componentes resultantes de uma transformação PCA aplicada aos dados originais. Por esse motivo, elas não possuem interpretação direta de negócio.

⚠️ Desbalanceamento das classes

O conjunto apresenta forte desbalanceamento entre as classes.

A quantidade de transações normais é muito superior à quantidade de transações fraudulentas.

Por esse motivo, a avaliação dos modelos não foi baseada apenas na acurácia.

Foram consideradas principalmente:

Precision
Recall
F1-score
ROC AUC
Average Precision
Falsos positivos
Falsos negativos
🔧 Preparação dos dados

Foi criada uma nova variável denominada log_amount a partir da variável Amount.

A transformação utilizada foi:

log_amount = np.log1p(df["Amount"])

A variável original Amount foi mantida no conjunto de dados.

Também foi realizada uma divisão estratificada dos dados em treinamento e teste, mantendo a proporção das classes.

📊 Divisão dos dados

Foi utilizada uma divisão de:

80% para treinamento
20% para teste

A divisão foi realizada de forma estratificada para preservar a proporção entre transações normais e fraudulentas.

Conjunto de treinamento
227.845 registros
227.451 transações normais
394 transações fraudulentas
Conjunto de teste
56.962 registros
56.864 transações normais
98 transações fraudulentas
🧪 Amostra utilizada no treinamento

Devido às limitações de hardware disponíveis para a execução do experimento, foi utilizada uma amostra estratificada de 50.000 registros para o treinamento dos modelos.

Essa escolha permitiu realizar os experimentos mantendo uma proporção das classes compatível com o conjunto original.

Os resultados apresentados neste projeto estão relacionados a essa configuração experimental.

📏 Padronização das variáveis

Foi utilizado o StandardScaler para padronizar as variáveis numéricas.

O scaler foi ajustado somente utilizando os dados de treinamento.

Depois disso, a transformação foi aplicada aos dados de teste.

Essa separação evita que informações do conjunto de teste sejam utilizadas durante o ajuste do processo de treinamento.

📊 Regressão Logística

Foi utilizado o modelo de Regressão Logística com tratamento do desbalanceamento das classes:

class_weight="balanced"

Também foram definidos:

max_iter=300
random_state=42
Resultados

Precision: 0,0764

Recall: 0,9082

F1-score: 0,1409

ROC AUC: 0,9616

Average Precision: 0,6945

Matriz de confusão
Verdadeiros negativos (TN): 55.788
Falsos positivos (FP): 1.076
Falsos negativos (FN): 9
Verdadeiros positivos (TP): 89

O modelo identificou 89 das 98 transações fraudulentas presentes no conjunto de teste, deixando 9 fraudes sem identificação.

Ao mesmo tempo, foram classificadas incorretamente 1.076 transações normais como possíveis fraudes.

Esse resultado demonstra um comportamento com Recall elevado e grande quantidade de falsos positivos.

📈 Curvas ROC e Precision-Recall

As curvas ROC e Precision-Recall foram utilizadas para complementar a avaliação do modelo.

Curva ROC




Curva Precision-Recall




🌲 Random Forest

Também foi utilizado o algoritmo Random Forest.

A configuração principal utilizada foi:

n_estimators=100
class_weight="balanced"
random_state=42
n_jobs=-1
Resultados

Precision: 0,8261

Recall: 0,7755

F1-score: 0,8000

ROC AUC: 0,9571

Average Precision: 0,8191

Matriz de confusão
Verdadeiros negativos (TN): 56.848
Falsos positivos (FP): 16
Falsos negativos (FN): 22
Verdadeiros positivos (TP): 76

O modelo identificou 76 das 98 transações fraudulentas presentes no conjunto de teste.

Foram registrados:

16 falsos positivos
22 falsos negativos

Nesse experimento, o Random Forest apresentou uma quantidade muito menor de falsos positivos em comparação com a Regressão Logística, enquanto apresentou Recall inferior.

🔎 Comparação entre os modelos

Os modelos apresentaram comportamentos diferentes diante do problema de detecção de fraudes.

Regressão Logística
Precision: 0,0764
Recall: 0,9082
F1-score: 0,1409
ROC AUC: 0,9616
Average Precision: 0,6945
Falsos positivos: 1.076
Falsos negativos: 9
Random Forest
Precision: 0,8261
Recall: 0,7755
F1-score: 0,8000
ROC AUC: 0,9571
Average Precision: 0,8191
Falsos positivos: 16
Falsos negativos: 22

A Regressão Logística apresentou Recall mais elevado, enquanto o Random Forest apresentou quantidade muito menor de falsos positivos no experimento realizado.

Essa diferença demonstra a importância de analisar diferentes métricas e tipos de erro em problemas de classificação de fraudes.

🎚️ Ajuste do limiar de classificação

Além da avaliação utilizando o limiar padrão de 0,50, foram realizados experimentos com diferentes valores de limiar no Random Forest.

Limiar 0,10
Precision: 0,5658
Recall: 0,8776
F1-score: 0,6880
Falsos positivos: 66
Falsos negativos: 12
Limiar 0,20
Precision: 0,7568
Recall: 0,8571
F1-score: 0,8038
Falsos positivos: 27
Falsos negativos: 14
Limiar 0,30
Precision: 0,8283
Recall: 0,8367
F1-score: 0,8325
Falsos positivos: 17
Falsos negativos: 16
Limiar 0,40
Precision: 0,8229
Recall: 0,8061
F1-score: 0,8144
Falsos positivos: 17
Falsos negativos: 19
Limiar 0,50
Precision: 0,8261
Recall: 0,7755
F1-score: 0,8000
Falsos positivos: 16
Falsos negativos: 22
Limiar 0,60
Precision: 0,8434
Recall: 0,7143
F1-score: 0,7735
Falsos positivos: 13
Falsos negativos: 28
Limiar 0,70
Precision: 0,8571
Recall: 0,6735
F1-score: 0,7543
Falsos positivos: 11
Falsos negativos: 32
Limiar 0,80
Precision: 0,8806
Recall: 0,6020
F1-score: 0,7152
Falsos positivos: 8
Falsos negativos: 39
Limiar 0,90
Precision: 0,9600
Recall: 0,4898
F1-score: 0,6486
Falsos positivos: 2
Falsos negativos: 50
🔎 Análise do limiar 0,30

No experimento realizado, o limiar de 0,30 apresentou:

Precision: 0,8283
Recall: 0,8367
F1-score: 0,8325
Falsos positivos: 17
Falsos negativos: 16

Esse resultado demonstra como a alteração do limiar modifica o equilíbrio entre Precision, Recall, falsos positivos e falsos negativos.

O valor de 0,30 foi utilizado como uma configuração de análise neste projeto.

Ele não deve ser interpretado como um valor universal ou como uma configuração definitiva para utilização em produção.

Em um ambiente real, a escolha do limiar dependeria dos custos associados aos falsos positivos e falsos negativos, do volume de alertas e das regras operacionais do sistema.

Visualização dos resultados







🧠 Importância das variáveis — Random Forest

Foi analisada a importância das variáveis utilizadas pelo Random Forest.

As dez variáveis com maior importância foram:

V14 — 0,190810
V10 — 0,152877
V11 — 0,110281
V12 — 0,085792
V4 — 0,073071
V17 — 0,071463
V3 — 0,045616
V2 — 0,029481
V7 — 0,029128
V16 — 0,023570

Esses valores representam a importância atribuída pelo modelo às variáveis utilizadas nas decisões das árvores.

Como as variáveis V1 a V28 são componentes resultantes de PCA, esses resultados não devem ser interpretados diretamente como características de negócio.

Visualização




🔬 Interpretação do modelo com SHAP

Para complementar a análise das variáveis, foi utilizada a biblioteca SHAP.

Foi realizada uma análise utilizando uma amostra aleatória de 1.000 registros do conjunto de teste.

A métrica utilizada para ordenar as variáveis foi o valor médio absoluto de SHAP.

As dez maiores contribuições em magnitude foram:

V14 — 0,070266
V12 — 0,067754
V11 — 0,054054
V10 — 0,051748
V4 — 0,050359
V3 — 0,038146
V17 — 0,029625
V9 — 0,020391
V7 — 0,015777
V2 — 0,014759
Comparação entre Random Forest e SHAP

Foi observado que várias das variáveis com maior importância no Random Forest também aparecem entre as variáveis com maiores valores médios absolutos de SHAP.

Entre elas:

V14
V12
V11
V10
V4
V3
V17

Essa sobreposição fornece uma visão complementar do comportamento do modelo.

Entretanto, o valor médio absoluto de SHAP representa a magnitude da contribuição da variável para as previsões analisadas.

Ele não indica, isoladamente, se a variável aumenta ou diminui a probabilidade prevista de fraude.

Além disso, a importância de uma variável não deve ser interpretada como causalidade.

Visualização SHAP




🔄 O que foi alterado em relação à abordagem da Expert

A abordagem inicial foi ampliada para incluir uma análise mais detalhada do comportamento dos modelos.

Foram realizadas as seguintes alterações:

inclusão da transformação log_amount para a variável Amount;
utilização de divisão estratificada entre treinamento e teste;
utilização de uma amostra de 50.000 registros para o treinamento devido às limitações de hardware;
comparação entre Regressão Logística e Random Forest;
análise de Precision, Recall, F1-score, ROC AUC e Average Precision;
análise das matrizes de confusão;
avaliação das curvas ROC e Precision-Recall;
análise de diferentes limiares de classificação;
análise das variáveis mais importantes no Random Forest;
utilização do SHAP para complementar a interpretação do modelo;
análise conjunta dos resultados para compreender os diferentes comportamentos dos modelos.
⚠️ Limitações do experimento

Os resultados apresentados devem ser interpretados considerando algumas limitações:

o treinamento foi realizado utilizando uma amostra de 50.000 registros, devido às limitações de hardware;
os resultados dependem da divisão específica entre treinamento e teste utilizada no experimento;
o conjunto de dados utilizado possui forte desbalanceamento entre as classes;
as variáveis V1 a V28 são componentes resultantes de transformação PCA e não possuem interpretação direta de negócio;
a escolha do limiar de classificação pode alterar significativamente Precision, Recall, falsos positivos e falsos negativos;
o limiar analisado neste projeto não deve ser considerado uma configuração de produção;
dados históricos podem não representar comportamentos futuros;
a análise SHAP descreve o comportamento do modelo, mas não estabelece relações de causalidade;
em um ambiente real, seria necessário considerar custos de falsos positivos e falsos negativos, volume de alertas, análise manual, atualização do modelo e mudanças no comportamento das transações.
📊 Conclusão

O projeto demonstrou a aplicação de técnicas de Machine Learning para a detecção de possíveis transações fraudulentas em um conjunto de dados desbalanceado.

A utilização de dois modelos permitiu observar diferentes comportamentos.

A Regressão Logística apresentou Recall mais elevado, identificando uma parcela maior das fraudes, mas também produziu uma quantidade significativamente maior de falsos positivos.

O Random Forest apresentou uma quantidade muito menor de falsos positivos no experimento realizado, enquanto apresentou Recall inferior ao da Regressão Logística.

A análise de diferentes limiares mostrou que a alteração do ponto de decisão modifica o equilíbrio entre Precision, Recall, falsos positivos e falsos negativos.

O uso do SHAP também permitiu complementar a análise da importância das variáveis, ajudando a compreender quais componentes tiveram maior influência nas previsões do modelo.

Dessa forma, o projeto demonstra que a avaliação de um sistema de detecção de fraudes não deve considerar apenas uma única métrica.

É necessário analisar o comportamento dos modelos, os tipos de erro e o impacto da escolha do limiar de classificação.

📁 Arquivos e resultados

Os principais arquivos utilizados no projeto estão disponíveis na pasta:

deteccao-fraudes/

Arquivos principais
projeto.py — código principal do projeto
projeto.ipynb — versão do projeto em Jupyter Notebook
comparacao_modelos.csv — comparação dos modelos
resultados_threshold.csv — resultados dos diferentes limiares
resultados_threshold_random_forest.csv — resultados dos limiares do Random Forest
importancia_variaveis_random_forest.csv — importância das variáveis
importancia_shap.csv — resultados da análise SHAP
Visualizações
curva_roc.png — curva ROC
curva_precision_recall.png — curva Precision-Recall
precision_recall_threshold_random_forest.png — relação entre Precision e Recall conforme o limiar
erros_threshold_random_forest.png — comportamento dos erros conforme o limiar
importancia_variaveis_random_forest.png — importância das variáveis no Random Forest
shap_importancia.png — importância das variáveis segundo SHAP

O arquivo creditcard.csv não foi incluído no repositório.

▶️ Execução

Para executar o projeto, é necessário ter o Python instalado e as bibliotecas utilizadas no projeto disponíveis no ambiente.

O projeto pode ser executado diretamente pelo arquivo:

projeto.py

Também é possível utilizar a versão:

projeto.ipynb

A versão em Notebook permite acompanhar as etapas do processamento, treinamento, avaliação e interpretação dos modelos de forma interativa.
