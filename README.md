# Croma

## `cromasfera.html` — Cromasfera Audio-Visualizer

Web app de arquivo único (HTML + Tailwind + Three.js via CDN) que transforma áudio em cor e forma segundo o método **Croma-Sônica** do livro *Cromasfera: The Seed of Interdisciplinary Harmony* (Vigmorã / CromaSomos).

- **Entradas:** microfone, upload / arrastar-e-soltar (.mp3 .wav .m4a .ogg) com player, e uma demonstração sintetizada.
- **DSP:** `AnalyserNode` com `fftSize = 4096`; cromagrama por picos espectrais (A4 = 440 Hz), nota dominante e secundárias, centroide espectral, RMS, BPM (autocorrelação do fluxo espectral), tonalidade (Krumhansl-Schmuckler), acordes.
- **Mapa:** Ré (D) = Verde 0 → … → Dó# = Azul-UV 11; naturais = círculos, ultravioletas = triângulos.
- **Mapa:** as ultravioletas têm a mesma cor das naturais (Yellow[1] = Yeluv[1], Violet[4] = Viluv[4], Green[6] = Gruv[6], Orange[8] = Oruv[8], Blue[11] = Bluv[11]).
- **Modos:** Cromasfera 3D (esfera + fita de 12 tons em curva de “bola de tênis”) · Flor Croma-Sônica (mandala de 12 pétalas) · Sentirama 3D (Plano Físico azul ↔ amarelo × Plano Espiritual vermelho ↔ rosa, cruzando-se na tônica).

### Teclado musical

**Teclado musical** transforma o teclado do computador num sintetizador: `Q W E R T Y U I O P` = Dó Ré Mi Fá Sol Lá Si Dó Ré Mi, `2 3 5 6 7 9 0` = sustenidos (layout de piano, lido pela posição física da tecla), `Z`/`X` = oitava. Doze instrumentos: sete clássicos (piano elétrico, órgão, cordas, pad etéreo, flauta, harpa e sino de cristal) e cinco **analógicos**, emulações de sintetizadores dos anos 70/80 feitas com Web Audio: **baixo analógico** (dois dentes-de-serra + sub-oscilador, filtro de 24 dB ressonante com ataque “pluck”), **lead analógico** (glide entre notas e vibrato), **metais sintéticos** (filtro que abre num “sopro”), **cordas de ensemble** (string machine com chorus de três LFOs) e **pad PWM** (pulso com largura modulada). O teclado da tela também toca (clique ou toque). O som entra na análise e pode ser gravado com **Gravar sessão**, que agora grava tudo o que está sendo analisado (microfone, teclado musical ou demonstração).

### Auto-rotação da câmera

O botão ↻ na barra superior (ou a opção *Auto-rotação da câmera*) liga e desliga a órbita automática da câmera. A escolha fica salva no navegador.

### Calibração

No painel de entrada, em **Calibração** (fica salva no navegador):

- **Afinação (Lá 4)**: 440 Hz (padrão) ou 432 Hz. Vale para o cromagrama em tempo real, para a demonstração e para o laudo.
- **Referência (Verde 0)**: qual nota é o Verde 0. O padrão do método é Ré (D); escolher outra nota renumera os 12 tons e as cores a partir dela (o teclado, o diagnóstico e o laudo seguem a escolha).

### Laudo (análise completa)

Além do tempo real, o app gera um **laudo** do áudio inteiro:

- **Analisar música inteira** (ou **Laudo** no player): processa o arquivo carregado do começo ao fim.
- **Gravar sessão**: com o microfone ativo, grava e analisa a gravação ao parar (a gravação pode ser baixada).
- O laudo traz o enquadramento no modelo em duas leituras — **de referência** (a nota escolhida como Verde 0, por padrão Ré) e **relativa** (tônica detectada = Verde 0) —, a afinação estimada da gravação (ex.: Lá 4 ≈ 432 Hz), índice Ar/Terra com seus componentes, perfil cromático, paleta de cores, trajetória no Sentirama, tonalidade por trecho, acordes, tensão Fá ↔ Si, andamento, parâmetros e limitações do método.
- **Baixar laudo (JSON)** exporta resumo + linha do tempo (~46 ms por quadro); **Abrir laudo salvo** reabre o JSON; **Imprimir / PDF** gera uma versão para papel.
- A análise roda num Web Worker, a 44,1 kHz mono e FFT de 4096 pontos, com o mesmo núcleo DSP (`dspCore`) do tempo real — o mesmo arquivo gera o mesmo laudo em qualquer aparelho.

### Leituras do laudo

- **Gramática das cores:** matriz de transições (qual cor leva a qual, por linha), matriz de coocorrência (quais soam juntas), alternância 12 tons ⇄ 7 cores e perfil de intervalos harmônicos.
- **Roda cromática:** o perfil como mandala de 12 pétalas (raio = energia, anel interno = tempo como nota dominante), nas duas leituras.
- **Replay no Sentirama:** um ponto com rastro percorre a trajetória da música, sincronizado com o player.
- **Melodia:** f0 por quadro (YIN via FFT, 55–1500 Hz), contorno no tempo, extensão, altura mediana, % do tempo com nota definida, desvio médio em cents e histograma de intervalos melódicos (±12 semitons).

### Partitura

O laudo traz a seção **Partitura**: a transcrição automática da música em três formas — **convencional** (pauta dupla com melodia, cifras e baixo), **Cromasônica · pauta colorida** (cada nota na cor do tom, cabeça triangular nos ultravioleta, número do tom embaixo) e **Cromasônica · pauta cromática** (12 linhas por oitava, uma por tom/cor). A melodia vem de um extrator de **melodia predominante** (soma harmônica dos picos espectrais, voz de cima, novo ataque em notas repetidas), as cifras do cromagrama por meio compasso e o baixo é inferido das cifras; a grade de tempo é afinada pelos ataques e a tonalidade é estimada pela própria transcrição. Há controles de andamento (÷2/×2), compasso, menor figura, início do compasso e cifras; **Ouvir a transcrição**; e download em **MusicXML** (comum e colorido) e **MIDI**. Na Ode à Alegria sintetizada pelo app (melodia + acordes + bumbo): 27 de 30 notas exatas, 25 de 30 durações e 8 de 9 cifras. É um rascunho para conferir e corrigir num editor, não uma prova. O motor de pauta (VexFlow 4.2.3) é carregado do jsDelivr só quando a seção aparece.

### Afinador

O botão **Afinador** na barra superior abre, acima do teclado, a nota com oitava, o ponteiro de −50 a +50 cents na cor do tom, a frequência e o contorno melódico dos últimos ~8 s. Segue a afinação e a referência escolhidas.

### Guia de pesquisa

**[docs/guia-de-pesquisa.md](docs/guia-de-pesquisa.md)** explica como conduzir e analisar cada pesquisa. O mesmo texto aparece no app (painel de entrada → Pesquisa → **Guia de pesquisa**, ou o botão **Guia** dentro de cada ferramenta), com versão para imprimir. Ele contém:

- as hipóteses testáveis do modelo (validade técnica com a Bancada; validade perceptiva H1–H5 com o Experimento e os Pesos);
- o passo a passo de cada ferramenta, com o que olhar e as armadilhas;
- a estatística em linguagem simples, a tabela de tamanho de amostra e as **regras de decisão** que o app aplica no Veredito por hipótese;
- exemplos resolvidos com números reais (bancada, laudo, A/B) e simulados (experimento, calibração);
- o estado atual do modelo, um modelo de relatório e o apêndice metodológico (pré-registro, ética, dicionário de dados, análise em R e Python).

Depois de editar o guia, rode `python3 tools/sync-guia.py` para copiá-lo para dentro de `cromasfera.html` (`--check` só confere).

### Ferramentas de pesquisa (painel de entrada → Pesquisa)

- **Bancada:** 33 estímulos sintetizados offline (12 notas isoladas, tríades maiores/menores, Fá + Si, Ré sustentado, 7 modos, 60/120/180 BPM, progressão em 432 Hz, timbre suave × brilhante) e 7 comparações em pares. São 33 verificações com critério (26 estímulos + 7 pares); os outros 7 estímulos são informativos. Em cada linha: ouvir, laudo, WAV, usar no A/B, adicionar ao experimento. Resultado atual: 32 de 33; o Ré eólio (terça menor fraca sobre um bordão) é lido como Ré maior.
- **Comparação A/B:** A e B podem ser um arquivo, um laudo JSON, um estímulo da bancada ou dois trechos do mesmo arquivo, sempre com a mesma calibração. Mostra a síntese das diferenças, a tabela A | B | Δ, perfis, rodas, paletas e o Sentirama com a seta A → B. Exporta CSV e JSON.
- **Experimento de escuta (teste cego):** trechos de arquivos, do player ou da bancada (inteiros ou N s do meio), em ordem aleatória, com código anônimo do participante. A tela cobre o app e o áudio não passa pela análise. Para cada trecho: cor sentida (7 + nenhuma), clique no Sentirama, Ar ↔ Terra e se conhece a música; o tempo de resposta é registrado. O modelo analisa o mesmo trecho. Resultados: números descritivos por resposta e o **Veredito por hipótese** (Apoia / Contradiz / Inconclusivo), calculado por trecho e por participante, com IC 95%, correção de Holm, teste do sinal e McNemar para referência × relativa. As sessões ficam no navegador; há CSV por resposta, CSV por trecho e JSON para juntar aparelhos (mescla sem duplicar).
- **Pesos Ar/Terra:** compara os pesos atuais (padrão 0,50 / 0,32 / 0,18) com os ajustados por mínimos quadrados às médias das pessoas por trecho, com validação cruzada deixando um trecho de fora e controles para testar à mão. *Aplicar estes pesos* passa a valer no tempo real e nos laudos novos (o laudo registra os pesos usados) e fica salvo no navegador; *Restaurar padrão* desfaz.

Para usar o microfone, sirva a pasta por `http://localhost` ou `https://`:

```
python3 -m http.server 8000
# abra http://localhost:8000/cromasfera.html
```

Atalhos: `1` `2` `3` modos (com o teclado musical desligado) · `Espaço` play/pause · `H` oculta a interface · `F` tela cheia · `?` teoria.

`assets/` contém as ilustrações de referência do livro exibidas no modal de teoria.

## `index.html` / `pitch16.html`

Versão anterior: *Cymatics Visualizer* (A4 = 432 Hz), 17 visualizações acionadas por detecção de altura via microfone.
