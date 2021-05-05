from os import path

symbolBASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 -,.'


class FTTCryptor:

    @staticmethod
    def toBinary(text):
        return ''.join(format(ord(x), 'b') for x in text)

    @staticmethod
    def fileToBytes(file):
        with open(file, "rb") as f:
            byteDump = f.read()
        return byteDump

    @staticmethod
    def bytesToFile(bytes, file):
        f = open(file, "wb")
        f.write(bytes)
        f.close()
        return file

    @staticmethod
    def bytesToSequence(byte):
        byteList = list(byte)
        byteSequence = str(byteList).replace("[", "").replace("]", "").replace(' ', '')
        return byteSequence

    @staticmethod
    def sequenceToBytes(sequence):
        listOfBytes = sequence.split(',')
        return bytes(list(map(int, listOfBytes)))

    def crypt(self, text, key, mode):
        translated = ''
        accessKey = 0
        token = 0

        for i in str(key):
            accessKey = accessKey + int(self.toBinary(i))
        for i in self.toBinary(str(accessKey)):
            token = token + int(i)
        for char in text:
            if char in symbolBASE:
                DUMPC = symbolBASE.find(char)
                if mode == 1:
                    indexC = DUMPC + token
                elif mode == 0:
                    indexC = DUMPC - token

                if indexC >= len(symbolBASE):
                    indexC = indexC - len(symbolBASE)
                elif indexC < 0:
                    indexC = indexC + len(symbolBASE)

                translated = translated + symbolBASE[indexC]
            else:
                translated = translated + char
        return translated

    def encryptText(self, text, key):
        return self.crypt(text, key, 1)

    def decryptText(self, cipher, key):
        return self.crypt(cipher, key, 0)

    def encryptFile(self, file, key):
        try:
            if path.exists(file):
                byteBase = self.fileToBytes(file)
                sequenceBase = self.bytesToSequence(byteBase)
                return self.encryptText(sequenceBase, key)
            return
        except Exception as err:
            print(err)
            return

    def decryptFile(self, cipher, key):
        try:
            if cipher:
                sequenceBase = self.decryptText(cipher, key)
                byteBase: bytes = self.sequenceToBytes(sequenceBase)
                return self.bytesToFile(byteBase)
            return
        except Exception as err:
            print(err)
            return


FTTCryptor = FTTCryptor()