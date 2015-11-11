import subprocess
import tempfile
import jinja2
import os
import io
import xml.etree.ElementTree as ET

import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email import encoders
from shutil import rmtree

import pdb


class MailGenerator(object):

    def __init__(self, template_path, working_path=None):
        template_loader = jinja2.FileSystemLoader(searchpath=template_path)
        self.env = jinja2.Environment(loader=template_loader)
        if working_path:
            self.working_path = working_path
        else:
            self.working_path = template_path
        self.template_path = template_path

    def parse_mail(self, template, variables=None):
        template = self.env.get_template(template)
        return template.render(variables)

    def get_mail(self, xml_mail):
        mail = MIMEMultipart()

        # pdb.set_trace()

        root = ET.fromstring(xml_mail)
        for child in root:
            if (child.tag == "from"):
                self._add_address(child.text, "From", mail)
            if (child.tag == "replyTo"):
                self._add_address(child.text, "Reply-to", mail)
            if (child.tag == "to"):
                self._add_address(child.text, "To", mail)
            if (child.tag == "cc"):
                self._add_address(child.text, "cc", mail)
            if (child.tag == "subject"):
                mail["Subject"] = child.text
            if child.tag == "txtBody":
                mail.attach(MIMEText(child.text, 'plain'))
            if child.tag == "htmlBody":
                mail.attach(MIMEText(child.text, 'html'))
            if child.tag == "attachment":
                filename = child.text
                self._attach_file(filename, mail)
        return mail

    def _add_address(self, text, tag, mail):
        mail[tag] = mail[tag] + ";" + text if mail[tag] else text

    def _attach_file(self, filename, mail):
        ctype, encoding = mimetypes.guess_type(filename)
        if ctype is None or encoding is not None:
            # No guess could be made, or the file is encoded (compressed), so
            # use a generic bag-of-bits type.
            ctype = 'application/octet-stream'
        maintype, subtype = ctype.split('/', 1)
        if maintype == 'text':
            with open(filename) as fp:
                # Note: we should handle calculating the charset
                part = MIMEText(fp.read(), _subtype=subtype)
        elif maintype == 'image':
            with open(filename, 'rb') as fp:
                part = MIMEImage(fp.read(), _subtype=subtype)
        elif maintype == 'audio':
            with open(filename, 'rb') as fp:
                part = MIMEAudio(fp.read(), _subtype=subtype)
        else:
            with open(filename, 'rb') as fp:
                part = MIMEBase(maintype, subtype)
                part.set_payload(fp.read())
            # Encode the payload using Base64
            encoders.encode_base64(part)
        # Set the filename parameter
        part.add_header('Content-Disposition', 'attachment', filename=filename)
        mail.attach(part)


class PdfGenerator(object):
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

    def __init__(self, template_path, working_path=None):
        template_loader = jinja2.FileSystemLoader(searchpath=template_path)
        ka = PdfGenerator.ENV_ARGS.copy()
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
