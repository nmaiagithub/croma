# Croma

## `cromasfera.html` — Cromasfera Audio-Visualizer

Web app de arquivo único (HTML + Tailwind + Three.js via CDN) que transforma áudio em cor e forma segundo o método **Croma-Sônica** do livro *Cromasfera: The Seed of Interdisciplinary Harmony* (Vigmorã / CromaSomos).

- **Entradas:** microfone, upload / arrastar-e-soltar (.mp3 .wav .m4a .ogg) com player, e uma demonstração sintetizada.
- **DSP:** `AnalyserNode` com `fftSize = 4096`; cromagrama por picos espectrais (A4 = 440 Hz), nota dominante e secundárias, centroide espectral, RMS, BPM (autocorrelação do fluxo espectral), tonalidade (Krumhansl-Schmuckler), acordes.
- **Mapa:** Ré (D) = Verde 0 → … → Dó# = Azul-UV 11; naturais = círculos, ultravioletas = triângulos.
- **Modos:** Cromasfera 3D · Flor Croma-Sônica · Sentirama 3D.

Para usar o microfone, sirva a pasta por `http://localhost` ou `https://`:

```
python3 -m http.server 8000
# abra http://localhost:8000/cromasfera.html
```

Atalhos: `1` `2` `3` modos · `Espaço` play/pause · `H` oculta a interface · `F` tela cheia · `?` teoria.

`assets/` contém as ilustrações de referência do livro exibidas no modal de teoria.

## `index.html` / `pitch16.html`

Versão anterior: *Cymatics Visualizer* (A4 = 432 Hz), 17 visualizações acionadas por detecção de altura via microfone.
