import base64
import io

import pandas


class FileParser:
    def __init__(self, contents, filename):
        self.contents = contents
        self.content_type, self.content_string = self.contents.split(",")
        self.filename = filename

    def csv(self):
        return pandas.read_csv(
            io.StringIO(base64.b64decode(self.content_string).decode("utf-8"))
        )

    def xls(self):
        return pandas.read_excel(io.BytesIO(base64.b64decode(self.content_string)))

    def execute(self):
        if "csv" in self.filename:
            return self.csv()
        if "xls" in self.filename:
            return self.xls()
