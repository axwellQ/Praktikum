class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        # Приводим текст к нижнему регистру
        text = text.lower()
        result = []
        n = len(self.alphabet)

        # Если расшифровка — инвертируем сдвиг
        actual_shift = shift if is_encrypt else -shift

        for char in text:
            if char in self.alphabet:
                idx = self.alphabet.index(char)
                new_idx = (idx + actual_shift) % n
                result.append(self.alphabet[new_idx])
            else:
                result.append(char)

        return ''.join(result)


# Проверка:
cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
))
