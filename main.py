import sys
import csv
import json
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLabel

class CSVtoJSONConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('CSV to JSON Converter')

        self.upload_button = QPushButton('Upload CSV File', self)
        self.upload_button.clicked.connect(self.upload_and_convert)
        self.upload_button.setGeometry(50, 50, 300, 30)

        self.result_label = QLabel('', self)
        self.result_label.setGeometry(50, 100, 300, 30)

    def upload_and_convert(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        csv_file_path, _ = QFileDialog.getOpenFileName(self, 'Select a CSV File', '', 'CSV Files (*.csv);;All Files (*)', options=options)

        if csv_file_path:
            json_file_path, _ = QFileDialog.getSaveFileName(self, 'Save JSON File', 'Name.json', 'JSON Files (*.json);;All Files (*)', options=options)
            
            if json_file_path:
                convert_csv_to_json(csv_file_path, json_file_path)
                self.result_label.setText('CSV to JSON conversion successful!')

def convert_csv_to_json(csv_file_path, json_file_path):
    data = []
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = CSVtoJSONConverter()
    converter.show()
    sys.exit(app.exec_())
