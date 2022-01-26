import subprocess
import os
from pathlib import Path
import plotly.graph_objects as go

def run_bash_command(bashCommand):
  """"
  Executa um comando bash
  @param: str bashCommand: comando bash
  """
  subprocess.run(bashCommand, shell=True, check=True, executable='/bin/bash')

def generate_list_locs_of_files(filename):
  """
  Retorna a lista de Locs de cada arquivo
  @param: str filename: nome do arquivo de entrada
  @return list list_locs_of_files
  """
  list_locs_of_files = []
  with open(filename) as file:
    for line in file:
      line = line.rstrip("\n")
      list_locs_of_files.append(line)
  return list_locs_of_files

def search_loc_of_file(file_name, list):
  """
  Para cada arquivo procura sua LOC (Lines of Code)
  @param: str file_name: nome do arquivo
  @param: str list: lista contendo todos os arquivos do projeto
  @return int Loc: do arquivo dado
  """
  for each in list:
    if file_name in each[1]:
      return int(each[0])

def generate_list_locs_of_files_updated(list_locs_of_files):
  """
  Cria uma lista com elementos que representam o LOC e o arquivo - tupla (Loc, arquivo)
  @param: list list_locs_of_files: lista contendo os locs de cada arquivo
  @return list_locs_of_files_updated: lista atualizada com os elementos (loc, arquivo)
  """
  list_locs_of_files_updated = []
  for each in list_locs_of_files:
    elementos = each.split(' ') 
    item = elementos[-2], elementos[-1]
    list_locs_of_files_updated.append(item)
  return list_locs_of_files_updated

# Gera um arquivo contendo diretorios e arquivos
def generate_list_of_files_and_directories(filename):
  """
  Gera uma lista de arquivos e diretorios do codigo analisado
  @param: str filename: arquivo txt contendo a arvore de diretorios
  @return list_of_files_and_directories
  """
  list_of_files_and_directories = []
  with open(filename) as file2:
    for line in file2:
      line = line.rstrip("\n")
      if 'java' in line:
        list_of_files_and_directories.append(line)
  return list_of_files_and_directories

def generate_list_of_files_and_directories_src(list_of_files_and_directories_updated, dir_src='src/main/java/'):
  """
   Escolhe o diretorio do source java
   Lista apenas arquivos e diretorios do src/main/java
  @param: list list_of_files_and_directories_updated: lista de arquivos e diretorios atualizada
  @param: str dir_src: diretorio que sera analisado valor defaul: src/main/java
  @return list_of_files_and_directories_src
  """
  list_of_files_and_directories_src = []
  for item in list_of_files_and_directories_updated:
    if 'src' in item:
      if dir_src in item:
        list_of_files_and_directories_src.append(item)
  return list_of_files_and_directories_src

def generate_labels_parents_values(list_of_files_and_directories_src, list_locs_of_files_updated):
  """
   Popula os labels, parents e values
   Adaptado de https://plotly.com/python/treemaps
  Retorna os labels, parents e values dos arquivos e diretorios
  @param: list list_of_files_and_directories_src: lista contendo o path completo dos arquivos e diretorios
  @param: list list_locs_of_files_updated: lista com os LOCs de cada arquivo
  @return labels, parents e values
  """
  labels = []
  parents = []
  for each in list_of_files_and_directories_src:
    nome_item = each.split('/')[-1]
    labels.append(nome_item)
    if os.path.isdir(each):
        pai = os.path.dirname(each)
        pai = pai.split('/')[-1]
        if pai == 'java':
          pai = ' '
        parents.append(pai)
    else: 
      elemento = Path(each).parent
      elemento = str(elemento)
      elemento = elemento.split('/')[-1]
      parents.append( str(elemento) )

  values = []
  for i in range(0, len(labels) ):
    each = list_of_files_and_directories_src[i]
    nome_item = each.split('/')[-1]
    loc = search_loc_of_file(nome_item, list_locs_of_files_updated)
    if '.java' in nome_item: 
      values.append(loc)
    else:
      values.append(1)
  return labels, parents, values

def generate_treemap(labels, values, parents, filename="mytreemap.html", show=False):
  """
  Gera a treemap e o arquivo html da treemap
  Retorna os labels, parents e values dos arquivos e diretorios
  @param: str labels: nomes dos arquivos e diretorios
  @param: str values: Loc de cada arquivo
  @param: str parents: pai de cada arquivo ou diretorio
  @param: str filename: nome do arquivo html que vai conter a treemap
  @param: bool show: mostra a treemap no browser
  @return labels, parents e values
  """
  fig = go.Figure(go.Treemap(
    labels = labels,
    values = values,
    parents = parents,
    marker_colorscale = 'Blues'
  ))
  fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))

  if show:
    fig.show()

  print('Cria o html do treemap')
  treemap_to_html = fig.to_html()
  html_file = open(filename, "w")
  html_file.write(treemap_to_html)
  html_file.close()
  print(f'Arquivo {filename} treemap criado com sucesso!')

# 1. Clona o repositorio que sera analisado
URL_REPOSITORIO = 'https://github.com/armandossrecife/promocity.git'
repositorio = 'promocity'
msg = f"Removido diretório {repositorio} antigo"
print(f"Removendo o diretorio {repositorio}...")
bashCommand_remove_repository = f"[ -d {repositorio} ] && echo {msg} && rm -d -rf {repositorio}"
run_bash_command(bashCommand_remove_repository)
bashCommand_git = f"git clone {URL_REPOSITORIO}"
run_bash_command(bashCommand_git)

# 2. Gera um arquivo txt contendo apenas arquivos .java do repositorio
file_loc_java = 'locarquivosjava.txt'
bashCommand_file = f"find {repositorio} -name *.java | xargs wc -l > {file_loc_java}"
run_bash_command(bashCommand_file)

# 3. Gera uma lista contendo linhas com LOCs e arquivos do repositorio
list_locs_of_files = generate_list_locs_of_files(file_loc_java)

# 4. Gera uma lista atualizada contendo tuplas (loc, arquivo) do repositorio
list_locs_of_files_updated = generate_list_locs_of_files_updated(list_locs_of_files)

# 5. Gera uma arvore contendo todos os arquivos e diretorios com seus paths completos
file_tree = 'treearquivosdir.txt'
bashCommand_tree = f"tree {repositorio}/src -i -f > {file_tree}"
run_bash_command(bashCommand_tree)

# 6. Gera a lista com os paths completos de todos os arquivos e diretorios do projeto
list_of_files_and_directories = generate_list_of_files_and_directories(file_tree)

# 7. Substitui o . por repositorio/
repositorio = repositorio + '/'
list_of_files_and_directories_updated = [each.replace('./', repositorio) for each in list_of_files_and_directories]

# 8. Gera a lista com os paths completos dos arquivos e diretorios do diretorio src/main/java (padrao)
list_of_files_and_directories_src = generate_list_of_files_and_directories_src(list_of_files_and_directories_updated)

# 9. Gera os labels, parents e values para a treemap
labels, parents, values = generate_labels_parents_values(list_of_files_and_directories_src, list_locs_of_files_updated)

# 11. Mostra os labels, parents e values gerados
print('')
print(f'Labels: {labels}')
print('')
print(f'Parents: {parents} ')
print('')
print(f'Values: {values}')

# 12 gera a treemap do diretorio de codigo analisado e salva o arquivo html
generate_treemap(labels, values, parents, filename="mytreemap.html", show=False)