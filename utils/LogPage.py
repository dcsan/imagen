class LogPage:

    def __init__(self, filename='log.html'):
        self.path = f'renders/{filename}'
        self.fp = open(self.path, "w")
        self.fp.write('<html><body>\n')

    def line(self, text):
        self.fp.write(f'<p>{text}</p>\n')
        self.fp.flush()

    def plain(self, text):
        '''no p wrapper'''
        self.fp.write(f'{text}\n')
        self.fp.flush()

    def close(self):
        self.fp.write('</body></html>\n')
        self.fp.close()
