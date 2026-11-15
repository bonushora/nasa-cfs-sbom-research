# Beyond SBOM Validity — v0.2

## Bilingual scientific edition / Edição científica bilíngue

**Edition prepared for distribution — publication pending at packaging time.**
**Edição preparada para distribuição — publicação pendente no momento do empacotamento.**

### English

Beyond SBOM Validity: A Configuration-Aware Composition
Witness for Software Supply Chain Assurance

An Experimental Study Using Synthetic Inventories and
NASA Core Flight System Configurations.

This independent study examines the distinction between
implemented SBOM documentary checks and composition
sufficiency against a frozen, configuration-specific
reference.

The English v0.1 edition is preserved without changes.
The Brazilian Portuguese translations are editorial
derivatives prepared with AI assistance and documented
review under human direction.

- [Original English edition](original-v0.1/README.md)
- [Scientific report](original-v0.1/research/v0.1/SCIENTIFIC-REPORT.md)
- [Experimental results](original-v0.1/research/v0.1/EXPERIMENTAL-RESULTS.md)
- [Reproduction limitations](original-v0.1/research/v0.1/REPRODUCTION.md)

### Português

Além da Validade do SBOM: Uma Testemunha de Composição
Sensível à Configuração para Garantia da Cadeia de
Suprimentos de Software.

Um Estudo Experimental Utilizando Inventários Sintéticos
e Configurações do NASA Core Flight System.

Esta pesquisa independente examina a distinção entre
os controles documentais implementados para SBOM e
a suficiência de composição em relação a uma referência
congelada e específica da configuração.

A edição original em inglês v0.1 permanece inalterada.
As traduções brasileiras foram preparadas com assistência
de IA e revisão documentada sob direção humana.

- [Edição traduzida](translations/pt-BR/README.md)
- [Relatório científico](translations/pt-BR/SCIENTIFIC-REPORT.md)
- [Resultados experimentais](translations/pt-BR/EXPERIMENTAL-RESULTS.md)
- [Limitações da reprodução](translations/pt-BR/REPRODUCTION.md)

### Author / Autor

Thales Rangel — Independent Researcher / Pesquisador Independente

ORCID: https://orcid.org/0000-0002-0629-9731

Original version DOI: https://doi.org/10.5281/zenodo.24230342

Concept DOI: https://doi.org/10.5281/zenodo.24230341

Candidate version / Versão candidata: 0.2

New version DOI / DOI da nova versão: 10.5281/zenodo.24241152

Reserved for publication; registration pending. / Reservado para publicação; registro pendente.

### Editorial context / Contexto editorial

[Editorial note / Nota editorial](EDITORIAL-NOTE.md)

### Rights / Direitos

- [Original LICENSE](original-v0.1/LICENSE)
- [Original NOTICE](original-v0.1/NOTICE)
- [Original file-level license manifest](original-v0.1/LICENSE-MANIFEST.json)

The original licenses remain unchanged.
Licensing of eligible new editorial contributions has been approved by the author.

As licenças originais permanecem inalteradas.
O licenciamento das contribuições editoriais elegíveis
foi aprovado pelo autor.

### Scientific limitations / Limitações científicas

No new experiments, external peer review, NASA endorsement,
global completeness, vulnerability discovery or operational
security qualification are claimed.

Não são alegados novos experimentos, revisão externa
por pares, endosso da NASA, completude global, descoberta
de vulnerabilidades ou qualificação de segurança operacional.

Related-work review / Revisão do estado da arte:
COMPLETED_DOCUMENTARY_REVIEW.

Targeted exploratory review; not an exhaustive systematic review.
Revisão exploratória direcionada; não constitui revisão sistemática exaustiva.

GLOBAL_GREEN=BLOCKED


## Related work / Estado da arte — v0.2 candidate

- [State of the art — English](related-work/STATE-OF-THE-ART.en.md)
- [Estado da arte — Português](related-work/STATE-OF-THE-ART.pt-BR.md)
- [Comparative matrix / Matriz comparativa](related-work/COMPARATIVE-MATRIX.json)
- [References / Referências](related-work/REFERENCES.md)
- [Candidate metadata / Metadados](BIBLIOGRAPHIC-METADATA.json)
- [License manifest / Manifesto de licenciamento](LICENSE-MANIFEST-v0.2.json)

The original scientific results and historical states are
preserved. This revision introduces no new experiments and
does not establish worldwide novelty or operational security.

Os resultados científicos originais e estados históricos
estão preservados. Esta revisão não introduz novos experimentos
nem estabelece novidade mundial ou segurança operacional.

Human editorial acceptance of E5-C: APPROVED.
New editorial licensing: AUTHOR_APPROVED.
Publication: NOT_AUTHORIZED.


## English editorial supplement

The historical English edition contains eight threat
descriptions in Portuguese. The original bytes are preserved.

- [Complete English rendering of the eight threats](editorial/THREATS-TO-VALIDITY.en.md)

A edição histórica em inglês contém oito descrições de ameaças
em português. Os bytes originais permanecem preservados.

O suplemento oferece a versão integral dessas descrições
em inglês, sem alterar os resultados ou as limitações.


## Integrity verification / Verificação de integridade

### English

After extracting the final v0.2 ZIP, run the following
command from the root of the extracted edition:

```bash
sha256sum --strict -c SHA256SUMS
```

The root manifest verifies the complete bilingual edition,
including `translations/pt-BR`.

To verify the preserved historical v0.1 independently,
enter `original-v0.1` and run the same command there.

The Portuguese translation directory has no separate
SHA256SUMS. Return to the v0.2 edition root for verification.

The root SHA256SUMS was generated during deterministic packaging
and is included in this archive.

### Português

Após extrair o ZIP final da v0.2, execute o comando
acima na raiz da edição extraída.

O manifesto da raiz verifica a edição bilíngue completa,
incluindo `translations/pt-BR`.

Para verificar independentemente a v0.1 preservada,
entre em `original-v0.1` e execute o mesmo comando.

A pasta de traduções não possui manifesto SHA256SUMS
separado. Retorne à raiz da edição v0.2 para a verificação.

O SHA256SUMS da raiz foi gerado no empacotamento determinístico
e está incluído neste arquivo.


## Licensing and attribution / Licenciamento e atribuição

Author / Autor: Thales Rangel — Independent Researcher /
Pesquisador Independente.

ORCID: https://orcid.org/0000-0002-0629-9731

Original work / Obra original:
Beyond SBOM Validity, v0.1.
DOI: https://doi.org/10.5281/zenodo.24230342

This v0.2 candidate includes Brazilian Portuguese translations
and new editorial contributions prepared with AI assistance
under human direction. The author has approved CC BY 4.0
for eligible contributions to these translations and editorial
documents, as identified in LICENSE-MANIFEST-v0.2.json.

The original Python prototypes retain Apache-2.0.
All historical original licenses and notices remain unchanged.
The license grant applies only to rights held by the author.
No NASA or other third-party rights are granted.

Esta edição candidata v0.2 inclui traduções brasileiras
e novas contribuições editoriais preparadas com assistência
de IA sob direção humana. O autor aprovou CC BY 4.0 para
as contribuições elegíveis dessas traduções e documentos
editoriais, conforme LICENSE-MANIFEST-v0.2.json.

Os protótipos Python originais permanecem sob Apache-2.0.
Todas as licenças e avisos históricos permanecem inalterados.
O licenciamento limita-se aos direitos detidos pelo autor.
Não são concedidos direitos da NASA ou de terceiros.

- [CC BY 4.0 legal text](original-v0.1/LICENSES/CC-BY-4.0.txt)
- [Apache-2.0 legal text](original-v0.1/LICENSES/Apache-2.0.txt)
- [File-level license scope](LICENSE-MANIFEST-v0.2.json)

The historical documents retain their original preparation
states. Their historical NOT_AUTHORIZED statements are not
new decisions about the published v0.1.

The license decisions for v0.2 are approved. The author accepted the E5-C candidate; this successor includes
authorized editorial adjustments. Publication remains unauthorized.

As decisões de licenciamento da v0.2 estão aprovadas.
O autor aceitou a candidata E5-C; esta sucessora incorpora
ajustes editoriais autorizados. A publicação permanece não autorizada.
