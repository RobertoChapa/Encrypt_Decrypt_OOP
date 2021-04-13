"""
Read, write, append objects
"""
class textIO:
    def __init__(self, Text_File, operation, text):
        self.Text_File = Text_File
        self.operation = operation # w,r,a
        self.text      = text

    def io_Text(self):
        TextFile = open(self.Text_File, self.operation)  # operation = w,r,a
        message  = ""

        try:
            if self.operation == 'w':
                TextFile.write(self.text)
                message = "write completed"
            elif self.operation == 'r':
                message = TextFile.read()
            elif self.operation == 'a':
                TextFile.write(self.text)
                message = "append completed"
            else:
                message = "Enter valid operation"
        except Exception as e:
            message = "Error: " + str(e)
        finally:
            TextFile.close()

        return message
