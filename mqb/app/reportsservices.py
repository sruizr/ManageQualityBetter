import latex
import jinja2
import os
#import pdb

print(os.getcwd())


class ReportGenerator(object):

    def __init__(self, template_path):
        template_loader = jinja2.FileSystemLoader(searchpath=template_path)
        self.env = jinja2.Environment(loader=template_loader)
        #pdb.set_trace()

    def printToPDF(self, template, variables=None):

        template = self.env.get_template(template)
        self._parsed_tex = template.render(variables)
        pdf = latex.build_pdf(self._parsed_tex)

        return pdf
