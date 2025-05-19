import subprocess
import sys

MIN_ARGS = 2
COMMAND_INDEX = 1
DB_COMMAND = "db_cafe"


def run_command(command):
    """Функция для выполнения команды в терминале."""
    try:
        subprocess.run(command, check=True, shell=True, text=True)
        print(f"Команда выполнена: {command}")
    except subprocess.CalledProcessError as e:
        print(
            f"Ошибка при выполнении команды: {command}\n"
            f"Код ошибки: {e.returncode}\nВывод:\n{e.stderr}"
        )


def filling_db():
    """Подготовка БД, наполнение БД из фикстуры db.json."""
    print("Подготовка БД...")
    run_command("python manage.py makemigrations")
    run_command("python manage.py migrate")
    print("Наполнение БД из фикстуры...")
    run_command("python manage.py loaddata db.json")
    print("Создание админа...")
    run_command("python manage.py createsuperuser")


if __name__ == "__main__":
    if len(sys.argv) < MIN_ARGS:
        print("Пример команды: python start_cafe.py [db_cafe]")
        sys.exit(COMMAND_INDEX)

    command = sys.argv[COMMAND_INDEX]
    commands = {
        DB_COMMAND: filling_db,
    }
    if command in commands:
        commands[command]()
    else:
        print(
            "Некорректный аргумент. Введите 'db_cafe'"
            "для подготовки БД."
        )
        sys.exit(COMMAND_INDEX)
