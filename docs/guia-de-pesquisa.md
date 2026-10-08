# Guia de pesquisa da Cromasfera

Este guia ensina a usar a Cromasfera Audio-Visualizer como instrumento de pesquisa: o que cada ferramenta mede, como conduzir cada estudo, como analisar os resultados e, principalmente, **quando um resultado permite concluir alguma coisa**. Ele vale para o método de análise `croma-dsp 1.4` (o número aparece em todo laudo, em *Identificação e parâmetros*).

A primeira parte é prática, passo a passo. A segunda explica a estatística em linguagem simples e fixa as regras de decisão. O apêndice traz o material para um estudo formal: pré-registro, ética, dicionário de dados e análise em R ou Python.

## Resumo em uma página

- **Duas perguntas diferentes.** "O aplicativo mede o som corretamente?" é a *validade técnica* e se responde com a **Bancada**. "As pessoas percebem o que o modelo prevê?" é a *validade perceptiva* e só se responde com o **Experimento de escuta**.
- **Laudo e Comparação A/B descrevem, não provam.** Servem para conhecer as músicas, escolher estímulos e formular previsões antes do experimento.
- **Conclusões só pelo Veredito por hipótese.** No Experimento, os números do topo (por resposta) são descritivos e exageram a certeza. O que decide é o quadro *Veredito por hipótese*: cada hipótese recebe **Apoia**, **Contradiz** ou **Inconclusivo**, por regras fixas descritas aqui.
- **Pesos Ar/Terra só mudam com validação cruzada e dados novos.** Pesos ajustados com os mesmos dados usados para testar a hipótese Ar/Terra tornam o teste circular.
- **Estado atual:** a bancada aprova 32 de 33 verificações técnicas. A leitura de modo em escalas sobre bordão é a limitação conhecida. **Nenhuma hipótese perceptiva foi testada com pessoas ainda.** Hoje se pode afirmar que o app mede notas, acordes, andamento e afinação corretamente. Ainda não se pode afirmar que as cores do modelo correspondem à percepção.

## Sumário

- [Como usar este guia](#como-usar-este-guia)
- [O que a pesquisa quer saber](#o-que-a-pesquisa-quer-saber)
- [Conceitos e medidas](#conceitos-e-medidas)
- [Fluxo de uma pesquisa](#fluxo-de-uma-pesquisa)
- [Bancada de estímulos](#bancada-de-estímulos)
- [Laudo de uma música](#laudo-de-uma-música)
- [Comparação A/B](#comparação-ab)
- [Experimento de escuta](#experimento-de-escuta)
- [Pesos Ar ↔ Terra](#pesos-ar--terra)
- [Estatística sem mistério](#estatística-sem-mistério)
- [Regras de decisão](#regras-de-decisão)
- [Exemplos resolvidos](#exemplos-resolvidos)
- [Estado atual do modelo](#estado-atual-do-modelo)
- [Modelo de relatório](#modelo-de-relatório)
- [Apêndice metodológico](#apêndice-metodológico)

## Como usar este guia

Cada ferramenta tem uma seção com o mesmo roteiro:

1. **Para que serve:** a pergunta que a ferramenta responde.
2. **Como realizar:** os passos, com os nomes dos botões do app.
3. **Como analisar:** o que olhar e o que cada número significa.
4. **Regra de decisão:** em destaque, o que permite concluir.
5. **Armadilhas:** os erros mais comuns.

Os resultados se dividem em três tipos. Não misture os três ao escrever conclusões:

| Tipo | Ferramentas | O que permite dizer |
|---|---|---|
| Medição | Bancada | "O app mede X corretamente (ou não) neste tipo de som." |
| Descrição | Laudo, Comparação A/B | "Segundo o modelo, esta música fica em tal lugar." É uma leitura, não uma prova. |
| Prova | Experimento de escuta; Pesos Ar/Terra com validação cruzada | "As pessoas percebem (ou não) o que o modelo prevê." |

No app, o painel **Guia de pesquisa** mostra este mesmo texto. Os botões **Guia** dentro de cada ferramenta abrem a seção correspondente, e **Imprimir / PDF** gera uma versão para papel.

## O que a pesquisa quer saber

O método Croma-Sônica afirma que som e cor formam uma mesma esfera de relações. Ré (D) é o Verde 0, o centro de equilíbrio, e cada semitom tem uma cor. O Sentirama cruza um Plano Físico, de frio (azul) a quente (amarelo), com um Plano Espiritual, de denso (vermelho) a sutil (rosa). O par Ar/Terra distingue o expansivo e leve do pesado e denso.

Para pesquisar essas afirmações, elas viram hipóteses testáveis:

| Código | Hipótese | Ferramenta | Medida principal |
|---|---|---|---|
| T | O app identifica corretamente nota, acorde, modo, andamento, afinação e brilho. | Bancada | Verificações aprovadas |
| H1 | As pessoas associam a um trecho a **cor** prevista pelo modelo mais do que o acaso. | Experimento | Concordância de cor × 1 em 7 |
| H2 | A posição que as pessoas marcam no **Sentirama** acompanha a do modelo, nos eixos frio ↔ quente (x) e denso ↔ sutil (y). | Experimento | Correlação entre trechos |
| H3 | A nota **Ar ↔ Terra** das pessoas acompanha o índice do modelo. | Experimento | Correlação entre trechos |
| H4 | Uma das duas **leituras** (referência, Ré = Verde 0; ou relativa, tônica = Verde 0) explica melhor a cor percebida. | Experimento | McNemar |
| H5 | **Pesos** do índice Ar/Terra ajustados às pessoas preveem melhor do que os padrão, inclusive em trechos fora do ajuste. | Pesos Ar/Terra | Correlação com validação cruzada |

T é pré-requisito. Se o app não mede bem um tipo de som, um experimento com esse som testa o defeito de medição, não o modelo.

## Conceitos e medidas

As fórmulas abaixo são as do código e servem para citar no método de um trabalho.

### Do som à cor

- **Cromagrama.** A cada ~46 ms (FFT de 4096 pontos, salto de 2048, janela Blackman, áudio em 44,1 kHz mono), o app encontra os picos do espectro entre 50 e 5000 Hz. Cada pico soma sua amplitude ao semitom mais próximo, com peso cos²(π·desvio): um pico exatamente afinado vale 1, e um pico a meio semitom de distância vale 0.
- **Tom Croma.** O número do semitom contado a partir da referência: tom = (classe da nota − referência + 12) mod 12. No padrão, Ré = 0.
- **Nota dominante.** O tom mais forte do quadro, se passar de 25% do máximo e houver som suficiente. Para trocar de nota dominante, a nova precisa superar a atual em 12%, o que evita oscilação.

| Tom | Nota (padrão) | Cor | Família | Natural? |
|---|---|---|---|---|
| 0 | Ré | Verde | Verde | sim |
| 1 | Ré# | Amarelo-UV | Amarelo | não |
| 2 | Mi | Laranja | Laranja | sim |
| 3 | Fá | Vermelho | Vermelho | sim |
| 4 | Fá# | Violeta-UV | Violeta | não |
| 5 | Sol | Azul | Azul | sim |
| 6 | Sol# | Verde-UV | Verde | não |
| 7 | Lá | Amarelo | Amarelo | sim |
| 8 | Lá# | Laranja-UV | Laranja | não |
| 9 | Si | Rosa | Rosa | sim |
| 10 | Dó | Violeta | Violeta | sim |
| 11 | Dó# | Azul-UV | Azul | não |

As **7 famílias de cor** são as que o Experimento pergunta: Verde, Amarelo, Laranja, Vermelho, Violeta, Azul e Rosa. As ultravioletas têm a mesma cor das naturais (Yellow[1] = Yeluv[1] etc.), por isso entram na mesma família.

### As duas leituras

- **Leitura de referência:** a nota escolhida em *Calibração → Referência (Verde 0)* é o Verde 0. O padrão do método é Ré.
- **Leitura relativa:** o cromagrama é girado para que a **tônica estimada** da música vire o Verde 0.

Numa música em Ré, as duas leituras coincidem. Por isso, para comparar as leituras (H4), é preciso usar trechos em outras tônicas.

### O Sentirama

Cada tom tem uma posição (x, y). x vai de −1 (Azul, frio) a +1 (Amarelo, quente) e y de −1 (Vermelho, denso) a +1 (Rosa, sutil):

| Tom | x | y | Tom | x | y |
|---|---|---|---|---|---|
| 0 Verde | 0 | 0 | 6 Verde-UV | 0 | 0 |
| 1 Amarelo-UV | +0,88 | −0,14 | 7 Amarelo | +1 | +0,14 |
| 2 Laranja | +0,66 | −0,66 | 8 Laranja-UV | +0,56 | −0,76 |
| 3 Vermelho | 0 | −1 | 9 Rosa | 0 | +1 |
| 4 Violeta-UV | −0,56 | +0,76 | 10 Violeta | −0,66 | +0,66 |
| 5 Azul | −1 | −0,14 | 11 Azul-UV | −0,88 | +0,14 |

- **Posição do instante:** a média dessas posições, ponderada pelo **quadrado** do cromagrama, de modo que as notas fortes pesam muito mais que as fracas.
- **Posição da música:** a média dos instantes com som.
- **Quadrante:** *Centro (tônica)* se |x| e |y| forem menores que 0,08. Caso contrário, Rosa–Amarelo (Ar: sutil, quente), Rosa–Azul (sutil, frio), Vermelho–Amarelo (denso, quente) ou Vermelho–Azul (Terra: denso, frio).

As posições de laranjas, violetas e do Verde 6, e a profundidade z (Kandinsky), são interpretação deste aplicativo, não do livro.

### O índice Ar ↔ Terra

> Ar/Terra = 0,50 · **modo** + 0,32 · **brilho** + 0,18 · **andamento**, limitado entre −1 (Terra) e +1 (Ar).

| Componente | Cálculo | Vale −1 quando | Vale +1 quando |
|---|---|---|---|
| modo | (r da melhor tonalidade maior − r da melhor menor) × 5 | perfil claramente menor | perfil claramente maior |
| brilho | log₂(centroide / 1500 Hz) / 1,6 | centroide ≈ 500 Hz ou menos | centroide ≈ 4500 Hz ou mais |
| andamento | (BPM − 110) / 50 | 60 BPM ou menos | 160 BPM ou mais |

- Sem andamento detectado, o componente vale 0.
- Entre −0,08 e +0,08 o laudo diz **Equilíbrio**.
- Os pesos 0,50 / 0,32 / 0,18 são do aplicativo e podem ser recalibrados (ver [Pesos Ar ↔ Terra](#pesos-ar--terra)).

### Outras medidas

- **Tonalidade:** correlação (r) do perfil cromático com os perfis de Krumhansl–Kessler nas 24 tonalidades. A melhor é a tônica estimada, e a segunda melhor aparece como "2ª hipótese".
- **Tensão Fá ↔ Si:** √(Fá × Si) × 2, limitada a 1. Só sobe quando o Vermelho 3 e o Rosa 9 soam juntos (o trítono do sistema).
- **Estabilidade:** entre os quadros que têm nota dominante, a fração em que ela é a referência (Verde 0). A *estabilidade na tônica* faz o mesmo na leitura relativa.
- **Acordes:** uma tríade é reconhecida se as três notas passam de 35% no cromagrama linear. Maior e menor são consonantes; diminuta e aumentada, não.
- **Andamento (BPM):** autocorrelação do fluxo espectral entre 60 e 190 BPM, em janelas de 8 s. Vale a mediana das janelas confiáveis.
- **Afinação estimada:** média circular do desvio de todos os picos em relação à afinação usada, que indica se a gravação está em 440 ou 432 Hz.
- **Melodia:** frequência fundamental pelo método YIN, de 55 a 1500 Hz. Um quadro só conta como nota definida com clareza acima de 0,8.

### Quando um número merece confiança

| Situação | Limite | O que fazer |
|---|---|---|
| Confiança da tonalidade | r ≥ 0,75 alta · 0,50–0,75 média · < 0,50 baixa | Com r < 0,50, não use a leitura relativa (a tônica é incerta). |
| Duração | menos de 15 s | Proporções instáveis: use trechos maiores. |
| Som efetivo | menos de 50% do áudio | Muito silêncio ou ruído: recorte o trecho. |
| Afinação | \|desvio\| > 15 cents | Refaça a análise na outra afinação (440 ↔ 432 Hz). |
| Acordes reconhecidos | menos de 20% do tempo | Comum em voz solo, fala ou percussão. As medidas de acorde não dizem nada. |
| Andamento | não detectado | O índice Ar/Terra usa só modo e brilho. |

O laudo mostra esses avisos automaticamente, no topo.

## Fluxo de uma pesquisa

1. **Bancada:** confira que o app mede bem, com a calibração que você vai usar (afinação, Verde 0, pesos).
2. **Laudos:** analise as músicas candidatas. Anote, para cada uma, a cor, o quadrante e o Ar/Terra previstos.
3. **Comparação A/B:** teste contrastes controlados, como a mesma música em maior × menor, lenta × rápida ou trechos diferentes. Sirva-se deles para escolher estímulos que variem bem.
4. **Pré-registro:** escreva as hipóteses, os estímulos, o número de participantes e a regra de decisão *antes* de coletar (modelo no [apêndice](#apêndice-metodológico)).
5. **Experimento de escuta:** colete as respostas às cegas.
6. **Pesos Ar/Terra (opcional):** ajuste com um conjunto de trechos e confirme com outro, novo.
7. **Relatório:** use o [modelo de relatório](#modelo-de-relatório).

## Bancada de estímulos

**Para que serve.** Responde a T: o app mede corretamente? A bancada gera sons controlados no próprio navegador, analisa cada um com o mesmo núcleo do laudo e compara com o que o método prevê.

**Como realizar.**

1. Painel de entrada → **Pesquisa** → **Bancada**.
2. Escolha o instrumento no seletor ao lado de *Rodar bancada*: piano elétrico, órgão (padrão), cordas, pad, flauta, harpa ou sino.
3. Confira a calibração no painel de entrada (afinação e Verde 0). A bancada usa a calibração atual.
4. Clique em **Rodar bancada**. Leva alguns minutos.
5. Em cada linha você pode **▶ Ouvir**, abrir o **Laudo**, baixar o **WAV**, mandar para o **A** ou o **B** da comparação, ou usar **+ Experimento** para incluir o estímulo no teste de escuta.

**O que ela contém.** São 33 estímulos e 7 comparações em pares, em seis grupos. Das 33 verificações com critério, 26 vêm de estímulos isolados e 7 dos pares. Outros 7 estímulos são **informativos** (mostram como o modelo lê casos sem previsão fechada).

| Grupo | Estímulos | Critério |
|---|---|---|
| Notas isoladas | as 12 notas, de Ré 4 a Dó# 4 | nota dominante = tom esperado |
| Tríades | Ré, Sol e Lá, maior e menor | acorde e modo corretos; Ar(maior) > Ar(menor) |
| Tensão e estabilidade | Fá + Si; Ré sustentado | tensão > 50% em mais da metade do tempo; Ré dominante > 60% |
| Modos | Ré nos 7 modos, escala sobre bordão | Jônio = Ré maior; Eólio = Ré menor; Ar(jônio) > Ar(eólio); os outros 5 são informativos |
| Andamento | I–IV–V–I a 60, 120 e 180 BPM | BPM ± 5%; Ar sobe com o andamento |
| Afinação e timbre | progressão em 432 Hz analisada em 440; Ré maior suave × brilhante | afinação estimada 432 ± 2 Hz; centroide e Ar maiores no brilhante |

**Como analisar.** O topo mostra aprovados, reprovados e informativos. Em cada linha, compare a coluna *Expectativa* com *Obtido*. Num reprovado, abra o laudo do estímulo para ver por quê.

> **Regra de decisão (T).** Com uma calibração, o app está **apto** para um tipo de som se todas as verificações daquele grupo forem aprovadas. Uma reprovação em **notas isoladas, afinação ou andamento** invalida o uso daquela calibração: corrija antes de qualquer experimento. Uma reprovação em **modos** restringe só os estímulos parecidos (escalas modais sobre bordão). O componente *modo* do Ar/Terra não é confiável nesses estímulos.

**Armadilhas.**

- Rode a bancada de novo sempre que mudar a afinação, o Verde 0 ou o instrumento. Ela vale para a calibração em que rodou.
- Aprovar a bancada não diz nada sobre percepção: só que a medição está correta.

## Laudo de uma música

**Para que serve.** Descrever onde uma música (ou gravação) se enquadra no modelo e gerar previsões para o experimento.

**Como realizar.**

1. Carregue um arquivo (*Upload Áudio* ou arraste para a tela) e clique em **Analisar música inteira**. Para gravar do microfone, ative o microfone e use **Gravar sessão**: a análise roda quando você para.
2. O laudo abre em tela cheia. **Baixar laudo (JSON)** guarda tudo, inclusive a linha do tempo quadro a quadro. **Abrir laudo salvo** reabre o JSON. **Imprimir / PDF** gera a versão em papel.

**Como analisar**, nesta ordem:

1. **Avisos** no topo (ver [quando um número merece confiança](#quando-um-número-merece-confiança)). Se a afinação sugerida for outra, refaça a análise antes de qualquer coisa.
2. **Veredito** (a frase em destaque): Ar/Terra, tônica, cor e quadrante predominantes.
3. **Leituras de referência e relativa:** se a tônica não for Ré, elas diferem. Anote as duas.
4. **A música no tempo:** veja se a música muda de região. Um valor médio pode esconder duas partes opostas. Clique num ponto para ouvir aquele instante.
5. **Perfil, paleta, roda e Sentirama:** a distribuição da energia pelas cores.
6. **Gramática das cores:**
   - *transições*: qual cor leva a qual (encadeamento melódico e harmônico);
   - *coocorrência*: quais soam juntas;
   - *intervalos*: consonantes (terças, quartas, quintas) × dissonantes (segundas, trítono).
7. **Melodia** (pensada para voz ou instrumento solo): extensão, afinação em cents, passos × saltos.
8. **Método e limitações:** as condições daquela análise.

> **Regra de decisão (laudo).** Um laudo **não prova** nada sobre percepção; ele descreve a leitura do modelo. Use-o para afirmar "segundo o modelo, a música X é predominantemente Verde, no quadrante Rosa–Azul, Ar/Terra +0,01 (equilíbrio)", sempre com a confiança da tonalidade e os avisos. Para comparar duas músicas, use a Comparação A/B. Para afirmar algo sobre como as pessoas sentem, use o Experimento.

**Armadilhas.**

- Comparar laudos feitos com calibrações diferentes. O A/B avisa quando isso acontece.
- Ler a leitura relativa com tonalidade de confiança baixa (r < 0,50).
- Tomar a média da música inteira por "a cor da música" quando a linha do tempo mostra partes muito diferentes. Nesse caso, analise trechos.
- Percussão e ruído espalham energia por todos os tons e puxam a música para o centro do Sentirama.

## Comparação A/B

**Para que serve.** Ver o que muda entre duas versões controladas: maior × menor, lento × rápido, timbre suave × brilhante, dois trechos da mesma música, duas interpretações.

**Como realizar.**

1. **Pesquisa** → **Comparação A/B**.
2. Em A e em B escolha a fonte: **Arquivo de áudio…**, **Áudio do player**, **Laudo salvo (.json)…** ou **Estímulo da bancada…**. Em B também há **Mesmo áudio de A**.
3. Para comparar trechos do mesmo arquivo, marque *Trecho* e digite início e fim (ex.: 0:00–0:30 × 1:00–1:30).
4. Clique em **Comparar**. **Baixar CSV** e **Baixar JSON** exportam A, B e Δ.

**Como analisar.**

- A **síntese** só menciona diferenças acima destes limiares:
  - |ΔAr| ≥ 0,10;
  - |Δx| ou |Δy| ≥ 0,08 no Sentirama;
  - |Δtensão| ≥ 0,10;
  - |ΔBPM| ≥ 8.
- A **tabela A | B | Δ** mostra B − A em 25 medidas. As que são porcentagens aparecem em pontos percentuais.
- As **sobreposições** (perfis, rodas, paletas e Sentirama com a seta A → B) mostram de onde vem a diferença.

> **Regra de decisão (A/B).** Um único par **ilustra**, não generaliza. Para afirmar uma regra geral, como "a versão menor é mais Terra que a maior", faça **vários pares** independentes e conte quantos vão na direção prevista. Use o teste do sinal: são necessários **5 de 5**, **7 de 8**, **9 de 10** ou **10 de 12** pares na direção prevista para p < 0,05 (unilateral). Abaixo disso, a regra fica sem confirmação.

**Armadilhas.**

- Mudar mais de uma coisa entre A e B (andamento e timbre juntos, por exemplo). Aí não dá para saber o que causou a diferença.
- Comparar análises feitas com calibrações diferentes.

## Experimento de escuta

**Para que serve.** Responder H1 a H4: as pessoas percebem o que o modelo prevê? É a única ferramenta que testa o modelo diante da percepção.

### Antes: desenho e preparação

**Estímulos.**

- **Quantidade:** no mínimo **20 trechos**; o ideal é **24 a 30** (ver [tamanho de amostra](#tamanho-de-amostra)).
- **Variedade:** os trechos precisam variar no que o modelo mede.
  - Cubra as 7 famílias de cor previstas, os dois modos, andamentos lentos e rápidos, e timbres escuros e brilhantes.
  - Inclua trechos em tônicas diferentes de Ré, para que as leituras de referência e relativa discordem (H4).
- **Duração:** 15 a 30 s cada. No app, use *Trecho tocado → Meio* com *Segundos do meio*.
- **Volume:** iguale o volume entre os trechos (normalize antes) para que intensidade não vire pista.
- **Pré-análise:** faça o laudo de cada trecho. Descarte os que tiverem avisos de confiança baixa da tonalidade, afinação errada ou som efetivo baixo.
- **Familiaridade:** músicas famosas trazem memória e letra. Prefira trechos instrumentais pouco conhecidos. O app pergunta se a pessoa conhece cada trecho, e isso pode ser analisado à parte.

**Participantes.**

- No mínimo **10**; o ideal são **12 a 20**.
- Use um código anônimo para cada pessoa (P1, P2…). Nunca use o nome.
- Mesmo equipamento para todos: fones fechados, ambiente silencioso, volume confortável e fixo.
- Sessões de até cerca de 20 minutos (24 trechos de 20 s com respostas cabem nisso). Faça pausas se houver mais trechos.

**Pré-registro.** Antes de coletar, registre as hipóteses, a lista de trechos, o número de participantes e a regra de decisão deste guia (modelo no apêndice). Isso impede ajustar a análise depois de ver os dados.

### Durante: roteiro da sessão

1. **Pesquisa** → **Experimento** → **Preparar**.
2. Adicione os trechos: **Adicionar arquivos…**, **Áudio do player** ou **Estímulos da bancada…** (na bancada, use *+ Experimento* nas linhas). Os trechos ficam só na aba aberta: se a página for recarregada, adicione-os de novo. As respostas ficam salvas.
3. Escolha *Trecho tocado* (Inteiro ou Meio, com os segundos) e deixe **Ordem aleatória** marcada.
4. Digite o **código do participante** e clique em **Iniciar sessão**. O app analisa os trechos antes de começar (a previsão do modelo é calculada sobre o mesmo trecho que será tocado).
5. Entregue o aparelho ao participante. A tela cobre o app inteiro e o áudio não passa pela análise: nada revela a resposta do modelo.

**Instrução para ler ao participante** (sempre a mesma):

> "Você vai ouvir alguns trechos de música. Para cada um, ouça quantas vezes quiser e responda com a primeira impressão; não há resposta certa ou errada. Primeiro, escolha a cor que você sente no trecho; se nenhuma cor vier, escolha 'Nenhuma'. Depois, clique no círculo: à esquerda é frio, à direita é quente; embaixo é denso, pesado, material; em cima é sutil, leve, espiritual. Em seguida, mova o controle entre Terra, pesado e denso, e Ar, leve e expansivo. Por fim, diga se você conhece a música."

6. Faça **um trecho de treino** (que não entra na análise) antes da sessão real. Pode ser uma sessão com o código "TREINO", apagada depois na planilha.
7. O botão *Próximo trecho* só libera quando todas as perguntas foram respondidas e o trecho foi ouvido. O tempo de resposta é registrado.
8. Ao final, a sessão é salva no navegador. Para juntar aparelhos, use **Baixar JSON** em cada um e **Importar JSON** num só (as sessões são mescladas sem duplicar).

### Depois: como analisar

Abra **Resultados**. A tela tem quatro partes:

1. **Números descritivos** (topo): concordância de cor e correlações calculadas resposta por resposta. Servem para ter uma ideia, mas tratam cada resposta como independente e exageram a certeza.
2. **Veredito por hipótese:** é aqui que se conclui. Cada hipótese tem o resultado, um selo (**Apoia**, **Contradiz** ou **Inconclusivo**) e o porquê. Ver [Regras de decisão](#regras-de-decisão).
3. **Gráficos:**
   - *Ar ↔ Terra por trecho*: média das pessoas × modelo; na diagonal, o modelo acerta.
   - *Cor: modelo × pessoas*: em cada linha (cor prevista), a porcentagem de cada cor escolhida; a diagonal é a concordância.
4. **Tabelas por trecho e por participante:** mostram quais trechos e quais pessoas puxam o resultado.

**Exportações:**

- **CSV respostas:** uma linha por resposta, com a previsão do modelo ao lado.
- **CSV por trecho:** uma linha por trecho, com médias das pessoas, concordância de cor e previsão.
- **Baixar JSON:** todas as sessões, para arquivar ou juntar aparelhos.

O filtro de participante no topo dos resultados recalcula tudo para uma pessoa. É útil para achar quem não entendeu a tarefa, mas o veredito por pessoa sempre sai inconclusivo, porque precisa de várias pessoas.

**Respostas "Nenhuma".** Ficam fora da concordância de cor, mas entram nas demais hipóteses. Uma proporção alta de "Nenhuma" (acima de 30%) é um resultado em si: indica que muitos trechos não evocam cor.

**Armadilhas.**

- Concluir pelos números do topo. Com 2 pessoas e 12 trechos eles podem dar p < 0,001 e, mesmo assim, o veredito é **Inconclusivo** ([exemplo 4](#exemplo-4--experimento-simulado-amostra-pequena)).
- Mudar a calibração no meio da coleta. A previsão de cada resposta é guardada com a calibração usada, mas misturar calibrações torna a leitura de referência incomparável.
- Usar só músicas em Ré: H4 fica sem dados.
- Mostrar o app (cores, laudo) ao participante antes ou durante a sessão.

## Pesos Ar ↔ Terra

**Para que serve.** Responder H5: existem pesos para modo, brilho e andamento que preveem melhor a nota Ar ↔ Terra das pessoas do que os pesos padrão (0,50 / 0,32 / 0,18)?

**Como realizar.**

1. Colete respostas no Experimento (ou importe o JSON).
2. **Pesquisa** → **Pesos Ar/Terra**, ou o link *Pesos Ar/Terra* em *Calibração*, ou o botão *Calibrar os pesos* nos resultados do experimento.
3. O painel mostra:
   - **Conjuntos de pesos:** padrão, em uso, ajustado por mínimos quadrados e à mão, com a correlação de cada um com as pessoas.
   - **Validação cruzada:** cada trecho é previsto por pesos ajustados sem ele.
   - **Testar à mão:** controles deslizantes com a correlação ao vivo e o gráfico pessoas × modelo.
   - **Por trecho:** a nota média das pessoas e os componentes do modelo.
4. **Aplicar estes pesos** passa a valer no tempo real e nos laudos novos (o laudo registra os pesos em *Identificação e parâmetros*). **Restaurar padrão** desfaz.

**Como analisar.**

- O que importa é o **r validado** (validação cruzada), não o r ajustado. O ajuste sempre parece bom nos próprios dados.
- Se o r validado for bem menor que o r ajustado, o ajuste está decorando ruído ([exemplo 7c](#exemplo-7--calibração-simulada-três-situações)).
- Um peso negativo significa que, naqueles dados, as pessoas ouvem o componente ao contrário do modelo.
- Os pesos são normalizados para que |modo| + |brilho| + |andamento| = 1, como no padrão. Assim o índice continua entre −1 e +1, e a correlação não muda.

> **Regra de decisão (H5).** Aplique os pesos ajustados só se houver **pelo menos 10 trechos** e o **r validado superar o r do padrão em mais de 0,05**. O painel faz essa conta e diz *Aplicar é recomendado*, *Mantenha o padrão* ou *Ainda não dá para decidir*. Para afirmar H5 num trabalho, **confirme com trechos novos**: ajuste com um conjunto, aplique e rode um segundo experimento com outros trechos. H5 se confirma se, no segundo conjunto, o r dos pesos novos for maior que o dos pesos padrão.

**Armadilhas.**

- **Circularidade.** Ajustar os pesos com os mesmos dados usados para testar H3 garante um resultado bom e sem valor. Teste H3 com os pesos registrados no pré-registro.
- Recalibrar a cada sessão: os laudos ficam incomparáveis. Mude os pesos raramente, registre a data e anote no relatório.

## Estatística sem mistério

### O acaso de 1 em 7

Com 7 cores, quem escolhe ao acaso acerta a cor prevista 1 vez em 7 (14,3%). A pergunta de H1 é se a concordância fica claramente acima disso.

### p-valor e intervalo de confiança

- **p-valor:** a chance de ver um resultado tão bom (ou melhor) se o modelo não tivesse relação nenhuma com a percepção. p < 0,05 é o limite usual para dizer "não parece acaso".
- **Intervalo de confiança (IC) de 95%:** a faixa de valores compatíveis com os dados. Ele diz mais do que o p, porque mostra o tamanho possível do efeito. "34% (IC 29%–40%)" quer dizer que a concordância verdadeira provavelmente está entre 29% e 40%, bem acima de 14%.

### Correlação (r)

Mede o quanto duas séries andam juntas, de −1 a +1. Neste guia: |r| < 0,1 é nula, < 0,3 fraca, < 0,5 moderada e ≥ 0,5 forte. Para H2 e H3, **r ≥ 0,30 é o menor efeito considerado relevante**.

### Por que não contar respostas soltas

Cada pessoa responde muitos trechos, e cada trecho é ouvido por muitas pessoas. As respostas não são independentes: duas respostas da mesma pessoa se parecem mais entre si do que duas respostas de pessoas diferentes. Tratar 24 respostas de 2 pessoas como 24 observações independentes finge uma certeza que não existe (é a *pseudorreplicação*).

Por isso o veredito usa unidades corretas:

- **o trecho**, para H2 e H3: a média das pessoas em cada trecho × o modelo;
- **a pessoa**, para checar a consistência: em quantas pessoas o efeito aparece (teste do sinal).

### Teste do sinal

Se o modelo não funcionasse, cada pessoa teria 50% de chance de ficar "a favor" (acima do acaso, ou com r > 0) e 50% "contra". O teste do sinal pergunta se as pessoas a favor são muitas demais para isso:

| Pessoas | Mínimo a favor para p < 0,05 |
|---|---|
| 5 | 5 |
| 6 | 6 |
| 8 | 7 |
| 10 | 9 |
| 12 | 10 |
| 15 | 12 |
| 20 | 15 |

Com menos de 5 pessoas, nenhum resultado passa nesse teste. Por isso o veredito exige pelo menos 5.

### Testes unilaterais e correção de Holm

- **Unilateral:** as hipóteses têm direção (concordância *acima* do acaso, r *positivo*). Por isso os testes são unilaterais.
- **Holm:** como quatro hipóteses são testadas juntas (cor, x, y, Ar/Terra), a chance de um falso positivo aumenta. A correção de Holm ajusta os p-valores para que a chance de *algum* falso positivo fique em 5%. O veredito sempre mostra o **p ajustado**.

### McNemar (H4)

Para saber qual leitura explica melhor a cor, só interessam as respostas em que uma leitura acerta e a outra erra. Se as duas fossem igualmente boas, esses casos se dividiriam meio a meio. O teste de McNemar verifica se a divisão é desequilibrada demais para isso. Com menos de 10 casos que distinguem as leituras, não há como decidir.

### Efeito × significância

Um efeito pode ser "significativo" e pequeno demais para importar, ou grande e ainda incerto. Por isso as regras olham as duas coisas: o p (é acaso?) e o IC (de que tamanho é?).

### Tamanho de amostra

Quantos **trechos** são necessários para detectar uma correlação (H2, H3) com 80% de chance:

| Correlação verdadeira | α = 0,05 | α = 0,0125 (Holm, pior caso) |
|---|---|---|
| r = 0,6 | 16 | 23 |
| r = 0,5 | 24 | 35 |
| r = 0,4 | 38 | 56 |
| r = 0,3 | 68 | 103 |

Quantas **respostas de cor** (sem "Nenhuma") são necessárias para detectar uma concordância acima de 14,3%, com 80% de chance, antes do efeito de agrupamento:

| Concordância verdadeira | α = 0,05 | α = 0,0125 |
|---|---|---|
| 30% | 38 | 56 |
| 25% | 77 | 115 |
| 20% | 255 | 385 |

Como as respostas se agrupam por pessoa, multiplique por um fator de 2 a 3. Com 24 trechos por pessoa e uma semelhança moderada entre as respostas da mesma pessoa, o fator é cerca de 2,2.

**Recomendação prática:** **12 a 20 participantes × 24 a 30 trechos** (288 a 600 respostas). Isso detecta correlações a partir de ~0,5 entre trechos e concordâncias de cor a partir de ~25%.

**Refutar custa mais que confirmar.** Para que o IC exclua r ≥ 0,30 quando o efeito verdadeiro é zero, com 80% de chance, são necessários cerca de **85 trechos**. Para a cor (IC abaixo de acaso + 5 p.p.), cerca de **385 respostas** efetivas. Com amostras menores, a ausência de efeito costuma dar **Inconclusivo**, não **Contradiz**, e isso é o correto.

## Regras de decisão

O app aplica exatamente estas regras no quadro *Veredito por hipótese*. Todos os testes de H1 a H3 são unilaterais na direção prevista, com p corrigido por Holm.

> **Apoia** = (1) resultado na direção prevista **e** (2) p ajustado < 0,05 **e** (3) o efeito aparece de forma consistente entre as pessoas (teste do sinal p < 0,05, com pelo menos 5 pessoas).
>
> **Contradiz** = amostra **adequada** (≥ 20 trechos e ≥ 10 participantes) **e** (efeito significativo na direção contrária **ou** limite superior do IC abaixo do menor efeito relevante).
>
> **Inconclusivo** = qualquer outro caso. O app diz o motivo: p alto, poucas pessoas, IC largo, amostra pequena.

| Hipótese | Medida principal | Apoia | Contradiz | Inconclusivo |
|---|---|---|---|---|
| T · Medição | verificações da bancada | todas aprovadas no grupo de estímulos usado | reprovação em notas, afinação ou andamento | — |
| H1 · Cor | concordância (sem "Nenhuma") × 1/7 | acima do acaso, p ajust. < 0,05, maioria das pessoas acima do acaso (sinal p < 0,05) | IC superior < 19,3% (acaso + 5 p.p.) ou significativamente abaixo do acaso | demais casos |
| H2 · Sentirama x e y | r entre trechos | r > 0, p ajust. < 0,05, maioria das pessoas com r > 0 (sinal p < 0,05) | IC superior de r < 0,30 ou r < 0 significativo | demais casos |
| H3 · Ar ↔ Terra | r entre trechos | idem H2 | idem H2 | demais casos |
| H4 · Leitura | McNemar | — | — | — |
| H5 · Pesos | r validado | ≥ 10 trechos e r validado > r padrão + 0,05; confirmado em trechos novos | r validado ≤ r padrão + 0,05 com ≥ 10 trechos (mantém o padrão) | < 10 trechos |

Para H4, o resultado é uma de quatro respostas: **leitura de referência melhor**, **relativa melhor** (McNemar p < 0,05), **empate** ou **poucos casos** (menos de 10 respostas que distinguem as leituras).

### Como escrever a conclusão

| Selo | Frase |
|---|---|
| Apoia | "Os dados apoiam H_: [resultado com IC e p ajustado]; o efeito apareceu em [k] de [n] participantes." |
| Contradiz | "Os dados contradizem H_: com [n] trechos e [m] participantes, o IC exclui efeitos relevantes ([IC])." |
| Inconclusivo | "Os dados não permitem concluir sobre H_ ([motivo]). É preciso [mais trechos / mais participantes]." |

Nunca escreva "o modelo foi comprovado" a partir de um único estudo. Escreva "os dados deste estudo apoiam H1 e H3". Uma confirmação ampla vem da repetição com outros estímulos e outras pessoas.

## Exemplos resolvidos

Os exemplos 1 a 3 são **reais**: foram gerados rodando o app (calibração padrão: Lá 4 = 440 Hz, Ré = Verde 0, pesos padrão, bancada com órgão). Os exemplos 4 a 7 usam **dados simulados** por computador, com respostas sintéticas, para mostrar como ler cada situação. Eles **não são resultados de pesquisa**.

### Exemplo 1 — Bancada completa

Resultado: **32 de 33 verificações aprovadas (97%)**, 1 reprovada e 7 informativas.

| Estímulo | Expectativa | Obtido | Resultado |
|---|---|---|---|
| 12 notas isoladas (Ré 4 … Dó# 4) | nota dominante = tom k | tom correto em 100% do tempo, nas 12 | 12 aprovados |
| Ré maior / Ré menor | acorde e modo | Ré maior, Ar +0,34 / Ré menor, Ar −0,67 | aprovados |
| Sol maior / Sol menor | acorde e modo | Sol maior, Ar +0,42 / Sol menor, Ar −0,59 | aprovados |
| Lá maior / Lá menor | acorde e modo | Lá maior, Ar +0,45 / Lá menor, Ar −0,55 | aprovados |
| 3 pares maior × menor | Ar(maior) > Ar(menor) | +0,34 × −0,67; +0,42 × −0,59; +0,45 × −0,55 | 3 aprovados |
| Fá + Si | tensão > 50% em mais da metade | média 90%, acima de 50% em 93% do tempo | aprovado |
| Ré sustentado | Ré dominante > 60% | 100% | aprovado |
| Ré Jônio | Ré maior | Ré maior (r 0,87), Ar +0,31 | aprovado |
| Ré Eólio | Ré menor | **Ré maior** (r 0,79), Ar −0,09 | **reprovado** |
| Jônio × Eólio | Ar(jônio) > Ar(eólio) | +0,31 × −0,09 | aprovado |
| Ré Dórico · Frígio · Lídio · Mixolídio | informativo | todos Ré maior (r 0,77–0,87); Ar +0,10 · −0,15 · +0,31 · +0,31 | informativos |
| Ré Lócrio | informativo | Sol# maior (r 0,42, confiança baixa), Ar −0,02 | informativo |
| I–IV–V–I a 60 / 120 / 180 BPM | BPM ± 5% | 61 / 118 / 184 BPM | 3 aprovados |
| 120 × 60 e 180 × 120 BPM | Ar sobe com o andamento | +0,34 × +0,14; +0,48 × +0,34 | 2 aprovados |
| Progressão em 432 Hz, analisada em 440 | 432 ± 2 Hz | 432,1 Hz (−31 cents) | aprovado |
| Ré maior suave / brilhante | informativo | centroide 313 Hz, Ar +0,18 / 2845 Hz, Ar +0,63 | informativos |
| Brilhante × suave | centroide e Ar maiores no brilhante | 2845 × 313 Hz; +0,63 × +0,18 | aprovado |

**Leitura.**

- **Medição:** a medição de nota, acorde, tensão, estabilidade, andamento, afinação e brilho está correta para esses sons. Pela regra T, o app está apto para experimentos com música tonal com acordes, nesta calibração.
- **Modos:** a escala de Ré eólio sobre um bordão de Ré e Lá é lida como Ré maior. Com a melodia passando rápido e o bordão (tônica + quinta) soando o tempo todo, a terça menor pesa pouco, e o perfil tonal fica ambíguo (r maior 0,79 × r menor 0,76).
  - Dos 7 modos, 6 saem como "Ré maior". O Ar/Terra, porém, ainda ordena os modos de forma coerente: Lídio, Mixolídio e Jônio (+0,31) > Dórico (+0,10) > Eólio (−0,09) > Frígio (−0,15).
  - **Conclusão:** nesses estímulos, o *nome* da tonalidade (maior/menor) não é confiável. O componente *modo* ainda carrega informação útil, como diferença contínua.
- **Notas isoladas:** uma nota de órgão sozinha sai com modo +0,22, levemente "maior", porque os harmônicos naturais (quinta e terça maior) entram no cromagrama. O componente modo não é neutro para sons sem harmonia.

### Exemplo 2 — Laudo da progressão de demonstração

Arquivo `demo-progressao.wav`: 32 s de progressão sintetizada (Ré, Sol, Lá, Ré menor, Dó, Mi…), 100% com som.

- **Veredito:** "Equilíbrio +0,01 · tônica Ré maior · cor Verde (referência) · quadrante Rosa–Azul (sutil, frio)".
- **Tonalidade:** Ré maior, **confiança média (r = 0,73)**; 2ª hipótese Sol maior (r = 0,64). A tônica é Ré, então as leituras de referência e relativa coincidem.
- **Ar/Terra +0,01** = 0,50 × modo (+0,48) + 0,32 × brilho (−0,80, centroide 621 Hz) + 0,18 × andamento (+0,16, 118 BPM). O modo puxa para Ar e o timbre escuro puxa para Terra: os dois se anulam.
- **Cor:** Verde em 25% do tempo; as outras seis famílias ficam entre 12% e 13% cada.
- **Sentirama:** centro de gravidade neutro (x = +0,02; y = +0,03). O tempo se divide entre os quatro quadrantes: Rosa–Azul 25%, Vermelho–Amarelo 25%, Vermelho–Azul 23%, Rosa–Amarelo 18% e centro 10%.
- **Outras medidas:** acordes consonantes em 100% dos acordes reconhecidos, que cobrem 68% do tempo; tensão Fá ↔ Si média de 16%; afinação estimada 439,9 Hz (sem aviso).

**Leitura.** "Segundo o modelo, a progressão está em equilíbrio entre Ar e Terra, centrada em Ré (Verde 0), sem quadrante predominante: percorre o Sentirama inteiro, como se espera de uma progressão que visita várias tonalidades vizinhas." A confiança média da tonalidade permite usar a leitura relativa com cautela. Para o experimento, essa música serviria como estímulo **neutro**, não como exemplo de uma cor.

### Exemplo 3 — A/B Ré maior × Ré menor

- **A** = tríade de Ré maior; **B** = tríade de Ré menor (estímulos da bancada).
- **Síntese:** "B está mais Terra que A (−1,01 no índice Ar/Terra); no Sentirama, B é mais denso (vermelho) (y −0,16); a cor predominante é a mesma (Verde); a tônica estimada passa de Ré maior para Ré menor."

**Tabela (trecho):**

| Medida | A | B | Δ |
|---|---|---|---|
| modo | +1,00 | −1,00 | −2,00 |
| brilho | −0,51 | −0,53 | −0,02 |
| Ar/Terra | +0,34 | −0,67 | −1,01 |
| Quadrante | Rosa–Amarelo 100% | Vermelho–Amarelo 94% | ≠ |

**Leitura.** Toda a diferença vem do componente modo; brilho e andamento são iguais. O resultado ilustra a previsão "maior = Ar, menor = Terra". Pela regra do A/B, porém, é **um par**: para afirmar a regra em geral, repita com vários pares independentes (outros instrumentos, tônicas, músicas) e aplique o teste do sinal.

### Exemplo 4 — Experimento simulado: amostra pequena

2 participantes × 12 trechos; as respostas simuladas seguem fortemente o modelo.

- **Números do topo (descritivos):** cor 50% (10 de 20), "p < 0,001"; Ar/Terra r = +0,81, "p < 0,001".
- **Veredito:** **Inconclusivo** em H1, H2 e H3, com o motivo "poucas pessoas para checar a consistência (2; mínimo 5)". H4: só 5 respostas distinguem as leituras.

**Leitura.** Os p-valores do topo tratam as 24 respostas como independentes, mas são só 2 pessoas. Não há como saber se o efeito vale para outras pessoas. Este é o caso típico de um **piloto**: serve para testar o procedimento, não para concluir.

### Exemplo 5 — Experimento simulado: efeito real

12 participantes × 24 trechos; as respostas simuladas seguem o modelo moderadamente, com ruído.

| Hipótese | Resultado | Selo |
|---|---|---|
| H1 · Cor | 34,1% (IC 29%–40%), p ajust. < 0,001; 12 de 12 pessoas acima do acaso | **Apoia** |
| H2 · x | r = +0,97 (IC +0,94 a +0,99); 12 de 12 pessoas com r > 0 | **Apoia** |
| H2 · y | r = +0,95 (IC +0,88 a +0,98); 12 de 12 | **Apoia** |
| H3 · Ar/Terra | r = +0,90 (IC +0,78 a +0,96); 11 de 12 | **Apoia** |
| H4 | 47 acertos só da referência × 11 só da relativa; p < 0,001 | **referência** melhor |

**Leitura.** "Os dados apoiam H1 a H3: a concordância de cor foi de 34% (IC 29–40%) contra 14% de acaso, e as posições no Sentirama e a nota Ar/Terra acompanharam o modelo entre trechos (r de 0,90 a 0,97). O efeito apareceu em praticamente todos os participantes. A leitura de referência explicou melhor a cor do que a relativa."

As correlações por trecho (r ≈ 0,9) são maiores que as por resposta (r ≈ 0,5–0,7), porque a média de 12 pessoas tira o ruído individual. As duas medidas são corretas, mas respondem perguntas diferentes.

### Exemplo 6 — Experimento simulado: respostas ao acaso

Dois tamanhos, com respostas simuladas sem nenhuma relação com o modelo.

| Hipótese | 12 pessoas × 24 trechos | 15 pessoas × 60 trechos |
|---|---|---|
| H1 · Cor | 14,4% (IC 11%–19%): **Contradiz** | 13,6% (IC 11%–16%): **Contradiz** |
| H2 · x | r = −0,22 (IC −0,57 a +0,21): **Contradiz** | r = −0,03 (IC −0,28 a +0,23): **Contradiz** |
| H2 · y | r = −0,22 (IC −0,58 a +0,20): **Contradiz** | r = +0,20 (IC −0,06 a +0,43): **Inconclusivo** |
| H3 · Ar/Terra | r = +0,14 (IC −0,28 a +0,52): **Inconclusivo** | r = +0,05 (IC −0,20 a +0,30): **Inconclusivo** |

**Leitura.**

- **Contradiz** só aparece quando o intervalo inteiro fica abaixo do efeito relevante.
- Com 24 trechos, isso aconteceu em x e y porque o r observado saiu negativo por acaso.
- Com 60 trechos, H3 ainda ficou no limite (IC até +0,30). Como explicado em [tamanho de amostra](#tamanho-de-amostra), refutar com segurança exige cerca de 85 trechos.

Um resultado **Inconclusivo** sem efeito não é "quase refutado". Ele diz que a amostra ainda não basta para descartar um efeito moderado.

### Exemplo 7 — Calibração simulada: três situações

| Situação | Ajustado (modo / brilho / andamento) | r padrão | r validado | Painel diz |
|---|---|---|---|---|
| a) Pessoas guiadas pelo brilho (14 trechos, 3 pessoas) | 0,12 / 0,74 / 0,14 | +0,56 | **+0,98** | Aplicar é recomendado |
| b) Pessoas guiadas pelo próprio índice padrão (24 trechos) | 0,53 / 0,33 / 0,14 | +0,90 | +0,86 | Mantenha o padrão |
| c) Respostas ao acaso (24 trechos) | 0,04 / 0,58 / −0,38 | +0,14 | **−0,13** | Mantenha o padrão |

**Leitura.**

- **(a)** Os pesos ajustados generalizam: o r validado supera muito o do padrão. Aplicar é justificado, e o próximo passo é confirmar com trechos novos.
- **(b)** O ajuste reencontra o padrão (0,53 / 0,33 / 0,14 ≈ 0,50 / 0,32 / 0,18), e o r validado não melhora. Manter o padrão é o correto.
- **(c)** O caso mais instrutivo. O ajuste parece bom nos próprios dados (r ajustado +0,29, com um peso negativo para andamento), mas o **r validado é −0,13**: o ajuste decorou ruído. Sem validação cruzada, alguém aplicaria pesos sem sentido.

## Estado atual do modelo

Este é o balanço até a versão `croma-dsp 1.4`. É uma conclusão provisória, que muda quando houver dados de pessoas.

**1. O que está demonstrado (medição).** A bancada aprova 32 de 33 verificações. Com sons tonais controlados, o aplicativo:

- identifica a nota e a cor de cada um dos 12 tons;
- reconhece tríades maiores e menores e o modo delas;
- detecta a tensão Fá ↔ Si e a estabilidade em Ré;
- mede o andamento (± 5%) e a afinação (432 × 440 Hz, ± 2 Hz);
- ordena corretamente Ar/Terra por modo (maior > menor), andamento (rápido > lento) e timbre (brilhante > suave).

**2. Limitação demonstrada.** Escalas modais sobre bordão têm o nome da tonalidade lido como maior, e o Ré eólio falha. Nesses sons, o maior/menor do laudo não deve ser citado como fato; o componente *modo* do Ar/Terra ainda ordena os modos de forma coerente. Notas isoladas aparecem levemente "maiores" por causa dos harmônicos.

**3. O que é escolha deste aplicativo, e não afirmação do livro:**

- a fórmula e os pesos do índice Ar/Terra;
- as posições no Sentirama de laranjas, violetas e do Verde 6;
- a profundidade z (Kandinsky);
- os limiares (35% para acordes, 0,08 para o centro do Sentirama etc.).

Os resultados sobre esses pontos testam a interpretação do aplicativo, não necessariamente o método original.

**4. O que ainda não foi testado.** **Nenhuma hipótese perceptiva (H1 a H5) foi testada com pessoas.** Os exemplos 4 a 7 usam dados simulados e mostram só que a análise funciona como descrito.

**Conclusão.**

- **Hoje é possível afirmar:** "o aplicativo mede corretamente nota, cor do tom, acorde, modo de tríades, tensão, andamento e afinação em sons tonais controlados, e o índice Ar/Terra responde como o modelo prevê a modo, andamento e brilho".
- **Ainda não é possível afirmar:** "as pessoas percebem as cores, as posições no Sentirama ou o caráter Ar/Terra que o modelo atribui à música". Essa afirmação depende do Experimento de escuta, com pelo menos 10 a 12 participantes e 20 a 24 trechos, pré-registrado e analisado pelas regras deste guia.

**Próximos passos recomendados:**

1. **Piloto:** 3 a 5 pessoas × 12 trechos, só para ajustar instruções e duração. Os dados não entram na análise.
2. **Estudo principal pré-registrado:** 12 a 20 pessoas × 24 a 30 trechos, com tônicas variadas e pesos padrão.
3. **Calibração dos pesos** com os dados do estudo principal.
4. **Estudo de confirmação** com trechos novos e os pesos calibrados (H5).

## Modelo de relatório

Copie e preencha os campos entre colchetes. Os números saem do quadro *Veredito por hipótese* e das exportações.

**Título:** Percepção de cor e caráter Ar/Terra em trechos musicais: um teste do modelo Croma-Sônica

**Resumo.** Testamos se ouvintes associam a trechos musicais as cores, posições no Sentirama e o caráter Ar/Terra previstos pelo modelo Croma-Sônica (Vigmorã/CromaSomos), implementado na Cromasfera Audio-Visualizer (`croma-dsp 1.4`). [n] participantes ouviram [m] trechos às cegas. A concordância de cor foi de [__]% (IC 95% [__–__]) contra 14,3% de acaso; as correlações entre trechos foram r = [__] (frio ↔ quente), r = [__] (denso ↔ sutil) e r = [__] (Ar ↔ Terra). [Conclusão por hipótese, com os selos.]

**1. Introdução.** O modelo, as duas leituras (referência e relativa) e as hipóteses H1 a H4 [e H5], conforme o pré-registro de [data/local].

**2. Método.**

- *Participantes:* [n], [idade, formação musical, critérios]. Consentimento livre e esclarecido [número do parecer, se houver].
- *Estímulos:* [m] trechos de [duração] s, [critério de escolha], volume normalizado. Tônicas: [lista]. Famílias de cor previstas: [distribuição].
- *Equipamento:* [aparelho, fones, ambiente].
- *Procedimento:* teste cego no módulo Experimento de escuta, ordem aleatória, trecho de treino, instrução padronizada (anexo). Respostas: cor (7 + nenhuma), posição no Sentirama, Ar ↔ Terra (−1 a +1) e familiaridade.
- *Previsão do modelo:* calculada sobre o mesmo trecho tocado, com Lá 4 = [440/432] Hz, Verde 0 = [Ré] e pesos Ar/Terra [0,50/0,32/0,18].
- *Análise:*
  - H1: binomial exato contra 1/7, IC de Wilson e teste do sinal por participante;
  - H2 e H3: correlação de Pearson entre as médias por trecho e o modelo, IC de Fisher e teste do sinal sobre o r de cada participante;
  - H4: McNemar;
  - correção de Holm para H1 a H3, α = 0,05 unilateral;
  - regras de decisão do Guia de pesquisa da Cromasfera.

**3. Resultados.**

- H1: "[__]% das respostas de cor coincidiram com a cor prevista (IC 95% [__–__]; p ajustado = [__]); [k] de [n] participantes ficaram acima do acaso. **[Selo]**."
- H2: "A posição frio ↔ quente marcada pelas pessoas correlacionou-se com a do modelo em r = [__] (IC [__ a __]; p ajustado = [__]; [k] de [n] pessoas com r > 0). **[Selo]**." Faça o mesmo para denso ↔ sutil.
- H3: "A nota Ar ↔ Terra média por trecho correlacionou-se com o índice do modelo em r = [__] (IC [__ a __]; p ajustado = [__]). **[Selo]**."
- H4: "[__] respostas acertaram só pela leitura de referência e [__] só pela relativa (McNemar p = [__])."
- Respostas "nenhuma cor": [__]%. Efeito da familiaridade: [descrever, se analisado].
- Figuras: gráfico Ar ↔ Terra por trecho; matriz de cor modelo × pessoas.

**4. Discussão.** O que os resultados significam para o modelo. Quais trechos ou pessoas destoaram, segundo as tabelas por trecho e por participante.

**5. Limitações.** Tamanho da amostra (comparar com a tabela de tamanho de amostra). Escolhas do aplicativo que não vêm do livro (posições intermediárias do Sentirama, fórmula do Ar/Terra). Limitação de modo em escalas sobre bordão. Equipamento e ambiente. Familiaridade com as músicas.

**6. Dados e reprodutibilidade.** Anexar:

- o CSV de respostas e o CSV por trecho;
- o JSON do experimento;
- os laudos (JSON) de cada trecho;
- a lista de arquivos de áudio;
- a versão do método (`croma-dsp 1.4`) e a calibração.

## Apêndice metodológico

### Desenho

- **Intra-sujeitos:** cada participante ouve todos os trechos, em ordem aleatória diferente para cada um.
- **Unidades de análise:** o **trecho** (H2 e H3, com médias), a **pessoa** (consistência, teste do sinal) e a resposta (H1 binomial e H4 McNemar, sempre acompanhados do teste por pessoa).
- **Variáveis:**
  - de resposta: cor, x, y, Ar/Terra, familiaridade e tempo de resposta;
  - previsões: cor (referência e relativa), x, y, Ar/Terra e os componentes modo, brilho e andamento.
- **Análise complementar recomendada:** modelos mistos com efeitos aleatórios de participante e de trecho (código abaixo). São mais precisos que o veredito do app e podem incluir a familiaridade como covariável.

### Pré-registro (modelo)

1. **Hipóteses:** H1 a H4 [e H5], como neste guia, com direção prevista.
2. **Estímulos:** lista fechada de arquivos, duração, critério de escolha, previsões do modelo de cada um (anexar os laudos).
3. **Amostra:** [n] participantes; critério de parada (número fixo, sem olhar os resultados no meio).
4. **Exclusões:** participantes que não completarem a sessão; sessões de treino; [outros critérios, definidos antes].
5. **Análise:** as regras de decisão deste guia (versão de [data]), α = 0,05 unilateral, Holm para H1 a H3.
6. **Calibração:** Lá 4 = [ ] Hz, Verde 0 = [ ], pesos Ar/Terra = [ ]. Não mudar durante a coleta.

Plataformas gratuitas de pré-registro: OSF (osf.io) e AsPredicted (aspredicted.org).

### Ética e consentimento

- Pesquisas com pessoas no Brasil seguem a **Resolução CNS nº 510/2016** (Ciências Humanas e Sociais). Para publicação acadêmica, submeta o projeto a um Comitê de Ética em Pesquisa (Plataforma Brasil).
- Use um **Termo de Consentimento Livre e Esclarecido (TCLE)** com:
  - objetivo;
  - duração;
  - ausência de riscos além do desconforto de ouvir música;
  - direito de desistir a qualquer momento;
  - anonimato;
  - uso dos dados.
- **LGPD:** o app não guarda nomes, só o código do participante. Mantenha a correspondência código ↔ pessoa (se existir) separada dos dados e protegida.
- Volume confortável e fixo; pausas em sessões longas.

### Triagem opcional de sinestesia

Pessoas com sinestesia som-cor podem ter associações fortes e idiossincráticas. Se for possível, pergunte no início ("Você costuma ver cores ao ouvir sons ou música?") e anote no código (ex.: P7-S). Analise com e sem essas pessoas. O filtro por participante e o CSV permitem isso.

### Dicionário de dados

**CSV respostas** (`experimento-escuta-cromasfera.csv`), uma linha por resposta:

| Coluna | Significado |
|---|---|
| participante, sessao, inicio | código, identificador da sessão, data e hora de início |
| ordem, trecho | posição na sequência; nome do trecho |
| resp_cor | cor escolhida (7 famílias ou "Nenhuma") |
| resp_x, resp_y | posição clicada no Sentirama (−1,1 a +1,1): x frio → quente, y denso → sutil |
| resp_ar_terra | controle de −1 (Terra) a +1 (Ar) |
| conhece | 1 se a pessoa conhece a música |
| vezes_ouvido, tempo_resposta_ms | quantas vezes tocou; tempo da primeira escuta até a resposta |
| modelo_cor_ref, modelo_x_ref, modelo_y_ref | previsão na leitura de referência |
| modelo_cor_rel, modelo_x_rel, modelo_y_rel | previsão na leitura relativa |
| modelo_ar_terra, modelo_comp_modo, modelo_comp_brilho, modelo_comp_andamento | índice e componentes |
| modelo_tonica | tonalidade estimada do trecho |
| trecho_inicio_s, trecho_fim_s | trecho do arquivo que foi tocado e analisado |
| verde0_pc, la4_hz, pesos_ar_terra | calibração usada (classe da nota do Verde 0, com Dó = 0; Lá 4; pesos) |

**CSV por trecho** (`experimento-por-trecho-cromasfera.csv`), uma linha por trecho:

- respostas, participantes;
- médias das pessoas para x, y e Ar/Terra, com o desvio-padrão do Ar/Terra;
- cor mais escolhida e sua fração;
- concordância de cor com as leituras de referência e relativa, fração de "Nenhuma" e de quem conhece a música;
- todas as previsões do modelo.

**CSV do A/B:** colunas medida, A, B e delta_B_menos_A, mais o perfil cromático tom a tom.

**JSON do laudo** (`format: "cromasfera-laudo"`):

- `params`: FFT, salto, taxa, janela, suavização, A4, ref, airWeights, versão do método;
- `source`: nome, tipo, duração;
- `summary`: todas as medidas do laudo;
- `timeline`: por quadro de ~46 ms, com tempo, nível, centroide, nota dominante, tensão, acorde, cromagrama de 12 tons (suavizado e bruto), f0 e clareza.

**JSON do experimento:** `format: "cromasfera-experimento"` e `sessions` (participante, configurações, respostas com a previsão completa).

### Análise em R e Python

**R**, com modelos mistos (pacote `lme4`):

```r
library(lme4)
d  <- read.csv("experimento-escuta-cromasfera.csv")
dc <- subset(d, resp_cor != "Nenhuma")
dc$acerto <- as.integer(dc$resp_cor == dc$modelo_cor_ref)
dc$off <- qlogis(1/7)                      # o acaso vira o zero do modelo
h1 <- glmer(acerto ~ 1 + offset(off) + (1 | participante) + (1 | trecho), family = binomial, data = dc)
summary(h1)                                # intercepto > 0 e significativo: acima do acaso
h3 <- lmer(resp_ar_terra ~ modelo_ar_terra + (1 + modelo_ar_terra | participante) + (1 | trecho), data = d)
summary(h3)                                # inclinação > 0: as pessoas acompanham o índice
```

**Python**, pela análise por trecho (a mesma do app) e um modelo misto por participante:

```python
import pandas as pd
from scipy.stats import pearsonr
import statsmodels.formula.api as smf

t = pd.read_csv("experimento-por-trecho-cromasfera.csv")
print(pearsonr(t.pessoas_ar_terra_media, t.modelo_ar_terra))   # H3 por trecho
print(pearsonr(t.pessoas_x_media, t.modelo_x_ref))             # H2 x

d = pd.read_csv("experimento-escuta-cromasfera.csv")
m = smf.mixedlm("resp_ar_terra ~ modelo_ar_terra", d, groups=d["participante"], re_formula="~modelo_ar_terra").fit()
print(m.summary())
```

### Fórmulas estatísticas usadas pelo app

- **Binomial exato (H1):** P(X ≥ k), com X ~ Binomial(n, 1/7).
- **IC de Wilson:** IC de 95% para a concordância de cor.
- **Pearson e IC de Fisher:** z = atanh(r), erro padrão 1/√(n − 3), IC = tanh(z ± 1,96 × erro padrão), p pela normal.
- **Teste do sinal e McNemar:** binomial com p = 1/2 (o sinal unilateral; o McNemar bilateral).
- **Holm:** ordena os p-valores e multiplica o i-ésimo menor por (m − i + 1), mantendo a ordem.
- **Calibração (H5):**
  - mínimos quadrados sem intercepto, com regularização 10⁻³;
  - pesos normalizados para soma dos valores absolutos = 1;
  - validação cruzada deixando um trecho de fora.

### Glossário

- **Cromagrama:** energia de cada um dos 12 semitons ao longo do tempo.
- **Tom Croma:** número de 0 a 11 do semitom, contado a partir do Verde 0.
- **Família de cor:** as 7 cores perguntadas no experimento; cada uma reúne um tom natural e, quando existe, sua ultravioleta.
- **Leitura de referência / relativa:** Verde 0 na nota escolhida (Ré) / na tônica da música.
- **Sentirama:** plano frio ↔ quente (x) × denso ↔ sutil (y).
- **Ar ↔ Terra:** índice de −1 a +1 que combina modo, brilho e andamento.
- **Centroide espectral:** o "centro de massa" do espectro em Hz; mais alto = timbre mais brilhante.
- **Tônica:** a nota central da tonalidade estimada.
- **IC 95%:** faixa de valores compatíveis com os dados.
- **Pseudorreplicação:** tratar respostas dependentes como independentes.
- **Validação cruzada:** testar um ajuste em dados que não participaram dele.
- **Pré-registro:** registro público das hipóteses e da análise antes da coleta.
