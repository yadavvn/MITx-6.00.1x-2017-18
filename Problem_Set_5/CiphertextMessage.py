from Problem_Set_5.Message import *


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)


    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        #
        max_score = 0
        best_shift = 0
        final_text = ''

        for shift in range(0,26):
            score = 0
            decrypt_shift = 25 - shift
            decoded_text = self.apply_shift(decrypt_shift)
            split_words = decoded_text.split()

            for word in split_words:
                if is_word(self.valid_words, word):
                    score += 1
            else:
                if score > max_score:
                    max_score = score
                    best_shift = decrypt_shift
                    final_text = decoded_text

        return best_shift, final_text

