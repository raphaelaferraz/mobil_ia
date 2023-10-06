Documentação Modelo Preditivo - Inteli

<img width="50%" alt="image" src="https://github.com/2023M3T9-Inteli/grupo1/assets/124217721/b2bb64d2-a186-4f52-9894-9d3c74615820">

### The Lorean
#### Ana Clara Madureira Marques, Heitor Elias Prudente, Henrique Cox Cabral Oliveira de Moura, Kaleb Isaias Souza de Carvalho, Lucas da Silva Barbosa, Raphaela Guiland Ferraz

## Sumário
[1. Introdução](#c1)

[2. Objetivos e Justificativa](#c2)

[3. Metodologia](#c3)

[4. Desenvolvimento e Resultados](#c4)

[5. Conclusões e Recomendações](#c5)

[6. Referências](#c6)

[Anexos](#attachments)


## <a name="c1"></a>1. Introdução

&emsp;&emsp; O parceiro de negócios deste projeto é a Mobly, uma empresa de médio porte com sede em São Paulo, Brasil. A Mobly atua no setor de comércio eletrônico de móveis e possui quatro lojas físicas na região de São Paulo, além de centros de distribuição em outros estados do país. Nesse sentido, a Mobly é reconhecida por oferecer uma ampla variedade de móveis e produtos para o lar [7].

&emsp;&emsp; O problema a ser resolvido neste projeto está relacionado à gestão de estoque da Mobly. Atualmente, a empresa enfrenta desafios relacionados ao controle e previsão de estoque, o que pode resultar na falta ou no excesso de produtos em estoque, afetando negativamente a eficiência operacional da organização e a satisfação de seus consumidores.

## <a name="c2"></a>2. Objetivos e Justificativa
### 2.1 Objetivos
#### 2.1.1 Objetivo Geral
&emsp;&emsp; A definição do objetivo geral é crucial, uma vez que ele é responsável por apresentar a ideia central do desenvolvimento de um projeto. Nesse contexto, o objetivo geral deste projeto é desenvolver um modelo preditivo denominado "Mobil.ia". Esse modelo será utilizado internamente pela equipe de Business Intelligence (BI) da empresa parceira Mobly, com o propósito de prever a quantidade de itens vendidos de produtos específicos (SKU's) ao longo de um período, que poderá ser semanal ou trimestral.
#### 2.1.2 Objetivos Específicos
&emsp;&emsp; Já a definição dos objetivos específicos é algo de extrema importância, dado que são eles que definem quais são os resultados que o projeto pretende alcançar, fazendo com que seja possível garantir o objetivo geral. Nesse sentido, os objetivos específicos deste projeto são:
* Realizar o entendimento do Termo de Abertura de Projeto do Inteli (TAPI);
* Realizar o entendimento da metodologia CRISP-DM;
* Realizar o entendimento do funcionamento mercadológico da Mobly;
* Realizar o entendimento dos dados fornecidos pela Mobly;
* Realizar o mapeamento das tecnologias utilizadas para o desenvolvimento do modelo preditivo;
* Realizar a preparação dos dados;
* Estudar sobre a biblioteca Pandas e Numpy;
* Estudar sobre as bibliotecas responsáveis por realizar a plotagem de gráficos;
* Estudar sobre as bibliotecas responsáveis por fornecer os algoritmos de aprendizagem de máquina;
* Estudar sobre as métricas que serão utilizadas para realizar a sua validação.

### 2.2 Proposta de solução
&emsp;&emsp; A solução desenvolvida trata-se de um modelo preditivo que irá entender, de forma detalhada, o processo atual que compõe o abastecimento do estoque de produtos da Mobly. O objetivo desse entendimento é fundamentado no pedido da empresa parceira de tornar o estoque mais otimizado, conforme os pedidos efetuados pelos consumidores, a fim de diminuir possíveis perdas de produtos, perda de clientes e perda de lucro.

&emsp;&emsp; O modelo preditivo, por meio da análise da base de dados fornecida pela organização, conseguirá prever a quantidade de produtos que os consumidores irão adquirir em um determinado período de tempo, que pode variar de dias até meses. Essa previsão será crucial para estipular quais materiais são verdadeiramente necessários no estoque, a fim de atender às demandas dos clientes, evitando perdas de materiais devido ao baixo giro de produtos ou perda de clientes devido à carência de um determinado produto.
 
&emsp;&emsp; Portanto, a solução proposta visa amenizar a dor apresentada pela Mobly, relacionada a um estoque pouco equilibrado em relação às demandas de seus clientes. Isso pode trazer benefícios significativos para a instituição, uma vez que os stakeholders, de forma geral, poderão usufruir dos resultados da solução devido a sua precisão, confiabilidade e acurácia.

### 2.3 Justificativa
&emsp;&emsp; A proposta de desenvolver o modelo preditivo "Mobil.ia" para otimizar o abastecimento do estoque da Mobly apresenta diversas justificativas sólidas e benefícios significativos para a empresa e seus stakeholders. Aqui estão algumas razões que sustentam essa proposta:

* Redução de custos: Ao prever com precisão a demanda por produtos, a Mobly poderá evitar o excesso de estoque e, ao mesmo tempo, garantir que os produtos certos estejam disponíveis quando os clientes precisarem. Isso reduzirá os custos associados ao armazenamento de produtos em excesso e evitará perdas devido à falta de produtos em demanda.
* Melhoria na experiência do cliente: Com o modelo preditivo, a Mobly poderá atender às expectativas dos clientes de forma mais eficaz, garantindo que os produtos que desejam estejam sempre disponíveis. Isso resultará em uma melhor experiência do cliente, maior satisfação e, consequentemente, fidelização.
* Aumento da receita: Ao evitar a falta de produtos populares, a Mobly poderá aumentar as vendas e, assim, aumentar a receita. Além disso, a otimização do estoque permite a alocação mais eficiente de recursos financeiros.
* Competitividade no mercado: Empresas que podem responder rapidamente às demandas dos clientes têm uma vantagem competitiva significativa. O modelo preditivo permitirá que a Mobly seja mais ágil na adaptação às tendências do mercado e às mudanças nas preferências dos consumidores.
* Sustentabilidade: Reduzir o desperdício de produtos devido à falta de demanda não apenas economiza recursos financeiros, mas também é ecologicamente responsável. Menos produtos desperdiçados resultam em uma pegada ambiental mais leve.
* Aprendizado contínuo: O desenvolvimento e a implementação desse modelo preditivo também oferecerão oportunidades de aprendizado contínuo para a equipe de Business Intelligence (BI) da Mobly, capacitando-os a lidar com análises de dados avançadas e machine learning. O modelo exige que seja continuamente treinado e atualizado com novos dados para permanecer preciso e relevante, e por isso a equipe de BI deve estar preparada para gerenciar e manter o modelo ao longo do tempo.

&emsp;&emsp; Portanto, a proposta não só aborda um problema real que a Mobly enfrenta, mas também demonstra a disposição da empresa em adotar tecnologias avançadas, como análise de dados e machine learning, para se manter à frente no mercado de varejo. Além disso, a utilização de metodologias bem estabelecidas, como CRISP-DM, garante uma abordagem robusta e confiável para o desenvolvimento do modelo.

## <a name="c3"></a>3. Metodologia
&emsp;&emsp; A metodologia utilizada para o desenvolvimento da Mobil.ia foi a CRISP-DM, a qual significa Cross Industry Standard Process for Data Mining. Desse modo, a CRISP-DM é uma metodologia ágil que ajuda a estruturar, de forma robusta, o planejamento de projetos que envolvem aprendizagem de máquina, análise de dados e mineração de dados [8]. Sendo assim, a figura 1 evidencia como é a organização da metodologia.

###### Figura 1 - Funcionamento da Metodologia CRISP-DM
![Funcionamento da Metodologia CRISP-DM](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/31d57b3b-1d8f-48af-971e-9bfc1a4c5067)
###### Fonte: [Metodologias de Mineração de Dados - CRISP](https://www.linkedin.com/pulse/metodologias-de-minera%C3%A7%C3%A3o-dados-crisp-fernanda-ministerio/?originalSubdomain=pt)

&emsp;&emsp; Em relação ao funcionamento da CRISP-DM, ela é fundamentada em um ciclo, uma vez que o projeto pode ser composto por diversos dados e, por conta disso, é possível sempre verificar se o projeto desenvolvido está atendendo ou não as regras de negócio estabelecidas pelo cliente [8]. Assim, o processo cíclico da metodologia fornece a possibilidade de retornar aos estágios anteriores sempre que for necessário, dependendo do andamento do projeto. Portanto, a autora aponta que o principal diferencial do CRISP-DM em relação às outras metodologias está na conexão entre cada etapa da metodologia. 
Tendo em vista a figura 1, a metodologia CRISP-DM é composta por algumas etapas, as quais são:
1. **Entendimento do negócio:** Nesta etapa é realizado um estudo aprofundado em relação ao negócio ou ao projeto, de modo a entender os objetivos e os interesses do cliente;
2. **Entendimento dos dados:** Esta etapa do ciclo consiste no entendimento aprofundado dos dados, de modo a realizar a **coleta de dados**, a **exploração** e a **mineração**. A partir desse estágio é possível construir uma familiaridade com os dados fornecidos pelo cliente, algo de extrema importância quando for realizar a modelagem dos dados;
3. **Preparação dos dados:** Nesta etapa é realizada a seleção dos dados que serão de fato utilizados para a modelagem. Sendo assim, para que tal seleção possa ocorrer de maneira concisa, é possível realizar alguns passo a passos, como: seleção em si, a qual é realizada a escolha dos dados mais relevantes; limpeza de dados, a qual tem o intuito de verificar se há dados insuficientes e, caso tenha, excluir tais dados ou tratar de alguma forma; construção de dados, a qual está relacionada à construção de um novo conjunto de dados depois da limpeza; integração dos dados, a qual tem como objetivo mesclar os dados para que se tenha um conjunto de dados consistentes;
4. **Modelagem:** Nesta etapa são escolhidas técnicas e algoritmos relacionados ao Aprendizado de Máquina e, por consequência disso, esta etapa fica em constante repetição com a etapa anterior para que seja possível comparar os resultados e, assim, escolher qual será a melhor solução para o cliente;
5. **Avaliação:** Nesta etapa será realizada a avaliação da qualidade e segurança dos resultados obtidos pela etapa anterior, a etapa de modelagem. Com isso, o principal diferencial da metodologia CRISP-DM está nesta etapa, haja vista que ela retoma a etapa de entendimento do negócio com o intuito de verificar se o modelo desenvolvido até o momento está coerente com os objetivos de negócios da empresa;
6. **Implantação:** Esta etapa só é realizada quando é atingida com sucesso todos os objetivos das etapas anteriores. Sendo assim, nesta etapa começa o desenvolvimento de fato dos modelos que foram criados e avaliados anteriormente. 

&emsp;&emsp; Desse modo, para que o desenvolvimento da Mobil.ia pudesse seguir tais etapas da CRISP-DM, foi necessário atribuir cada sprint para cada uma dessas etapas e, de um modo geral, é possível definir que: 
* Sprint 1: Partimos da primeira etapa da metodologia, de modo a entendermos como é o modelo de negócios da Mobly;
* Sprint 2: Depois de realizarmos o entendimento de negócios da empresa parceira, partimos para o entendimento dos dados que nos foram disponibilizados;
* Sprint 3: Depois de ser revisar o entendimento do negócios da Mobly (primeira etapa da metodologia) e depois de realizarmos o entendimento dos dados (segunda etapa), partimos para a preparação dos dados e para a modelagem de tais dados;
* Sprint 4: A partir da modelagem desenvolvida, partimos para a etapa de avaliação, a qual iremos verificar se a Mobil.ia está alinhada com os propósitos mercadológicos da Mobly. Essa avaliação será realizada de três formas:
    1. Como diferencial do CRISP-DM é retornar para a etapa de entendimento de negócios, nós realizaremos tal retorno, uma vez que, nessa etapa, desenvolvemos alguns artefatos atrelados ao entendimento do negócio da Mobly, algo que servirá de auxílio para identificar a relação entre a Mobil.ia e os objetivos de negócios da Mobly;
    2. Além da retomada da etapa de entendimento de negócios, iremos avaliar o modelo por meio de métricas específicas de regressão, como MAE (Erro Absoluto Médio), MSE (Erro Quadrático Médio), RMSE (Raiz Quadrada do Erro Médio) e R^2 (Coeficiente de Determinação), os quais indicarão numericamente a eficiência e a precisão da Mobil.ia;
    3. Após entendermos o alinhamento da Mobil.ia com a Mobly e após avaliarmos as métricas de regressão aplicadas ao modelo desenvolvido, iremos apresentar o nosso modelo preditivo para o parceiro, de modo que eles possam ponderar, de forma clara e direta, a compatibilidade entre o que foi desenvolvido e a Mobly, algo de extrema importância para a avaliação final do modelo. 
* Sprint 5: Depois de validarmos com o parceiro tudo que já foi desenvolvido, iremos ajustar a Mobil.ia através de todas as ponderações realizadas pelo parceiro, fazendo com que o projeto esteja totalmente alinhado com a Mobly.


## <a name="c4"></a>4. Desenvolvimento e Resultados
### 4.1. Compreensão do Problema
#### 4.1.1. Contexto da indústria 

&emsp;&emsp; A Mobly é uma empresa que está dentro do segmento de venda de móveis (ou, de forma
mais abrangente, casa e decoração) e, portanto, é uma empresa que utiliza do modelo B2C
como principal, ou seja,  “Business to Consumer” (Empresa para Consumidor) como a maioria
das empresas nesse segmento. Entretanto, aproximadamente 20% dos produtos são vendidos por
meio de marketplace, categorizando a parte B2B (“Business to Business” ou Empresa para Empresa)
da Mobly [1].

&emsp;&emsp; O mercado moveleiro do qual a Mobly faz parte possui uma certa estabilidade pela necessidade
desses produtos na rotina da maioria da população. Entretanto, essa estabilidade pode ser
atingida por questões externas e/ou sazonais como, por exemplo, nas épocas de black friday em que existe uma alta nas vendas. 
Já um exemplo de questão externa não prevista foi durante o ano de 2020 em que houve um aumento na demanda, mas que não 
conseguiu ser totalmente acompanhado pelos fornecedores, visto a fase de isolamento. Mas após um intervalo de tempo conseguiu evoluir bastante, com um crescimento de demanda que não só foi acompanhado pelos fornecedores, mas que
impulsionou o investimento em tecnologia e inovação. Atualmente a tendência de crescimento do setor é
positiva, considerando a volta processual da estabilidade econômica e poder aquisitivo [2].

&emsp;&emsp; Considerando esse cenário, o volume de concorrentes é significativamente alto, contando com várias
empresas que buscam por diferenciação para atrair novos clientes. Ao mesmo tempo, existe no setor um
amplo espaço para crescimento de diferentes empresas, pois mesmo existindo algumas mais estabelecidas
que outras não há um monopólio no setor que dificulte a existência de instituições variadas.

&emsp;&emsp; A seguir é possível visualizar uma análise aprofundada do negócio a partir do modelo de
“5 forças de Porter”. Criada por Michael Porter em 1970, o framework tem como objetivo uma análise
mais completa sobre o contexto de mercado, descrevendo a concorrência, os fornecedores, clientes e
produtos e como todos eles impactam a empresa estudada [3].

&emsp;&emsp; Para isso, Michael Porter destaca 5 frentes de análise:
   
* **Poder de barganha dos fornecedores:** pesquisa sobre como a defesa dos interesses do fornecedor
pode afetar a empresa e seus produtos.

* **Poder de barganha dos clientes:** entende como os clientes, ao buscar por vantagens comparativas,
chegam ou não a empresa estudada, comparando questões como preços e qualidade.

* **Ameaça de produtos substitutos:** estuda qual a possibilidade dos produtos vendidos pela empresa
serem trocados por outros e, se for possível, quais são esses produtos e sua tendência de serem uma
opção principal.

* **Ameaça de entrada de novos concorrentes:** analisa como o segmento está aberto para novos
competidores, ao mesmo tempo que aprofunda quais comportamentos e características atraíram novos clientes.

* **Rivalidade entre concorrentes:** expõe quais são as principais concorrentes no segmento e quais as
ameaças que oferecem com base nos pontos positivos que possuem e que se sobressaem em relação à empresa estudada.

###### Figura 2 - 5 Forças de Porter da empresa Mobly
![5 Forças de Porter (1)](https://github.com/2023M3T9-Inteli/grupo1/assets/124217721/b1a8c1e8-4528-4a2f-ab5f-7fbd401dbfec)

###### Fonte: Elaborada pelos autores (2023)

&emsp;&emsp;Sendo assim, após a definição de cada um dos tópicos das 5 Forças de Porter, abaixo há a análise completa que foi feita pelo grupo, algo que também está expresso na figura 2:
* **Poder de barganha dos fornecedores:** As indústrias de móveis se caracterizam como o pilar principal de fornecimento da Mobly.  A empresa em si produz grande parte dos móveis que vendem, sendo algo benéfico por garantir a disponibilidade de produtos. Ao mesmo tempo, no que diz respeito as indústrias de móveis que estão fora de seu controle, a Mobly não precisa se preocupar com a concentração de fornecedores, uma vez que no Brasil existem mais de 19 mil indústrias no setor. Portanto, existe uma oferta equilibrada com a demanda, dando poder a Mobly para analisar as vantagens comparativas entre os concorrentes e fazer a escolha que melhor se encaixa com seus objetivos;
* **Poder de barganha dos clientes:** O público que busca adquirir móveis é pulverizado, uma vez que a compra desses itens é essencial em qualquer residência. No entanto, é importante notar que, dentro desse mercado, a maioria dos consumidores não possui um grande poder de influência econômica sobre os produtos disponíveis, o que resulta em uma capacidade limitada de negociação por parte dos clientes. Isso ocorre devido à grande quantidade de compradores, que equilibram a relação de oferta e demanda;
* **Ameaça de produtos substitutos:** Uma vez que a empresa Mobly trabalha com a venda de móveis, a ameaça de produtos substitutos não se apresenta com muita força, pois móveis são produtos dificilmente substituíveis. Entretanto, a empresa pode se preocupar com variantes do produto, como a venda de móveis usados (que já é muito difundida, principalmente entre classes sociais mais baixas), ou até móveis de papelão, que se mostram como uma alternativa sustentável para a substituição de alguns tipos de mobília [20];
* **Ameaça de entrada de novos concorrentes:** A possibilidade de novas empresas entrarem no mercado é sempre uma consideração relevante, especialmente em um setor que engloba produtos de alta demanda, tornando as barreiras de entrada baixas. Contudo, dado o número de empresas já estabelecidas, os novos competidores precisariam de diferenciais para se destacar significativamente. Isso poderia ser alcançado através da introdução de designs inovadores, a implementação de uma logística altamente eficiente, a adoção de tecnologias de ponta e a criação de experiências de compra excepcionais tanto em lojas físicas quanto virtuais. Qualquer novo concorrente que conseguisse equilibrar com sucesso todas essas vantagens poderia representar um risco para o setor e, consequentemente, para a empresa Mobly;
* **Rivalidade entre concorrentes:** Como é um mercado vasto com vários tipos de lojas, a Mobly precisa lidar com vários tipos de concorrentes. Alguns dos principais são: Magazine Luiza, Tok&Stok e MadeiraMadeira. No caso da Magazine Luiza os pontos mais ameaçadores são o tempo de mercado estabilizado no Brasil, a possibilidade da loja física em vários estados e também da loja virtual e preços acessíveis. Já a Tok&Stok apresenta um design diferenciado, a possibilidade de personalização dos produtos e também lojas virtuais e físicas em vários estados [18]. No caso da MadeiraMadeira, que apresenta um foco de vendas online, as principais ameaças são o trabalho com produtos sustentáveis, produtos de qualidade feitos em madeira e comercialização direta com o estoque dos fornecedores [19].



#### 4.1.2. Análise SWOT 
&emsp;&emsp; A matriz SWOT (Strengths, Weaknesses, Opportunities, Threats), de acordo com Volpato (2022) trata-se de uma ferramenta estratégica que permite analisar alguns aspectos de uma empresa, como as suas forças, fraquezas, oportunidades e ameaças. Por meio da análise desses aspectos é possível que a organização tome decisões de forma mais assertiva, uma vez que tal matriz fornece um panorama geral do estágio em que a empresa em questão se encontra. Dessa forma, a análise SWOT consegue identificar o ambiente interno e externo de uma organização. O ambiente interno está atrelado aos fatores que a empresa consegue ter controle (aspectos como as forças e fraquezas), já o ambiente externo está ligada aos fatores que a instituição não possui um controle (aspectos como oportunidade e ameaças). 

&emsp;&emsp; Tendo isso em vista, a figura 3 expõe a Matriz SWOT elaborada por este grupo em relação à empresa Mobly. 

###### Figura 3 - Análise SWOT da empresa Mobly
![Matriz SWOT da Mobly](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/ef171cca-5bf6-4039-876b-180155f23887)
###### Fonte: Elaborada pelos autores (2023)

Sendo assim, após a definição da Matriz SWOT, abaixo há a análise completa que foi feita pelo grupo, algo que também está expresso na figura 3:
* **Forças (Strengths):**
  * Posicionamento da Mobly tanto online quanto presencial;
  * Foco na experiência e nas preferências dos clientes por meio do armazenamento das informações dos clientes no banco de dados, o que possibilita a utilização de ferramentas de inteligência de negócios;
  * Cobertura de entrega dos móveis em todo o território nacional;
  * Produtos de diversos tipos, designs e com diferentes funcionalidades, fazendo com que um número considerável de clientes sejam contemplados [21];
  * Centro de distribuição (CD) em estados estratégicos, como São Paulo, Minas Gerais e Santa Catarina, além de um CD em Campinas, uma cidade interiorana de São Paulo;
  * Loja "Phygital" apenas no estado de São Paulo, um local estratégico, a qual oferece para o cliente a experiência da compra online com os benefícios da compra física;
  * Utilização estratégica da plataforma omnichannel, de modo a fazer com que o cliente tenha uma experiência cada vez mais personalizada e eficiente;
  * Diferentes tipos de lojas para diferentes tipos de necessidades dos clientes (Megastore, outlet e Mobly ZIP);
  * Presença de uma forte tecnologia nas compras dos clientes, de modo a oferecer aos cliente maior certeza e flexibilidade ao comprar um produto online;
  * Marketing segmentado, de modo a contemplar diferentes públicos-alvos;
Site que fornece uma especificação técnica completa e relevante sobre o produto, fazendo com que o cliente possa escolher o produto certo;
  * Móveis de linha exclusiva da Mobly, isto é, móveis que são produzidos pela própria equipe da Mobly, contando com um design único;
  * Formas de pagamento flexíveis;
  * Fortes benefícios para os funcionários, incluindo vale-refeição, plano de saúde e descontos nos produtos da Mobly.

* **Fraquezas (Weaknesses):**
  * Carência de lojas físicas em outros estados do Brasil, fazendo com que a experiência de visitação e compra em loja física fique limitada apenas para o estado de São Paulo;
  * Manual de montagem dos móveis confusos [22];
  * Atraso na entrega dos produtos [23];
  * Ineficiência em relação ao abastecimento do estoque dos produtos da Mobly, uma vez que não há uma ferramenta que possibilite tal abastecimento de modo a evitar a obsolescência ou custos desnecessários dos produtos;
  * Diversidade limitada de produtos quando comparada com empresas concorrentes.
   
* **Oportunidades (Opportunities):**
  * Público-alvo propenso a buscar por lojas virtuais que oferecem tecnologias que possam contribuir para a escolha do produto [24];
  * Busca pela ressignificação do lar, principalmente após a pandemia, pois as pessoas passaram a valorizar o ambiente doméstico, de modo a torná-lo um ambiente propício para lazer, descanso, encontros familiares, etc [25];
  * Adoção do trabalho remoto, fazendo com que as pessoas busquem móveis de escritórios e outros móveis para que tornem o ambiente doméstico mais propício para o trabalho;
  * Busca pelo acompanhamento das atuais tendências de móveis e decoração devido ao grande compartilhamento nas redes sociais desses produtos;
  * Adoção do homeschooling, fazendo com que as pessoas busquem móveis adequados para a realização dos estudos em casa;
Tendência da geração mais nova de buscar móveis mais modernos, práticos e versáteis;
  * Presença crescentes de influenciadores arquitetos, os quais compartilham diferentes tendências e dicas nas redes sociais;
  * Possibilidade de fusão com a Tok&Stok, de modo a agregar mais clientes para a Mobly.

* **Ameaças (Threats):**
  * Mudança de gosto constante dos consumidores, influenciada, principalmente, pelas tendências compartilhadas nas redes sociais [27];
  * Falta de um departamento que analise, cuidadosamente, as tendências do mercado de acordo com as redes sociais, de modo a ajustar as campanhas de marketing dos produtos da empresa;
  * Alta concorrência com empresas mais consolidadas/acessadas, como a Magazine Luiza, Tok&Stok e MadeiraMadeira;
  * A instabilidade econômica, em geral, pode resultar em um menor poder de compra por parte dos clientes, devido à alta taxa de desemprego, o que torna a compra de móveis uma prioridade baixa. Além disso, a economia é afetada pela atual taxa de juros elevada [26];
  * Riscos de ataques cibernéticos, haja vista que é uma loja que possui mais de 800 mil usuários ativos na plataforma de compra online.
#### 4.1.3. Planejamento Geral da Solução
##### 4.1.3.1. Problema que está sendo resolvido
&emsp;&emsp; Atualmente a Mobly enfrenta um desafio significativo em relação ao equilíbrio entre o abastecimento do estoque e as demandas de seus clientes [4]. Dessa forma, alguns dos impactos que podem ser gerados devido ao desafio mencionado são:
* **Baixo giro de produtos:** A falta de equilíbrio entre os produtos disponíveis no estoque e a demanda real dos consumidores pode levar a um baixo giro de determinados móveis, algo que gera materiais parados e que podem sofrer desgastes físicos, tornando-os, então, inutilizáveis;
* **Desperdício de materiais:** Devido ao desequilíbrio já mencionado e ao baixo giro de produtos, a empresa acaba desperdiçando materiais, uma vez que eles não são utilizados para a produção de móveis ofertados, resultando, então, em perdas financeiras;
* **Perda de vendas:** Devido a falta de otimização do estoque é possível que ocorra a carência de determinados materiais para a produção de móveis, algo que pode levar a perda de vendas.
  
&emsp;&emsp; Ademais, a empresa não possui nenhuma ferramenta inteligente que possa amenizar tal problemática, pois eles se baseiam apenas no histórico de compras de seus clientes, algo que não pode ser tão eficiente na maioria das vezes [1].

&emsp;&emsp; Portanto, por causa de todos os aspectos já mencionados acima, todos eles podem impactar negativamente a operacionalidade da empresa, além da sua lucratividade, fazendo com que seja crucial a busca de uma solução estratégica capaz de amenizar tal problemática.

##### 4.1.3.2. Solução Proposta
&emsp;&emsp; Tendo em vista o problema que a Mobly tem enfrentado, a solução proposta para amenizá-lo consiste no desenvolvimento de um modelo preditivo que utilizará técnicas de análise de dados para prever a quantidade de produtos que serão vendidos em um determinado período de tempo. Tal modelo preditivo será uma ferramenta estratégica para realizar o abastecimento de forma equilibrada do estoque, permitindo que a instituição atenda às demandas dos seus clientes de forma eficiente e reduza as perdas de materiais e de vendas.

&emsp;&emsp; Assim, a previsão dessas informações será possível devido à análise detalhada de uma base de dados (dataset) fornecida pela Mobly, a qual contém diversas informações sobre as vendas realizadas pela organização. Ademais, para que essa previsão seja eficiente, é de extrema importância uma boa acurácia dos dados, a qual poderá ser alcançada seguindo alguns passos, como:
* **Entendimento detalhado das _features_ presentes na base de dados:** Os membros do grupo realizarão uma exploração completa dos dados disponíveis, de modo a selecionar as informações mais relevantes para o desenvolvimento do modelo preditivo;
* **Tratamento e limpeza dos dados:** A base de dados que a organização forneceu pode conter algumas informações incompletas, duplicadas ou até mesmo inconsistentes, fazendo com que seja necessário aplicar técnicas de tratamento e limpeza de dados;
* **Criação de gráficos para validar o entendimento das _features_ e o tratamento/limpeza dos dados:** Para que os membros do grupo possam entender o conteúdo das _features_ da base de dados, capturar possíveis relações entre essas informações e validar o tratamento dos dados, é relevante a criação de gráficos para que a visualização dessas informações seja mais clara, contribuindo para o entendimento das _features_; 
* **Treinamento de modelos com diferentes _features_:** Para alcançar uma melhor acurácia é possível criar modelos com diferentes abordagens através da utilização de diferentes _features_, de modo a encontrar a combinação de informações que forneça melhores resultados. 

&emsp;&emsp; Os passos mencionados não são fixos, uma vez que, de acordo com o desenvolvimento do projeto, o grupo pode adicionar ou retirar alguma das etapas mencionadas, de modo a tornar o aprendizado do grupo mais fluído e a acurácia do modelo preditivo mais definida.

##### 4.1.3.3. Como utilizar a Solução Proposta
&emsp;&emsp; O modelo preditivo será utilizado pela área de _Business_ _Intelligence_ (BI) da Mobly [1]. Dessa forma, será necessário o acesso ao Google Colab - serviço de nuvem gratuito hospedado pelo próprio Google que permite desenvolver códigos voltados ao Aprendizado de Máquina e à Inteligência Artificial [5], de modo a anexar o _dataset_ e ter acesso aos resultados gerados pelo modelo.

&emsp;&emsp; O processo de utilização do modelo preditivo inicia-se com o carregamento de um _dataset_ que contém as informações necessárias sobre as vendas para que seja possível realizar a previsão. Ao carregar tal _dataset_ o modelo consegue analisar e aprender através dos dados presentes.

&emsp;&emsp; Após o processo de análise e aprendizado por parte do modelo, ele conseguirá fornecer como _output_, isto é, o resultado da previsão, o qual evidenciará a quantidade estimada de produtos a serem vendidos e o período de tempo que tais vendas ocorrerão.

&emsp;&emsp; Portanto, o _output_ fornecido pelo modelo auxiliarão a equipe de BI a fornecer informações precisas para a equipe de _Supply_ _Chain_ da Mobly, a qual é responsável pelo processo de abastecimento do estoque [1], para que a compra dos materiais seja realizada com eficiência, garantido que a empresa esteja preparada para atender às demandas dos seus clientes.

##### 4.1.3.4. Benefícios gerados pela solução
Os benefícios que o modelo preditivo desenvolvido pode trazer para a Mobly são:
* **Equilíbrio entre o abastecimento do estoque e as demandas dos clientes:** Tal equilíbrio será alcançado por meio das previsões realizadas pelo modelo, uma vez que ele fornecerá as informações relacionadas às demandas futuras de determinados produtos, algo que auxiliará na compra assertiva, por parte da equipe de Supply Chain da Mobly, dos materiais necessários para atender os seus consumidores;
* **Maior captação de clientes:** Por meio do equilíbrio do estoque com as demandas dos consumidores, a Mobly conseguirá atender os seus clientes com mais precisão, haja vista que a falta de produtos devido à falta de material no estoque será um cenário de difícil ocorrência;
* **Maximização do lucro:** A otimização do estoque irá fazer com que as demandas dos consumidores da Mobly sejam atendidas de forma imediata, gerando mais vendas. Além disso, tal otimização evitará gastos desnecessários com materiais;
* **Diminuição de desperdício de materiais:** Com o abastecimento do estoque equilibrado com as demandas, será reduzida a compra de muitos materiais que, por vezes, ficam parados no estoque, algo que gera perda de lucro;
* **Diminuição do baixo giro dos produtos presentes no estoque:** Como a compra dos materiais do estoque estarão alinhadas com as demandas dos clientes, os móveis serão vendidos com maior precisão, evitando que eles fiquem parados por muito tempo no estoque.

##### 4.1.3.5. Critérios de sucesso e medidas utilizadas para avaliar o modelo
&emsp;&emsp; O sucesso do modelo preditivo desenvolvido será alcançado, principalmente, por meio da previsão dos produtos que serão vendidos e qual o período de tempo que tal venda irá ocorrer.

&emsp;&emsp; Em relação às medidas que serão utilizadas para avaliar o modelo, elas estão relacionadas à acurácia das informações de acordo com o período da venda. Segundo O TAPI deste projeto, essas medidas serão:
* Quantidade de vendas por produto (SKU) por dia, buscando alcançar uma acurácia mínima de 70%;
* Quantidade de vendas por produto (SKU) por semana, visando alcançar uma acurácia superior a 90%. 

#### 4.1.4. Value Proposition Canvas
&emsp;&emsp; O _Value Proposition Canvas_, também conhecido como Quadro de Proposta de Valor, é uma ferramenta visual amplamente utilizada em estratégias de desenvolvimento de produtos e serviços. Tal ferramenta é projetada para ajudar as empresas a compreenderem melhor as necessidades, desejos e dores dos clientes, além de criar propostas de valor convincentes. O quadro consiste em dois lados interconectados: o "Perfil do Cliente", que explora os segmentos de cliente, trabalhando em detalhes relacionadas as suas características, tarefas, dores e ganhos, e a "Proposta de Valor", que descreve como o produto ou serviço atende a esses elementos do perfil do cliente, delineando os benefícios específicos, produtos e serviços oferecidos. Ao preencher e analisar o _Value Proposition Canvas_, as organizações podem identificar oportunidades de melhoria, ajustar estratégias de marketing e inovação e, finalmente, criar ofertas mais alinhadas com as reais necessidades dos clientes.

&emsp;&emsp; Sabendo disso, a figura 4 demonstra o _Value Proposition Canvas_ esquematizado entre o projeto desenvolvido e a empresa Mobly.

###### Figura 4 - Value Proposition Canvas da empresa Mobly
![Value Proposition Canvas da empresa Mobly](https://github.com/2023M3T9-Inteli/grupo1/assets/123953851/2138643b-9795-42ae-984c-e5fd8e61f0b0)
###### Fonte: Elaborada pelos autores (2023)



#### 4.1.5. Matriz de Riscos
&emsp;&emsp; A matriz de risco é uma ferramenta utilizada no projeto que oferece uma representação visual que classifica os riscos de acordo com sua probabilidade de ocorrência e o impacto potencial tanto no andamento do projeto quanto no produto final, neste caso o modelo preditivo. Ao categorizar os riscos em células que representam diferentes combinações de probabilidade e impacto, a matriz de risco permite uma identificação clara dos eventos mais críticos e a alocação adequada de recursos para a prevenção destes. O uso da matriz ajuda o nosso grupo a tomar decisões estratégicas, focando naqueles riscos que podem ter as consequências mais significativas, ao mesmo tempo, em que ajuda o time a entender quais são os riscos mais aceitáveis para o projeto.

###### Figura 5 - Matriz de risco
![Matriz de Risco e Oportunidade](https://github.com/2023M3T9-Inteli/grupo1/assets/123921392/c143ab09-1ba1-48b0-a802-7bb0a461f39f)
###### Fonte: Elaborada pelos autores (2023)


#### 4.1.6. Personas
&emsp;&emsp; Personas são representações fictícias de arquétipos de clientes ou usuários, baseadas em dados demográficos, comportamentais, objetivos e características. Elas são usadas em marketing, design de produtos e desenvolvimento de serviços para compreender melhor o público-alvo de uma empresa ou projeto e criar estratégias mais eficazes.

&emsp;&emsp; Dessa forma, para que o entendimento do problema e de como a solução pode de fato contribuir positivamente para a Mobly, foi desenvolvido duas personas para representar os possíveis usuários da Mobil.ia. Assim, as figuras 6 e 7 demonstram essas personas.

###### Figura 6 - Persona Gisele Cunha
![Persona - Gisele Cunha](https://github.com/2023M3T9-Inteli/grupo1/assets/124165852/5353726a-cbfb-4c46-914a-60745f2e1dad)
###### Fonte: Elaborada pelos autores (2023)

###### Figura 7 - Persona Mario Azevedo
![Persona - Mario Azevedo](https://github.com/2023M3T9-Inteli/grupo1/assets/124165852/5dcaaefa-476d-4808-a975-3ceb2964e4ef)
###### Fonte: Elaborada pelos autores (2023)


#### 4.1.7. Jornadas do Usuário
&emsp;&emsp; A jornada do usuário é uma ferramenta utilizada de forma recorrente nos processos de UX design para entender o produto que se estuda e seu cenário. Para tanto, o template a seguir oferece dados referentes às personas criadas para o entendimento do projeto, informando a sua atuação e seu envolvimento com o produto.

&emsp;&emsp; Para o entendimento da jornada, o template conta com a expecificação das fases que a persona vive no dia a dia e que são impactadas pelo modelo preditivo, as ações e pensamentos referentes a cada fase e as expectativas da persona. A partir disso, são elaboradas as sessões de oportunidades (onde é analisado o que o produto precisa ter para tornar a jornada do usuário melhor) e responsabilidades (em que funções são atribuídas para chegar a esses objetivos).

###### Figura 8 - Jornada do usuário (Gisele)
![Jornada de Usuário (Gisele)](https://github.com/2023M3T9-Inteli/grupo1/assets/124217721/f1b59e74-4667-473d-8ef2-e6887acbdec5)
###### Fonte: Elaborada pelos autores (2023)
###### Figura 9 - Jornada do usuário (Mário)
![Jornada de Usuário (Mário)](https://github.com/2023M3T9-Inteli/grupo1/assets/124217721/b148d97a-b04c-4c73-936e-73c06094955b)
###### Fonte: Elaborada pelos autores (2023)


#### 4.1.8 Política de Privacidade
&emsp;&emsp; A MOBLY COMÉRCIO VAREJISTA LTDA., pessoa jurídica de direito privado, com sede na Av. das Nações Unidas, 16737 Várzea de Baixo, São Paulo - SP - CEP 04730-090, inscrita no CNPJ/MF sob o nº 14.055.516/0001-48 (“Lojista” ou “nós”) leva a sua privacidade a sério e zela pela segurança e proteção de dados de todos os seus clientes, parceiros, fornecedores e usuários (“Usuários” ou “você”) do site “mobly.com.br” e qualquer outro site, Loja, aplicativo operado pelo Lojista (aqui designados, simplesmente, “Loja”).

&emsp;&emsp; Esta Política de Privacidade (“Política de Privacidade”) destina-se a informá-lo sobre o modo como nós utilizamos e divulgamos informações coletadas em suas visitas à nossa Loja e em mensagens que trocamos com você (“Comunicações”).

&emsp;&emsp; AO ACESSAR A LOJA, ENVIAR COMUNICAÇÕES OU FORNECER QUALQUER TIPO DE DADO PESSOAL, VOCÊ DECLARA ESTAR CIENTE E DE ACORDO COM ESTA POLÍTICA DE PRIVACIDADE, A QUAL DESCREVE AS FINALIDADES E FORMAS DE TRATAMENTO DE SEUS DADOS PESSOAIS QUE VOCÊ DISPONIBILIZAR NA LOJA.

&emsp;&emsp; Esta Política de Privacidade fornece uma visão geral de nossas práticas de privacidade e das escolhas que você pode fazer, bem como direitos que você pode exercer em relação aos Dados Pessoais tratados por nós. Se você tiver alguma dúvida sobre o uso de Dados Pessoais, entre em contato com [contato@mobly.com.br](mailto:contato@mobly.com.br).

&emsp;&emsp; Além disso, a Política de Privacidade não se aplica a quaisquer aplicativos, produtos, serviços, site ou recursos de mídia social de terceiros que possam ser oferecidos ou acessados por meio da Loja. O acesso a esses links fará com que você deixe a Loja e possa resultar na coleta ou compartilhamento de informações sobre você por terceiros. Nós não controlamos, endossamos ou fazemos quaisquer representações sobre esses sites de terceiros ou suas práticas de privacidade, que podem ser diferentes das nossas. Recomendamos que você revise a política de privacidade de qualquer site com o qual você interaja antes de permitir a coleta e o uso de seus Dados Pessoais.

&emsp;&emsp; Caso você nos envie Dados Pessoais referentes a outras pessoas físicas, você declara ter a competência para fazê-lo e declara ter obtido o consentimento necessário para autorizar o uso de tais informações nos termos desta Política de Privacidade.

### Definições

&emsp;&emsp; Para os fins desta Política de Privacidade:

- **“Dados Pessoais”** significa qualquer informação que, direta ou indiretamente, identifique ou possa identificar uma pessoa natural, como por exemplo, nome, CPF, data de nascimento, endereço IP, dentre outros;
- **“Dados Pessoais Sensíveis”** significa qualquer informação que revele, em relação a uma pessoa natural, origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico;
- **“Tratamento de Dados Pessoais”** significa qualquer operação efetuada no âmbito dos Dados Pessoais, por meio de meios automáticos ou não, tal como a recolha, gravação, organização, estruturação, armazenamento, adaptação ou alteração, recuperação, consulta, utilização, divulgação por transmissão, disseminação ou, alternativamente, disponibilização, harmonização ou associação, restrição, eliminação ou destruição. Também é considerado Tratamento de Dados Pessoais qualquer outra operação prevista nos termos da legislação aplicável;
- **“Leis de Proteção de Dados”** significa todas as disposições legais que regulem o Tratamento de Dados Pessoais, incluindo, porém sem se limitar, a Lei nº 13.709/18, Lei Geral de Proteção de Dados Pessoais (“LGPD”).

### Uso de Dados Pessoais

&emsp;&emsp; Coletamos e usamos Dados Pessoais para gerenciar seu relacionamento conosco e melhor atendê-lo quando você estiver adquirindo produtos e/ou serviços na Loja, personalizando e melhorando sua experiência. Exemplos de como usamos os dados incluem:

* Viabilizar que você adquira produtos e/ou serviços na Loja;
* Para confirmar ou corrigir as informações que temos sobre você;
* Para enviar informações que acreditamos ser do seu interesse;
* Para personalizar sua experiência de uso da Loja;
* Para personalizar o envio de publicidades para você, baseada em seu interesse em nossa Loja; e
* Para entrarmos em contato por um número de telefone e/ou endereço de e-mail fornecido. Podemos entrar em contato com você pessoalmente, por mensagem de voz, através de equipamentos de discagem automática, por mensagens de texto (SMS), por e-mail, ou por qualquer outro meio de comunicação que seu dispositivo seja capaz de receber, nos termos da lei e para fins comerciais razoáveis.

&emsp;&emsp; Além disso, os Dados Pessoais fornecidos também podem ser utilizados na forma que julgarmos necessária ou adequada: (a) nos termos das Leis de Proteção de Dados; (b) para atender exigências de processo judicial; (c) para cumprir decisão judicial, decisão regulatória ou decisão de autoridades competentes, incluindo autoridades fora do país de residência; (d) para proteger nossas operações; (e) para proteger direitos, privacidade, segurança nossos, seus ou de terceiros; (f) para detectar e prevenir fraude; (g) permitir-nos usar as ações disponíveis ou limitar danos que venhamos a sofrer; (h) de outros modos permitidos por lei.

&emsp;&emsp; A NOSSA LOJA NÃO SE DESTINA A PESSOAS COM MENOS DE 18 (DEZOITO) ANOS E PEDIMOS QUE TAIS PESSOAS NÃO NOS FORNEÇAM QUALQUER DADO PESSOAL

### Não fornecimento de Dados Pessoais

&emsp;&emsp; Você não é obrigado a compartilhar os Dados Pessoais que solicitamos, no entanto, se você optar por não os compartilhar, em alguns casos, não poderemos fornecer a você acesso completo à Loja, alguns recursos especializados ou ser capaz de prestar a assistência necessária ou, ainda, viabilizar a entrega do produto ou prestar o serviço contratado por você.

### Dados coletados

&emsp;&emsp; O público em geral poderá navegar na Loja sem necessidade de qualquer cadastro e envio de Dados Pessoais. No entanto, algumas das funcionalidades da Loja poderão depender de cadastro e envio de Dados Pessoais como concluir a compra/contratação do serviço e/ou a viabilizar a entrega do produto/prestação do serviço por nós.

&emsp;&emsp; No contato a Loja, nós podemos coletar:

* Dados de contato. Nome, sobrenome, número de telefone, cidade, Estado e endereço de e-mail; e
* Informações que você envia. Informações que você envia via formulário (dúvidas, reclamações, sugestões, críticas, elogios etc.).

&emsp;&emsp; Na navegação geral na Loja, nós poderemos coletar:

* **Dados de localização:** Dados de geolocalização quando você acessa a Loja;
* **Preferências:** Informações sobre suas preferências e interesses em relação aos produtos/serviços (quando você nos diz o que eles são ou quando os deduzimos do que sabemos sobre você);
* **Dados de navegação na Loja:** Informações sobre suas visitas e atividades na Loja, incluindo o conteúdo (e quaisquer anúncios) com os quais você visualiza e interage, informações sobre o navegador e o dispositivo que você está usando, seu endereço IP, sua localização, o endereço do site a partir do qual você chegou. Algumas dessas informações são coletadas usando nossas Ferramentas de Coleta Automática de Dados, que incluem cookies, web beacons e links da web incorporados. Para saber mais, leia como nós usamos Ferramentas de Coleta Automática de Dados no item 7 abaixo;
* **Dados anônimos ou agregados:** Respostas anônimas para pesquisas ou informações anônimas e agregadas sobre como a Loja é usufruída. Durante nossas operações, em certos casos, aplicamos um processo de desidentificação ou pseudonimização aos seus dados para que seja razoavelmente improvável que você identifique você através do uso desses dados com a tecnologia disponível; e
* **Outras informações que podemos coletar:** Outras informações que não revelem especificamente a sua identidade ou que não são diretamente relacionadas a um indivíduo, tais como informações sobre navegador e dispositivo; dados de uso da Loja; e informações coletadas por meio de cookies, pixel tags e outras tecnologias.

&emsp;&emsp; Ao menos que você informe em algum formulário livre preenchido por você, nós não coletamos Dados Pessoais Sensíveis.

### Compartilhamento de Dados Pessoais com terceiros

Nós poderemos compartilhar seus Dados Pessoais:

* Com a(s) empresa(s) parceira(s) que você selecionar ou optar em enviar os seus dados, dúvidas, perguntas etc., bem como com provedores de serviços ou parceiros para gerenciar ou suportar certos aspectos de nossas operações comerciais em nosso nome. Esses provedores de serviços ou parceiros podem estar localizados nos Estados Unidos, na Argentina, no Brasil ou em outros locais globais, incluindo servidores para homologação e produção, e prestadores de serviços de hospedagem e armazenamento de dados, gerenciamento de fraudes, suporte ao cliente, vendas em nosso nome, atendimento de pedidos, personalização de conteúdo, atividades de publicidade e marketing (incluindo publicidade digital e personalizada) e serviços de TI, por exemplo;
* Com terceiros, com o objetivo de nos ajudar a gerenciar a Loja; 
* Com terceiros, caso ocorra qualquer reorganização, fusão, venda, joint venture, cessão, transmissão ou transferência de toda ou parte da nossa empresa, ativo ou capital (incluindo os relativos à falência ou processos semelhantes).

### Transferências internacionais de Dados

&emsp;&emsp; Dados Pessoais e informações de outras naturezas coletadas por nós podem ser transferidos ou acessados por entidades pertencentes ao grupo corporativo das empresas parceiras em todo o mundo de acordo com esta Política de Privacidade.

### Forma de coleta automática de Dados Pessoais

&emsp;&emsp; Quando você visita a Loja, ela pode armazenar ou recuperar informações em seu navegador, seja na forma de cookies e de outras tecnologias semelhantes. Essas informações podem ser sobre você, suas preferências ou seu dispositivo e são usadas principalmente para que a Loja funcione como você espera. As informações geralmente não o identificam diretamente, mas podem oferecer uma experiência na internet mais personalizada.

&emsp;&emsp; De acordo com esta Política de Privacidade, nós e nossos prestadores de serviços terceirizados podemos coletar seus Dados Pessoais de diversas formas, incluindo, entre outros:

* **Por meio do navegador ou do dispositivo:** Algumas informações são coletadas pela maior parte dos navegadores ou automaticamente por meio de dispositivos de acesso à internet, como o tipo de computador, resolução da tela, nome e versão do sistema operacional, modelo e fabricante do dispositivo, idioma, tipo e versão do navegador de Internet que está utilizando. Podemos utilizar essas informações para assegurar que a Loja funcione adequadamente.
* **Uso de cookies:** Os cookies permitem a coleta de informações tais como o tipo de navegador, o tempo dispendido na Loja, as páginas visitadas, as preferências de idioma, e outros dados de tráfego anônimos. Nós e nossos prestadores de serviços podemos utilizar essas informações para, dentre outros, personalizar sua experiência ao utilizar a Loja, assim como para direcionar publicidade para você, de acordo com os seus interesses. Também coletamos informações estatísticas sobre o uso da Loja para aprimoramento contínuo do nosso design e funcionalidade.
Caso não deseje que suas informações sejam coletadas por meio de cookies, você pode configurar os cookies no menu "opções" ou "preferências" do seu browser. Nos links abaixo você encontra mais detalhes sobre como ajustar as preferências de cookies dos navegadores de internet mais populares:
  * [Google Chrome](https://support.google.com/chrome/answer/95647?hl=pt-BR)
  * [Mozilla Firefox](https://support.mozilla.org/pt-BR/kb/ative-e-desative-os-cookies-que-os-sites-usam)
  * [Safari](https://support.apple.com/pt-br/guide/safari/sfri11471/mac)
  * [Internet Explorer](https://support.microsoft.com/pt-br/help/17442/windows-internet-explorer-delete-manage-cookies)
  * [Microsoft Edge](https://support.microsoft.com/pt-br/microsoft-edge/excluir-cookies-no-microsoft-edge-63947406-40ac-c3b8-57b9-2a946a29ae09)
  - [Opera](https://help.opera.com/pt-BR/latest/security-and-privacy/)

### Uso de pixel tags e outras tecnologias similares

&emsp;&emsp; Pixel tags (também conhecidos como Web beacons e GIFs invisíveis) podem ser utilizados para rastrear ações de usuários da Loja (incluindo destinatários de e-mails), medir o sucesso das nossas campanhas de marketing e coletar dados estatísticos sobre o uso da Loja e taxas de resposta. Em caso de ter ativa a personalização de anúncios em ferramentas como Facebook, Google ou Bing, a informação pode ser usada para mostrar anúncios em seus serviços.No caso de você não desejar ser rastreado pode pedir para cada um dos serviços:

* [Facebook](https://www.facebook.com/help/568137493302217)
* [Google](https://support.google.com/ads/answer/2662922?hl=pt-BR)
* [Bing](https://about.ads.microsoft.com/pt-br/recursos/politicas/microsoft-advertising-policies/personalized-ads)

&emsp;&emsp; Podemos contratar empresas de publicidade comportamental, para obter relatórios sobre os anúncios da Loja em toda a internet. Para isso, essas empresas utilizam cookies, pixel tags e outras tecnologias para coletar informações sobre a sua utilização, ou sobre a utilização de outros usuários, da nossa Loja e de site de terceiros. Nós não somos responsáveis por pixel tags, cookies e outras tecnologias similares utilizadas por terceiros. Você pode configurar suas preferências no menu do seu browser. Esteja ciente de que se você mudar de computador ou navegador, ou usar vários computadores ou navegadores, você precisará repetir este processo para cada computador e cada navegador.

### Direitos do Usuário

Você pode, a qualquer momento, requerer:

* Confirmação de que seus Dados Pessoais estão sendo tratados;
* Acesso aos seus Dados Pessoais;
* Correções a dados incompletos, inexatos ou desatualizados;
* Anonimização, bloqueio ou eliminação de dados desnecessários, excessivos ou tratados em desconformidade com o disposto em lei;
* Portabilidade de Dados Pessoais a outro prestador de serviços, contanto que isso não afete nossos segredos industriais e comerciais;
* Eliminação de Dados Pessoais tratados com seu consentimento, na medida do permitido em lei;
* Informações sobre as entidades às quais seus Dados Pessoais tenham sido compartilhados;
* Informações sobre a possibilidade de não fornecer o consentimento e sobre as consequências da negativa; e
* Revogação do consentimento.

&emsp;&emsp; Os seus pedidos serão tratados com especial cuidado de forma a que possamos assegurar a eficácia dos seus direitos. Poderá lhe ser pedido que faça prova da sua identidade de modo a assegurar que a partilha dos Dados Pessoais é apenas feita com o seu titular.

&emsp;&emsp; Você deverá ter em mente que, em certos casos (por exemplo, devido a requisitos legais), o seu pedido poderá não ser imediatamente satisfeito, além de que nós poderemos não conseguir atendê-lo por conta de cumprimento de obrigações legais.

### Segurança dos Dados Pessoais

&emsp;&emsp; Buscamos adotar as medidas técnicas e organizacionais previstas pelas Leis de Proteção de Dados adequadas para proteção dos Dados Pessoais na nossa organização. Infelizmente, nenhuma transmissão ou sistema de armazenamento de dados tem a garantia de serem 100% seguros. Caso tenha motivos para acreditar que sua interação conosco tenha deixado de ser segura (por exemplo, caso acredite que a segurança de qualquer uma de suas contas foi comprometida), favor nos notificar imediatamente.

### Links de hipertexto para outros sites e redes sociais

&emsp;&emsp; A Loja poderá, de tempos a tempos, conter links de hipertexto que redirecionará você para sites das redes dos nossos parceiros, anunciantes, fornecedores etc. Se você clicar em um desses links para qualquer um desses sites, lembramos que cada site possui as suas próprias práticas de privacidade e que não somos responsáveis por essas políticas. Consulte as referidas políticas antes de enviar quaisquer Dados Pessoais para esses sites.

&emsp;&emsp; Não nos responsabilizamos pelas políticas e práticas de coleta, uso e divulgação (incluindo práticas de proteção de dados) de outras organizações, tais como Facebook, Apple, Google, Microsoft, ou de qualquer outro desenvolvedor de software ou provedor de aplicativo, Loja de mídia social, sistema operacional, prestador de serviços de internet sem fio ou fabricante de dispositivos, incluindo todos os Dados Pessoais que divulgar para outras organizações por meio dos aplicativos, relacionadas a tais aplicativos, ou publicadas em nossas páginas em mídias sociais. Nós recomendamos que você se informe sobre a política de privacidade de cada site visitado ou de cada prestador de serviço utilizado.

### Atualizações desta Política de Privacidade

&emsp;&emsp; Se modificarmos nossa Política de Privacidade, publicaremos o novo texto na Loja, com a data de revisão atualizada. Podemos alterar esta Política de Privacidade a qualquer momento. Caso haja alteração significativa nos termos dessa Política de Privacidade, podemos informá-lo por meio das informações de contato que tivermos em nosso banco de dados ou por meio de notificação em nossa Loja.

&emsp;&emsp; Recordamos que nós temos como compromisso não tratar os seus Dados Pessoais de forma incompatível com os objetivos descritos acima, exceto se requerido ou permitido por lei. O tratamento de Dados Pessoais incompatível será realizado mediante a revisão desta Política de Privacidade, acompanhada de novo aviso de privacidade ou notificação.

### 4.2. Compreensão dos Dados

#### 4.2.1. Exploração de dados

&emsp;&emsp; Para poder realizar a exploração dos dados da melhor forma, a tarefa foi realizada em quatro etapas:

##### 4.2.1.1. Divisão entre dados numéricos e categóricos
&emsp;&emsp; Nessa etapa o foco foi compreender todos os dados a partir da descrição de cada coluna e o tipo de dado que contém (figura 10), para então poder classificá-los de acordo com a definição de dados categóricos e numéricos. Dados categóricos se caracterizam como uma forma de classificação de variáveis que não implicam em uma relação numérica entre si, e, mesmo que contenham números, trata-se de valores simbólicos e discretos [6]. Já os dados numéricos apresentam números com relação de cálculo ou hierarquia e ordem entre si, podendo configurar valores contínuos [5].

&emsp;&emsp; A partir dessas informações, o comando `df.dtypes` permite a visualização de uma tabela, a qual está expressa na figura 10, que evidencia o nome da _feature_ e o seu respectivo tipo de dado.

###### Figura 10 - Análise do tipo de dado de cada tabela
![Análise do tipo de dado de cada tabela](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/b44d6707-ca8e-435f-a79d-a0cc458203c3)

###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

&emsp;&emsp; Ademais, a título de organização e identificação de cada coluna de forma mais prática, o grupo montou uma tabela que contém o nome da coluna, o que ela significa e qual seu tipo de dado, sendo numérica ou categórica. Sendo assim, a figura 11 demonstra essa divisão. 

###### Figura 11 - Descrição e divisão das colunas em categóricas ou numéricas
![Descrição e divisão das colunas em categóricas ou numéricas](https://github.com/2023M3T9-Inteli/grupo1/assets/124217721/cb1912f0-37bb-4e21-b1e3-a229c44ffcab)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

##### 4.2.1.2. Estatística descritiva
&emsp;&emsp; Já a estatística descritiva, foi feita pelo método describe() da biblioteca Pandas em Python. Tal método retorna:

* **count:** O número de valores não nulos.

* **mean:** A média dos valores.

* **std:** O desvio padrão dos valores.

* **min:** O valor mínimo.

* **25%:** O primeiro quartil (25ª percentil).

* **50% (median):** O valor mediano ou segundo quartil (50ª percentil).

* **75%:** O terceiro quartil (75ª percentil).

* **max:** O valor máximo.

&emsp;&emsp; Dessa forma, para gerar a estatística descritiva de todas as _features_ numéricas presentes no dataframe, foi executado o comando `df.describe()` o qual geral os resultados expressos na figura 12:

###### Figura 12 - Estatística Descritiva das features numéricas
![Estatística descritiva das features numéricas](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/7af1e8c1-4d68-42f7-8fe0-e048b796069a)

###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab
##### 4.2.1.3. Tipos de Variáveis e análise de correlação
&emsp;&emsp; Nessa etapa o grupo procurou categorizar as colunas de acordo com os tipos de variáveis e depois estabelecer uma relação entre elas. Para tanto, utilizamos as definições de Sharda [5] em que temos:

* **Variáveis Nominais:** Apresentam características distintas, não numéricos e não mensuráveis, podendo ser representados por valores binominais ou multinomiais.

* **Variáveis Ordinais:** São passíveis de ordenação, hierarquização ou ranqueamento, mesmo não sendo por definição numéricos.

* **Variáveis Intervalares:** Variáveis que possibilitam uma análise quantificável dos intervalos dos dados entre si. Tais dados podem ainda ser divididos em intervalares de razão, onde é possível encontrar um zero absoluto.

&emsp;&emsp; Pensando nisso, foi elaborada a seguinte divisão:

###### Figura 13 - Classificação de acordo com os tipos de variáveis
![Classificação de acordo com os tipos de variáveis](https://github.com/2023M3T9-Inteli/grupo1/assets/124217721/2a3fd381-35c0-4bcd-8cc0-e8b779016c71)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

&emsp;&emsp; Feito isso, é montada a matriz de correlação, em que é possível analisar o nível de impacto entre uma variável e outra. Tal matriz é composta por valores de -1 a 1 em que:

* Quanto mais próximo de -1, mais existe uma relação inversamente proporcional entre as variáveis;

* Quanto mais próximo de 1 mais existe uma relação diretamente proporcional entre as variáveis;

* Quanto mais próximo de 0 menor o nível de influência entre as variáveis

###### Figura 14 - Matriz de correlação
![Matriz de correlação](https://github.com/2023M3T9-Inteli/grupo1/assets/124217721/00d5bbd0-6ae5-442b-b11c-df13e4745d09)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

&emsp;&emsp; De acordo com a matriz é possível perceber que:

* Itens com maior relação diretamente proporcional são: `revenue` e `items_sold`, `sku_lenght` e `sku_weight`, `avg_website_visits_last_week` e `items_sold`, `avg_website_visits_last_week` e `revenue`;

* Itens com maior relação inversamente proporcional são: `sku_lenght` e `supplier_delivery_time`, `unit_price` e `items_sold`, `sku_width` e `stock_qty`.

###### Figura 15 - Gráfico 1 - Quantidade de itens vendidos por macro categoria
![Gráfico 1 - Quantidade de itens vendidos por macro categoria](https://github.com/2023M3T9-Inteli/grupo1/assets/124165852/ac4d0be2-e4fe-4c41-8b22-21b2c672dbc7)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

Conclusão: As áreas com mais vendas são sofás, cadeiras de escritório e closets

###### Figura 16 - Gráfico 2 - Quantidade de itens vendidos por micro categoria
![Gráfico 2 - Quantidade de itens vendidos por micro categoria](https://github.com/2023M3T9-Inteli/grupo1/assets/124165852/ebe4a4c5-6618-45a6-a2ce-50138ecfb914)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

Conclusão: As áreas que acumulam mais venda são sala de estar, quarto e escritório

###### Figura 17 - Gráfico 3 - Quantidade de itens vendidos por dia da semana
![Gráfico 3 - Quantidade de itens vendidos por dia da semana](https://github.com/2023M3T9-Inteli/grupo1/assets/124165852/aa54c766-4518-418b-8146-7d2c4581355b)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

Conclusão: As vendas se mantém regulares durante todos os dias da semana, havendo algumas variancias não significativas


###### Figura 18 - Gráfico 4 - Mapa de calor de itens vendidos por dia e mês
![Gráfico 4 - Mapa de calor de itens vendidos por dia e mês](https://github.com/2023M3T9-Inteli/grupo1/assets/124217721/9d0dc03b-e068-4ce0-8f5f-6c3f9f2df05f)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

Conclusão: Os últimos dias do mês de novembro apresentam maior número de vendas, já os últimos dias do mês de dezembro e os primeiros dias do mês de janeiro apresentam uma baixa nas vendas. Além disso, é possível perceber que durante os seis primeiros meses do meio para o fim do mês ocorre uma leve queda nas vendas também.

###### Figura 19 - Gráfico 5 - Receita ao longo do tempo
![Gráfico 5 - Receita ao longo do tempo](https://github.com/2023M3T9-Inteli/grupo1/assets/124165852/f6d72678-3738-4d08-93b7-116107608e5a)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

Conclusão: É possível perceber que durante o fim de novembro de todos os três anos há um grande aumento de receita, enquanto que nos meses de dezembro e janeiro existe uma tendência de queda na receita

###### Figura 20 - Gráfico 6 - Quantidade de produtos vendidos por peso
![Gráfico 6 - Quantidade de produtos vendidos por peso](https://github.com/2023M3T9-Inteli/grupo1/assets/124165852/e52ceffd-cde8-4406-a12d-45ce739b41c6)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

Conclusão: Produtos mais leves apresentam maior quantidade de vendas

#### 4.2.2. Pré-processamento dos dados

&emsp;&emsp; O pré-processamento de dados é uma etapa fundamental no ciclo de vida de um projeto de análise de dados ou de aprendizado de máquina. Dessa forma, essa etapa envolve uma série de técnicas e procedimentos aplicados aos dados brutos para prepará-los e transformá-los em uma forma adequada para realizar diversas outras análises [6]. Sendo assim, uma das razões pelas quais a etapa de pré-processamento se torna crucial para os projetos já citados anteriormente está relacionada com a qualidade e a confiabilidade dos resultados que se deseja obter por meio desses dados, isto é, quanto mais eles são tratados, mais resultados precisos serão obtidos. 
Portanto, para que os dados utilizados durante o desenvolvimento do Mobil.ia estejam preparados corretamente, seguimos alguns passos, os quais são:
1. Tratamento de _missing values_: Etapa em que são identificados as colunas da base de dados que possuem algum dado nulo e, após identificá-los, é possível tratá-los através de algumas técnicas;
2. Limpeza de Dados: Etapa em que são removidas algumas colunas da base de dados que não serão utilizadas para o treinamento do modelo preditivo;
3. Tratamento de Outliers e Normalização das Variáveis Numéricas: Etapa em que são identificadas os outliers das variáveis numéricas, de modo a eliminar possíveis ruídos nos dados que serão utilizados no treinamento do modelo. Ademais, tal etapa conta com a normalização das variáveis numéricas, de modo a deixar os dados na mesma escala;
4. Transformação dos tipos de dados das variáveis: Etapa em que os dados da coluna são transformados para o seu tipo correto, uma vez que o próprio Pandas realiza tal identificação de forma automática, podendo, então, fazer a associação do tipo de forma equivocada;
5. Codificação das variáveis categóricas: Etapa em que as variáveis identificadas como categóricas, isto é, variáveis que armazenam conteúdos diferentes de números, são codificadas para números, uma vez que o modelo só conseguirá entender os dados neste formato. 

##### 4.2.2.1. Tratamento de _missing values_
&emsp;&emsp; Tendo em vista a importância do pré-processamento dos dados, foi realizado o tratamento de _missing values_ dentro da base de dados enviada pela Mobly. Em princípio, missing values, ou valores ausentes, são informações que deveriam estar presentes em uma coluna da base de dados, mas não foram registradas. Esses valores ausentes podem ocorrer por uma variedade de razões e podem ter um impacto significativo na qualidade e na utilidade dos dados. A partir disso, buscamos identificar esses _missing values_ dentro dos dados da Mobly, por meio dos comandos `df_day.isnull().sum()`, e obtemos, conforme demonstra a figura 21, as seguintes informações:


###### Figura 21 - _Missing values_ no conjunto de dados
![Missing values no conjunto de dados](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/86f9b674-1961-462d-8754-030ada8a0925)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

&emsp;&emsp; A figura acima destaca que as seguintes colunas possuem dados nulos: `sku_height`, `sku_width`, `sku_length`, `sku_weight` e `winning_price`.

&emsp;&emsp; Sabendo disso, foi necessário o tratamento desses dados. Para lidar com _missing values_, pode-se optar por diversas abordagens: 
* **Remoção:** Se os _missing values_ são relativamente poucos em relação ao tamanho total do conjunto de dados, é possível simplesmente remover as observações que possuem esses valores ausentes;
* **Preenchimento:** É possível preencher os _missing values_ com valores estimados, como a média, mediana ou moda da variável em questão. Isso mantém o tamanho do conjunto de dados, mas introduz uma certa imprecisão;
* **Modelagem:** Pode-se utilizar técnicas de modelagem para prever os valores ausentes com base em outras variáveis, pode ser uma abordagem mais sofisticada. Por exemplo, regressão pode ser usada para prever valores faltantes com base em outras variáveis disponíveis;
* **Agrupamento:** Em alguns casos, é possível agrupar as observações em _clusters_ semelhantes e, em seguida, estimar os missing values com base nos valores dos grupos.

&emsp;&emsp; Assim, para que pudéssemos tratar esses valores nulos, utilizamos a abordagem de **remoção**, isto é, dado as colunas `sku_height`, `sku_width`, `sku_weight` e `sku_length`, nós optamos por remover todos os registros identificados como nulos. Para confirmar essa remoção utilizamos o comando `df_filtred.isnull().sum()`. Sendo assim, a figura 22 evidencia a quantidade de dados nulos em tais colunas.


###### Figura 22 - Remoção dos _missing values_ 
![Remoção dos missing values](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/e9714877-7900-4367-8940-778bb5427afa)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

&emsp;&emsp; Em relação à coluna `winning_price` ela foi preenchida por meio de uma nova base de dados, a qual contém as informações atualizadas e completas relacionadas a essa _feature_. Portanto, ela não foi removida do dataframe, mas, sim, preenchida com valores atualizados, conforme indicado pelo parceiro em validação de sprint.

##### 4.2.2.2. Limpeza dos Dados
&emsp;&emsp; Uma outra etapa do pré-processamento dos dados consiste na limpeza das informações que não serão utilizadas, em um primeiro momento, durante o treinamento do modelo preditivo. Desse modo, o grupo optou por realizar a exclusão das seguintes colunas: `mobly_item`, `flag_bundle`, `revenue_bundle` e `items_sold_bundle`.

&emsp;&emsp; Em princípio, optamos excluir a coluna `mobly_item` devido a sua insignificância para o modelo, uma vez que não há nenhuma informação que possa ser aproveitada pelo modelo preditivo, algo que é evidenciado pela figura 23. Ademais, tal exclusão foi validada com o parceiro, o qual concordou com a ação:

###### Figura 23 - Dados da coluna `mobly_item`
![Dados da coluna "mobly_item"](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/a7da4940-f9c2-46fe-9b85-1c034b8700bf)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

&emsp;&emsp; Já em relação à exclusão das colunas `flag_bundle`, `revenue_bundle` e `items_sold_bundle`, nós optamos devido a sua função mais de complemento do que de relevância para o modelo preditivo. Tivemos esse entendimento, pois, de acordo com o TAPI, os produtos que estão cadastrados na base de dados foram registrados como produtos filhos (sozinhos), fazendo com que todas as suas características sejam relacionadas apenas a ele e tais colunas foram adicionadas como um complemento para a base de dados. Sendo assim, essa exclusão foi validada com o parceiro e eles concordaram com a ação. 

##### 4.2.2.3. Outliers e Normalização dos Dados
&emsp;&emsp; Essa etapa do pré-processamento é relacionada à identificação de valores que são muito destoantes da distribuição padrão dos dados, algo que pode ser negativo para determinados modelos preditivos. Dessa forma, como buscamos entender melhor os dados da Mobly, não tratamos diretamente esses outliers por exclusão com qualquer outra técnica (como a de substituição). Ademais, é válido ressaltar que o grupo optou por dois métodos de identificação de outliers:
* O método do z-score foi escolhido pelo grupo devido a sua assertividade com dados que possuem um comportamento de distribuição normal ou aproximadamente normal, uma vez que iremos normalizar todos os dados possíveis.
* Já o método de bloxpot foi escolhido devido a sua visualização mais clara dos outliers, além de que ele pode ter uma assertividade um pouco maior do que o método do z-score em determinados dados.

&emsp;&emsp; Assim, esses dois métodos serão utilizados para que possamos entender melhor os outliers, além de que fornece uma possibilidade de comparação entre os outliers identificados.
Além disso, para que possamos identificar os outliers de todas as colunas abaixo, todas elas passaram pelo processo de normalização utilizando a transformação logarítmica.

&emsp;&emsp; Em princípio, identificamos os outliers da coluna `unit_price`, a qual se trata do preço unitário dos produtos, para que possamos entender melhor o comportamento dos dados dessa coluna e a figura 24 evidencia alguns outliers utilizando o método do z-score, enquanto a figura 25 evidencia os outliers utilizando o método de bloxpot:

###### Figura 24 - Outliers identificados da coluna `unit_price` utilizando o método do z-score
![Outliers identificados da coluna `unit_price` utilizando o método do z-score](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/a1365bcc-bff8-4e69-8e82-95fef2ef68a9)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab


###### Figura 25 - Outliers identificados da coluna `unit_price` utilizando o método de bloxpot
![Outliers identificados da coluna `unit_price` utilizando o método de bloxpot](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/e5f0ecc7-dd8e-477d-b526-4b8fd66f81a6)

###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab


&emsp;&emsp; Uma outra coluna que identificamos outliers é a coluna `revenue`, que está relacionada à receita do produto. Assim, a figura 26 evidencia que não há outliers em tal coluna utilizando o método do z-score, enquanto a figura 27 também demonstra que não há outliers utilizando o método de bloxpot:

###### Figura 26 - Outliers identificados da coluna `revenue` utilizando o método do z-score
![Outliers identificados da coluna `revenue` utilizando o método do z-score](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/4bc1df1b-0f65-4800-bc91-01e4b3862e3a)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab


###### Figura 27 - Outliers identificados da coluna `revenue` utilizando o método de bloxpot
![Outliers identificados da coluna `revenue` utilizando o método de bloxpot](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/f4823d51-a0ff-49fe-a8e2-c8499ba0c095)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

&emsp;&emsp; Identificamos os outliers da coluna `avg_website_visits_last_week`, a qual está relacionada à média diária de visitas do produto no site nos últimos 7 dias. Sendo assim, a figura 28 evidencia os outliers utilizando o método do z-score, enquanto a figura 29 também os outliers utilizando o método de bloxpot:

###### Figura 28 - Outliers identificados da coluna `avg_website_visits_last_week` utilizando o método do z-score
![Outliers identificados da coluna `avg_website_visits_last_week` utilizando o método do z-score](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/0336eca8-90d1-4cfe-b266-c6d1ebe3f1d1)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

###### Figura 29 - Outliers identificados da coluna `avg_website_visits_last_week` utilizando o método de bloxpot
![Outliers identificados da coluna `avg_website_visits_last_week` utilizando o método de bloxpot](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/469e0fa9-436c-411e-a5fc-88f9bd770798)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

&emsp;&emsp; Tanto a figura acima quanto o método do z-score evidenciam que há diversos outliers. Assim, optamos por entender melhor o comportamento dos outliers à esquerda, os quais foram evidenciados pelo bloxpot, e, após entendermos melhor, verificamos que esses outliers se tratam de dados que representam o comportamento de acesso de usuários. 

&emsp;&emsp; Após isso, identificamos os outliers da coluna `supplier_delivery_time`, a qual se trata do tempo de entrega do fornecedor em dias. Portanto, a figura 30 evidencia que não há outliers utilizando o método do z-score, enquanto a figura 31 identifica os outliers utilizando o método de bloxpot:

###### Figura 30 - Outliers identificados da coluna `supplier_delivery_time` utilizando o método do z-score
![Outliers identificados da coluna `supplier_delivery_time` utilizando o método do z-score](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/a338a921-1cb6-43ef-9f3a-f87010822168)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

###### Figura 31 - Outliers identificados da coluna `supplier_delivery_time` utilizando o método de bloxpot
![Outliers identificados da coluna `supplier_delivery_time` utilizando o método de bloxpot](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/98c42e65-ba6d-4632-a21a-9fde21736422)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

&emsp;&emsp; O método de z-score evidencia que não há outliers na coluna `supplier_delivery_time`, mas o bloxpot evidencia que há outliers concentrados à esquerda e à direita. Sendo assim, como há uma diferenciação considerável na identificação de outliers de tal coluna, além de que são dados que representam uma realidade do tempo de entrega dos fornecedores, apresentamos tal gráfico para o parceiro, o qual explicou e disse que talvez tal coluna não seja tão necessária para o treinamento do modelo. 

&emsp;&emsp; Em relação aos outliers da coluna `stock_qty`, que se trata da quantidade em estoque, a figura 32 evidencia que não há outliers em tal coluna utilizando o método do z-score, enquanto a figura 33 também demonstra que não há outliers utilizando o método de bloxpot:

###### Figura 32 - Outliers identificados da coluna `stock_qty` utilizando o método do z-score
![Outliers identificados da coluna `stock_qty` utilizando o método do z-score](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/f321ade4-8952-4035-bf8b-ce86885b5bfa)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

###### Figura 33 - Outliers identificados da coluna `stock_qty` utilizando o método de bloxpot
![Outliers identificados da coluna `stock_qty` utilizando o método de bloxpot](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/ec553931-41f2-459e-9c36-f0ee1d8980e4)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

&emsp;&emsp; Por fim, identificamos os outliers da coluna `items_sold`, a qual se trata da quantidade de itens vendidos. Com isso, a figura 34 evidencia os outliers utilizando o método do z-score, enquanto a figura 35 também os outliers utilizando o método de bloxpot:

###### Figura 34 - Outliers identificados da coluna `items_sold` utilizando o método do z-score
![Outliers identificados da coluna `items_sold` utilizando o método do z-score](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/d964d7fc-453e-4f64-89c8-4b86c8f5ebeb)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

###### Figura 35 - Outliers identificados da coluna `items_sold` utilizando o método de bloxpot
![Outliers identificados da coluna `items_sold` utilizando o método de bloxpot](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/60199655-fd8a-44fa-916e-395388ced860)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

&emsp;&emsp; Por meio do entendimento dessas características, entendemos que tais outliers são produtos que possuem uma alta quantidade vendida, um preço mais acessível e o seu pico de venda é durante o período da blackfriday. 

&emsp;&emsp; Há colunas que não identificamos outliers, pois não vimos uma necessidade tão grande, uma vez que se tratam das características físicas dos produtos, como as colunas: `sku_height`, `sku_width`, `sku_length` e `sku_weight`. Desse modo, verificamos se era necessária a aplicação da normalização de seus dados e, de acordo com a figura 36, tal normalização não foi necessária, haja vista que estão na mesma escala.

###### Figura 36 - Dataframe apenas com as colunas `sku_height`, `sku_width`, `sku_length` e `sku_weight`
![Dataframe apenas com as colunas `sku_height`, `sku_width`, `sku_length` e `sku_weight`](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/13068204-f60a-4c17-8d81-b5c7bd6ea808)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

##### 4.2.2.4. Codificação das variáveis categóricas
&emsp;&emsp; Para que o modelo possa compreender as variáveis categórias presentes na base de dados, é necessário converter as suas informações em números. Nesse sentido, optamos por escolher dois métodos: 
* Utilizando o `LabelEncoder` do `sklearn`, o qual realiza um mapeamento dos rótulos presentes na variável e as convertem em números inteiros de forma automática
* Utilizando o `map` do `Pandas`, o qual é semelhante ao LabelEncoder, porém ele é mais utilizado quando deseja mapear rótulos mais binários (como “sim” e “não”) para números inteiros.

&emsp;&emsp; Assim, utilizamos o `LabelEncoder` para as colunas `weekday_name`, `sku_color`, `anchor_category`,  `product_category`, `product_department` e `sku`, uma vez que tais colunas possuem muitos valores diferentes. Já em relação às colunas `shipment_type`, `origin_country` e `process_costing` foi utilizado o método `map`, já que tais colunas possuem valores mais binários, como “yes” ou “no”. 

&emsp;&emsp; Portanto, a figura 37 exibe, de forma generalista, como ficou o dataframe com essa codificação:  
###### Figura 37 - Dataframe com as variáveis categóricas codificadas
![Dataframe com as variáveis categóricas codificadas](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/2c3c30b3-fb47-41ec-91a3-884a805ad0f3)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

#### 4.2.3. Hipóteses

#### Hipótese 1

##### Gráfico 2 - Quantidade de itens vendidos por micro categoria (Figura 16)

&emsp;&emsp; Nesse gráfico, utilizamos a diferenciação por barras verticais, divididas por categoria do produto. Os gráficos de barras verticais são especialmente eficazes para comparar valores entre várias categorias ou grupos. Os valores são organizados de forma linear ao longo do eixo horizontal, tornando mais intuitiva a comparação entre as barras adjacentes.

**Premissa:** Os produtos da categoria "Sala de Estar" são os que apresentam mais vendas (800 mil).

**Hipótese:** A sala de estar é uma parte fundamental de qualquer casa ou apartamento. É o espaço onde as pessoas geralmente se reúnem para relaxar, assistir TV, conversar com a família e receber visitas. Portanto, os móveis e acessórios para a sala de estar são considerados essenciais para a maioria das pessoas, o que cria uma demanda constante por esses produtos. Além disso, é possível perceber no Gráfico 1 - Quantidade de itens vendidos por macro categoria que os sofás também são os que apresentam mais vendas, o que pode contribuir para a colocação da micro categoria Sala de Estar.

#### Hipótese 2

##### Gráfico 4 - Mapa de calor de itens vendidos por dia e mês (Figura 18)

&emsp;&emsp; Para esse gráfico, pensamos em um mapa de calor por deixar evidente e destacado em cores os períodos em que houve uma maior incidência de vendas, facilitando a visualização. Cada coluna representa um dia e cada linha representa um mês.

**Premissa:** Com base na análise do gráfico de calor, é evidente que as vendas da Mobly mantêm uma certa constância ao longo do ano, com exceção de um aumento significativo no final do mês de novembro.

**Hipótese:** O aumento acentuado nas vendas no final de novembro, conforme observado no gráfico de calor, pode ser atribuído à participação da Mobly na Black Friday. A Black Friday é um evento de compras amplamente reconhecido, caracterizado por descontos significativos e promoções especiais oferecidas por várias empresas.

&emsp;&emsp; Essa hipótese sugere que a Mobly aproveita a Black Friday como uma oportunidade estratégica para impulsionar suas vendas. Durante esse período, a empresa pode adotar uma estratégia agressiva de marketing, oferecendo descontos substanciais em seus produtos ou promovendo ofertas exclusivas para atrair um grande volume de compradores. Esse aumento nas atividades promocionais e nas ofertas especiais leva a um aumento nas vendas, que é claramente refletido no gráfico de calor.

&emsp;&emsp; A constância nas vendas ao longo do ano, com exceção desse pico em novembro, indica que a Mobly provavelmente planeja cuidadosamente suas operações e estratégias de vendas para manter um equilíbrio entre a estabilidade de receita durante o ano e a maximização das vendas durante eventos como a Black Friday. Portanto, a hipótese enfatiza a importância estratégica da Black Friday como um período de aumento significativo nas vendas, graças às suas ofertas especiais e promoções. Um indício da veracidade dessa suposição, é que é um evento sazonal, ou seja, é perceptível em todos os quatro anos da base de dados (2020-2023).

#### Hipótese 3

##### Gráfico 6 - Quantidade de produtos vendidos por peso (Figura 20)

&emsp;&emsp; Neste gráfico tivemos o objetivo de transmitir de forma visual a relação do peso dos produtos, com seu volume de vendas. Optamos por um gráfico de dispersão (Scatter Plot), que utiliza pontos para apresentar as vendas

**Premissa:** Produtos mais leves são mais vendidos.

**Hipótese:** A relação entre o peso de um produto e suas vendas é inversamente proporcional, indicando que produtos mais leves tendem a ser mais vendidos do que produtos mais pesados, consumidores geralmente preferem produtos que sejam mais fáceis de manusear, transportar e armazenar. Produtos mais leves podem oferecer maior conveniência e praticidade. Além disso, estes produtos muitas vezes são acompanhados de preços, e custo de entrega mais baixos. Por exemplo, o custo de entrega de uma luminária geralmente é mais baixo que o custo de entrega de um armário. Além disso, a instalação de um produto leve costuma ser muito mais simples e prática do que a de um produto mais pesado.

&emsp;&emsp; Ressalta-se que na apresentação de validação com os parceiros ao final da sprint 2, foi pontuado que essa relação entre menores pesos apresentarem mais vendas não é causal, ou seja, não são os menores pesos que influenciam diretamente na hora da compra. Foi pontuado que isso acontece por, geralmente, os consumidores optarem por levar mais unidades de produtos mais baratos e, também, mais leves, como, por exemplo, um kit de cadeiras apresenta mais saídas de um produto em uma única compra do que a compra de uma unidade de sofá.

### 4.3. Preparação dos Dados e Modelagem

#### 4.3.1. Modelagem para o problema
##### 4.3.1.1 Escolha das features

&emsp;&emsp; No momento de escolha das features, o grupo optou por dividir entre features internas (que já fazem parte do dataframe) e features externas (que estão relacionadas a dados exteriores e que serão implementados dentro do dataframe).

&emsp;&emsp; Em relação às variáveis externas, o grupo optou por adicionar duas: **cotação do dólar** e **empregabilidade**. Tal escolha foi feita considerando o pedido do parceiro, haja vista que tais features externas podem representar características que influenciam ou não no poder de compra dos clientes e, portanto, na quantidade de itens vendidos. Nesse sentido, um outro aspecto que fundamenta a escolha dessas duas features é o poder que elas possuem ao se juntarem com outras variáveis internas, como o mês de compras, uma vez que o dólar e a empregabilidade pode variar bastante de mês e mês, algo evidenciado pela figura 38. Ademais, um último motivo seria o desempenho que tais várias forneceram para as métricas do modelo final, algo evidenciado no notebook "Dataset_Updates", o qual mostra os testes do modelo com o conjunto de dados sem e com a presença das variáveis externas. A partir desses testes realizados no notebook já citado, é evidente que as métricas do modelo obtiveram uma melhora significativa com a presença das __features__ externas no conjunto de dados. 

###### Figura 38 - Mapa de correlação do conjunto de dados com as features externas
![Mapa de correlação do conjunto de dados com as features externas](https://github.com/2023M3T9-Inteli/grupo1/assets/86068799/0241b912-b207-41a8-9573-f2bf1bc1af15)
###### Fonte: Elaborada pelos autores (2023), utilizando o Google Colab

&emsp;&emsp; Ao longo do treinamento dos modelos, mais _features_ sofreram mudanças que condizem com as etapas seguintes e, portanto, serão explicadas durante a modelagem dos dados.

##### 4.3.1.2 Processo de Modelagem
  &emsp;&emsp; Após termos realizado todo o preparamento dos dados, escolhemos dois algoritmos de aprendizagem de máquina para testar, de forma inicial, o desempenho desses algoritmos nos dados que passaram por um pré-processamento. Sendo assim, esses dois modelos foram escolhidos com o intuito de entender melhor o funcionamento de ambos e o quanto eles poderiam ser aplicáveis no projeto que está sendo desenvolvido. Com isso, selecionamos o modelo **Random Forest** e o **Prophet**.

  &emsp;&emsp; Em relação ao Random Forest, ele é um modelo que tem como base um algoritmo que cria um conjunto de árvores de decisões individuais e combina suas previsões para um resultado mais preciso. A escolha desse algoritmo para teste foi feito porque ele lida bem com modelos de regressão e se mostra ser bem completo, lidando com diferentes tipos de features e questões como _ovefitting_ e outliers.

 &emsp;&emsp; Durante a aplicação do algoritmo, foi necessário excluir algumas colunas que poderiam diminuir a performance do modelo, uma vez que o Random Forest consegue lidar melhor com dados brutos ao invés de normalizados. Sendo assim, essas colunas são:
 
* A coluna `date`, pois o algoritmo não aceita dados que são do tipo `date.time`. Essa exclusão não alterou de forma negativa o modelo, uma vez que tal coluna já havia sido fragmentada em três colunas: `day`, `month` e `year`;
* As colunas de log, uma vez que o modelo lida bem com dados não normalizados e essas colunas normalizadas a partir do log poderiam abrir brechas para a ocorrência do overffiting ou, até mesmo, de uma variância indesejada dos dados gerados pelo modelo. Além disso, essas colunas de log geram dados muito granulares, fazendo com que as árvores do modelo se torne muito complexa;
* A coluna `winning_price`, uma vez que apresentava dados nulos. Essa coluna foi preenchida posteriormente, haja vista que o parceiro disponibilizou uma base de dados que contém tal coluna preenchida;
* A coluna revenue, uma vez que ela sobrepõe as colunas `items_sold` e `unit_price` e, portanto, gera data leakage.

&emsp;&emsp; Depois de realizarmos essa limpeza de ruídos realizamos o treinamento do modelo e, depois, avaliamos as suas métricas, as quais estarão destacadas no tópico 4.3.3.

&emsp;&emsp; Já em relação ao Prophet, ele também é um algoritmo de aprendizagem de máquina, criado pelo Facebook, e que realiza previsões de séries temporais [12]. Neste contexto, uma série temporal refere-se a um conjunto de dados que varia com o tempo, como as vendas de produtos ao longo de meses ou anos. Embora seja uma ferramenta poderosa e de fácil uso, é importante notar que o Prophet se mostrou limitado ao lidar com muitas variáveis ou dados complexos, já que ele considera apenas duas colunas: a coluna de data das vendas e a coluna de itens vendidos. É válido ressaltar que a escolha do Prophet, em um primeiro momento, teve a motivação baseada na curiosidade de entender como o algoritmo poderia contribuir para o desenvolvimento da Mobil.ia.


#### 4.3.2. Métricas

&emsp;&emsp; As métricas desempenham um papel essencial na avaliação de modelos de regressão supervisionados, fornecendo uma avaliação quantitativa do desempenho e da qualidade das previsões. Em um modelo de regressão, o objetivo principal é criar uma relação entre variáveis de entrada e variáveis de saída, permitindo que o modelo faça previsões precisas com base nos dados de treinamento.
Sabendo disso, pensamos em 4 métricas para o nosso modelo, sendo elas:

**1. MAE (Erro Absoluto Médio)**: O Erro Absoluto Médio (MAE) foi selecionado como uma métrica de avaliação para nosso modelo de regressão supervisionado devido às suas características valiosas. Nesse sentido, o MAE mede a média das diferenças absolutas entre as previsões do modelo e os valores reais, independentemente de serem erros positivos ou negativos [9], algo evidenciado na figura 39. Esta escolha é relevante para o contexto deste projeto, pois estamos interessados em avaliar a precisão média das previsões sem favorecer erros positivos ou negativos.
Ao utilizar o MAE como métrica de avaliação, garantimos que o modelo desenvolvido seja sensível a todos os tipos de erros, o que é importante para entender como as previsões geradas se desviam dos valores reais em termos de magnitude média.

###### Figura 39 - Fórmula do MAE
![Fórmula do MAE](https://github.com/2023M3T9-Inteli/grupo1/assets/123953851/b3228e0d-7351-42c4-a090-624ebf27b138)
###### Fonte: Elaborada pelos autores (2023)

&emsp;&emsp; Tendo em vista a figura acima, abaixo há uma explicação sobre as incógnitas presentes na fórmula: 
- n:  número de amostras.
- Y<sub>i</sub>: valores reais.
- Ŷ<sub>i</sub>: previsões feitas pelo modelo para as respectivas amostras.


**2. MSE (Erro Quadrático Médio):** O Erro Quadrático Médio (MSE) foi escolhido como uma métrica adicional para a avaliação do modelo de regressão supervisionado. Optamos por incluir o MSE devido à sua capacidade de penalizar erros maiores de forma mais significativa, o que é relevante para nossa necessidade de identificar previsões que tenham erros consideráveis.
A inclusão do MSE como métrica complementar ao MAE permite uma visão mais abrangente do desempenho do modelo. Nessa direção, o MSE leva em consideração a magnitude dos erros e, ao elevar os erros ao quadrado [9], conforme evidencia a figura 40, proporciona maior peso a erros maiores, fornecendo uma perspectiva mais sensível a previsões imprecisas.

###### Figura 40 - Fórmula do MSE
![Fórmula do MSE](https://github.com/2023M3T9-Inteli/grupo1/assets/123953851/ac3823e2-20b7-4e94-bf21-5156639782cd)
###### Fonte: Elaborada pelos autores (2023)

&emsp;&emsp; Tendo em vista a figura acima, abaixo há uma explicação sobre as incógnitas presentes na fórmula: 
- n:  número de amostras.
- Y<sub>i</sub>: valores reais.
- Ŷ<sub>i</sub>: previsões feitas pelo modelo para as respectivas amostras.

**3. RMSE (Raiz quadrada do erro-médio):** O RMSE foi escolhido com métrica para o modelo desenvolvido, pois desempenha um papel fundamental ao quantificar a diferença entre os valores previstos pelo modelo e os valores reais observados. Desse modo, o cálculo do RMSE envolve a determinação da raiz quadrada da média dos erros ao quadrado [9], algo mostrado na figura 41, o que resulta em uma medida que expressa a dispersão dos erros de previsão. A utilidade do RMSE se mostra na capacidade de refletir a magnitude dos erros cometidos pelo modelo em relação aos dados reais. Um RMSE baixo indica que o modelo está produzindo previsões próximas aos valores reais, enquanto um RMSE elevado sugere que há espaço para melhorias no ajuste do modelo.


###### Figura 41 - Fórmula do RMSE
![Fórmula do RMSE](https://github.com/2023M3T9-Inteli/grupo1/assets/123921392/7ddc7ec9-2494-4bee-817d-b4bca54cff04)
###### Fonte: Elaborada pelos autores (2023)

&emsp;&emsp; Tendo em vista a figura acima, abaixo há uma explicação sobre as incógnitas presentes na fórmula: 
- n:  Número de amostras.
- Y<sub>i</sub>: Valores reais.
- Ŷ<sub>i</sub>: Previsões feitas pelo modelo para as respectivas amostras.

**3. R² Score (Coeficiente de Determinação):** O Coeficiente de Determinação foi escolhido como a métrica principal para a avaliação do nosso modelo e o _R² Score_ varia de 0 a 1, onde valores próximos de 1 indicam que o modelo é capaz de explicar uma grande parte da variação nos dados, enquanto valores próximos de 0 indicam que o modelo não está explicando bem a variabilidade [10]. A importância do _R² Score_ se dá na sua capacidade de fornecer uma visão panorâmica da qualidade global do ajuste do modelo. Ele não se concentra na magnitude dos erros individuais, mas sim na capacidade do modelo de explicar as variações totais nos dados. A figura 42 evidencia a fórmula utilizada para calcular o _R² Score_.

###### Figura 42 - Fórmula do _R² Score_
![Fórmula do _R² Score_](https://github.com/2023M3T9-Inteli/grupo1/assets/123921392/13b0173e-c9c2-42c7-9889-15350426b583)
###### Fonte: Elaborada pelos autores (2023)

&emsp;&emsp; Tendo em vista a figura acima, abaixo há uma explicação sobre as incógnitas presentes na fórmula: 
- Y<sub>i</sub>: Valores reais.
- Ŷ<sub>i</sub>: Previsões feitas pelo modelo para as respectivas amostras.
- Y Linha: Média dos valores reais observados.
- n: Número de amostras.

&emsp;&emsp; Em resumo, a escolha cuidadosa das métricas é fundamental para a avaliação do modelo. O uso dessas métricas permite quantificar o desempenho do modelo, destacando sua capacidade de fazer previsões precisas e capturar relacionamentos entre variáveis. Ao adotar métricas adequadas e interpretar seus resultados de maneira significativa, o grupo consegue ajustar parâmetros do modelo e garantir que ele atenda aos requisitos específicos do projeto. Dessa forma, as métricas se tornam ferramentas valiosas para orientar o desenvolvimento e a otimização do modelo.

#### 4.3.3. Modelo Candidato e Discussão dos seus Resultados 
&emsp;&emsp; Após realizarmos a modelagem do problema no tópico 4.3.1, escolhemos utilizar para o desenvolvimento do modelo preditivo para a Mobly o algoritmo **Random Forest**.

&emsp;&emsp; O Random Forest é um algoritmo que seleciona subconjuntos de features e, a partir deles, é possível formar diversas mini árvores de decisão [11]. Sendo assim, o algoritmo, por meio de suas diversas árvores de decisão, consegue produzir previsões mais robustas e precisas.
Em relação ao contexto do projeto, que é prever a quantidade de itens de um determinado SKU em um certo período, o Random Forest demonstrou ser um algoritmo compatível com o objetivo do projeto, haja vista que:
* A base de dados fornecida pela Mobly possui várias features com diferentes características, algo que o Random Forest tem facilidade de lidar para realizar a previsão;
* O Random Forest ajuda a reduzir o risco de overfitting devido à presença da combinação de diferentes árvores de decisão, algo importante para que o modelo consiga se ajustar, de forma equilibrada, tanto aos dados de teste quanto aos dados de treino, gerando, então, uma generalização dos dados balanceada e previsões confiáveis;
* O Random Forest consegue lidar, de forma robusta, com a presença de outliers nos dados que estão sendo utilizados para formular o modelo, algo que ajuda a diminuir os impactos nas previsões.

&emsp;&emsp; Portanto, após todas essas análises mais profundas sobre o Random Forest, é visível que tal algoritmo se destaca para solucionar o problema do projeto em questão e, por isso, escolhemos tal algoritmo para que ele seja o nosso modelo candidato. Ademais, no tópico a seguir será destacado os seus resultados em comparação com os outros modelos que testamos no tópico Testes de diferentes modelos. 

&emsp;&emsp; Como destacado anteriormente, escolhemos o **Random Forest** como o nosso modelo candidato para prever a quantidade de itens vendidos durante um período e, por isso, buscamos analisar de forma mais detalhada as métricas de avaliação dos seus resultados, algo que é de suma importância para o objetivo do projeto desenvolvido para a Mobly. 

&emsp;&emsp; Em princípio, as métricas utilizadas para avaliar tal desempenho do modelo foram aquelas destacadas no tópico 4.3.2, que são: MAE (Erro Absoluto Médio), MSE (Erro Quadrático Médio), RMSE (Raiz Quadrada do Erro Médio) e _R² Score_ (Coeficiente de Determinação). É válido destacar que, diante dessas quatro métricas, a que mais prezamos para avaliar o desempenho do **Random Forest** treinado foi a _R² Score_, dado que ela é fácil de interpretar e de entender, além de que consegue expressar uma medida da qualidade geral do modelo, haja vista que tal métrica explica a variabilidade presente nos dados de saída gerados pelo modelo. 


&emsp;&emsp; Sendo assim, mesmo prezando pela _R² Score_, realizamos a análise de todas as métricas citadas, pois são fundamentais para fornecer uma avaliação quantitativa da qualidade das previsões geradas pelo modelo, decidimos treinar o modelo **Random Forest** e analisar tais métricas aplicadas ao modelo e, assim, obtemos os seguintes resultados:
* **Erro Absoluto Médio (MAE):** 1.537142967017472
* **Erro Quadrático Médio (MSE):** 11.464828062709106
* **Raiz quadrada do erro-médio (RMSE):** 3.385975201136167
* **Coeficiente de Determinação (R² Score):** 0.6854606655019839

&emsp;&emsp; Tendo esses números de cada métrica de avaliação em vista, é importante destacar qual a importância de tais resultados. Em relação ao MAE, como ele representa a média das diferenças absolutas entre as previsões, o valor do MAE de aproximadamente 1,54 sugere que, em média, o modelo desenvolvido consegue prever a quantidade de itens vendidos por SKU com um erro absoluto de cerca de 1,54 unidades. Isso sugere que as previsões geradas pelo modelo estão, de certa forma, precisas, haja vista que, quanto mais próximo de zero o valor do MAE estiver, mais preciso é o modelo.

&emsp;&emsp; Sobre o MSE, como ele calcula a média dos quadrados das diferenças entre as previsões geradas pelo modelo e os valores reais, o valor do MSE de aproximadamente 11,46 indica que o modelo tem um erro médio quadrático de cerca de 11,46 unidades. Isso sugere que o modelo contém erros médios significativos, podendo ser um ponto de alerta para que o modelo preditivo desenvolvido seja mais preciso do que isso. Sendo assim, o próximo passo será ajustar tal modelo candidato para que essa métrica de avaliação possa ser otimizada.

&emsp;&emsp; No que diz respeito ao RMSE, o qual calcula a raiz quadrada do MSE, o seu valor de aproximadamente 3,39 unidades de quantidade de itens vendidos indica que o modelo erra em cerca de 3,39 unidades em suas previsões. Isso indica que o modelo está gerando previsões que ainda não alcançaram o estágio de precisão desejado, o que evidencia que o modelo está no caminho certo, porém precisa passar por alguns processos de melhorias e otimização.

&emsp;&emsp; No que tange o _R² Score_, como ele consegue fornecer a proporção da variação dos dados, o valor de _R² Score_ de cerca de 0,69 significa que o modelo desenvolvido é capaz de explicar 69% das variações presentes nos dados de vendas. Com isso, é possível observar que o modelo apresenta um desempenho razoavelmente bom, haja vista que, quanto mais próximo o valor de _R² Score_ estiver de 1, mais o modelo consegue explicar as variações presentes nos dados e, seguindo essa linha, o modelo treinado e desenvolvido até então está conseguindo explicar mais da metade da variabilidade presente nos dados, indicando que tal modelo candidato está conseguindo capturar determinados padrões de dados de forma coerente. 


### 4.4. Comparação de Modelos
#### 4.4.1 Métrica de Avaliação dos Modelos Candidatos 

&emsp;&emsp; Em princípio, as métricas que serão utilizadas para avaliar o desempenho dos modelos candidatos abaixo são explicadas no tópico 4.3.2 e são: MAE (Erro Absoluto Médio), MSE (Erro Quadrático Médio), RMSE (Raiz Quadrada do Erro Médio) e _R² Score_ (Coeficiente de Determinação). Mas, mesmo observando todas essas métricas em cada um dos modelos, optamos por ter um foco maior em três delas, sendo o _R² Score_, o MAE e o RMSE, uma vez que tais métricas fornecem informações mais precisas sobre a assertividade do modelo. Além de que os seus valores possuem uma fácil interpretação.

&emsp;&emsp; Em relação ao _R² Score_, tal métrica representa uma medida geral da qualidade do modelo, pois quantifica a capacidade do modelo em explicar a variabilidade presente nos dados de saída gerados pelo algoritmo.

&emsp;&emsp; Já em relação às métricas MAE e RMSE, embora compartilhem a mesma escala, ambas fornecem informações valiosas sobre o erro das previsões. O MAE representa o erro médio dos dados gerados pelo modelo, enquanto o RMSE indica o erro médio, mas também consegue penalizar os erros mais significativos.

&emsp;&emsp; A partir disso, é válido destacar que as três métricas escolhidas pelo grupo para avaliar os modelos possuem uma extrema relevância para o desenvolvimento da Mobil.ia, dado que o modelo precisa prever a quantidade de itens vendidos por SKU com a maior precisão possível (algo destacado tanto pelo TAPI quanto pelos parceiros da Mobly), de modo que a equipe de Supply Chain da organização possa tomar as devidas decisões para equilibrar o abastecimento de estoque. A importância da precisão do modelo desenvolvido está centrada, principalmente, no quanto os resultados gerados pelo algoritmo podem afetar a empresa parceira, pois:
* Caso o algoritmo realize uma grande quantidade de previsões corretas (ou minimamente corretas), a Mobly poderá ter o seu lucro aumentado, pois terá produtos disponíveis para suprir as demandas dos seus clientes, sem desperdiçar materiais e, por consequência, sem perder o dinheiro investido. Além de que, por meio dessa disponibilidade, há a possibilidade da Mobly ter mais clientes e, consequentemente, aumentar o seu número de vendas e melhorar a imagem da marca;
* Caso o algoritmo realize uma grande quantidade de previsões incorretas, a Mobly poderá ter uma queda no seu lucro, pois a disponibilidade dos produtos pode variar, haja vista que o estoque não será bem abastecido. Além disso, a empresa pode lidar com o desperdício de materiais (e, como consequência, a perda de dinheiro), com a perda de clientes e com a desvalorização da marca.

&emsp;&emsp; Sendo assim, como as métricas _R² Score_, MAE e RMSE conseguem explicar a variabilidade e o erro médio dos dados de forma mais direta que as demais métricas, elas são de extrema importância para que o modelo preditivo desenvolvido consiga contribuir positivamente para a Mobly. Ademais, é válido destacar que as outras métricas não serão descartadas ou ignoradas, apenas iremos analisar de forma mais concentrada as três métricas já citadas, além de que essa decisão foi validada com o parceiro de projeto na terceira sprint.

#### 4.4.2 Modelos candidatos com tunings hiperparâmetros e métricas alcançadas

&emsp;&emsp; Após realizarmos a escolha inicial de um modelo candidato no tópico 4.3.3, que foi o **Random Forest**, o grupo continuou explorando outros algoritmos de aprendizagem de máquina para selecionar um modelo concreto para o desenvolvimento da Mobil.ia. Sendo assim, selecionamos outros dois algoritmos novos e aprimoramos o algoritmo **Random Forest**. 

&emsp;&emsp;Ademais, é válido ressaltar que, além da escolha de dois novos modelos preditivos e o aprimoramento do **Random Forest**, neste tópico será evidenciada a aplicação de otimização dos três algoritmos por meio dos hiperprâmetros. Nesse sentido, a otimização dos hiperparâmetros é o método responsável por ajustar as configurações próprias de cada modelo de predição, a fim de buscar aquelas que melhor se encaixam com o conjunto de dados utilizados para treinar esse algoritmo. Dessa forma, essa otimização é utilizada para melhorar o desempenho do modelo, promovendo uma melhor adaptação ao caso específico e ao seu conjunto de dados.

&emsp;&emsp;Dentre os algoritmos de otimização existentes, os mais utilizados são o **Random search** e o **Grid search**. O **Grid Search** é um algoritmo de otimização de hiperparâmetros relativamente simples e realiza a busca, em um conjunto de dados, de um ou mais hiperparâmetros, de modo a testar todas as combinações possíveis entre eles [13]. Os benefícios desse modelo consistem em uma exploração mais completa e robusta por meio de uma abordagem simples de implementar. Ao mesmo tempo, pode não ser tão viável em alguns casos, como, por exemplo, em _datasets_ muito grandes, podendo ser ineficiente e demorado. Já o **Random Search** possui um funcionamento muito parecido com o algoritmo anterior, porém, ao invés de testar todas as combinações, ele realiza uma busca aleatória, isto é, esse algoritmo testa combinações aleatórias de hiperparâmetros, de acordo com um número especificado de amostras [13]. Entre os benefícios desse algoritmo, é possível destacar a eficiência, uma vez que consegue ser aplicado em um tempo razoável (sendo ideal para datasets maiores) e, ao mesmo tempo, apresentar bons resultados. Entretanto, uma desvantagem desse algoritmo é que não há garantia de encontrar o melhor conjunto de hiperparâmetros, uma vez que não consegue abranger todos os tipos de combinações.

&emsp;&emsp; A partir disso, o grupo optou por aplicar os dois algoritmos de otimização citados para os modelos escolhidos. A aplicação do algoritmo de otimização será ajustada conforme o desempenho deles em cada modelo, e ao fim, será escolhido o melhor algoritmo para cada modelo e as respectivas métricas resultantes.


&emsp;&emsp; Portanto, abaixo será apresentado os dois algoritmos novos e suas respectivas otimização por meio de hiperparâmetros.

##### 4.4.2.1 **Regressão Linear** 
 
&emsp;&emsp; A regressão linear é uma técnica estatística fundamental no campo da análise de dados e aprendizado de máquina. Ela é usada para modelar a relação entre uma variável dependente (rótulo) e uma ou mais variáveis independentes (características) por meio de uma equação linear. O objetivo da regressão linear é encontrar a linha reta que melhor se ajusta aos dados, permitindo fazer previsões ou inferências sobre os valores da variável dependente com base nas variáveis independentes. É uma abordagem simples e interpretável para a modelagem de relacionamentos lineares entre variáveis e é amplamente aplicada em diversos domínios, incluindo economia, ciências sociais, ciência dos dados e engenharia [17].

&emsp;&emsp; Entretanto, a regressão linear possui limitações importantes. A principal delas é a suposição de uma relação estritamente linear entre as variáveis. Isso implica que o modelo presume que as mudanças nas variáveis independentes têm um efeito linear nas mudanças na variável dependente. Quando essa suposição não se aplica, a regressão linear torna-se inadequada. Se, por exemplo, a relação entre as variáveis for curvilínea ou não linear, a regressão linear não será capaz de captar essa complexidade. Além disso, essa abordagem não lida bem com relações não lineares entre variáveis [17].

&emsp;&emsp; Tendo em vista as limitações presentes no algoritmo de Regressão Linear, treinamos e testamos o modelo, utilizando o pacote `sklearn` e foi obtido os seguintes resultados em relação às métricas utilizadas:

* **Erro Absoluto Médio (MAE):** 2.3551262630973295
* **Erro Quadrático Médio (MSE):** 25.32130884490815
* **Raiz quadrada do erro-médio (RMSE):** 5.03202830326978
* **Coeficiente de Determinação (R² Score):** 0.30530596803262156

&emsp;&emsp; Assim, conduzimos um processo de otimização de hiperparâmetros para o modelo de Regressão Linear. Utilizamos dois algoritmos de busca de hiperparâmetros: **Random Search** e **Grid Search**, com o objetivo de avaliar se poderíamos melhorar o desempenho deste modelo.

**Random Search aplicado ao algoritmo de Regressão Linear**

&emsp;&emsp; Inicialmente, aplicamos o **Random Search** com 50 iterações, a partir da configuração própria do algoritmo, o `n_iter`, para explorar um amplo espaço de hiperparâmetros. O número de iterações corresponde à quantidade de tentativas que serão realizadas na busca aleatória por hiperparâmetros. 

&emsp;&emsp; Utilizamos os seguintes hiperparâmetro para o **Random Search** :

  * `positive`: Quando definido como `True`, impõe a restrição de que os coeficientes do modelo devem ser não negativos. Isso é útil quando você tem conhecimento prévio de que os coeficientes devem ser positivos [29].

  * `fit_intercept`: Este parâmetro determina se a intercepção (ou viés) deve ser ajustada no modelo linear. Se for definido como `True`, o modelo ajustará a intercepção. Se for definido como `False`, o modelo não terá uma intercepção e passará pela origem [29]. 

  * `copy_X`: Este parâmetro determina se os dados de entrada (X) devem ser copiados antes do ajuste do modelo. Quando definido como `True`, uma cópia dos dados é feita para evitar modificações indesejadas. Quando definido como `False`, o modelo ajusta os dados diretamente [29]. 

&emsp;&emsp; Com isso, os melhores hiperparâmetros encontrados foram:

``` {'positive': False, 'fit_intercept': True, 'copy_X': True} ```

&emsp;&emsp; Após a otimização, as métricas de desempenho do modelo de **Regressão Linear**, com o **Random Search** aplicado, foram as seguintes:

* **Erro Absoluto Médio (MAE):** 2.262477724751736
* **Erro Quadrático Médio (MSE):** 20.573031793205057
* **Raiz quadrada do erro-médio (RMSE):** 4.535750411255568
* **Coeficiente de Determinação (R² Score):** 0.32892618312915434

**Grid Search aplicado ao algoritmo de Regressão Linear**

&emsp;&emsp; Utilizamos os seguintes hiperparâmetro para o **Grid Search** :

  * `positive`: Quando definido como `True`, impõe a restrição de que os coeficientes do modelo devem ser não negativos. Isso é útil quando você tem conhecimento prévio de que os coeficientes devem ser positivos [29].

  * `fit_intercept`: Este parâmetro determina se a intercepção (ou viés) deve ser ajustada no modelo linear. Se for definido como `True`, o modelo ajustará a intercepção. Se for definido como `False`, o modelo não terá uma intercepção e passará pela origem [29]. 

  * `copy_X`: Este parâmetro determina se os dados de entrada (X) devem ser copiados antes do ajuste do modelo. Quando definido como `True`, uma cópia dos dados é feita para evitar modificações indesejadas. Quando definido como `False`, o modelo ajusta os dados diretamente [29]. 

&emsp;&emsp; Em seguida, aplicamos o **Grid Search** para uma busca mais exaustiva de hiperparâmetros. Os melhores hiperparâmetros encontrados foram:

``` {'copy_X': True, 'fit_intercept': True, 'positive': False}```

&emsp;&emsp; Surpreendentemente, os resultados após a otimização com o **Grid Search** foram idênticos aos obtidos com o **Random Search**:
* **Erro Absoluto Médio (MAE):** 2.262477724751736
* **Erro Quadrático Médio (MSE):** 20.573031793205057
* **Raiz quadrada do erro-médio (RMSE):** 4.535750411255568
* **Coeficiente de Determinação (R² Score):** 0.32892618312915434

&emsp;&emsp; É evidente que, mesmo após a otimização de hiperparâmetros, as métricas de desempenho do modelo de Regressão Linear não apresentaram uma melhoria significativa. Isso salienta a conclusão de que, no contexto deste projeto específico, a Regressão Linear pode não ser a escolha mais adequada. Isso se deve ao modelo alternativo identificado no notebook de "Modelagem", que ostenta um valor de _R² Score_ de cerca de 68%, consideravelmente superior ao valor obtido pela otimização da Regressão Linear, que alcançou aproximadamente 32%. Além disso, é pertinente comparar o MAE e o RMSE da Regressão Linear com o modelo alternativo mencionado anteriormente. O MAE da Regressão Linear é aproximadamente 2,26 unidades, enquanto o RMSE é aproximadamente 4,53. Em contraste, o modelo alternativo apresenta um MAE de 1,53 e um RMSE de 3,38, evidenciando que o modelo de Regressão Linear está cometendo significativos erros em suas previsões. Portanto, com base nestes resultados, seria apropriado considerar a exploração de modelos mais complexos ou mais adequados para abordar o problema em questão.

##### 4.4.2.2 **Árvore de decisão** 
 
 &emsp;&emsp; A Árvore de Decisão funciona construindo uma estrutura de árvore na qual cada nó representa uma decisão baseada em uma característica (ou atributo) específica dos dados. A ideia principal por trás de uma árvore de decisão é dividir iterativamente o conjunto de dados em subconjuntos menores e mais homogêneos com base nas características, até que uma decisão final seja tomada. A segmentação que a Árvore faz, permite a captura de padrões e interações entre os preditores. Essa abordagem também lida bem com dados heterogêneos e pode acomodar variáveis categóricas, tornando-a uma escolha versátil para a modelagem de regressão em uma grande quantidade de aplicações.

 
 &emsp;&emsp;No entanto, o algoritmo de árvore de decisão apresenta algumas limitações que devem ser levadas em consideração ao utilizar um dataset com uma grande quantidade de dados, algo que é a realidade deste projeto. Uma dessas limitações é a tendência de criar modelos excessivamente complexos, que memorizam o conjunto de treinamento, resultando em possíveis problemas de overfitting. Isso pode prejudicar a capacidade do modelo de fazer previsões precisas quando novos dados são introduzidos [14].

 &emsp;&emsp;Além disso, o algoritmo de Árvore de Decisão pode ser instável, pois pequenas variações nos dados de treinamento podem levar a árvores de decisão bastante diferentes. Outra limitação está relacionada à demanda incomum de recursos computacionais quando se lida com datasets muito grandes. Isso ocorre devido aos cálculos envolvidos no algoritmo, o que resulta em um aumento no tempo de execução do algoritmo [15].

&emsp;&emsp; Mesmo diante das limitações acima, resolvemos treinar e testar o modelo de Árvore de Decisão, utilizando o pacote `sklearn`, para saber qual seria o desempenho do algoritmo. Sendo assim, foi obtido os seguintes resultados em relação às métricas utilizadas:

* **Erro Absoluto Médio (MAE):** 2.3976261886782666
* **Erro Quadrático Médio (MSE):** 26.63081900872144
* **Raiz quadrada do erro-médio (RMSE):** 5.160505693119759
* **Coeficiente de Determinação (R² Score):** 0.269379353765814

&emsp;&emsp; Com essas métricas do modelo em mãos, o grupo optou por otimizar o modelo a partir dos algoritmos **Random Search** e **Grid Search**. 

**Random Search aplicado ao algoritmo de Árvore de Decisão**

&emsp;&emsp; Assim como ocorreu no modelo de Regressão Linear, aplicamos o algoritmo de otimização de hiperparâmetro **Random Search** no modelo de Árvore de Decisão com 50 iterações. Essa escolha de iterações está atrelada a possibilidade de se observar um amplo espaço de hiperparâmetros. Portanto, o algoritmo de otimização por hiperparâmetros **Random Search** gerou os melhores hiperparâmetros possíveis:

`{'min_samples_split': 3, 'min_samples_leaf': 9, 'max_depth': 14}`

&emsp;&emsp;A partir da obtenção dos hiperparâmetros acima, através do **Random Search** aplicado ao algoritmo de Árvore de Decisão, é necessário compreender, de maneira abrangente, o significado de cada um deles, bem como a capacidade que possuem de afetar o desempenho do modelo de Árvore de Decisão. Nesse sentido, abaixo será definido cada um dos hiperparâmetros:

* **min_samples_split:** Trata-se de um hiperparâmetro  que define o "número mínimo de amostras necessárias para dividir um nó interno" [30]. Esse hiperparâmetro controla o quão "criteriosa" a árvore deve ser ao decidir dividir um nó interno em subnós. No caso do modelo em questão, o número mínimo de amostras necessárias para dividir um nó interno é três.
* **min_samples_leaf:** Esse hiperparâmetro trata-se do "número mínimo de amostras necessárias para estar em um nó folha" [30]. Esse hiperparâmetro afeta o tamanho mínimo permitido para um nó folha. Sendo assim, neste modelo o número mínimo de amostras necessárias para estar em um nó fola é nove.
* **max_depth:** Por fim, esse hiperparâmetro define a "profundidade máxima das árvores" [30]. A profundidade de uma árvore de decisão determina até que ponto ela pode se ramificar, o que impacta a complexidade do modelo. A partir disso, a profundidade máxima deste modelo é 14.

&emsp;&emsp; Já em relação as métricas obtidas por meio da otimização de hiperparâmetros com o algoritmo **Random Search**, no caso deste modelo, são:
* **Erro Absoluto Médio (MAE):** 1.6351466432565025
* **Erro Quadrático Médio (MSE):** 10.969213266190533
* **Raiz quadrada do erro-médio (RMSE):** 3.311980263556915
* **Coeficiente de Determinação (R² Score):** 0.6421941166180443 

&emsp;&emsp; A análise dos resultados obtidos acima evidencia a eficácia da otimização de hiperparâmetros utilizando o algoritmo **Random Search**. Inicialmente, o modelo não otimizado apresentava um valor aproximado do _R² Score_ de 26%, enquanto, após a aplicação da otimização, tal métrica aumentou consideravelmente para cerca de 64%. No que se refere ao MAE, o valor inicial era de 2,39, mas, com a otimização, essa medida de erro médio diminuiu para 1,63, indicando uma notável melhoria na precisão do modelo. Quanto ao RMSE, o valor inicial era de 5,16, e após a otimização, diminuiu significativamente para 3,31, demonstrando uma redução notável na penalização de erros significativos.

&emsp;&emsp; Esses resultados, quando comparados com a otimização máxima do modelo de Regressão Linear, indica que o modelo de Árvore de Decisão possui um melhor desempenho com os dados utilizados neste projeto. Entretanto, quando comparado ao modelo **Random Forest** sem qualquer otimização, o _R² Score_ é ligeiramente inferior, o MAE é um pouco maior, e o RMSE é apenas marginalmente menor. Isso sugere a possibilidade de explorar estratégias adicionais de otimização para o modelo de Árvore de Decisão, a fim de aprimorar ainda mais suas métricas de desempenho.

**Grid Search aplicado ao algoritmo de Árvore de Decisão**

&emsp;&emsp; Para verificarmos o quanto o modelo de Árvore de Decisão poderia ser otimizado, aplicamos o algoritmo de otimização de hiperparâmetros **Grid Search**. Portanto, o algoritmo de otimização por hiperparâmetros **Grid Search** gerou os melhores hiperparâmetros possíveis:

`{'max_depth': 10, 'min_samples_leaf': 4, 'min_samples_split': 5}`

&emsp;&emsp; Anteriormente foi explicado a definição desses mesmos hiperparâmetros, porém é válido ressaltar o que cada resultado significa. Com isso, o `max_depth` indica que a profundidade máxima das árvores é dez. Já o `min_samples_leaf` define que o número mínimo de amostras necessárias para estar em um nó folha é quatro. Por fim, o `min_samples_split` indica que o número mínimo de amostras necessárias para dividir um nó interno é cinco. 

A partir disso, as métricas obtidas através do **Grid Search**, aplicado ao modelo de Árvore de Decisão, foram:
* **Erro Absoluto Médio (MAE):** 1.7888623000764408
* **Erro Quadrático Médio (MSE):** 12.850584895123045
* **Raiz quadrada do erro-médio (RMSE):** 3.584771247251775
* **Coeficiente de Determinação (R² Score):** 0.5808254640698448

&emsp;&emsp; Os resultados das métricas apresentados acima evidenciam que o **Grid Search** oferece uma melhoria para o modelo de Árvore de Decisão, haja vista que o _R² Score_ gerado é maior (58%) que a mesma métrica do modelo sem otimização (26%). Porém, é válido destacar que o MAE e o RMSE do modelo otimizado com **Grid Search** são maiores, indicando que o modelo está errando um pouco mais. Mas, em relação à otimização anterior, é evidente que o _R² Score_ é maior no algoritmo **Random Search**, que é 64%, do que neste algoritmo, que é 58%. 

&emsp;&emsp; Portanto, é válido ressaltar que mesmo com as duas otimizações aplicadas, o modelo de Árvore de Decisão não se comportou melhor que o modelo de **Random Forest**.

##### 4.4.2.3 **Random Forest**

&emsp;&emsp;No tópico 4.3.3 foi destacado a importância do algoritmo de aprendizagem de máquina **Random Forest**, haja vista que ele permite, por meio de suas diversas árvores de decisão, produzir previsões mais precisas e robustas da quantidade de SKU vendido em determinado período. Tendo em vista essa motivação, o grupo optou por manter esse modelo durante essa rodada de testes com a presença da otimização de hiperparâmetros, de modo a entender o quanto ele seria otimizado e quais seriam as suas métricas. Ademais, é válido ressaltar que as suas métricas, sem a otimização de hiperparâmetros, foram: 
* **Erro Absoluto Médio (MAE):** 1.537142967017472
* **Erro Quadrático Médio (MSE):** 11.464828062709106
* **Raiz quadrada do erro-médio (RMSE):** 3.385975201136167
* **Coeficiente de Determinação (R² Score):** 0.6854606655019839

&emsp;&emsp;O dataset utilizado para o treinamento do Random Forest, o qual obteve as métricas acima, não possuía a coluna `winning_price` preenchida, haja vista que ela continha muitos dados nulos, algo que é inviável para o treinamento do modelo. Sendo assim, após a terceira sprint, foi realizado o preenchimento dos dados nulos de tal coluna e, como o **Random Forest** foi escolhido como modelo candidato no tópico 4.3.3, resolvemos testá-lo novamente com essa nova variável, de modo a entendermos o seu desempenho. Portanto, as suas métricas, sem a otimização de hiperparâmetros, foram:
* **Erro Absoluto Médio (MAE):** 1.5389725166963635
* **Erro Quadrático Médio (MSE):** 11.448398912332877
* **Raiz quadrada do erro-médio (RMSE):** 3.383548272499282
* **Coeficiente de Determinação (R² Score):** 0.6859114017884282

&emsp;&emsp; Ao comparar as métricas antes e depois da coluna `winning_price` ser preenchida, é possível observar que não há uma diferença significativa do desempenho do modelo **Random Forest**, segundo as métricas expressas. Contudo, para que tal algoritmo possa apresentar um melhor desempenho, aplicamos a otimização de hiperparâmetros.

Para realizar a otimização de hiperparâmetros de forma eficaz, é fundamental adquirir um entendimento abrangente dos hiperparâmetros que afetam o desempenho do modelo Random Forest, bem como compreender suas respectivas definições. Nesse sentido, recorremos, novamente, às definições propostas por Bruno Faboci [30], as quais esclarecem os seguintes hiperparâmetros:

* **n_estimators:** Este parâmetro representa o "número de árvores na floresta". Ele influencia diretamente a quantidade de árvores de decisão que serão combinadas para formar o ensemble.
* **max_depth:** Trata-se da "profundidade máxima das árvores". A profundidade de uma árvore de decisão determina até que ponto ela pode se ramificar, o que impacta a complexidade do modelo.
* **min_samples_split:** Aqui, nos referimos ao "número mínimo de amostras necessárias para dividir um nó interno". Esse hiperparâmetro controla o quão "criteriosa" a árvore deve ser ao decidir dividir um nó interno em subnós.
* **min_samples_leaf:** Por último, mas não menos importante, temos o "número mínimo de amostras necessárias para estar em um nó folha". Esse hiperparâmetro afeta o tamanho mínimo permitido para um nó folha.

Tendo em mente essas definições cruciais, prosseguimos com as otimizações de hiperparâmetros:


**Random Search aplicado ao algoritmo de Random Forest**

&emsp;&emsp;No caso do modelo Random Forest, o grupo optou por testar diferentes iterações dentro do algoritmo de otimização de hiperparâmetro **Random Search**. Assim, a escolha de testar diferentes valores está fundamentada no fato de que o modelo Random Forest leva um tempo considerável para processar o algoritmo de otimização, dificultando executar de uma só vez um número alto de iterações. Nesse sentido, ao testar diferentes números de iterações mais baixos, é possível comparar qual apresenta melhor desempenho.

&emsp;&emsp;Considerando o que foi exposto no parágrafo acima, a seguir será evidenciado quais foram as métricas obtidas por meio da otimização de hiperparâmetros com o algoritmo **Random Search**, no caso do modelo Random Forest, com três, seis e nove iterações:

* **Random Search aplicado ao Random Forest com três iterações:**
  * **Erro Absoluto Médio (MAE):** 1.4559071270701858
  * **Erro Quadrático Médio (MSE):** 8.291097825027418
  * **Raiz quadrada do erro-médio (RMSE):** 2.879426648662441
  * **Coeficiente de Determinação (R² Score):** 0.7295518366268021

* **Random Search aplicado ao Random Forest com seis iterações:**
  * **Erro Absoluto Médio (MAE):** 1.4544637332616124
  * **Erro Quadrático Médio (MSE):** 8.265656812026746
  * **Raiz quadrada do erro-médio (RMSE):** 2.8750055325210675
  * **Coeficiente de Determinação (R² Score):** 0.7303816996178786

* **Random Search aplicado ao Random Forest com nove iterações:**
  * **Erro Absoluto Médio (MAE):** 1.4643446317746063
  * **Erro Quadrático Médio (MSE):** 8.291285890774173
  * **Raiz quadrada do erro-médio (RMSE):** 2.879459305281839
  * **Coeficiente de Determinação (R² Score):**  0.7295457020910776

&emsp;&emsp; É possível observar que o algoritmo de otimização de hiperparâmetro **Random Search** realmente consegue melhorar o desempenho do modelo **Random Forest**, haja vista que a principal métrica escolhida para ser observada, o _R² Score_, possui, originalmente, o valor de, aproximadamente, 68%. Mas, após ser aplicada a otimização de hiperparâmetro com o **Random Search de seis iterações**, o _R² Score_ alcançou um valor superior de, aproximadamente, 73%. Isso significa que, de fato, tal algoritmo de otimização de hiperparâmetro consegue otimizar o modelo **Random Forest**. 

&emsp;&emsp; Adicionalmente, é válido ressaltar que as métricas MAE e RMSE também sofreram alterações em seus valores, haja vista que o MAE deste modelo, sem nenhuma otimização, alcança o valor de 1,53, mas, com a otimização, o MAE cai para 1,45. Já o RMSE, no modelo sem otimização, o seu valor é de 3,38, enquanto essa métrica com o modelo otimizado atinge o valor de 2,87. Dessa forma, é evidente que o **Random Forest** otimizado, além de conseguir explicar melhor a variabilidade dos seus dados de saída, a sua média de erro também diminuiu, indicando uma maior precisão do modelo.

&emsp;&emsp; Ademais, é válido destacar que os melhores hiperparâmetros encontrados com o **Random Search de seis iterações** foram:

`{'n_estimators': 200, 'min_samples_split': 5, 'min_samples_leaf': 1, 'max_depth': 20}`

&emsp;&emsp; A partir da definição realizada anteriormente, o hiperparâmetro `n_estimators` gerado indica que a quantidade de árvores necessárias para o algoritmo é 200. Já o `min_samples_split` diz que o número mínimo de amostras necessárias para dividir um nó interno é cinco. O `min_samples_leaf` aponta que o número mínimo de amostras necessárias para estar em um nó folha é um e, por fim, o valor de `max_depth` demonstra que a profundidade das árvores é 20.   

**Grid Search aplicado ao algoritmo de Random Forest**

&emsp;&emsp;Em relação ao algoritmo de **Grid Search**, a decisão tomada foi de aplicá-lo de forma reduzida. Isso porque, como o _dataset_ utilizado para o desenvolvimento deste projeto é extenso, o tempo de execução do algoritmo é muito alto, não tornando viável para o projeto executá-lo em sua integridade.Assim sendo, o `param_grid` (uma grade de parâmetros) foi diminuído, a fim de conseguir executar o **Grid Search** e comparar os seus resultados com os apresentados no algoritmo anterior. O `param_grid` é um conjunto predefinido de combinações de hiperparâmetros que o **Grid Search** explora sistematicamente para encontrar a configuração mais adequada para um modelo de aprendizado de máquina [16]. Reduzir o tamanho do `param_grid` significa considerar menos combinações de hiperparâmetros durante a busca, o que pode economizar tempo computacional.

&emsp;&emsp;Ademais, é válido destacar que os melhores hiperparâmetros encontrados com o *Grid Search* foram:
`{'max_depth': 5, 'min_samples_leaf': 4, 'min_samples_split': 5, 'n_estimators': 200}`

&emsp;&emsp; Com isso, tendo em vista a definição realizada anteriormente, o `max_depth` demonstra que a profundidade das árvores devem ser cinco. Já o `min_samples_leaf` aponta que o número mínimo de amostras necessárias para estar em um nó folha é quatro. O `min_samples_split` diz que o número mínimo de amostras necessárias para dividir um nó interno é cinco e, por fim, o `n_estimators` gerado indica que a quantidade de árvores necessárias para o algoritmo é 200.

&emsp;&emsp;Sendo assim, as métricas obtidas por meio da otimização de hiperparâmetros com o algoritmo **Grid Search**, no caso do modelo **Random Forest**, são:
* **Erro Absoluto Médio (MAE):** 17.80755335081607
* **Erro Quadrático Médio (MSE):** 8.291285890774173
* **Raiz quadrada do erro-médio (RMSE):** 4.219899684923337
* **Coeficiente de Determinação (R² Score):** 0.4191336057619707

&emsp;&emsp; Tendo em vista os resultados das métricas gerados pelo algoritmo de otimização de hiperparâmetros **Grid Search**, é possível observar que não há uma melhora das métricas do algoritmo **Random Forest**, haja vista que a métrica principal, o _R² Score_, possui o valor de 68% no modelo sem a otimização de hiperparâmetro e o _R² Score_ gerado pela otimização em questão assume o valor de, aproximadamente, 42%. Além disso, é notório o quanto o valor de MAE e do RMSE tiveram um aumento absurdo, indicando que o modelo passou a errar mais. Diante disso, é notório que o **Grid Search** não otimizou o modelo, mas, sim, piorou os seus resultados. 

#### 4.4.3 Modelho Escolhido

&emsp;&emsp;Considerando o desempenho dos diferentes modelos, nomeadamente o **Random Forest**, a **Regressão Linear** e a **Árvore de Decisão**, juntamente com as respetivas otimizações de hiperparâmetros, a escolha recaiu sobre o **Random Forest** com otimização através do método de **Random Search**, com um total de 6 iterações. Esta seleção baseia-se na comparação das métricas obtidas anteriormente, revelando-se o mais eficiente, como destacado a seguir:


- **Random Search aplicado ao Random Forest com seis iterações:**
  - **Erro Absoluto Médio (MAE):** 1.4544637332616124
  - **Erro Quadrático Médio (MSE):** 8.265656812026746
  - **Raiz Quadrada do Erro Médio (RMSE):** 2.8750055325210675
  - **Coeficiente de Determinação (R² Score):** 0.7303816996178786

&emsp;&emsp;Os resultados obtidos estão em harmonia com os objetivos específicos do modelo, como explicado em maior detalhe no tópico **4.3.3**. O algoritmo Random Forest é robusto e abrangente, permitindo uma avaliação minuciosa das características do conjunto de dados e fornecendo previsões precisas.

&emsp;&emsp;Para uma melhor compreensão da qualidade das previsões efetuadas por este modelo, é necessário uma análise mais aprofundada das métricas. O MAE de cerca de 1,45 e o RMSE de aproximadamente 2,87 indicam que, em média, o modelo pode errar em cerca de 1,45 e 2,87 unidades nas previsões de vendas de produtos, o que é considerado satisfatório, dadas as metas do projeto. O valor de _R² Score_, que se aproxima de 73%, significa que é possível explicar uma parte significativa da variabilidade das características nos valores alvo, o que também é relevante para os objetivos do projeto. O RMSE, que penaliza erros mais significativos, situa-se em cerca de 8,26, indicando que existem previsões que se desviam consideravelmente dos valores reais, sendo um ponto a ter em consideração, embora não represente uma queda drástica no desempenho.

&emsp;&emsp;Portanto, com base na análise anteriormente realizada, o modelo selecionado efetua previsões satisfatórias do número de vendas da empresa Mobly, sendo essencial para o propósito de otimizar a gestão de estoque e melhorar a eficiência das operações de entrega.

### 4.5. Avaliação

#### 4.5.1 Descrição da solução final
&emsp;&emsp;A solução final, denominada Mobil.ia, trata-se de um modelo de regressão utilizando o Random Forest, o qual é otimizado por hiperparâmetros através do algoritmo Random Search com 6 iterações (conforme detalhado no tópico 4.4.2.3). A escolha desse modelo, como já destacado em tópicos anteriores, está diretamente alinhada com os objetivos do projeto em parceria com a Mobly, pois visam resolver, da forma mais eficiente e precisa possível, o problema da falta de um abastecimento equilibrado do estoque de produtos da empresa. Nesse sentido, o modelo Mobil.ia tem a capacidade de prever a quantidade de vendas futuras dos produtos em um determinado período com uma alta precisão, permitindo que a Mobly possa equilibrar o abastecimento do estoque e evitar o desperdício ou a falta de materiais.

&emsp;&emsp;Em princípio, o modelo Mobil.ia, como destacado, trata-se do modelo Random Forest. A seleção desse algoritmo de machine learning foi realizada devido à sua capacidade de lidar com uma ampla gama de informações em um dataset, fazendo com que o modelo consiga compreender bem a variabilidade de produtos que podem estar presentes no estoque da Mobly, os quais possuem suas características e padrões de demandas singulares. No entanto, como o Mobil.ia consegue lidar com essa variedade de produtos, é evidente que o Random Forest é um algoritmo robusto que consegue capturar relações complexas entre os atributos e consegue lidar bem com dados heterogêneos, tornando-o ideal para o contexto deste projeto.

&emsp;&emsp; Nessa direção, o modelo escolhido foi otimizado com o intuito de obter mais precisão nas informações de quantidade de vendas fornecidas pelo modelo. Com isso, a otimização de hiperparâmetros utilizando o Random Search permite ajustar o modelo para evitar overfitting, permitindo que o modelo consiga se adequar, da maneira mais geral possível, aos novos dados. Isso é fundamental, uma vez que garante a permanência da robustez do modelo ao longo do tempo, mesmo quando as condições mercadológicas da Mobly sofram alterações. Dessa maneira, para avaliar o desempenho do modelo foram utilizadas as seguintes métricas:

* Erro Absoluto Médio (MAE): 1.4544637332616124
* Erro Quadrático Médio (MSE): 8.265656812026746
* Raiz Quadrada do Erro Médio (RMSE): 2.8750055325210675
* Coeficiente de Determinação (R² Score): 0.7303816996178786

&emsp;&emsp;A partir das métricas acima, é possível observar o quanto o modelo consegue explicar os dados gerados em relação à quantidade de itens vendidos em um período especificado. Tendo isso em vista, o coeficiente de determinação (R² Score) de 0,73 indica que o modelo explica aproximadamente 73% da variabilidade presente nos dados de vendas, o que é um resultado sólido. Quanto mais próximo de 1 esse valor, melhor o modelo é em explicar as variações nos dados.

&emsp;&emsp;Outra métrica importante é o MAE e o seu valor de 1,45 revela que o modelo tem um erro absoluto médio de 1,45 unidades em comparação com os dados reais de vendas, o que é aceitável considerando a complexidade do problema e a diversidade de produtos no estoque.

&emsp;&emsp;Em relação ao RMSE, o seu valor de 2,87 indica que o modelo tem um erro médio de 2,87 unidades e ajuda a entender o impacto de erros maiores. Nesse contexto, esse valor também é razoável.

&emsp;&emsp;Já MSE com o valor de 8,26 representa o erro médio do modelo, e embora haja desvios consideráveis em algumas previsões, isso é aceitável dadas as circunstâncias do projeto.

&emsp;&emsp;Portanto, o grupo validou essas métricas ao decorrer das sprints, visando verificar se o modelo desenvolvido está alcançando os objetivos e o escopo estipulado para o projeto, e o parceiro concordou com tais resultados, dizendo que é satisfatório para atingir os objetivos do projeto. 

#### 4.5.2 Plano de Contingência

&emsp;&emsp;O modelo preditivo desenvolvido, mesmo que tenha passado por etapas para o aperfeiçoamento dos dados, com o objetivo do algoritmo gerar o melhor resultado possível, continua passível de apresentar falhas em suas predições e isso pode ocorrer por diversos motivos. Assim sendo, uma das formas de fazer com que o modelo desenvolvido não prejudique a empresa parceira é formulando um plano de contingência. Desse modo, o grupo desenvolveu dois planos de contingência que o parceiro pode seguir caso o modelo desenvolvido apresenta falhas:

**Plano 1:** Estabelecer um sistema automatizado para monitorar continuamente as previsões geradas pelo modelo em tempo real, comparando-as com os dados reais de vendas à medida que elas são registradas. 
* Ação de Contingência: Se o sistema de monitoramento detectar que as previsões do modelo estão significativamente discrepantes em relação aos valores reais de vendas, as seguintes ações devem ser tomadas:
  * Alerta Imediato: Um alerta será gerado automaticamente e enviado para a equipe responsável pelo estoque e pela gestão das vendas. Isso pode ser feito por meio de mensagens de texto, e-mails ou notificações em um sistema de gerenciamento interno;
  * Avaliação Manual: A equipe responsável revisará imediatamente as previsões e irão compará-las com os dados reais de vendas disponíveis, de modo a identificar discrepâncias específicas, como produtos com alta demanda não prevista ou produtos com vendas abaixo das expectativas;
  * Revisão do Estoque: Com base na análise das discrepâncias, a equipe deve considerar ajustar os níveis de estoque, de modo a evitar desperdício ou excesso de materiais;
  * Aprimoramento do Modelo: Além das ações imediatas, a equipe documentará as discrepâncias e as causas subjacentes. Esses dados podem ser usados posteriormente para melhorar o modelo de previsão, incorporando informações sobre eventos inesperados ou tendências não previstas.

&emsp;&emsp;Nesse sentido, este plano de contingência garante uma resposta rápida e eficaz quando o modelo de previsão de vendas dos produtos falha em fornecer previsões precisas, permitindo que a empresa se adapte às mudanças nas condições do mercado em tempo real e tome decisões concretas sobre o estoque.

**Plano 2:** Estabelecer métricas de desempenho adicionais alinhadas com as operações diárias de vendas para avaliar constantemente a qualidade das previsões do modelo.
* Ação de Contingência: Se o modelo começar a demonstrar um desempenho abaixo ou acima do esperado, serão tomadas as medidas para reajustar ou atualizar o modelo:
  * Monitoramento regular das métricas já estabelecidas: A equipe deverá acompanhar regularmente as métricas já definidas para avaliar o desempenho do modelo, como o R^2, o MSE e o RMSE, de modo a identificar a possível localização do erro do modelo;
  * Definição de métricas alternativas: À medida que o modelo é usado no dia a dia, será possível observar a possível necessidade de outras métricas mais específicas para avaliar o desempenho do algoritmo e, por isso, é válido ajustar o modelo para utilizar outras métricas, como, por exemplo, o Erro Absoluto Percentual (MAPE).

&emsp;&emsp;Em relação a este plano de contingência, ele permite que o modelo seja aperfeiçoado, de modo a ser cada vez mais compatível com o cenário real de vendas da Mobly, fazendo com que seja uma ferramenta verdadeiramente útil para o abastecimento equilibrado do estoque de tal organização.

#### 4.5.3 Explicabilidade do modelo

&emsp;&emsp;A explicabilidade dos modelos de machine learning é fundamental, haja vista que ela fornece um panorama sobre o que está sendo utilizado para chegar nos resultados que estão sendo gerados pelo algoritmo, de modo a fazer com que os usuários confiem nesses valores [31]. Nessa direção, a explicabilidade é essencial para situações em que o modelo lida com dados que podem violar determinados direitos humanos ou que estão sujeitos à determinada lei ou regulamentação.  

&emsp;&emsp; Tendo isso em vista, seria de grande valia aplicar a explicabilidade no projeto desenvolvido para a Mobly, uma vez que seria uma forma de avaliar a confiabilidade dos resultados gerados pelo Mobil.ia. No entanto, é válido destacar que as previsões de vendas não envolvem informações críticas dos clientes, uma vez que o conjunto de dados utilizado para treinar o modelo se concentra estritamente em informações das vendas da Mobly, excluindo dados pessoais dos clientes. Nesse sentido, a explicabilidade do modelo desenvolvido para a Mobly não é tão necessário, pois o intuito do modelo é de ser uma ferramenta eficaz para a gestão do estoque e para a tomada de decisão de compra de materiais. Ademais, é válido ressaltar que, além da motivação anterior apresentada para a não aplicação da explicabilidade, tais informações não foram solicitadas pelo parceiro ao longo das sprints de validações e nem consta no TAPI tal necessidade.  

&emsp;&emsp;Dessa forma, mesmo sabendo que a explicabilidade, no contexto deste projeto, não é algo de extrema necessidade, o grupo tentou utilizar uma técnica avançada de explicabilidade conhecida como SHAP (SHapley Additive exPlanations), o qual se trata de um framework que ajuda a entender como as variáveis de entrada do modelo contribuem para a formulação das previsões feitas pelo modelo preditivo [31]. No entanto, o grupo enfrentou desafios de desempenho computacional ao rodar o algoritmo do SHAP e, ao procurar professores especialistas, eles alertaram que o conjunto de dados utilizado neste projeto é muito extenso, causando uma sobrecarga no kernel do Jupyter Notebook ao tentar rodar o SHAP. Com isso, não foi possível executar o algoritmo SHAP, porém abaixo há o código que ilustra a tentativa do grupo de utilizar tal técnica de explicabilidade:
````
#  'best_rf' é um objeto Pipeline com o modelo final
model = best_rf.named_steps['model']

# Cria o Explainer SHAP com o modelo
explainer = shap.Explainer(model, X_train)

# Calcula os valores SHAP
shap_values = explainer.shap_values(X_test)

# Cria um gráfico de resumo SHAP
shap.summary_plot(shap_values, X_test)
````
&emsp;&emsp;Além disso, é válido ressaltar que as tomadas de decisão da Mobly são baseadas, frequentemente, em uma variedade de fatores, como análise de mercado e de tendências de consumo, haja vista que a empresa opera em um setor de varejo online. Sendo assim, por mais que a explicabilidade seja valiosa em alguns casos, as decisões da Mobly seriam tomadas com base em dados concretos do mercado e em estratégias de negócios bem estabelecidas, ao invés de dependerem exclusivamente das previsões do modelo Mobil.ia. 

&emsp;&emsp;Portanto, a ausência da demonstração de explicabilidade no modelo desenvolvido para a Mobly é resultado das limitações práticas que enfrentamos ao tentar incorporar técnicas de explicabilidade no projeto, combinada com a falta de necessidade de tal explicação dos dados, considerando o escopo e os objetivos do projeto. 
	

## <a name="c5"></a>5. Conclusões e Recomendações

&emsp;&emsp;O projeto desenvolvido para a Mobly visa criar um modelo preditivo chamado Mobil.ia, o qual será utilizado como uma ferramenta para abastecer, cada vez mais precisamente, o estoque de produtos da organização, de modo a evitar o desperdício ou o excesso de materiais, algo que pode afetar no lucro total da empresa e em possíveis tomadas de decisões. A partir dessas motivações, é notório que o modelo preditivo possa gerar os dados da quantidade de vendas futuras de determinados produtos em um período da forma mais precisa possível. 

&emsp;&emsp;Nesse sentido, tal projeto conseguiu alcançar o seu objetivo principal, haja vista que o modelo Mobil.ia conseguirá otimizar o abastecimento de estoque devido a sua precisão. Essa precisão, conforme foi apresentado ao longo deste documento, foi alcançada de forma satisfatória, algo evidenciado pelas métricas de avaliação do modelo, como o R² de 73%, indicando que o modelo consegue explicar uma parte substancial da variabilidade nos dados relacionados à quantidade de itens vendidos.

&emsp;&emsp;A precisão do modelo foi validada e aprovada pelo parceiro Mobly durante o desenvolvimento, destacando sua utilidade para atender às demandas da empresa. 

&emsp;&emsp; No entanto, como foi apresentado nos tópicos anteriores a importância do modelo final, a sua explicabilidade e os planos de contingência, é válido destacar algumas recomendações formais, as quais abordam ações que podem ser tomadas para garantir o uso eficaz e sustentável do modelo Mobil.ia. Assim, essas recomendações são:
* Ampliação do conjunto de dados: Continue alimentando o modelo com dados atualizados e diversificados. Quanto mais dados o modelo tiver à disposição, mais precisas serão suas previsões. Isso permitirá atender às demandas dos clientes de forma mais eficiente;
* Monitoramento contínuo: É de extrema importância monitorar o funcionamento do modelo, bem como os seus resultados, para que as equipes responsáveis pelo abastecimento do estoque, como Supply Chain, não tome decisões precitadas ou equivocadas;
* Avaliação de impacto: Avalie o impacto das decisões tomadas com base nas previsões do modelo nas operações e nos resultados financeiros da Mobly, de modo a verificar o quanto o modelo Mobil.ia está conforme as regras de negócios da empresa.


&emsp;&emsp; Em suma, o modelo Mobil.ia, o qual foi desenvolvido para a empresa parceira Mobly, representa uma ferramenta valiosa para a Mobly na gestão de seu estoque e, ao seguir as recomendações acima e garantindo uma abordagem ética e transparente da utilização do modelo, a organização em questão conseguirá aproveitar ao máximo o potencial de tal tecnologia e tomará decisões estratégicas baseada em dados confiáveis.

## <a name="c6"></a>6. Referências

[1] Entrevista realizada com parceiros do projeto da empresa Mobly. Entrevista realizada em 4 ago 2023. Local da Entrevista: Instituto de Tecnologia e Liderança (Inteli). Entrevista concedida a: Turma 9.

[2] Mannesoft Mais Lojas. Os desafios e oportunidades do mercado de móveis pós-pandemia. 24 nov. 2022. Disponível em: https://www.mannesoftmaislojas.com.br/blog/os-desafios-e-oportunidades-do-mercado-de-moveis-pos-pandemia. Acesso em: 4 ago. 2023.

[3] Casarotto, Camila. 5 forças de Porter: entenda como elas influenciam sua estratégia. Rock Content, 11 dez. 2020. Disponível em: https://rockcontent.com/br/blog/5-forcas-de-porter/. Acesso em: 4 ago. 2023.
Galvão, Regina. As 5 principais tendências do mercado de decoração em 2021. Exame, 11 fev. 2021. Disponível em: https://exame.com/revista-exame/ambientados-ao-novo-normal/. Acesso em: 5 ago. 2023.

[4] Inteli - Instituto de Tecnologia e Liderança, 2023. Termo de Abertura de Projeto do Inteli - TAPI: Projeto Parceiro Empresa Mobly - 3° Módulo - Modelo Preditivo

[5] Santos, Thiago G. Google Colab: o que é, tutorial de como usar e criar códigos. 20 jun. 2023. Disponível em: https://www.alura.com.br/artigos/google-colab-o-que-e-e-como-usar. Acesso em: 7 ago. 2023. 

[6] SHARDA, Ramesh; DELEN, Dursun; TURBAN, Efraim. Business Intelligence e Análise de Dados para Gestão do Negócio. [2019] [Bookman Editora].

[7] Mobly. Disponível em: https://www.mobly.com.br/. Acesso em: 4 ago. 2023.

[8] Affonso, Aline. Descubra o que é a metodologia CRISP DM. Voitto, 05 mar. 2021. Disponível em: https://www.voitto.com.br/blog/artigo/crisp-dm.  Acesso em 29 ago. 2023. 

[9] M, Padhma. End-to-End Introduction to Evaluating Regression Models. Analytics Vidhya, 28 out. 2021 https://www.analyticsvidhya.com/blog/2021/10/evaluation-metric-for-regression-models/. Acesso em 5 set. 2023.

[10] Obi Tayo, Benjamin. What Really is R2-Score in Linear Regression? Medium, 5 nov. 2021. Disponível em: https://benjaminobi.medium.com/what-really-is-r2-score-in-linear-regression-20cafdf5b87c. Acesso em 5 set. 2023.

[11] Pessanha, Cínthia. Random Forest: como funciona um dos algoritmos mais populares de ML. Medium, 20 nov. 2019. Disponível em: https://medium.com/cinthiabpessanha/random-forest-como-funciona-um-dos-algoritmos-mais-populares-de-ml-cc1b8a58b3b4. Acesso em: 5 set. 2023.

[12] Santo, J. E. Previsão de Séries Temporais com “Prophet”. Flai, 28 jun. 2022. Disponível em: https://www.flai.com.br/jonatas/previsao-de-series-temporais-com-prophet/. Acesso em 14 set. 2023. 

[13] Miura, Lucas. Modelos de Predição | Otimização de Hiperparâmetros em Python. Medium, 12 abr. 2020. Disponível em: https://medium.com/turing-talks/modelos-de-predi%C3%A7%C3%A3o-otimiza%C3%A7%C3%A3o-de-hiperpar%C3%A2metros-em-python-3436fc55016e#. Acesso em 18 set. 2023. 

[14] Remigio, Matheus. Árvores de Decisão - Decision Trees. Medium, 9 ago. 2020. Disponível em: https://medium.com/@msremigio/%C3%A1rvores-de-decis%C3%A3o-decision-trees-4cb6857671b3. Acesso em: 21 set. 2023. 

[15] S, Gabriel. Árvores de decisão e machine learning: uma combinação poderosa para análise preditiva. Linkedin, 24 abr. 2023. Disponível em: https://www.linkedin.com/pulse/%C3%A1rvores-de-decis%C3%A3o-e-machine-learning-uma-combina%C3%A7%C3%A3o-para-s-fraga/?originalSubdomain=pt. Acesso em: 21 set. 2023.

[16] Lewis, Christopher. Optimize Hyperparameters with GridSearch. Medium, 7 mai. 2021. Disponível em: https://medium.com/analytics-vidhya/optimize-hyperparameters-with-gridsearch-d351b0fd339d. Acesso em: 21 set. 2023.

[17] Damaceno, Laura. Regressão Linear?. Medium, 10 jun. 2020. Disponível em: https://medium.com/@lauradamaceno/regress%C3%A3o-linear-6a7f247c3e29. Acesso em: 13 set. 2023.

[18] Tok&Stok. Disponível em: https://www.tokstok.com.br/. Acesso em: 4 ago. 2023.

[19] MadeiraMadeira. Disponível em: https://www.madeiramadeira.com.br/. Acesso em: 4 ago. 2023.

[20] G1 - Globo Economia. Empresa fatura R$ 150 mil ao mês produzindo móveis de papelão. 25 mai. 2013. Disponível em: https://g1.globo.com/economia/pme/noticia/2013/05/empresa-fatura-r-150-mil-ao-mes-produzindo-moveis-de-papelao.html. Acesso em: 4 ago. 2023.

[21] Mobly. Keva Móveis. Disponível em: https://www.mobly.com.br/keva-moveis/. Acesso em: 5 ago. 2023.

[22] PROTESTE. Lista de Reclamações Públicas. Disponível em: https://www.proteste.org.br/reclame/lista-de-reclamacoes-publicas/reclamacoes-publicas?referenceid=CPTBR01032811-52. Acesso em: 5 ago. 2023.

[23] Reclame Aqui. Mobly. Disponível em: https://www.reclameaqui.com.br/empresa/mobly/. Acesso em: 5 ago. 2023.

[24] Redação Olist. A expansão do e-commerce de Casa, Móveis e Decoração em 2023. 27 fev. 2023. Disponível em: https://olist.com/blog/pt/como-vender-mais/inteligencia-competitiva/e-commerce-de-casa-moveis-e-decoracao/. Acesso em: 5 ago. 2023.

[25] Rondinelli, Júlia. O case da Mobly como uma história de constante crescimento e aprendizado. E-commerce Brasil, 15 jun. 2021. Disponível em: https://www.ecommercebrasil.com.br/noticias/o-case-da-mobly-como-uma-historia-de-constante-crescimento-e-aprendizado. Acesso em: 5 ago. 2023.

[26] Silva, Ana Claudia. Com crescimento do mercado de casa e decoração, aumentam oportunidades para empreender online. 27 abr. 2023. Disponível em: https://www.segs.com.br/demais/343826-com-crescimento-do-mercado-de-casa-e-decoracao-aumentam-oportunidades-para-empreender-online. Acesso em: 5 ago. 2023.

[27] Souza, Karina. Mobly: em tempos difíceis, empresa faz 'operação de guerra' e zera consumo de caixa. Exame, 12 nov. 2022. Disponível em:
https://exame.com/exame-in/mobly-em-tempos-dificeis-empresa-faz-operacao-de-guerra-e-zera-consumo-de-caixa/. Acesso em: 5 ago. 2023. 

[28] Volpato, Bruno. Tudo sobre a análise SWOT: o que é, como fazer e template para baixar. Resultados Digitais, 23 ago. 2022. Disponível em: https://resultadosdigitais.com.br/marketing/analise-swot/. Acesso em: 7 ago. 2023.

[29] scikit-learn. Scikit-learn: Machine Learning in Python. Versão 0.24.2. 2021. Disponível em: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

[30] Faboci, Bruno. Otimizando Random Forest com GridSearch. LinkedIn. Disponível em: https://www.linkedin.com/pulse/otimizando-random-forest-com-gridsearch-bruno-faboci/?originalSubdomain=pt. Acesso em: 22 de setembro de 2023.

[31] Tran, Khuyen. SHAP: Explain Any Machine Learning Model in Python. Towards Data Science. 24 set. 2021. Disponível em: https://towardsdatascience.com/shap-explain-any-machine-learning-model-in-python-24207127cad7 Acesso em 3 de outubro de 2023.


## <a name="attachments"></a>Anexos
## Anexo 1 - Instrução para o funcionamento do modelo
O notebook final disponibilizado, denominado `Mobil_ia.ipynb`, possibilita realizar a entrada de uma determinada data, por meio do input, para que o modelo consiga realizar a predição da quantidade de itens vendidos para cada produto (SKU). Sendo assim, o passo a passo que precisa ser seguido é:
1. Acesse os CSV's com todos os dados necessários para realizar a predição, os quais estarão neste [link](https://drive.google.com/drive/folders/1FYMzd0ZusiduNc_04lXpIUziaPxQ2F6w?usp=drive_link);
2. Execute todas as células do notebook `Final_Model.ipynb` para obter o modelo treinado;
3. A partir da execução do notebook anterior, será realizado o download de um arquivo com a extensão `.joblib`, o qual estará localizado na seguinte pasta: `notebooks/outros/modelos`;
4. Execute todas as células do notebook `Mobil_ia.ipynb`;
5. Durante a execução do notebook anterior, será necessário informar, por meio de um input, uma data futura para que o modelo consiga realizar a previsão. Sendo assim, a data informada precisará seguir o seguinte formato: `YYYY/MM/DD`;
6. Após a execução do modelo final, será realizado o download do CSV com as predições realizadas pelo modelo, de acordo com a data digitada pelo usuário. Assim, tal arquivo estará localizado na seguinte pasta: `notebooks/outros/tabela_previsao`.



