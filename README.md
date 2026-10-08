# Croma

## `cromasfera.html` — Cromasfera Audio-Visualizer

Web app de arquivo único (HTML + Tailwind + Three.js via CDN) que transforma áudio em cor e forma segundo o método **Croma-Sônica** do livro *Cromasfera: The Seed of Interdisciplinary Harmony* (Vigmorã / CromaSomos).

- **Entradas:** microfone, upload / arrastar-e-soltar (.mp3 .wav .m4a .ogg) com player, e uma demonstração sintetizada.
- **DSP:** `AnalyserNode` com `fftSize = 4096`; cromagrama por picos espectrais (A4 = 440 Hz), nota dominante e secundárias, centroide espectral, RMS, BPM (autocorrelação do fluxo espectral), tonalidade (Krumhansl-Schmuckler), acordes.
- **Mapa:** Ré (D) = Verde 0 → … → Dó# = Azul-UV 11; naturais = círculos, ultravioletas = triângulos.
- **Mapa:** as ultravioletas têm a mesma cor das naturais (Yellow[1] = Yeluv[1], Violet[4] = Viluv[4], Green[6] = Gruv[6], Orange[8] = Oruv[8], Blue[11] = Bluv[11]).
- **Modos:** Cromasfera 3D (esfera + fita de 12 tons em curva de “bola de tênis”) · Flor Croma-Sônica (mandala de 12 pétalas) · Sentirama 3D (Plano Físico azul ↔ amarelo × Plano Espiritual vermelho ↔ rosa, cruzando-se na tônica).

### Calibração

No painel de entrada, em **Calibração** (fica salva no navegador):

- **Afinação (Lá 4)**: 440 Hz (padrão) ou 432 Hz. Vale para o cromagrama em tempo real, para a demonstração e para o laudo.
- **Referência (Verde 0)**: qual nota é o Verde 0. O padrão do método é Ré (D); escolher outra nota renumera os 12 tons e as cores a partir dela (o teclado, o diagnóstico e o laudo seguem a escolha).

### Laudo (análise completa)

Além do tempo real, o app gera um **laudo** do áudio inteiro:

- **Analisar música inteira** (ou **Laudo** no player): processa o arquivo carregado do começo ao fim.
- **Gravar sessão**: com o microfone ativo, grava e analisa a gravação ao parar (a gravação pode ser baixada).
- O laudo traz o enquadramento no modelo em duas leituras — **de referência** (a nota escolhida como Verde 0, por padrão Ré) e **relativa** (tônica detectada = Verde 0) —, a afinação estimada da gravação (ex.: Lá 4 ≈ 432 Hz),, índice Ar/Terra com seus componentes, perfil cromático, paleta de cores, trajetória no Sentirama, tonalidade por trecho, acordes, tensão Fá ↔ Si, andamento, parâmetros e limitações do método.
- **Baixar laudo (JSON)** exporta resumo + linha do tempo (~46 ms por quadro); **Abrir laudo salvo** reabre o JSON; **Imprimir / PDF** gera uma versão para papel.
- A análise roda num Web Worker, a 44,1 kHz mono e FFT de 4096 pontos, com o mesmo núcleo DSP (`dspCore`) do tempo real — o mesmo arquivo gera o mesmo laudo em qualquer aparelho.

Para usar o microfone, sirva a pasta por `http://localhost` ou `https://`:

```
python3 -m http.server 8000
# abra http://localhost:8000/cromasfera.html
```

Atalhos: `1` `2` `3` modos · `Espaço` play/pause · `H` oculta a interface · `F` tela cheia · `?` teoria.

`assets/` contém as ilustrações de referência do livro exibidas no modal de teoria.

## `index.html` / `pitch16.html`

Versão anterior: *Cymatics Visualizer* (A4 = 432 Hz), 17 visualizações acionadas por detecção de altura via microfone.
