#  adds an int to ascii int
#  adds an int to shift ascii binary to the left
class Encrypt:
    # constructor
    def __init__(self, plainText, shift, distance):
        self.plainText = plainText
        self.shift = shift
        self.distance = distance

    def stringEncrypt(self):
        bs = ""

        for char in self.plainText:
            ordValue = ord(char) + self.distance  # gets int value and then adds distance int

            if ordValue > 127:  # must fall in the range of 1 - 127 for ascii charaters
                self.distance - (127 - ordValue + 1)

            bs += self.bitShifter_Left(ordValue) + " "

        return bs

        # shift ascii bit string left. takes in ascii int and int to shift left int as arguments
        # converts ascii int to a binary string and then shifts left

    def bitShifter_Left(self, cipherValue):
        ss = ""  # shifted string
        bs = ""  # bit string

        while cipherValue > 0:  # convert ascii int to binary
            r = cipherValue % 2
            cipherValue //= 2  # divides and returns the int value of quotient
            bs = str(r) + bs  # bit string conversion

        if len(bs) < 8:  # if binary bit string is less than 8 characters than adds '0' to the front
            bs = '0' + str(bs)

        bs = bs[self.shift:] + bs[0:self.shift]  # bit shifter, first element + all elements except the last

        ss += bs + " "  # full bit string after shift to the left

        return ss  # returns shifted string

# subtracts an int to ascii int
# subtracts an int to shift ascii binary to the left
class Decrypt:
    def __init__(self, binaryString, distance, shift):
        self.binaryString = binaryString
        self.distance = distance
        self.shift = shift

    # shift bit string right(reverse).
    # takes in ascii bit string, int to shift right, and distance as arguments
    def stringDecrypt(self):
        bsList = self.binaryString.split()  # split binaryString into individual word bit strings
        shiftBinaryString = ""
        sbs = ""
        intsbs = 0

        for bs in bsList:  # iterate through each bit string in the list
            sbs = bs[-self.shift:] + bs[0:-self.shift]  # shift right 'reverse' bit shift from encryption

            if len(sbs) < 8:  # add '0' to the front of bit string if less than 8 char
                sbs = '0' + sbs

            intsbs = int(sbs, 2) - self.distance  # convert from binary to base 10 int

            if intsbs < 0:  # must fall in the range of 1 - 127 for ascii charaters
                intsbs = 127 - (self.distance - (1 - intsbs))

            ascii_char = chr(intsbs)  # convert from base 10 int to ascii charater

            shiftBinaryString += ascii_char  # concatenates bit strings characters

        return shiftBinaryString.strip()
