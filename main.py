import os, re, time, sys


def get_current_os():
    # Получаем текущую ОС
    current_platform = sys.platform
    return current_platform


def shutdown():
    current_platform = get_current_os()
    time_text = input("Введите время для отключения(например, 1ч 20м 15с): ")

    # Ищем совпадения
    h_match = re.search(r"(\d+)[Чч]", time_text)
    m_match = re.search(r"(\d+)[Мм]", time_text)
    s_match = re.search(r"(\d+)[Сс]", time_text)

    # Извлекаем текст и конвертируем в числа (если не найдено, ставим 0)
    hours = int(h_match.group(1)) if h_match else 0
    minutes = int(m_match.group(1)) if m_match else 0
    seconds = int(s_match.group(1)) if s_match else 0

    # Считаем общее время
    result_time = (hours * 3600) + (minutes * 60) + seconds

    if current_platform == "win32":
        # Логика таймера и выключения
        if result_time > 0:
            print(f"Таймер запущен. Времени до отключения: {result_time}с")
            os.system(f"shutdown /s /t {result_time}")  # Команда для Windows
            time.sleep(5)
        else:
            print("Время не распознано или равно нулю.")
    elif current_platform == "linux" or current_platform == "darwin":
        if result_time > 0:
            print(f"Таймер запущен. Времени до отключения: {result_time}с")
            os.system(f"shutdown -h +{result_time}")
            time.sleep(5)


def shutdown_restart():
    current_platform = get_current_os()
    time_text = input("Введите время для перезагрузки(например, 1ч 20м 15с): ")

    # Ищем совпадения
    h_match = re.search(r"(\d+)[Чч]", time_text)
    m_match = re.search(r"(\d+)[Мм]", time_text)
    s_match = re.search(r"(\d+)[Сс]", time_text)

    # Извлекаем текст и конвертируем в числа (если не найдено, ставим 0)
    hours = int(h_match.group(1)) if h_match else 0
    minutes = int(m_match.group(1)) if m_match else 0
    seconds = int(s_match.group(1)) if s_match else 0

    # Считаем общее время
    result_time = (hours * 3600) + (minutes * 60) + seconds

    if current_platform == "win32":
        # Логика таймера и выключения
        if result_time > 0:
            print(f"Таймер запущен. Времени до перезагрузки: {result_time}с")
            os.system(f"shutdown /r /t {result_time}")  # Команда для Windows
            time.sleep(5)
        else:
            print("Время не распознано или равно нулю.")
    elif current_platform == "linux" or current_platform == "darwin":
        if result_time > 0:
            print(f"Таймер запущен. Времени до перезагрузки: {result_time}с")
            os.system(f"shutdown -r +{result_time}")
            time.sleep(5)
        else:
            print("Время не распознано или равно нулю.")


def cancel_shutdown():
    print("Shutdown is canceled")
    os.system("shutdown -a")
    time.sleep(5)


def operation():
    select_op = input(
        "Выберите операцию:\n1. Отложенное выключение\n2. Отложенная перезагрузка\n3. Отмена отложенного отключения\nВаш выбор: "
    )
    match select_op:
        case "1":
            shutdown()
        case "2":
            shutdown_restart()
        case "3":
            cancel_shutdown()
        case _:
            print("Неверная операция!!!")


if __name__ == "__main__":
    operation()
