import subprocess
import sys

MIN_ARGS = 2
COMMAND_INDEX = 1
DB_COMMAND = "db_cafe"
ADMIN = "admin"
GENERAL_COMMAND = "all"
INSTALL_TEST_COMMAND = "test"


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


def creat_admin():
    """Создание админа с предустановленными значениями."""
    print("Создание админа...")
    run_command("python manage.py createsuperuser")


def all_commands():
    """Подготовка приложения под ключ."""
    print("Подготовка приложения под ключ...")
    filling_db()
    creat_admin()
    # run_command("python manage.py runserver")


if __name__ == "__main__":
    if len(sys.argv) < MIN_ARGS:
        print("Пример команды: python start_cafe.py [db_cafe|admin|all]")
        sys.exit(COMMAND_INDEX)

    command = sys.argv[COMMAND_INDEX]
    commands = {
        DB_COMMAND: filling_db,
        ADMIN: creat_admin,
        GENERAL_COMMAND: all_commands,
    }
    if command in commands:
        commands[command]()
    else:
        print("Некорректный аргумент. Введите 'db_cafe'"
              "для подготовки БД или 'admin' для cоздание админа, "
              "'all' для запуска приложения под ключ, "
              "'test' для запуска тестов.")
        sys.exit(COMMAND_INDEX)
