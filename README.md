# Numerologia Cabalística em Python

## 📜 Sobre o Projeto

Este é um sistema completo de **Numerologia Cabalística** desenvolvido em Python, que realiza uma análise numerológica profunda baseada no nome completo e data de nascimento do usuário. O projeto é uma evolução e melhoria significativa do algoritmo original disponível no repositório [silverat/Numerologia-Cabalistica-Python](https://github.com/silverat/Numerologia-Cabalistica-Python/tree/main).

## 🔄 Principais Melhorias

Em relação ao código original, foram implementadas as seguintes melhorias:

- **🔧 Refatoração do código**: Estrutura mais limpa, organizada e com melhor legibilidade
- **🐛 Correção de bugs**: Diversos problemas na lógica de cálculo foram corrigidos
- **📊 Nova funcionalidade de pirâmide numérica**: Geração automática da pirâmide numerológica a partir do nome
- **📝 Formatação aprimorada**: Saída mais clara e organizada no terminal e em arquivos
- **📂 Exportação para arquivo**: Geração automática de um arquivo `.txt` com todos os resultados
- **🎯 Separação de vogais e consoantes**: Análise detalhada e visualização formatada
- **🧩 Cálculos refinados**: Melhor precisão nos cálculos de números mestres (11, 22)
- **🔄 Código modular**: Funções mais reutilizáveis e com responsabilidades bem definidas

## ✨ Funcionalidades

O sistema realiza uma análise numerológica completa incluindo:

### 📊 Números Principais
- **Número de Motivação** - Desejo interior e impulsos da alma
- **Número de Impressão/Aparência** - Como os outros o percebem
- **Número de Expressão** - Talentos e habilidades inatas
- **Número de Destino** - Propósito de vida e caminho
- **Número da Missão** - O que veio fazer neste planeta

### 📈 Análises Avançadas
- **Lições Cármicas** - Desafios a serem superados
- **Tendências Ocultas** - Padrões de comportamento
- **Dívidas Cármicas** - Transgressões de vidas passadas
- **Resposta do Subconsciente** - Reações em situações de emergência
- **Análise do Dia de Nascimento** - Características específicas

### 🔄 Ciclos e Períodos
- **Ciclos de Vida** - 3 grandes períodos da existência
- **Desafios** - Obstáculos a serem superados
- **Momentos Decisivos** - Fases importantes da vida
- **Ano Pessoal, Mês Pessoal e Dia Pessoal** - Vibrações atuais
- **Tabela de Ano Universal** - Influências cósmicas

### 💕 Relacionamentos
- **Número do Amor** - Compatibilidade amorosa
- **Harmonia Conjugal** - Análise de relacionamentos
- **Números Harmônicos, Neutros e Incompatíveis**
- **Cores Favoráveis** - Para equilíbrio e bem-estar

### 🏛️ Pirâmide Numérica
- **Geração automática** da pirâmide a partir do nome
- **Visualização** dos níveis da pirâmide com formatação centralizada
- **Cálculo** das reduções sucessivas para cada nível

## 📋 Como Usar

### Pré-requisitos
- Python 3.7 ou superior

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/numerologia-cabalistica.git

# Navegue até o diretório
cd numerologia-cabalistica

# Execute o programa
python3 numerologia.py
```

### Entrada de Dados

O programa solicitará:

1. **Nome completo**: Digite seu nome completo (ex: "João Silva Santos")
2. **Data de nascimento**: Digite no formato `dd/mm/aaaa` (ex: "15/03/1985")

### Saída

O programa gera dois tipos de saída:

1. **Saída no Terminal**: Exibição formatada com cores e estrutura clara
2. **Arquivo de Texto**: Arquivo `.txt` com todos os resultados para consulta futura

## 🧮 Como Funciona

O sistema utiliza a tabela de correspondência numerológica cabalística, onde cada letra possui um valor numérico específico. Os cálculos principais são:

### Cálculo de Valores Numéricos

```python
cabalacod = {'A': 1, 'I': 1, 'Q': 1, 'B': 2, 'K': 2, 'R': 2, ...}
```

### Redução dos Números

Os números são reduzidos a um único dígito (exceto números mestres 11, 22, 33) através da soma dos dígitos.

### Exemplo de Cálculo

Para o nome "JOÃO" e data "15/03/1985":

1. **Motivação**: Soma das vogais → 1 + 7 + 1 = 9
2. **Expressão**: Soma de todas as letras → 1 + 7 + 1 + 6 = 15 → 1 + 5 = 6
3. **Destino**: Soma da data → 15 + 3 + 1985 = 2003 → 2 + 0 + 0 + 3 = 5

## 📁 Estrutura do Projeto

```
numerologia-cabalistica/
├── numerologia.py          # Código principal
├── README.md               # Documentação do projeto
└── [nome]_[data].txt       # Arquivos gerados com resultados
```

## 🎯 Melhorias Implementadas

### Correções de Lógica
- **Refatoração** da função `reduzir()` para melhor tratamento de números mestres
- **Correção** do cálculo de anos pessoais para quando o aniversário já passou
- **Ajuste** na função `reduzirdata()` para cálculos mais precisos
- **Correção** da verificação de vogais e consoantes

### Novas Funcionalidades
- **Separação formatada** de vogais e consoantes (`separar_vogais_consoantes_formatado`)
- **Pirâmide numérica** com centralização automática
- **Geração de arquivo** com formatação completa
- **Tratamento de acentos** em português

### Melhorias de Usabilidade
- **Formatação** mais clara e organizada
- **Cores** para destacar informações importantes no terminal
- **Descrições** mais detalhadas e compreensíveis
- **Código** mais modular e documentado

## 📝 Licença

Este projeto está sob a licença **GNU GENERAL PUBLIC LICENSE - Version 3, 29 June 2007**.

## 👨‍💻 Autor

- **@BIOHACK**
- E-mail: b10h4ck.br@protonmail.me

## 🙏 Agradecimentos

- Ao projeto original de [silverat](https://github.com/silverat/Numerologia-Cabalistica-Python) pela base
- À comunidade de código aberto pelo suporte e inspiração
- Aos estudiosos da Numerologia Cabalística que mantêm viva essa tradição milenar

## 🔮 Sobre a Numerologia Cabalística

A Numerologia Cabalística é um sistema que combina elementos da Cabala Judaica com a numerologia tradicional. Ela busca revelar aspectos ocultos da personalidade, propósito de vida, desafios e oportunidades através da análise dos números associados ao nome e data de nascimento.

### Principais Conceitos

- **Números Mestres**: 11, 22 (e por extensão 33) - números com vibração especial
- **Ciclos de Vida**: Períodos de 9 anos com temas específicos
- **Karma e Dharma**: Lições a aprender e propósito de vida
- **Vibrações**: Energias que influenciam diferentes aspectos da vida

## 🚀 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

---

**⚠️ Aviso**: Este programa é fornecido para fins educacionais e de estudo. A numerologia deve ser vista como uma ferramenta de autoconhecimento, não como uma fonte de verdades absolutas.
