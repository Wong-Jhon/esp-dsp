# -*- coding: utf-8 -*-
#
# English Language RTD & Sphinx config file
#
# Uses IDF_PATH/conf_common.py for most non-language-specific settings.

# Importing conf_common adds all the non-language-specific
# parts to this conf module
import sys, os
# I don't know...
# idf_path = os.getenv("IDF_PATH")
# docs_path=idf_path + '/docs'
# print('Idf path is: {} .'.format(idf_path))
# print('Import module from {} .'.format(docs_path))
#sys.path.insert(0, os.path.abspath(docs_path))
sys.path.insert(0, os.path.abspath('.'))
from conf_common import *

# General information about the project.
project = u'Espressif DSP Library'
copyright = u'2016 - 2018, Espressif Systems (Shanghai) PTE LTD'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'
