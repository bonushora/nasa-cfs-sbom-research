# Visão geral da pesquisa — tradução complementar em português

## Escopo e identificadores imutáveis

Este estudo complementar independente abrange o conjunto público de código-fonte NASA cFS v7.0.1, ancorado em `088b2fa828db9ff7e00733f1908e0eeb59f66ce3`. A versão científica v0.2 está ancorada em `c7981ea2fd501b3e1fb6d0f856e85c1274894e06`. Os metadados de citação foram acrescentados posteriormente em `b612e0269fab9667cba57c2048100dd281572b53`; esse commit exclusivo de metadados **não** substitui o commit da pesquisa.

## Métodos

**Reconciliação VDD.** A identidade registrada do arquivo TAR do VDD oficial é conferida antes da inspeção; membros inseguros do arquivo são rejeitados. A Seção 7 é interpretada como 25 componentes únicos com identificadores Git completos de 40 caracteres, comparados à tabela controlada de Gitlinks. Os VDDs individuais confirmam os rótulos de versão v7.0.1, mas não verificam independentemente cada SHA Git.

**Inventário delimitado das árvores Git.** As entradas-folha recursivas são enumeradas na árvore-raiz fixada e nas árvores Git de cada um dos 25 componentes. Os Gitlinks são representados sem percorrer recursivamente seus alvos dentro da árvore-pai. Arquivos regulares, cópias de trabalho filtradas, links simbólicos, Gitlinks e ponteiros Git LFS são classificados separadamente. Arquivos não rastreados e gerados são excluídos.

**Evidências de dependências e licenças.** A matriz distingue 25 Gitlinks fixados de declarações sintáticas presentes em `find_package`, `add_subdirectory`, `target_link_libraries` e `include`. Essas declarações não comprovam resolução transitiva, vinculação na compilação selecionada ou carregamento em execução. As observações de licenças provêm de arquivos de licença/aviso fixados e de identificadores SPDX; o licenciamento em nível de pacote permanece `NOASSERTION`.

**Segurança e normas.** A pesquisa de vulnerabilidades é uma investigação documental delimitada, não testes de exploração nem constatação de que um commit específico está afetado. O mapeamento NTIA/SPDX é uma autoavaliação por campo, não certificação de conformidade. A conversão CycloneDX foi adiada até haver ferramentas e esquema validados.

## Resultados relatados

| Dimensão | Resultado relatado | Limite de interpretação |
|---|---|---|
| Reconciliação VDD–Gitlink | 25/25 SHAs Git completos correspondentes e 25/25 VDDs individuais identificando v7.0.1 | Apenas consistência das revisões de código-fonte |
| Inventário de árvores Git | 4.341 entradas delimitadas | Não representa composição de binários ou implantação |
| Evidências de dependências | 316 linhas | Somente 25 Gitlinks são relações fixadas verificadas |
| Evidências de licença | 28 linhas | Sem inferências de licença para pacotes inteiros |
| Investigação de vulnerabilidades | `DEFERRED_PARTIAL` | Sem conclusões de afetação em nível de commit |
| Mapeamento NTIA/SPDX | `PASS_WITH_GAPS` | Persistem lacunas de fornecedor e processo |
| Resultado CycloneDX | `DEFERRED` | Nenhum BOM CycloneDX emitido |

## Limites e proveniência de terceiros

Esta pesquisa não demonstra completude de compilação, binários, execução ou implantação, nem qualificação para voo, ausência de vulnerabilidades ou certificação da NASA. A discussão pública #1188 do GitHub NASA cFS é apenas fonte de proveniência documental. Seus participantes não são apresentados como coautores ou revisores, e os comentários não constituem aprovação ou endosso. O arquivo VDD e os documentos NASA extraídos são referenciados, não redistribuídos neste suplemento.

## Referências primárias

- Visão geral original: `research/v0.2/README.md`
- Metodologia: `research/v0.2/METHODOLOGY.md`
- Proveniência: `research/v0.2/PROVENANCE.md`
- Reconciliação VDD: `research/v0.2/vdd/vdd-crosswalk.md`
- Limites da pesquisa de segurança: `research/v0.2/security/vulnerability-research.md`
- Direitos: `research/v0.2/RIGHTS_AND_ATTRIBUTION.md`
- Interação pública: `research/v0.2/EXTERNAL-CFS-VDD-RECONCILIATION-1188.md`

Fonte científica: https://github.com/bonushora/nasa-cfs-sbom-research/tree/c7981ea2fd501b3e1fb6d0f856e85c1274894e06
