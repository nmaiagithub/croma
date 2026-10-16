#!/usr/bin/env python3
"""Copia docs/guia-de-pesquisa.md para dentro de cromasfera.html.

O app mostra o guia no painel "Guia de pesquisa" a partir do Markdown embutido em
<script type="text/markdown" id="guia-md">. Rode este script sempre que editar o guia:

    python3 tools/sync-guia.py          # atualiza o HTML
    python3 tools/sync-guia.py --check  # só confere (sai com erro se estiverem diferentes)
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MD = ROOT / 'docs' / 'guia-de-pesquisa.md'
HTML = ROOT / 'cromasfera.html'
BLOCK = re.compile(r'(<script type="text/markdown" id="guia-md">\n)(.*?)(</script>)', re.S)


def main() -> int:
    md = MD.read_text(encoding='utf-8')
    if '</script' in md.lower():
        sys.exit('O guia não pode conter "</script>".')
    html = HTML.read_text(encoding='utf-8')
    m = BLOCK.search(html)
    if not m:
        sys.exit('Bloco <script id="guia-md"> não encontrado em cromasfera.html.')
    body = md if md.endswith('\n') else md + '\n'
    if '--check' in sys.argv:
        if m.group(2) != body:
            print('cromasfera.html está desatualizado: rode python3 tools/sync-guia.py')
            return 1
        print('Guia sincronizado.')
        return 0
    HTML.write_text(html[:m.start(2)] + body + html[m.end(2):], encoding='utf-8')
    print(f'Guia copiado para {HTML.name} ({len(body.splitlines())} linhas).')
    return 0


if __name__ == '__main__':
    sys.exit(main())
