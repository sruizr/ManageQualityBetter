import subprocess
import tempfile
import jinja2
import os
import pdb
from shutil import rmtree

print(os.getcwd())


class ReportGenerator(object):

    def __init__(self, template_path, working_path):
        template_loader = jinja2.FileSystemLoader(searchpath=template_path)
        self.env = jinja2.Environment(loader=template_loader)
        self.working_path = working_path
        self.template_path = template_path
        # pdb.set_trace()

    def parse_tex_file(self, template, variables=None):
        template = self.env.get_template(template)
        return template.render(variables)

    def print_to_PDF(self, tex_content):
        temp_dir = tempfile.mkdtemp(dir=self.template_path)

        tex_file = tempfile.TemporaryFile(mode="w+t",
                                          dir=temp_dir, suffix=".tex",
                                          delete=False)
        tex_file.write(tex_content)
        tex_file.close()

        base_filename = os.path.splitext(tex_file.name)[0]
        pdf_filename = base_filename + '.pdf'

        latex_cmd = ['pdflatex',
                     '-interaction=batchmode',
                     '-halt-on-error',
                     '-no-shell-escape',
                     '-file-line-error',
                     '%O',
                     '%S',
                     ]

        latex_cmd = ['latexmk', '-pdf',
                                '-pdflatex={}'.format(' '.join(latex_cmd)),
                                tex_file.name, ]

        # create environment
        newenv = os.environ.copy()
        # newenv['TEXINPUTS'] = os.pathsep.join(texinputs) + os.pathsep

        try:
            subprocess.check_call(
                args=latex_cmd,
                cwd=temp_dir,
                env=newenv,
                stdin=open(os.devnull, 'r'),
                stdout=open(os.devnull, 'w'),
                stderr=open(os.devnull, 'w'),
            )
        except subprocess.CalledProcessError as e:
            print(e)

        # pdb.set_trace()

        yield open(pdf_filename, 'rb')
        rmtree(temp_dir)
