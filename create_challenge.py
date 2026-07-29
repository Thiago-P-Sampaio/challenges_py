## Script para criar pastas automaticas com comandos!
from pathlib import Path
import argparse

#comando: python create_challenge.py <<nivel>> <<nome_pasta>>
# Caminho raiz onde todos os desafios serão criados(partindo do diretório do arquivo py)
ROOT = Path(__file__).parent

# Nome das pastas de nível
LEVELS = {
    "easy": "Easy",
    "medium": "Medium",
    "hard": "Hard"
}


def create_files(challenge_path: Path, challenge_name: str):
    drafts = challenge_path / "Drafts"
    solution = challenge_path / "Solution"

    drafts.mkdir(parents=True, exist_ok=True)
    solution.mkdir(parents=True, exist_ok=True)

    draft_file = drafts / "main.py"
    solution_file = solution / "solution.py"

    if not draft_file.exists():
        draft_file.write_text(
            f"""# Challenge: {challenge_name}


def main():
    pass


if __name__ == "__main__":
    main()
""",
            encoding="utf-8"
        )

    if not solution_file.exists():
        solution_file.write_text(
            f"""# Solution: {challenge_name}


def solution():
    pass


if __name__ == "__main__":
    solution()
""",
            encoding="utf-8"
        )


def main():
    parser = argparse.ArgumentParser(
        description="Cria automaticamente a estrutura de um desafio."
    )

    parser.add_argument(
        "level",
        type=str.lower,          # Converte automaticamente para minúsculas
        choices=LEVELS.keys(),   # Aceita easy, Easy, EASY, eAsY...
        help="Nível do desafio: easy, medium ou hard."
    )

    parser.add_argument(
        "name",
        nargs="+",
        help="Nome do desafio."
    )

    args = parser.parse_args()

    level = LEVELS[args.level]
    challenge_name = " ".join(args.name).title()

    challenge_path = ROOT / level / challenge_name

    create_files(challenge_path, challenge_name)

    print("✔ Estrutura criada com sucesso!")
    print(challenge_path)


if __name__ == "__main__":
    main()