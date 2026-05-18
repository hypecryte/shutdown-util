import os, re, time


def shutdown():
    time_text = input("Введите время: ")
    # Получаем время из текста
    hours = r"\d{1,}(?=[Чч])"
    minuts = r"\d{1,}(?=[Мм])"
    seconds = r"\d{1,}(?=[Сс])"
    # Конвертируем итоговое время
    result_time = (hours * 60 * 60) + minuts * 60 + seconds
    print(result_time)
    time.sleep()


if __name__ == "__main__":
    main()
