import subprocess
import tempfile
import jinja2
import os
import pdb
import io
from shutil import rmtree
import email

ENV_ARGS = {
    'block_start_string': '\BLOCK{',
    'block_end_string': '}',
    'variable_start_string': '\VAR{',
    'variable_end_string': '}',
    'comment_start_string': '\#{',
    'comment_end_string': '}',
    'line_statement_prefix': '%-',
    'line_comment_prefix': '%#',
    'trim_blocks': True,
}


class MailGenerator(object):
    def __init__(self, template_path, working_path=None):
        pass

    def parse_mail(self, template, variables=None):
        pass

    def get_mail(self, mail_content):
        pass


class PdfGenerator(object):

    def __init__(self, template_path, working_path=None):
        template_loader = jinja2.FileSystemLoader(searchpath=template_path)
        ka = ENV_ARGS.copy()
        self.env = jinja2.Environment(loader=template_loader, **ka)
        if working_path:
            self.working_path = working_path
        else:
            self.working_path = template_path
        self.template_path = template_path

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

        pdf_file = open(pdf_filename, 'rb')

        output = io.BytesIO(pdf_file.read())
        pdf_file.close()
        rmtree(temp_dir)

        return output
