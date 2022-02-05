from utils import utility, msr  

URL_REPOSITORIO = 'https://github.com/armandossrecife/promocity.git'
repositorio = 'promocity'
repositorio_src = repositorio + '/' + 'src'
dir_src_java = 'src/main/java'

print('Testa os scripts do MSR')

# 1. Lista todos os commmits do repositorio
all_commits = msr.list_all_commits(repositorio)

print('\n Lista os detalhes de um commit especifico')
# 2. Lista os detalhes de um commit especifico
commit_hash = 'e3b8141b1e905e8230ce791e16e3d3abb8b619c6'
my_commit = msr.list_single_commit(repositorio, commit_hash)
print(f'Hash: {commit_hash}, Committer: {my_commit.committer.name}, Author: {my_commit.author.name}, Commiter Date: {my_commit.committer_date}')

# # 3. Lista os commits de uma lista de Hashs (NAO FUNCIONA!)
# # hash_list = ["e3b8141b1e905e8230ce791e16e3d3abb8b619c6", "9e4ae2ca924ad7ead9eb02d12bd04c739e45fb37"]
# # for each in hash_list:
# #     my_commit = msr.list_single_commit(repositorio, each)
# #     print(f'Hash: {commit_hash}, Committer: {my_commit.committer.name}, Author: {my_commit.author.name}, Commiter Date: {my_commit.committer_date}')

print('\n Lista todos os arquivos modificados em todos os commits do repositorio')
# 3. Lista todos os arquivos modificados em todos os commits do repositorio
all_modified_files = msr.list_all_modified_files_in_commits(repositorio)
for k,v in all_modified_files.items():
    print(k,[file.filename for file in v] )

print('\n Mostra todos os arquivos modificados em um commit especifico')
# 4. Mostra todos os arquivos modificados em um commit especifico
commit_hash = '2bee7e5fc9a40784e59a3aa98cce08b239027ec4'
print(commit_hash)
all_modified_files_in_commit = msr.list_all_modified_files_in_single_commit(repositorio, commit_hash)
for each in all_modified_files_in_commit:
    print(each.filename)

print('\n Mostra todas as tags do repositorio')
# 5. Mostra todas as tags do repositorio
all_tags = msr.list_all_tags(repositorio)
for each in all_tags:
    print(each)

print('\n Mostra todos os arquivos modificados das tags do repositorio')
# 6. Mostra todos os arquivos modificados das tags do repositorio
all_modified_files_in_tags = msr.list_all_modified_files_in_tags(repositorio)
for k, v in all_modified_files_in_tags.items():
    print(k, [file.filename for file in v])

print('\n Mostra os arquivos modificados em uma tag especifica')
# 7. Mostra os arquivos modificados em uma tag especifica
modified_files_in_tag = msr.list_modified_files_in_tag(path_repository=repositorio, tag_name='promocity-v1.1.0')
for each in modified_files_in_tag:
    print(each.filename)

# 8. Lista os commits entre duas tags
print('\n Lista os commits entre duas tags')
commits_between_tag1_tag2 = msr.list_all_commits_between_tags(repositorio, 'promocity-v1.0.0','promocity-v1.1.0')
for each in commits_between_tag1_tag2:
    print(each.hash)

print('\n Frequencia de commits')
# 9. Mostra a frequencia de commits de cada arquivo ao longo de todos os commits do repositorio
files_frequency = msr.get_files_frequency_in_commits(repositorio)
for k,v  in files_frequency.items():
    print(k, v)

print('\n L changes')
# 10. Mudancas de linhas dos arquivos ao longo de todos os commits
files_lines_changes = msr.get_number_of_lines_of_code_changes_in_commits(repositorio)
for k,v  in files_lines_changes.items():
    print(k, v)

print('\n CC')
# 11 CC dos arquivos ao longo de todos os commits
files_cc = msr.get_files_cyclomatic_complexity_in_commits(repositorio)
for k,v  in files_cc.items():
    print(k, v)

print('\n Mostra apenas os .java modificados em todos os commits')
# 12. Mostra apenas os .java modificados em todos os commits
java_modified = msr.list_java_modified_files_in_commits(repositorio)
for k,v in java_modified.items():
    print(k, [file.filename for file in v])

print('\n Mostra apenas os .java modificados de um commit')
# 13. Mostra apenas os .java modificados de um commit
java_modified_from_commit = msr.list_java_modified_files_in_single_commit(repositorio, commit_hash)
for each in java_modified_from_commit:
    print(each.filename)

print('\n Mostra apenas os .java modificados entre duas tag')
# 14. Mostra apenas os .java modificados entre duas tag
java_modified_from_tags = msr.list_java_modified_files_in_tags(repositorio)
for k, v in java_modified_from_tags.items():
    print(k, [file.filename for file in v])

print('\n Mostra a frequencia de alteracoes dos .java de um repositorio')
# 15. Mostra a frequencia de alteracoes dos .java de um repositorio
java_frequency = msr.get_java_files_frequency_in_commits(repositorio)
for k, v in java_frequency.items():
    print(k, v)

print('\n Mostra as linhas modificadas dos .java de um repositorio')
# 16. Mostra as linhas modificadas dos .java de um repositorio
java_lines_changes = msr.get_java_number_of_lines_of_code_changes_in_commits(repositorio)
for k, v in java_lines_changes.items():
    print(k, v)

print('\n Mostra a cc dos .java de um repositorio')
# 17. Mostra a cc dos .java de um repositorio
java_cc = msr.get_java_files_cyclomatic_complexity_in_commits(repositorio)
for k, v in java_cc.items():
    print(k, v)