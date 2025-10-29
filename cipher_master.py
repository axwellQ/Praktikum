class CipherMaster:
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        original_text = original_text.lower()
        result = []
        n = len(self.alphabet)

        for char in original_text:
            if char in self.alphabet:
                idx = self.alphabet.index(char)
                new_idx = (idx + shift) % n
                result.append(self.alphabet[new_idx])
            else:
                result.append(char)

        return ''.join(result)

    def decipher(self, cipher_text, shift):
        return self.cipher(cipher_text, -shift)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))
