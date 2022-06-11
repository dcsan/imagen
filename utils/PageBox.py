class PageBox:
    def __init__(self):
        self.path = f'renders/log.html'
        self.fp = open(self.path, "w")
        self.fp.write('<html><body>\n')

    def add(self, text):
        self.fp.write(f'<p>{text}</p>\n')
        self.fp.flush()

    def close(self):
        self.fp.write('</body></html>\n')
        self.fp.close()
