from utils import utility

URL_REPOSITORIO = 'https://github.com/armandossrecife/promocity.git'
repositorio = 'promocity'
repositorio_src = repositorio + '/' + 'src'
dir_src_java = 'src/main/java'

print("Testa os scripts utility")
# 1. Clona o repositorio que sera analisado
# 1.1 Remove o diretorio caso ele ja exista
bashCommand_remove_repository = f"if [ -d {repositorio} ]; then rm -rf {repositorio}; fi"
status = utility.run_bash_command(bashCommand_remove_repository)
if status == 0:
    print(f'The repository {repositorio} was removed with success!')
else:
    raise Exception(f'Erro: result: {status} The repository {repositorio} was not removed!')

# 1.2 Clona o repositorio
bashCommand_git = f"git clone {URL_REPOSITORIO}"
status = utility.run_bash_command(bashCommand_git)
if status == 0:
    print(f'The repository {repositorio} was cloned with success!')
else:
    raise Exception(f'Erro: result: {status} The repository {repositorio} was not cloned!')

# 2. Gera uma lista contendo todos os arquivos e diretorios do repositorio src
files_and_directories = utility.create_file_from_bash_tree(repositorio_src, "arquivosediretorios.txt")
all_files_and_directories = utility.convert_file_in_list(files_and_directories)

# 3. Gera uma lista contendo todos os diretorios do repositorio src
directories = utility.create_file_from_bash_tree(repositorio_src, "diretorios.txt", all_files_directories=False)
all_directories = utility.convert_file_in_list(directories)

# 4. Lista de diretorios do diretório src/main/java ou src/java do repositorio
all_directories_from_src = [ each for each in all_directories if (dir_src_java in each) ]

# 5 Lista todos os diretorios que estao no dir_src_java
all_directories_and_java_files_from_src = [each for each in all_files_and_directories if (dir_src_java in each)]

# 6. Lista todos os arquivos .java do diretório src/main/java do repositório
all_java_files_from_src = [each for each in all_files_and_directories if ((dir_src_java in each) and ('.java' in each))]

print(f'Lista todos os arquivos .java do {repositorio} no diretorio {dir_src_java}')
for each in all_java_files_from_src:
    print(each)
print('')

# 7. Lista todos os arquivos .java com suas LoCs
file_loc_files = utility.create_loc_file_from_bash_tree(repositorio_src, 'locarquivosjava.txt')
list_locs_files = utility.generate_list_locs_files(repositorio, file_loc_files)
list_locs_java_files = [each for each in list_locs_files if (dir_src_java in each[1]) ]

print(f'Lista todos os arquivos .java e suas LoCs do {repositorio} no diretorio {dir_src_java}')
for each in list_locs_java_files:
    print(each)
print('')

# 8. Lista todos os arquivos .java com suas CCs
list_cc_files = utility.generate_list_cc_files(list_locs_files)
list_cc_src_java_files = [each for each in list_cc_files if (dir_src_java in each[1]) ]
utility.print_n(10, list_cc_src_java_files)

print(f'Lista todos os arquivos .java e suas CCs do {repositorio} no diretorio {dir_src_java}')
for each in list_cc_src_java_files:
    print(each)
print('')
print('')