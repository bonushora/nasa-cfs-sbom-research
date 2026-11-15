# Além da Validade do SBOM: Uma Testemunha de Composição Sensível à Configuração para Garantia da Cadeia de Suprimentos de Software

Um Estudo Experimental Utilizando Inventários Sintéticos e Configurações do NASA Core Flight System

## Resumo
Este estudo experimental independente distingue a validade documental de um SBOM da suficiência em relação a uma referência de composição congelada. Uma testemunha sintética avaliou 11 casos em dois perfis (44 execuções); um comparador tipado distinto avaliou oito casos derivados de snapshots instalados das configurações STD e EDS do NASA cFS (16 avaliações). Todas as 16 avaliações derivadas de dados reais concordaram com os oráculos pré-registrados; oito pares apresentaram resultados idênticos nas repetições. Seis casos negativos e dois controles positivos foram avaliados duas vezes cada, sem aceitações indevidas observadas (0/12) e sem bloqueios indevidos observados (0/4). Os resultados dizem respeito a identidades de arquivos e declarações dinâmicas diretas, não à completude global, à descoberta de vulnerabilidades ou à garantia operacional.

## Método
As referências foram congeladas antes das alterações deliberadas. W04 compara entidades e arestas sintéticas; B2-A compara caminhos de arquivos qualificados pela configuração, alegações SHA-256 e declarações DT_NEEDED diretas, não identidades de pacotes nem provedores resolvidos. STD utiliza o relacionamento histórico DYNAMIC_LINK; EDS utiliza comentários JSON. B2-B1 materializou e verificou 16 documentos SPDX antes da avaliação; B2-B2 executou oito avaliações primárias e oito avaliações de repetição em processos separados. O schema Draft7 e as verificações de referências implementadas não constituem certificação de conformidade normativa integral com SPDX. A referência é separada das mutações submetidas, mas compartilha a mesma linhagem de compilação.

## Resultados
STD: 546 arquivos instalados, 474 ELF, 432 declarações diretas; EDS: 565, 483, 458. ELF constitui um subconjunto dos arquivos instalados. As contagens representam ocorrências específicas da configuração. Sintéticos: 11 casos distintos, 44 execuções, 330+330 asserções de nível folha, 22/22 pares, 3/3 verificações pareadas. Perfil original: aceitação indevida 0/11, bloqueio indevido N/A (sem positivos); perfil suplementado: 0/8 e 0/3. Derivados de dados reais: 8 casos distintos, 16 avaliações, concordância com os oráculos de 16/16, 8/8 pares, aceitação indevida 0/12, bloqueio indevido 0/4. Primária: 0/6 e 0/2; repetição: 0/6 e 0/2. Não agregar unidades distintas nem tratar repetições como casos independentes.

## Alegações
### H1 — SUPPORTED_SYNTHETIC_ONLY
Uma política ingênua não constitui um defeito de scanner.
O controle positivo com aviso de segurança inserido deliberadamente e a omissão pareada sustentam apenas o contrafactual. Uma ausência de correspondência delimitada pelo escopo ou o bloqueio de um veredito amplo não constitui falha.
Nenhuma alegação sobre qualquer scanner real.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W05-B-20261114T153932.563503Z/COMPARISON.json SHA256 37c307b6646c17cbfbb7bd269f90513228f286b117cdd5a1ca27ce8e696599b5
- SSSVL-SBOM-WITNESS-CFS-v0.1-W05-B-20261114T153932.563503Z/METRICS.json SHA256 07795a1f894faf587b9e0e09f31da83e92a21b601de6a45161a399507289566e
- SSSVL-SBOM-WITNESS-CFS-v0.1-W01-W02-R1-20261113T141925.233282Z/HYPOTHESES.md SHA256 37dfa5911a84f6148ee6a9b8e764f8f025f2ba025a61dee30b74f2b38faa2ece
### H2 — SUPPORTED_BOUNDED
Casos elaborados em conjunto com o avaliador podem favorecer sua implementação.
Identidades ausentes, incompatibilidade de hash e declarações ausentes foram detectadas nos casos selecionados. A aceitação de uma incompatibilidade relativa a um requisito refutaria a previsão.
W04 e B2-A são distintos; a referência é independente das mutações submetidas, mas não foi obtida por uma compilação independente.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W05-B-20261114T153932.563503Z/COMPARISON.json SHA256 37c307b6646c17cbfbb7bd269f90513228f286b117cdd5a1ca27ce8e696599b5
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/METRICS.json SHA256 f32199df0cc27feb829a9926987395b2c380b693f7ab0ec7b5c54fe9a895d98b
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/ORACLE.json SHA256 4a4fe5b8c2c7dbfdf6491849ae43aa60cbe85c0471e3596bdf2f99e09579622e
- SSSVL-SBOM-WITNESS-CFS-v0.1-W01-W02-R1-20261113T141925.233282Z/HYPOTHESES.md SHA256 37dfa5911a84f6148ee6a9b8e764f8f025f2ba025a61dee30b74f2b38faa2ece
### H3 — SUPPORTED_BOUNDED
O schema e os hashes regenerados dos documentos não comprovam conformidade normativa integral.
REAL-03/04 omitem uma identidade da referência; o schema e as verificações de integridade implementadas são aprovados enquanto a cobertura delimitada falha. Uma falha de schema/checksum invalidaria essa construção.
REAL-07 é um teste distinto: a alegação SHA256 muda, SHA1 permanece; sem alteração física.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B1-20261114T164606.435303Z/REPORT.json SHA256 27e02fc452d8a0108f13206d818b7188d251eae016642dc1eecc33d0ef82782a
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B1-20261114T164606.435303Z/MATERIALIZATION.json SHA256 4da5aa562fb93d20f0de495ab7d729206ac9ab40075df05f4e861e7bfbb8d1ab
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/METRICS.json SHA256 f32199df0cc27feb829a9926987395b2c380b693f7ab0ec7b5c54fe9a895d98b
- SSSVL-SBOM-WITNESS-CFS-v0.1-W01-W02-R1-20261113T141925.233282Z/HYPOTHESES.md SHA256 37dfa5911a84f6148ee6a9b8e764f8f025f2ba025a61dee30b74f2b38faa2ece
### H4 — SUPPORTED_BOUNDED
O chamador fornece a configuração; REAL-08 bloqueia antes da avaliação dos papéis.
A incompatibilidade explícita é detectada; universos requeridos equivalentes invalidariam a distinção alegada. Não misturar código-fonte/compilação/instalação/runtime.
Sem descoberta autônoma da configuração ou resistência à falsificação de identidade.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W05-B-20261114T153932.563503Z/COMPARISON.json SHA256 37c307b6646c17cbfbb7bd269f90513228f286b117cdd5a1ca27ce8e696599b5
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/primary-REAL-08.json SHA256 4f2cfccf7f277342e1316f839795c7234689bed8cfc6546985bdc48e08e32de3
- SSSVL-SBOM-WITNESS-CFS-v0.1-W01-W02-R1-20261113T141925.233282Z/HYPOTHESES.md SHA256 37dfa5911a84f6148ee6a9b8e764f8f025f2ba025a61dee30b74f2b38faa2ece
### H5 — SUPPORTED_SYNTHETIC_ONLY
A exclusão opcional não estabelece o tratamento de duplicatas legítimas.
EXP-SBOM-08 sustenta apenas a exclusão justificada. O bloqueio incorreto de exclusões justificadas ou de duplicatas legítimas refutaria a especificidade.
PARTIAL_COVERAGE; duplicatas legítimas NOT_ESTABLISHED; especificidade em dados reais NOT_TESTED.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W05-B-20261114T153932.563503Z/PRIMARY.json SHA256 a139139b81357770dbc3d84e989ed94d81bff93e5f75daf83922395b6f67662a
- SSSVL-SBOM-WITNESS-CFS-v0.1-W05-B-20261114T153932.563503Z/ORACLE-FROZEN.json SHA256 99a573305e661829a27b0e48ff276ba903609a38803935bf1d1cfc29243f80a1
- SSSVL-SBOM-WITNESS-CFS-v0.1-W01-W02-R1-20261113T141925.233282Z/HYPOTHESES.md SHA256 37dfa5911a84f6148ee6a9b8e764f8f025f2ba025a61dee30b74f2b38faa2ece
### C6 — SUPPORTED_BOUNDED
A linhagem de compilação compartilhada pode compartilhar omissões sistemáticas.
Os snapshots instalados exatos correspondem a 546/474/432 STD e 565/483/458 EDS.
Não constitui um universo requerido pela missão; sem promoção para provedores/pacotes/dependências transitivas/runtime.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B1-Q1-M1-20261114T162308.349789Z/METRICS.json SHA256 d0a721c0cae53a54701e95bcdec45719d45154b3e5153022ee9d61744b30c7ff
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/REFERENCE.json SHA256 d33c6b9c28e6dd0743d76cce64ecab9a0aba2baf8d70d2a112dc01bbc1cf11fb
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/primary-REAL-01.json SHA256 956809121580cfe88152096adc27ceae8d21ac8bb59cb876db4d2d23a115b384
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/primary-REAL-02.json SHA256 6a0e9214427ff8ff0a78ab97f49a2efb5cf00205cf89692e9e20e18abe714496
### C7 — SUPPORTED_BOUNDED
Execuções repetidas não constituem amostras independentes.
8 casos distintos, 16 avaliações, 8 pares idênticos.
Nenhuma alegação de taxa de erro populacional, reprodutibilidade externa ou isolamento pelo sistema operacional.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/METRICS.json SHA256 f32199df0cc27feb829a9926987395b2c380b693f7ab0ec7b5c54fe9a895d98b
### C8 — NOT_ESTABLISHED
Nenhum scanner ou exploit foi testado.
Sem evidência de defeito em scanner comercial ou vulnerabilidade no cFS.
Manter as alegações separadas e não estabelecidas.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/REPORT.json SHA256 5b7ffa7966f481e80a3fd13e47f496095390d5268c283e29a92ac3fbbf85bff4
- SSSVL-SBOM-WITNESS-CFS-v0.1-W05-B-20261114T153932.563503Z/REPORT.json SHA256 b9b7cd109818c55bc4f8a79c00bda379537df3b527931daa595678c9954aa896
### C9 — NOT_ESTABLISHED
O escopo do snapshot exclui runtime e outras dimensões da composição.
O veredito de suficiência não possui autoridade sobre segurança operacional.
Pacote/versão, provedor, componentes estáticos, dependências transitivas e runtime permanecem UNKNOWN/NOT_VERIFIED.
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/REPORT.json SHA256 5b7ffa7966f481e80a3fd13e47f496095390d5268c283e29a92ac3fbbf85bff4
- SSSVL-SBOM-WITNESS-CFS-v0.1-W06-B2-B2-20261114T165525.320516Z/CONTRACT.json SHA256 a6f53691a4458485b1fc45bf325765c0dbd3d818c0d2400a55513c2163e1d109

## Ameaças à validade
### T1
Casos elaborados pela equipe do comparador; oráculos pré-registrados não garantem independência metodológica.
Resposta: o pré-registro mitiga ajustes posteriores, não o viés de concepção compartilhada; recomenda-se replicação independente.
Residual: OPEN_LIMITATION (limitação em aberto).
### T2
Mesma linhagem de compilação entre inventários e referência; não constitui reprodução independente da compilação.
Resposta: congelar a referência antes da mutação; a linhagem de compilação compartilhada permanece uma limitação.
Residual: OPEN_LIMITATION (limitação em aberto).
### T3
Repetições determinísticas não constituem amostra estatística independente.
Resposta: relatar separadamente os casos distintos e as repetições pareadas; sem taxa estatística agregada.
Residual: OPEN_LIMITATION (limitação em aberto).
### T4
W04 utiliza entidades e arestas sintéticas; B2-A utiliza arquivo e declaração direta, não pacote ou provedor.
Resposta: distinguir as entidades/arestas sintéticas de W04 dos papéis de arquivo/declaração de B2-A.
Residual: OPEN_LIMITATION (limitação em aberto).
### T5
Validade formal limitada a schema/referências; REAL-07 preserva SHA1 e altera a alegação SHA256.
Resposta: limitar as alegações de schema ao Draft7 e às verificações de referências implementadas; distinguir uma alegação de hash incorreta de bytes alterados.
Residual: OPEN_LIMITATION (limitação em aberto).
### T6
Configuração autenticada pelo chamador; REAL-08 testa incompatibilidade explícita, não descoberta autônoma.
Resposta: relatar incompatibilidade explícita de configuração, não inferência autônoma.
Residual: OPEN_LIMITATION (limitação em aberto).
### T7
Sem scanner real, runtime, vulnerabilidade ou segurança operacional demonstrada.
Resposta: nenhuma conclusão sobre scanner, exploit ou segurança em runtime; trabalho adicional exige autorização separada.
Residual: OPEN_LIMITATION (limitação em aberto).
### T8
Sem isolamento qualificado pelo sistema operacional; Evidence Vault pendente.
Resposta: separação entre processos não equivale a isolamento por sandbox; o vault e MT06 permanecem bloqueados/não verificados.
Residual: OPEN_LIMITATION (limitação em aberto).

## Limitações
Escopo: EXACT_SNAPSHOT_NOT_MISSION_REQUIRED_UNIVERSE. Mapeamento pacote/versão, resolução de provedores, componentes estáticos e fechamento transitivo UNKNOWN; runtime NOT_VERIFIED. MT06 NOT_VERIFIED; isolamento da testemunha pelo sistema operacional BLOCKED; Evidence Vault BLOCKED_PENDING_HUMAN_ACTION. Nenhuma falha de scanner comercial, vulnerabilidade no cFS, completude global ou segurança operacional estabelecida. Novidade NOT_ESTABLISHED; revisão da literatura NOT_AUTHORIZED; revisão externa por pares NOT_PERFORMED.

## Conclusão
A reconciliação delimitada detectou as omissões e incompatibilidades selecionadas apesar da aprovação nas verificações documentais implementadas. Trata-se de evidência experimental delimitada, não de uma alegação de novidade ou certificação de segurança.
