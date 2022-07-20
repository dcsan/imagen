class MdPage:

    def __init__(self, filename='output.md'):
        # self.path = f'output/renders/{filename}'
        self.path = filename
        self.fp = open(self.path, "w")

    def line(self, text):
        self.fp.write(text + '\n')
        self.fp.flush()

    # without newline
    def item(self, text):
        self.fp.write(text)
        self.fp.flush()

    def plain(self, text):
        '''no p wrapper'''
        self.fp.write(f'{text}\n')
        self.fp.flush()

    def close(self):
        # self.fp.write('</body></html>\n')
        self.fp.close()
