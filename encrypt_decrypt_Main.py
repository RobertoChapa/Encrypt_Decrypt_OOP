from crypto_Objects import Encrypt as em  # encrypto method
from crypto_Objects import Decrypt as dm  # decrypt method
from textIO_Objects import textIO as iot  # text input/output stream method


def main():
    # --------------------user data-------------------------#
    plainText_File = 'plain.txt'
    encryptedText_File = 'encrypt.txt'
    decryptedText_File = 'decrypt.txt'
    shift = 3  # number to add to the ascii integer
    distance = 5  # number of bits to shift the Ascii Binary string left

    # --------------------get plain text and encrypt--------#

    iot_1 = iot(plainText_File, 'r', '')  # set object variables
    plainText = iot_1.io_Text()  # read plain text from Plain.txt

    em_e = em(plainText, shift, distance)  # set encrypt object variables
    es = em_e.stringEncrypt()  # encrypt plain text string

    # set input/output class object variables
    iot_1.Text_File = encryptedText_File
    iot_1.operation = 'w'
    iot_1.text = es
    iot_1.io_Text()  # write encypted text to Encrypt.txt

    # ---------------------decrypt--------------------------#

    # set input/output class object variables
    iot_1.operation = 'r'  # read
    iot_1.text = ''

    binaryString = iot_1.io_Text()  # get encrypted text from Encrypt.txt

    # set decrypt class object variables
    dm_e = dm(binaryString, distance, shift)
    ds = dm_e.stringDecrypt()  # decrypt text and then get text

    # set input/output class object variables
    iot_1.Text_File = decryptedText_File
    iot_1.operation = 'w'  # write
    iot_1.text = ds

    iot_1.io_Text()  # write decrypted text to Decrypt.txt

    # ---------------------output to console------------------#

    # output to console
    print()
    print(plainText + '\r\n')
    print('Shift: ' + str(shift), ' distance:' + str(distance), '\r\n',
          es + '\r\n')  # encrypted text with the shift int and distance int
    print(ds + '\r\n')  # decrypted text
    print()

    return


if __name__ == "__main__":
    main()
