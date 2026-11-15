# Estado da Arte e Posicionamento Científico

## Escopo e método

Esta é uma revisão documental exploratória direcionada,
não uma revisão sistemática exaustiva da literatura nem um
benchmark comparativo. Examina fontes primárias públicas
sobre garantia de configuração, correção de SBOM,
proveniência e aceitação baseada em evidências.

Nenhuma ferramenta concorrente foi executada. Nenhum novo
experimento foi realizado. O estudo não alega acesso a
processos internos da NASA, endosso da NASA, conformidade
formal com a NASA ou revisão externa por pares.

## Trabalhos relacionados

### R01 — NASA. Software Assurance and Software Safety Standard. NASA-STD-8739.8B, 2022.

Define uma estrutura de ciclo de vida para garantia de software, segurança e verificação e validação independentes.

### R02 — NASA. Software Engineering Handbook, Revision D. SWE-084: Configuration Audits.

Auditorias de configuração confrontam os itens de configuração efetivos com os registros que os definem.

### R03 — Yu, S.; Song, W.; Hu, X.; Yin, H. On the Correctness of Metadata-Based SBOM Generation: A Differential Analysis Approach. IEEE/IFIP DSN, 2024.

Uma avaliação diferencial de quatro geradores de SBOM baseados em metadados encontrou divergências e dependências ausentes em 7.876 projetos de código aberto.

### R04 — Xiao, Y.; Kirat, D.; Schales, D. L.; Jang, J.; Xing, L.; Liao, X. JBomAudit: Assessing the Landscape, Compliance, and Security Implications of Java SBOMs. NDSS, 2025.

O JBomAudit avalia dependências declaradas em relação aos artefatos Java associados. Seu estudo examinou 25.882 SBOMs e arquivos JAR associados e reportou 7.907 SBOMs com dependências diretas omitidas.

### R05 — SPDX. SPDX Specification v2.3.1, Clause 7: Package information.

Especifica identificadores e campos descritivos de pacotes, incluindo informações de integridade no nível de pacote.

### R06 — Ecma International. ECMA-424: CycloneDX Bill of Materials Specification. Second edition, December 2025; CycloneDX v1.7.

Oferece representação estruturada de componentes, dependências, composições e evidências de suporte.

### R07 — SLSA. Version 1.2: Build Provenance.

A proveniência de build registra contexto de produção, parâmetros, saídas e dependências resolvidas quando conhecidas.

### R08 — in-toto Witness. Policies.

Políticas assinadas avaliam atestações, signatários confiáveis, consistência de artefatos e condições de política.

### R09 — CycloneDX Project. CycloneDX CLI.

Documenta validação, comparação, conversão e operações relacionadas a BOMs.

### R10 — Interlynk. sbomqs.

Documenta pontuação de qualidade e verificações de conformidade de SBOMs.

### R11 — CISA. CISA, U.S. Government and International Partners Release Updated Minimum Elements for a Software Bill of Materials. 29 July 2026.

Anuncia orientações atualizadas de SBOM que abrangem hashes de componentes e contexto de geração, entre outros campos.


## Contribuição científica e limites

Auditoria de configuração, qualidade de inventários,
integridade criptográfica e decisões de confiança baseadas
em evidências são práticas estabelecidas. A reconciliação
entre inventários e artefatos possui antecedentes
metodológicos diretos, especialmente o JBomAudit [R04].
O in-toto Witness [R08] constitui antecedente de aceitação
baseada em políticas, atestações e consistência de artefatos.

Este estudo não reivindica ser a primeira implementação
de reconciliação de SBOM. A abordagem geral possui
antecedentes estabelecidos, e a novidade mundial da
combinação experimental específica não foi demonstrada.

Sua contribuição documentada é uma avaliação experimental
delimitada de reconciliação tipada utilizando snapshots
instalados das configurações STD e EDS do NASA cFS,
referências congeladas, identidades de arquivos, hashes,
declarações dinâmicas diretas e critérios pré-registrados
de aceitação e bloqueio.

A referência foi congelada antes das mutações experimentais
e é independente dos documentos mutados, mas compartilha a
linhagem de build. O experimento modificou inventários, não
os binários do cFS. STD e EDS utilizam representações
históricas distintas das declarações dinâmicas.

A campanha sintética e a campanha derivada do cFS permanecem
inalteradas. As repetições não são amostras estatisticamente
independentes. Esta edição não introduz novos resultados empíricos.

A avaliação diz respeito a snapshots exatos, não ao universo
completo de software requerido pela missão. Contagens de
arquivos e ELF não são contagens de pacotes. Declarações
dinâmicas diretas não estabelecem resolução em runtime,
composição estática ou fechamento transitivo de dependências.

O estudo não estabelece completude global, segurança
operacional, superioridade sobre ferramentas existentes,
vulnerabilidade da NASA ou defeito em scanner comercial.
A reprodução externa independente permanece não qualificada.

## Estado editorial

Esta é uma edição candidata v0.2 derivada da v0.1 publicada.
As alegações científicas e limitações permanecem congeladas.
O licenciamento das novas contribuições elegíveis foi aprovado pelo autor.
A aceitação editorial humana da E5-C foi aprovada.
A publicação não está autorizada.

Consulte as [referências](REFERENCES.md), a
[matriz comparativa](COMPARATIVE-MATRIX.json) e a
[edição em inglês](STATE-OF-THE-ART.en.md).
