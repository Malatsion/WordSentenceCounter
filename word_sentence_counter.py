import re


def count_words_sentences(file_path):
    """
    Функція зчитує вміст текстового файлу та підраховує кількість слів і речень.
    :param file_path: шлях до файлу
    :return: кортеж (кількість слів, кількість речень)
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    words = re.split(r'[\s,;:]+', text.strip())
    words = [word for word in words if word]  # Видаляємо порожні елементи

    sentences = re.split(r'(?<!\.)[.!?]+\s', text.strip())
    sentences = [sentence for sentence in sentences if sentence]  # Видаляємо порожні елементи

    return len(words), len(sentences)


if __name__ == "__main__":
    file_path = input("Введіть шлях до файлу: ")
    words_count, sentences_count = count_words_sentences(file_path)
    print(f"Кількість слів: {words_count}")
    print(f"Кількість речень: {sentences_count}")
