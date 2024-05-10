## Ferramenta de Consulta para Processos Administrativos - Comparador de Listas 

Este script Python é uma ferramenta eficiente para auxiliar em processos administrativos que envolvem a comparação de grandes conjuntos de dados. Com uma interface simples e funcionalidade robusta, ele permite comparar dois arquivos de texto contendo listas de nomes e identificar quais nomes estão presentes em ambos os arquivos e quais estão ausentes em um deles.

### Funcionalidades Principais

- **Consulta Eficiente**: O código é capaz de lidar com grandes quantidades de dados de forma rápida e eficiente.
- **Comparação Precisa**: Identifica com precisão os nomes que estão presentes em ambos os arquivos e os que estão apenas em um deles.
- **Resultados Organizados**: Os nomes encontrados e não encontrados são salvos em arquivos separados, facilitando a análise posterior.

### Como Usar

1. **Preparação dos Arquivos**: Certifique-se de ter os arquivos de texto contendo as listas de nomes que deseja comparar. Nomeie-os conforme necessário e ajuste os caminhos no código, se necessário.

2. **Execução do Script**: Execute o script Python, fornecendo os caminhos para os arquivos de entrada e especificando os nomes dos arquivos de saída para os resultados.

3. **Análise dos Resultados**: Após a execução, verifique os arquivos de saída para os nomes encontrados e não encontrados, conforme especificado durante a execução do script.

### Requisitos

- Python 3.x

### Como Contribuir

Se você encontrar problemas ou tiver sugestões para melhorar este script, sinta-se à vontade para abrir uma issue ou enviar um pull request para o repositório.

### Exemplo de Uso

```python
# Arquivos de texto com os nomes
arquivo1 = 'lista1.txt'
arquivo2 = 'lista2.txt'
encontrado_file = 'nomes_encontrados.txt'
nao_encontrado_file = 'nomes_nao_encontrados.txt'

# Comparar as listas e salvar em arquivos
comparar_listas(arquivo1, arquivo2, encontrado_file, nao_encontrado_file)
```

