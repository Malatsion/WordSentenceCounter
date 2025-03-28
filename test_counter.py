import pytest
from word_sentence_counter import count_words_sentences

@pytest.fixture
def sample_text_file(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("Привіт, світ! Як справи? Все добре.")
    return str(file)

@pytest.mark.parametrize("content, expected_words, expected_sentences", [
    ("Привіт, світ!", 2, 1),
    ("Один. Два. Три!", 3, 3),
    ("Простий текст без розділових знаків", 5, 1),
    ("Що ж... Це тестовий файл.", 5, 2)
])
def test_count_words_sentences(tmp_path, content, expected_words, expected_sentences):
    file = tmp_path / "test.txt"
    file.write_text(content, encoding='utf-8')
    assert count_words_sentences(str(file)) == (expected_words, expected_sentences)
