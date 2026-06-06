import json
import os

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

def adicionar(tarefas):
    titulo = input("Título da tarefa: ")
    tarefas.append({"titulo": titulo, "concluida": False})
    print("✓ Tarefa adicionada!")

def listar(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\n--- MINHAS TAREFAS ---")
    for i, tarefa in enumerate(tarefas):
        status = "✓" if tarefa["concluida"] else " "
        print(f"{i+1}. [{status}] {tarefa['titulo']}")

def concluir(tarefas):
    listar(tarefas)
    if not tarefas:
        return
    try:
        idx = int(input("Número da tarefa a concluir: ")) - 1
        if 0 <= idx < len(tarefas):
            tarefas[idx]["concluida"] = True
            print("✓ Tarefa concluída!")
        else:
            print("Número inválido.")
    except:
        print("Digite um número válido.")

def remover(tarefas):
    listar(tarefas)
    if not tarefas:
        return
    try:
        idx = int(input("Número da tarefa a remover: ")) - 1
        if 0 <= idx < len(tarefas):
            removida = tarefas.pop(idx)
            print(f"✓ Tarefa '{removida['titulo']}' removida!")
        else:
            print("Número inválido.")
    except:
        print("Digite um número válido.")

def main():
    tarefas = carregar_tarefas()
    while True:
        print("\n" + "="*30)
        print("    SISTEMA DE TAREFAS")
        print("="*30)
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Concluir tarefa")
        print("4. Remover tarefa")
        print("5. Sair")
        print("-"*30)
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar(tarefas)
        elif opcao == "2":
            listar(tarefas)
        elif opcao == "3":
            concluir(tarefas)
        elif opcao == "4":
            remover(tarefas)
        elif opcao == "5":
            salvar_tarefas(tarefas)
            print("\n✓ Tarefas salvas! Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()