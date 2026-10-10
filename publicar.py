import os
import subprocess
import sys

# ============================================================
# CONFIGURAÇÕES — EDITE AQUI SE PRECISAR
# ============================================================
PASTA = r"C:\Users\matth\OneDrive\Desktop\MEU_SITE"

USUARIO_GITHUB = "mattheusribeiro2025"
NOME_REPOSITORIO = "Mattheus"

URL_REMOTE = f"https://github.com/{USUARIO_GITHUB}/{NOME_REPOSITORIO}.git"

NOME_GIT = "Mattheus"
EMAIL_GIT = "mattheusribeiro2025@users.noreply.github.com"

MENSAGEM_COMMIT = "Primeiro commit - Site Streamlit"


# ============================================================
# FUNÇÃO AUXILIAR — Executa comando no terminal
# ============================================================
def rodar(comando):
    print(f"\n▶️  {comando}")
    resultado = subprocess.run(
        comando,
        shell=True,
        cwd=PASTA,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )
    if resultado.stdout.strip():
        print(resultado.stdout.strip())
    if resultado.stderr.strip():
        print(resultado.stderr.strip())
    return resultado.returncode


# ============================================================
# 1. VERIFICA SE O GIT ESTÁ INSTALADO
# ============================================================
def verificar_git():
    print("=" * 55)
    print("🔍 Verificando se o Git está instalado...")
    print("=" * 55)
    resultado = subprocess.run(
        "git --version",
        shell=True,
        capture_output=True,
        text=True
    )
    if resultado.returncode != 0:
        print("❌ Git não está instalado.")
        print("👉 Baixe em: https://git-scm.com/download/win")
        sys.exit(1)
    print(f"✅ {resultado.stdout.strip()}")


# ============================================================
# 2. VERIFICA SE A PASTA EXISTE
# ============================================================
def verificar_pasta():
    if not os.path.exists(PASTA):
        print(f"❌ Pasta não encontrada: {PASTA}")
        sys.exit(1)
    print(f"✅ Pasta existe: {PASTA}")


# ============================================================
# 3. INICIALIZA O GIT (se ainda não foi)
# ============================================================
def inicializar_git():
    pasta_git = os.path.join(PASTA, ".git")
    if os.path.exists(pasta_git):
        print("✅ Repositório Git já inicializado")
        return
    print("🔧 Inicializando repositório Git...")
    rodar("git init")


# ============================================================
# 4. CONFIGURA USUÁRIO E EMAIL
# ============================================================
def configurar_git():
    print("🔧 Configurando usuário e e-mail do Git...")
    rodar(f'git config user.name "{NOME_GIT}"')
    rodar(f'git config user.email "{EMAIL_GIT}"')


# ============================================================
# 5. ADICIONA E FAZ O COMMIT
# ============================================================
def adicionar_e_commitar():
    print("📦 Adicionando arquivos...")
    rodar("git add .")

    print("📝 Fazendo commit...")
    rodar(f'git commit -m "{MENSAGEM_COMMIT}"')


# ============================================================
# 6. REMOVE O REMOTE ANTIGO (se existir)
# ============================================================
def remover_remote_antigo():
    resultado = subprocess.run(
        "git remote",
        shell=True,
        cwd=PASTA,
        capture_output=True,
        text=True
    )
    if "origin" in resultado.stdout:
        print("🔄 Removendo remote antigo...")
        rodar("git remote remove origin")


# ============================================================
# 7. ADICIONA O REMOTE CORRETO
# ============================================================
def adicionar_remote():
    print(f"🔗 Adicionando remote: {URL_REMOTE}")
    rodar(f'git remote add origin {URL_REMOTE}')


# ============================================================
# 8. MUDA A BRANCH PARA main
# ============================================================
def definir_branch_main():
    print("🌿 Definindo branch principal como 'main'...")
    rodar("git branch -M main")


# ============================================================
# 9. FAZ O PUSH
# ============================================================
def fazer_push():
    print("🚀 Enviando arquivos para o GitHub...")
    print("⚠️  Se aparecer uma janela do navegador, autorize o Git.")
    rodar("git push -u origin main")


# ============================================================
# EXECUÇÃO PRINCIPAL
# ============================================================
def main():
    print("\n" + "=" * 55)
    print("🚀 PUBLICANDO O SITE NO GITHUB")
    print("=" * 55)

    verificar_git()
    verificar_pasta()
    inicializar_git()
    configurar_git()
    adicionar_e_commitar()
    remover_remote_antigo()
    adicionar_remote()
    definir_branch_main()
    fazer_push()

    print("\n" + "=" * 55)
    print("✅ PROCESSO CONCLUÍDO!")
    print("=" * 55)
    print(f"\n📦 Repositório: https://github.com/{USUARIO_GITHUB}/{NOME_REPOSITORIO}")
    print()
    print("🎯 Próximos passos:")
    print("  1) Acesse: https://github.com/mattheusribeiro2025/Mattheus")
    print("  2) Confirme se os arquivos foram enviados")
    print("  3) Publique no Streamlit Cloud: https://streamlit.io/cloud")


if __name__ == "__main__":
    main()