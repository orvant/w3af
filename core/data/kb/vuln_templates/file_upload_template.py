'''
file_upload_template.py

Copyright 2013 Andres Riancho

This file is part of w3af, http://w3af.org/ .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

'''
from core.data.kb.vuln_templates.base_template import BaseTemplate
from core.data.options.opt_factory import opt_factory
from core.data.parsers.url import URL


class FileUploadTemplate(BaseTemplate):
    '''
    Vulnerability template for arbitrary file upload vulnerability.
    '''
    def __init__(self):
        super(FileUploadTemplate, self).__init__()
        
        self.name = self.get_vulnerability_name()
        self.file_vars = []
        self.file_dest = URL('http://host.tld/uploads/file.ext')
        self.method = 'POST'
    
    def get_options(self):
        opt_lst = super(FileUploadTemplate, self).get_options()
        
        d = 'Comma separated list of variable names of type "file"'
        o = opt_factory('file_vars', self.file_vars, d, 'list')
        opt_lst.add(o)

        d = 'URL for the directory where the file is stored on the remote'\
            ' server after the POST that uploads it.'
        o = opt_factory('file_dest', self.file_dest, d, 'url')
        opt_lst.add(o)

        return opt_lst
    
    def set_options(self, options_list):
        super(FileUploadTemplate, self).set_options(options_list)
        self.file_vars = options_list['file_vars'].get_value()
        self.file_dest = options_list['file_dest'].get_value()
    
    def create_vuln(self):
        v = super(FileUploadTemplate, self).create_vuln()

        # User configured
        v['file_vars'] = self.file_vars
        v['file_dest'] = self.file_dest

        return v
    
    def get_kb_location(self):
        '''
        :return: A tuple with the location where the vulnerability will be saved,
                 example return value would be: ('eval', 'eval')
        '''
        return ('file_upload', 'file_upload')

    def get_vulnerability_name(self):
        '''
        :return: A string containing the name of the vulnerability to be added
                 to the KB, example: 'SQL Injection'. This is just a descriptive
                 string which can contain any information, not used for any
                 strict matching of vulns before exploiting.
        '''
        return 'Arbitrary file upload'

    def get_vulnerability_desc(self):
        return 'Code execution through arbitrary file upload vulnerability'
