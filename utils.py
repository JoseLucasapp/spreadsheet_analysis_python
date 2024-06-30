import subprocess

system_path = r'C:\Users\josel\AppData\Local\Programs\Python\Python311\python.exe -m jupyter nbconvert --to script'
# system_path = 'jupyter nbconvert --to script'


class Utils:
    def autopct_format(self, values):
        def my_format(pct):
            total = sum(values)
            val = int(round(pct*total/100.0))
            return '{v:d}'.format(v=val)
        return my_format

    def convert_file(self):
        self.notebook_path = 'chart_generator.ipynb'
        self.script_path = 'chart_generator.py'
        convert_command = f'{system_path} ./{self.notebook_path}'
        subprocess.run(convert_command, shell=True, check=True)
