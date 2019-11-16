#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Sat Nov 16 11:55:38 2019 by generateDS.py version 2.34.1.
# Python 2.7.16 (default, Oct  7 2019, 17:36:04)  [GCC 8.3.0]
#
# Command line options:
#   ('-f', '')
#   ('-o', 'schema_v16_py2.py')
#   ('--use-getter-setter', 'none')
#   ('--export', 'write literal etree sqlalchemy')
#
# Command line arguments:
#   ../data/darwin/schema/rttiPPTSchema_v16.xsd
#
# Command line:
#   /usr/local/bin/generateDS -f -o "schema_v16_py2.py" --use-getter-setter="none" --export="write literal etree sqlalchemy" ../data/darwin/schema/rttiPPTSchema_v16.xsd
#
# Current working directory (os.getcwd()):
#   code
#

import os
import sys
import re as re_
import base64
# imports for django and/or sqlalchemy
import json as json_
try:
    import models_sqa as models_sqa_
except ImportError:
    models_sqa_ = None
import datetime as datetime_
import decimal as decimal_
try:
    from lxml import etree as etree_
except ImportError:
    from xml.etree import ElementTree as etree_


Validate_simpletypes_ = True
SaveElementTreeNode = True
if sys.version_info.major == 2:
    BaseStrType_ = str
else:
    BaseStrType_ = str


def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    try:
        if isinstance(infile, os.PathLike):
            infile = os.path.join(infile)
    except AttributeError:
        pass
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

def parsexmlstring_(instring, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        try:
            parser = etree_.ETCompatXMLParser()
        except AttributeError:
            # fallback to xml.etree
            parser = etree_.XMLParser()
    element = etree_.fromstring(instring, parser=parser, **kwargs)
    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }
#

try:
    from generatedsnamespaces import GenerateDSNamespaceDefs as GenerateDSNamespaceDefs_
except ImportError:
    GenerateDSNamespaceDefs_ = {}
try:
    from generatedsnamespaces import GenerateDSNamespaceTypePrefixes as GenerateDSNamespaceTypePrefixes_
except ImportError:
    GenerateDSNamespaceTypePrefixes_ = {}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from generatedscollector import GdsCollector as GdsCollector_
except ImportError:

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print(("Warning: {}".format(msg)))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {}\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ImportError:
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError as exp:
    
    class GeneratedsSuper(object):
        __hash__ = object.__hash__
        tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
        class _FixedOffsetTZ(datetime_.tzinfo):
            def __init__(self, offset, name):
                self.__offset = datetime_.timedelta(minutes=offset)
                self.__name = name
            def utcoffset(self, dt):
                return self.__offset
            def tzname(self, dt):
                return self.__name
            def dst(self, dt):
                return None
        def gds_format_string(self, input_data, input_name=''):
            return input_data
        def gds_parse_string(self, input_data, node=None, input_name=''):
            return input_data
        def gds_validate_string(self, input_data, node=None, input_name=''):
            if not input_data:
                return ''
            else:
                return input_data
        def gds_format_base64(self, input_data, input_name=''):
            return base64.b64encode(input_data)
        def gds_validate_base64(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_integer(self, input_data, input_name=''):
            return '%d' % input_data
        def gds_parse_integer(self, input_data, node=None, input_name=''):
            try:
                ival = int(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires integer value: %s' % exp)
            return ival
        def gds_validate_integer(self, input_data, node=None, input_name=''):
            try:
                value = int(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires integer value')
            return value
        def gds_format_integer_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_integer_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    int(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of integer valuess')
            return values
        def gds_format_float(self, input_data, input_name=''):
            return ('%.15f' % input_data).rstrip('0')
        def gds_parse_float(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires float or double value: %s' % exp)
            return fval_
        def gds_validate_float(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires float value')
            return value
        def gds_format_float_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_float_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of float values')
            return values
        def gds_format_decimal(self, input_data, input_name=''):
            return ('%0.10f' % input_data).rstrip('0')
        def gds_parse_decimal(self, input_data, node=None, input_name=''):
            try:
                decimal_value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return decimal_value
        def gds_validate_decimal(self, input_data, node=None, input_name=''):
            try:
                value = decimal_.Decimal(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires decimal value')
            return value
        def gds_format_decimal_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_decimal_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    decimal_.Decimal(value)
                except (TypeError, ValueError):
                    raise_parse_error(node, 'Requires sequence of decimal values')
            return values
        def gds_format_double(self, input_data, input_name=''):
            return '%e' % input_data
        def gds_parse_double(self, input_data, node=None, input_name=''):
            try:
                fval_ = float(input_data)
            except (TypeError, ValueError) as exp:
                raise_parse_error(node, 'Requires double or float value: %s' % exp)
            return fval_
        def gds_validate_double(self, input_data, node=None, input_name=''):
            try:
                value = float(input_data)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires double or float value')
            return value
        def gds_format_double_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_double_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                try:
                    float(value)
                except (TypeError, ValueError):
                    raise_parse_error(
                        node, 'Requires sequence of double or float values')
            return values
        def gds_format_boolean(self, input_data, input_name=''):
            return ('%s' % input_data).lower()
        def gds_parse_boolean(self, input_data, node=None, input_name=''):
            if input_data in ('true', '1'):
                bval = True
            elif input_data in ('false', '0'):
                bval = False
            else:
                raise_parse_error(node, 'Requires boolean value')
            return bval
        def gds_validate_boolean(self, input_data, node=None, input_name=''):
            if input_data not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires boolean value '
                    '(one of True, 1, False, 0)')
            return input_data
        def gds_format_boolean_list(self, input_data, input_name=''):
            return '%s' % ' '.join(input_data)
        def gds_validate_boolean_list(
                self, input_data, node=None, input_name=''):
            values = input_data.split()
            for value in values:
                if value not in (True, 1, False, 0, ):
                    raise_parse_error(
                        node,
                        'Requires sequence of boolean values '
                        '(one of True, 1, False, 0)')
            return values
        def gds_validate_datetime(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_datetime(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                    input_data.year,
                    input_data.month,
                    input_data.day,
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        @classmethod
        def gds_parse_datetime(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            time_parts = input_data.split('.')
            if len(time_parts) > 1:
                micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
                input_data = '%s.%s' % (
                    time_parts[0], "{}".format(micro_seconds).rjust(6, "0"), )
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt
        def gds_validate_date(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_date(self, input_data, input_name=''):
            _svalue = '%04d-%02d-%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
            )
            try:
                if input_data.tzinfo is not None:
                    tzoff = input_data.tzinfo.utcoffset(input_data)
                    if tzoff is not None:
                        total_seconds = tzoff.seconds + (86400 * tzoff.days)
                        if total_seconds == 0:
                            _svalue += 'Z'
                        else:
                            if total_seconds < 0:
                                _svalue += '-'
                                total_seconds *= -1
                            else:
                                _svalue += '+'
                            hours = total_seconds // 3600
                            minutes = (total_seconds - (hours * 3600)) // 60
                            _svalue += '{0:02d}:{1:02d}'.format(
                                hours, minutes)
            except AttributeError:
                pass
            return _svalue
        @classmethod
        def gds_parse_date(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
            dt = dt.replace(tzinfo=tz)
            return dt.date()
        def gds_validate_time(self, input_data, node=None, input_name=''):
            return input_data
        def gds_format_time(self, input_data, input_name=''):
            if input_data.microsecond == 0:
                _svalue = '%02d:%02d:%02d' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                )
            else:
                _svalue = '%02d:%02d:%02d.%s' % (
                    input_data.hour,
                    input_data.minute,
                    input_data.second,
                    ('%f' % (float(input_data.microsecond) / 1000000))[2:],
                )
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
            return _svalue
        def gds_validate_simple_patterns(self, patterns, target):
            # pat is a list of lists of strings/patterns.
            # The target value must match at least one of the patterns
            # in order for the test to succeed.
            found1 = True
            for patterns1 in patterns:
                found2 = False
                for patterns2 in patterns1:
                    mo = re_.search(patterns2, target)
                    if mo is not None and len(mo.group(0)) == len(target):
                        found2 = True
                        break
                if not found2:
                    found1 = False
                    break
            return found1
        @classmethod
        def gds_parse_time(cls, input_data):
            tz = None
            if input_data[-1] == 'Z':
                tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
                input_data = input_data[:-1]
            else:
                results = GeneratedsSuper.tzoff_pattern.search(input_data)
                if results is not None:
                    tzoff_parts = results.group(2).split(':')
                    tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                    if results.group(1) == '-':
                        tzoff *= -1
                    tz = GeneratedsSuper._FixedOffsetTZ(
                        tzoff, results.group(0))
                    input_data = input_data[:-6]
            if len(input_data.split('.')) > 1:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
            else:
                dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
            dt = dt.replace(tzinfo=tz)
            return dt.time()
        def gds_check_cardinality_(
                self, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if min_occurs is not None:
                if min_occurs > 0:
                    if (value is None or
                            (isinstance(value, list) and len(value) < min_occurs)):
                        self.gds_collector_.add_message(
                            "Required value {}{} is missing".format(
                                input_name, self.gds_get_node_lineno_()))
            if max_occurs is not None:
                if max_occurs < 9999999:
                    if (value is None or
                            (isinstance(value, list) and len(value) > max_occurs)):
                        self.gds_collector_.add_message(
                            "Required values {}{} are missing".format(
                                input_name, self.gds_get_node_lineno_()))
            if required is not None:
                if required:
                    if value is None:
                        self.gds_collector_.add_message(
                            "Required value {}{} is missing".format(
                                input_name, self.gds_get_node_lineno_()))
        def gds_validate_builtin_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value, input_name=input_name)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_validate_defined_ST_(
                self, validator, value, input_name,
                min_occurs=None, max_occurs=None, required=None):
            if value is not None:
                try:
                    validator(value)
                except GDSParseError as parse_error:
                    self.gds_collector_.add_message(str(parse_error))
        def gds_str_lower(self, instring):
            return instring.lower()
        def get_path_(self, node):
            path_list = []
            self.get_path_list_(node, path_list)
            path_list.reverse()
            path = '/'.join(path_list)
            return path
        Tag_strip_pattern_ = re_.compile(r'\{.*\}')
        def get_path_list_(self, node, path_list):
            if node is None:
                return
            tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
            if tag:
                path_list.append(tag)
            self.get_path_list_(node.getparent(), path_list)
        def get_class_obj_(self, node, default_class=None):
            class_obj1 = default_class
            if 'xsi' in node.nsmap:
                classname = node.get('{%s}type' % node.nsmap['xsi'])
                if classname is not None:
                    names = classname.split(':')
                    if len(names) == 2:
                        classname = names[1]
                    class_obj2 = globals().get(classname)
                    if class_obj2 is not None:
                        class_obj1 = class_obj2
            return class_obj1
        def gds_build_any(self, node, type_name=None):
            # provide default value in case option --disable-xml is used.
            content = ""
            content = etree_.tostring(node, encoding="unicode")
            return content
        @classmethod
        def gds_reverse_node_mapping(cls, mapping):
            return dict(((v, k) for k, v in list(mapping.items())))
        @staticmethod
        def gds_encode(instring):
            if sys.version_info.major == 2:
                if ExternalEncoding:
                    encoding = ExternalEncoding
                else:
                    encoding = 'utf-8'
                return instring.encode(encoding)
            else:
                return instring
        @staticmethod
        def convert_unicode(instring):
            if isinstance(instring, str):
                result = quote_xml(instring)
            elif sys.version_info.major == 2 and isinstance(instring, str):
                result = quote_xml(instring).encode('utf8')
            else:
                result = GeneratedsSuper.gds_encode(str(instring))
            return result
        def __eq__(self, other):
            def excl_select_objs_(obj):
                return (obj[0] != 'parent_object_' and
                        obj[0] != 'gds_collector_')
            if type(self) != type(other):
                return False
            return list(
                filter(excl_select_objs_, list(self.__dict__.items()))
            ) == list(
                filter(excl_select_objs_, list(other.__dict__.items())))
        def __ne__(self, other):
            return not self.__eq__(other)
        # Django ETL transform hooks.
        def gds_djo_etl_transform(self):
            pass
        def gds_djo_etl_transform_db_obj(self, dbobj):
            pass
        # SQLAlchemy ETL transform hooks.
        def gds_sqa_etl_transform(self):
            return 0, None
        def gds_sqa_etl_transform_db_obj(self, dbobj):
            pass
        def gds_get_node_lineno_(self):
            if (hasattr(self, "gds_elementtree_node_") and
                    self.gds_elementtree_node_ is not None):
                return ' near line {}'.format(
                    self.gds_elementtree_node_.sourceline)
            else:
                return ""
    
    
    def getSubclassFromModule_(module, class_):
        '''Get the subclass of a class from a specific module.'''
        name = class_.__name__ + 'Sub'
        if hasattr(module, name):
            return getattr(module, name)
        else:
            return None


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = ''
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {}
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')
CDATA_pattern_ = re_.compile(r"<!\[CDATA\[.*?\]\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None

#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, outfile, level, name, namespace,
               pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(
                outfile, level, namespace, name_=name,
                pretty_print=pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' % (
                self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' % (
                self.name,
                base64.b64encode(self.value),
                self.name))
    def to_etree(self, element):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(
                element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s", "%s"),\n' % (
                    self.category, self.content_type,
                    self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write(
                'model_.MixedContainer(%d, %d, "%s",\n' % (
                    self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#


class AlertAudienceType(Enum):
    """Alert Audience Data Type"""
    CUSTOMER='Customer'
    STAFF='Staff'
    OPERATIONS='Operations'


class AlertType(Enum):
    """Alert Type Data Type"""
    NORMAL='Normal'
    FORCED='Forced'


class CategoryType(Enum):
    """Association Category Type: JJ=Join, VV=Split, LK=Linked, NP=Next-
    Working"""
    JJ='JJ'
    VV='VV'
    LK='LK'
    NP='NP'


class MsgCategoryType(Enum):
    """The category of operator message"""
    TRAIN='Train'
    STATION='Station'
    CONNECTIONS='Connections'
    SYSTEM='System'
    MISC='Misc'
    PRIOR_TRAINS='PriorTrains'
    PRIOR_OTHER='PriorOther'


class MsgSeverityType(Enum):
    """The severity of operator message"""
    _0='0'
    _1='1'
    _2='2'
    _3='3'


class ToiletStatus(Enum):
    """The service status of a toilet in coach formation data."""
    UNKNOWN='Unknown'
    IN_SERVICE='InService'
    NOT_IN_SERVICE='NotInService'


class DataResponse(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, schedule=None, deactivated=None, association=None, scheduleFormations=None, TS=None, formationLoading=None, OW=None, trainAlert=None, trainOrder=None, trackingID=None, alarm=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if schedule is None:
            self.schedule = []
        else:
            self.schedule = schedule
        self.schedule_nsprefix_ = None
        if deactivated is None:
            self.deactivated = []
        else:
            self.deactivated = deactivated
        self.deactivated_nsprefix_ = None
        if association is None:
            self.association = []
        else:
            self.association = association
        self.association_nsprefix_ = None
        if scheduleFormations is None:
            self.scheduleFormations = []
        else:
            self.scheduleFormations = scheduleFormations
        self.scheduleFormations_nsprefix_ = None
        if TS is None:
            self.TS = []
        else:
            self.TS = TS
        self.TS_nsprefix_ = None
        if formationLoading is None:
            self.formationLoading = []
        else:
            self.formationLoading = formationLoading
        self.formationLoading_nsprefix_ = None
        if OW is None:
            self.OW = []
        else:
            self.OW = OW
        self.OW_nsprefix_ = None
        if trainAlert is None:
            self.trainAlert = []
        else:
            self.trainAlert = trainAlert
        self.trainAlert_nsprefix_ = None
        if trainOrder is None:
            self.trainOrder = []
        else:
            self.trainOrder = trainOrder
        self.trainOrder_nsprefix_ = None
        if trackingID is None:
            self.trackingID = []
        else:
            self.trackingID = trackingID
        self.trackingID_nsprefix_ = None
        if alarm is None:
            self.alarm = []
        else:
            self.alarm = alarm
        self.alarm_nsprefix_ = None
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DataResponse)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DataResponse.subclass:
            return DataResponse.subclass(*args_, **kwargs_)
        else:
            return DataResponse(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.schedule or
            self.deactivated or
            self.association or
            self.scheduleFormations or
            self.TS or
            self.formationLoading or
            self.OW or
            self.trainAlert or
            self.trainOrder or
            self.trackingID or
            self.alarm
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1"  xmlns:sch2="http://www.thalesgroup.com/rtti/PushPort/Schedules/v2"  xmlns:for="http://www.thalesgroup.com/rtti/PushPort/Forecasts/v3"  xmlns:fm="http://www.thalesgroup.com/rtti/PushPort/Formations/v1"  xmlns:sm="http://www.thalesgroup.com/rtti/PushPort/StationMessages/v1"  xmlns:ta="http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1"  xmlns:tor="http://www.thalesgroup.com/rtti/PushPort/TrainOrder/v1"  xmlns:td="http://www.thalesgroup.com/rtti/PushPort/TDData/v1"  xmlns:alm="http://www.thalesgroup.com/rtti/PushPort/Alarms/v1" ', name_='DataResponse', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DataResponse')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DataResponse')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DataResponse', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DataResponse'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1"  xmlns:sch2="http://www.thalesgroup.com/rtti/PushPort/Schedules/v2"  xmlns:for="http://www.thalesgroup.com/rtti/PushPort/Forecasts/v3"  xmlns:fm="http://www.thalesgroup.com/rtti/PushPort/Formations/v1"  xmlns:sm="http://www.thalesgroup.com/rtti/PushPort/StationMessages/v1"  xmlns:ta="http://www.thalesgroup.com/rtti/PushPort/TrainAlerts/v1"  xmlns:tor="http://www.thalesgroup.com/rtti/PushPort/TrainOrder/v1"  xmlns:td="http://www.thalesgroup.com/rtti/PushPort/TDData/v1"  xmlns:alm="http://www.thalesgroup.com/rtti/PushPort/Alarms/v1" ', name_='DataResponse', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for schedule_ in self.schedule:
            namespaceprefix_ = self.schedule_nsprefix_ + ':' if (UseCapturedNS_ and self.schedule_nsprefix_) else ''
            schedule_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='schedule', pretty_print=pretty_print)
        for deactivated_ in self.deactivated:
            namespaceprefix_ = self.deactivated_nsprefix_ + ':' if (UseCapturedNS_ and self.deactivated_nsprefix_) else ''
            deactivated_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='deactivated', pretty_print=pretty_print)
        for association_ in self.association:
            namespaceprefix_ = self.association_nsprefix_ + ':' if (UseCapturedNS_ and self.association_nsprefix_) else ''
            association_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='association', pretty_print=pretty_print)
        for scheduleFormations_ in self.scheduleFormations:
            namespaceprefix_ = self.scheduleFormations_nsprefix_ + ':' if (UseCapturedNS_ and self.scheduleFormations_nsprefix_) else ''
            scheduleFormations_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='scheduleFormations', pretty_print=pretty_print)
        for TS_ in self.TS:
            namespaceprefix_ = self.TS_nsprefix_ + ':' if (UseCapturedNS_ and self.TS_nsprefix_) else ''
            TS_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TS', pretty_print=pretty_print)
        for formationLoading_ in self.formationLoading:
            namespaceprefix_ = self.formationLoading_nsprefix_ + ':' if (UseCapturedNS_ and self.formationLoading_nsprefix_) else ''
            formationLoading_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='formationLoading', pretty_print=pretty_print)
        for OW_ in self.OW:
            namespaceprefix_ = self.OW_nsprefix_ + ':' if (UseCapturedNS_ and self.OW_nsprefix_) else ''
            OW_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OW', pretty_print=pretty_print)
        for trainAlert_ in self.trainAlert:
            namespaceprefix_ = self.trainAlert_nsprefix_ + ':' if (UseCapturedNS_ and self.trainAlert_nsprefix_) else ''
            trainAlert_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='trainAlert', pretty_print=pretty_print)
        for trainOrder_ in self.trainOrder:
            namespaceprefix_ = self.trainOrder_nsprefix_ + ':' if (UseCapturedNS_ and self.trainOrder_nsprefix_) else ''
            trainOrder_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='trainOrder', pretty_print=pretty_print)
        for trackingID_ in self.trackingID:
            namespaceprefix_ = self.trackingID_nsprefix_ + ':' if (UseCapturedNS_ and self.trackingID_nsprefix_) else ''
            trackingID_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='trackingID', pretty_print=pretty_print)
        for alarm_ in self.alarm:
            namespaceprefix_ = self.alarm_nsprefix_ + ':' if (UseCapturedNS_ and self.alarm_nsprefix_) else ''
            alarm_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='alarm', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='DataResponse', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        for schedule_ in self.schedule:
            schedule_.to_etree(element, name_='schedule', mapping_=mapping_)
        for deactivated_ in self.deactivated:
            deactivated_.to_etree(element, name_='deactivated', mapping_=mapping_)
        for association_ in self.association:
            association_.to_etree(element, name_='association', mapping_=mapping_)
        for scheduleFormations_ in self.scheduleFormations:
            scheduleFormations_.to_etree(element, name_='scheduleFormations', mapping_=mapping_)
        for TS_ in self.TS:
            TS_.to_etree(element, name_='TS', mapping_=mapping_)
        for formationLoading_ in self.formationLoading:
            formationLoading_.to_etree(element, name_='formationLoading', mapping_=mapping_)
        for OW_ in self.OW:
            OW_.to_etree(element, name_='OW', mapping_=mapping_)
        for trainAlert_ in self.trainAlert:
            trainAlert_.to_etree(element, name_='trainAlert', mapping_=mapping_)
        for trainOrder_ in self.trainOrder:
            trainOrder_.to_etree(element, name_='trainOrder', mapping_=mapping_)
        for trackingID_ in self.trackingID:
            trackingID_.to_etree(element, name_='trackingID', mapping_=mapping_)
        for alarm_ in self.alarm:
            alarm_.to_etree(element, name_='alarm', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='DataResponse'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('schedule=[\n')
        level += 1
        for schedule_ in self.schedule:
            showIndent(outfile, level)
            outfile.write('model_.Schedule8(\n')
            schedule_.exportLiteral(outfile, level, name_='Schedule8')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('deactivated=[\n')
        level += 1
        for deactivated_ in self.deactivated:
            showIndent(outfile, level)
            outfile.write('model_.DeactivatedSchedule(\n')
            deactivated_.exportLiteral(outfile, level, name_='DeactivatedSchedule')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('association=[\n')
        level += 1
        for association_ in self.association:
            showIndent(outfile, level)
            outfile.write('model_.Association(\n')
            association_.exportLiteral(outfile, level, name_='Association')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('scheduleFormations=[\n')
        level += 1
        for scheduleFormations_ in self.scheduleFormations:
            showIndent(outfile, level)
            outfile.write('model_.ScheduleFormations9(\n')
            scheduleFormations_.exportLiteral(outfile, level, name_='ScheduleFormations9')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('TS=[\n')
        level += 1
        for TS_ in self.TS:
            showIndent(outfile, level)
            outfile.write('model_.TS(\n')
            TS_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('formationLoading=[\n')
        level += 1
        for formationLoading_ in self.formationLoading:
            showIndent(outfile, level)
            outfile.write('model_.Loading(\n')
            formationLoading_.exportLiteral(outfile, level, name_='Loading')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('OW=[\n')
        level += 1
        for OW_ in self.OW:
            showIndent(outfile, level)
            outfile.write('model_.StationMessage(\n')
            OW_.exportLiteral(outfile, level, name_='StationMessage')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('trainAlert=[\n')
        level += 1
        for trainAlert_ in self.trainAlert:
            showIndent(outfile, level)
            outfile.write('model_.TrainAlert(\n')
            trainAlert_.exportLiteral(outfile, level, name_='TrainAlert')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('trainOrder=[\n')
        level += 1
        for trainOrder_ in self.trainOrder:
            showIndent(outfile, level)
            outfile.write('model_.TrainOrder(\n')
            trainOrder_.exportLiteral(outfile, level, name_='TrainOrder')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('trackingID=[\n')
        level += 1
        for trackingID_ in self.trackingID:
            showIndent(outfile, level)
            outfile.write('model_.TrackingID(\n')
            trackingID_.exportLiteral(outfile, level, name_='TrackingID')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('alarm=[\n')
        level += 1
        for alarm_ in self.alarm:
            showIndent(outfile, level)
            outfile.write('model_.RTTIAlarm(\n')
            alarm_.exportLiteral(outfile, level, name_='RTTIAlarm')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.DataResponse_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        for child in self.schedule:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.schedule.append(child_dbobj)
        for child in self.deactivated:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.deactivated.append(child_dbobj)
        for child in self.association:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.association.append(child_dbobj)
        for child in self.scheduleFormations:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.scheduleFormations.append(child_dbobj)
        for child in self.TS:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.TS.append(child_dbobj)
        for child in self.formationLoading:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.formationLoading.append(child_dbobj)
        for child in self.OW:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.OW.append(child_dbobj)
        for child in self.trainAlert:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.trainAlert.append(child_dbobj)
        for child in self.trainOrder:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.trainOrder.append(child_dbobj)
        for child in self.trackingID:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.trackingID.append(child_dbobj)
        for child in self.alarm:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.alarm.append(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'schedule':
            obj_ = Schedule8.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.schedule.append(obj_)
            obj_.original_tagname_ = 'schedule'
        elif nodeName_ == 'deactivated':
            obj_ = DeactivatedSchedule.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.deactivated.append(obj_)
            obj_.original_tagname_ = 'deactivated'
        elif nodeName_ == 'association':
            obj_ = Association.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.association.append(obj_)
            obj_.original_tagname_ = 'association'
        elif nodeName_ == 'scheduleFormations':
            obj_ = ScheduleFormations9.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.scheduleFormations.append(obj_)
            obj_.original_tagname_ = 'scheduleFormations'
        elif nodeName_ == 'TS':
            obj_ = TS.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TS.append(obj_)
            obj_.original_tagname_ = 'TS'
        elif nodeName_ == 'formationLoading':
            obj_ = Loading.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.formationLoading.append(obj_)
            obj_.original_tagname_ = 'formationLoading'
        elif nodeName_ == 'OW':
            obj_ = StationMessage.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OW.append(obj_)
            obj_.original_tagname_ = 'OW'
        elif nodeName_ == 'trainAlert':
            obj_ = TrainAlert.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.trainAlert.append(obj_)
            obj_.original_tagname_ = 'trainAlert'
        elif nodeName_ == 'trainOrder':
            obj_ = TrainOrder.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.trainOrder.append(obj_)
            obj_.original_tagname_ = 'trainOrder'
        elif nodeName_ == 'trackingID':
            obj_ = TrackingID.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.trackingID.append(obj_)
            obj_.original_tagname_ = 'trackingID'
        elif nodeName_ == 'alarm':
            obj_ = RTTIAlarm.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.alarm.append(obj_)
            obj_.original_tagname_ = 'alarm'
# end class DataResponse


class Pport(GeneratedsSuper):
    """Push Ports SchemaLocal Timestamp"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ts=None, version=None, QueryTimetable=None, TimeTableId=None, GetSnapshotReq=None, GetFullSnapshotReq=None, SnapshotId=None, StartUpdateReq=None, StopUpdateReq=None, FailureResp=None, uR=None, sR=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ts = _cast(None, ts)
        self.ts_nsprefix_ = None
        self.version = _cast(None, version)
        self.version_nsprefix_ = None
        self.QueryTimetable = QueryTimetable
        self.QueryTimetable_nsprefix_ = None
        self.TimeTableId = TimeTableId
        self.TimeTableId_nsprefix_ = None
        self.GetSnapshotReq = GetSnapshotReq
        self.GetSnapshotReq_nsprefix_ = None
        self.GetFullSnapshotReq = GetFullSnapshotReq
        self.GetFullSnapshotReq_nsprefix_ = None
        self.SnapshotId = SnapshotId
        self.validate_SnapshotIDType(self.SnapshotId)
        self.SnapshotId_nsprefix_ = None
        self.StartUpdateReq = StartUpdateReq
        self.StartUpdateReq_nsprefix_ = None
        self.StopUpdateReq = StopUpdateReq
        self.StopUpdateReq_nsprefix_ = None
        self.FailureResp = FailureResp
        self.FailureResp_nsprefix_ = None
        self.uR = uR
        self.uR_nsprefix_ = None
        self.sR = sR
        self.sR_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Pport)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Pport.subclass:
            return Pport.subclass(*args_, **kwargs_)
        else:
            return Pport(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_SnapshotIDType(self, value):
        result = True
        # Validate type SnapshotIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 40:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on SnapshotIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_RTTIDateTimeType(self, value):
        # Validate type ct:RTTIDateTimeType, a restriction on xs:dateTime.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, datetime_.datetime):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (datetime_.datetime)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def hasContent_(self):
        if (
            self.QueryTimetable is not None or
            self.TimeTableId is not None or
            self.GetSnapshotReq is not None or
            self.GetFullSnapshotReq is not None or
            self.SnapshotId is not None or
            self.StartUpdateReq is not None or
            self.StopUpdateReq is not None or
            self.FailureResp is not None or
            self.uR is not None or
            self.sR is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1"  xmlns:ct="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='Pport', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Pport')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Pport')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Pport', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='Pport'):
        if 'ts' not in already_processed:
            already_processed.add('ts')
            outfile.write(' ts=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ts), input_name='ts')), ))
        if 'version' not in already_processed:
            already_processed.add('version')
            outfile.write(' version=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.version), input_name='version')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1"  xmlns:ct="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='Pport', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.QueryTimetable is not None:
            namespaceprefix_ = self.QueryTimetable_nsprefix_ + ':' if (UseCapturedNS_ and self.QueryTimetable_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sQueryTimetable>%s</%sQueryTimetable>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.QueryTimetable), input_name='QueryTimetable')), namespaceprefix_ , eol_))
        if self.TimeTableId is not None:
            namespaceprefix_ = self.TimeTableId_nsprefix_ + ':' if (UseCapturedNS_ and self.TimeTableId_nsprefix_) else ''
            self.TimeTableId.export(outfile, level, namespaceprefix_, namespacedef_='', name_='TimeTableId', pretty_print=pretty_print)
        if self.GetSnapshotReq is not None:
            namespaceprefix_ = self.GetSnapshotReq_nsprefix_ + ':' if (UseCapturedNS_ and self.GetSnapshotReq_nsprefix_) else ''
            self.GetSnapshotReq.export(outfile, level, namespaceprefix_, namespacedef_='', name_='GetSnapshotReq', pretty_print=pretty_print)
        if self.GetFullSnapshotReq is not None:
            namespaceprefix_ = self.GetFullSnapshotReq_nsprefix_ + ':' if (UseCapturedNS_ and self.GetFullSnapshotReq_nsprefix_) else ''
            self.GetFullSnapshotReq.export(outfile, level, namespaceprefix_, namespacedef_='', name_='GetFullSnapshotReq', pretty_print=pretty_print)
        if self.SnapshotId is not None:
            namespaceprefix_ = self.SnapshotId_nsprefix_ + ':' if (UseCapturedNS_ and self.SnapshotId_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSnapshotId>%s</%sSnapshotId>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.SnapshotId), input_name='SnapshotId')), namespaceprefix_ , eol_))
        if self.StartUpdateReq is not None:
            namespaceprefix_ = self.StartUpdateReq_nsprefix_ + ':' if (UseCapturedNS_ and self.StartUpdateReq_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sStartUpdateReq>%s</%sStartUpdateReq>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.StartUpdateReq), input_name='StartUpdateReq')), namespaceprefix_ , eol_))
        if self.StopUpdateReq is not None:
            namespaceprefix_ = self.StopUpdateReq_nsprefix_ + ':' if (UseCapturedNS_ and self.StopUpdateReq_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sStopUpdateReq>%s</%sStopUpdateReq>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.StopUpdateReq), input_name='StopUpdateReq')), namespaceprefix_ , eol_))
        if self.FailureResp is not None:
            namespaceprefix_ = self.FailureResp_nsprefix_ + ':' if (UseCapturedNS_ and self.FailureResp_nsprefix_) else ''
            self.FailureResp.export(outfile, level, namespaceprefix_, namespacedef_='', name_='FailureResp', pretty_print=pretty_print)
        if self.uR is not None:
            namespaceprefix_ = self.uR_nsprefix_ + ':' if (UseCapturedNS_ and self.uR_nsprefix_) else ''
            self.uR.export(outfile, level, namespaceprefix_, namespacedef_='', name_='uR', pretty_print=pretty_print)
        if self.sR is not None:
            namespaceprefix_ = self.sR_nsprefix_ + ':' if (UseCapturedNS_ and self.sR_nsprefix_) else ''
            self.sR.export(outfile, level, namespaceprefix_, namespacedef_='', name_='sR', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Pport', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.ts is not None:
            element.set('ts', self.gds_format_datetime(self.ts))
        if self.version is not None:
            element.set('version', self.gds_format_string(self.version))
        if self.QueryTimetable is not None:
            QueryTimetable_ = self.QueryTimetable
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}QueryTimetable').text = self.gds_format_string(QueryTimetable_)
        if self.TimeTableId is not None:
            TimeTableId_ = self.TimeTableId
            TimeTableId_.to_etree(element, name_='TimeTableId', mapping_=mapping_)
        if self.GetSnapshotReq is not None:
            GetSnapshotReq_ = self.GetSnapshotReq
            GetSnapshotReq_.to_etree(element, name_='GetSnapshotReq', mapping_=mapping_)
        if self.GetFullSnapshotReq is not None:
            GetFullSnapshotReq_ = self.GetFullSnapshotReq
            GetFullSnapshotReq_.to_etree(element, name_='GetFullSnapshotReq', mapping_=mapping_)
        if self.SnapshotId is not None:
            SnapshotId_ = self.SnapshotId
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}SnapshotId').text = self.gds_format_string(SnapshotId_)
        if self.StartUpdateReq is not None:
            StartUpdateReq_ = self.StartUpdateReq
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}StartUpdateReq').text = self.gds_format_string(StartUpdateReq_)
        if self.StopUpdateReq is not None:
            StopUpdateReq_ = self.StopUpdateReq
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}StopUpdateReq').text = self.gds_format_string(StopUpdateReq_)
        if self.FailureResp is not None:
            FailureResp_ = self.FailureResp
            FailureResp_.to_etree(element, name_='FailureResp', mapping_=mapping_)
        if self.uR is not None:
            uR_ = self.uR
            uR_.to_etree(element, name_='uR', mapping_=mapping_)
        if self.sR is not None:
            sR_ = self.sR
            sR_.to_etree(element, name_='sR', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='Pport'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.ts is not None and 'ts' not in already_processed:
            already_processed.add('ts')
            showIndent(outfile, level)
            outfile.write('ts=%s,\n' % (self.ts,))
        if self.version is not None and 'version' not in already_processed:
            already_processed.add('version')
            showIndent(outfile, level)
            outfile.write('version="%s",\n' % (self.version,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.QueryTimetable is not None:
            showIndent(outfile, level)
            outfile.write('QueryTimetable=%s,\n' % self.gds_encode(quote_python(self.QueryTimetable)))
        if self.TimeTableId is not None:
            showIndent(outfile, level)
            outfile.write('TimeTableId=model_.TimeTableIdType(\n')
            self.TimeTableId.exportLiteral(outfile, level, name_='TimeTableId')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.GetSnapshotReq is not None:
            showIndent(outfile, level)
            outfile.write('GetSnapshotReq=model_.GetSnapshotReqType(\n')
            self.GetSnapshotReq.exportLiteral(outfile, level, name_='GetSnapshotReq')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.GetFullSnapshotReq is not None:
            showIndent(outfile, level)
            outfile.write('GetFullSnapshotReq=model_.GetFullSnapshotReqType(\n')
            self.GetFullSnapshotReq.exportLiteral(outfile, level, name_='GetFullSnapshotReq')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.SnapshotId is not None:
            showIndent(outfile, level)
            outfile.write('SnapshotId=%s,\n' % self.gds_encode(quote_python(self.SnapshotId)))
        if self.StartUpdateReq is not None:
            showIndent(outfile, level)
            outfile.write('StartUpdateReq=%s,\n' % self.gds_encode(quote_python(self.StartUpdateReq)))
        if self.StopUpdateReq is not None:
            showIndent(outfile, level)
            outfile.write('StopUpdateReq=%s,\n' % self.gds_encode(quote_python(self.StopUpdateReq)))
        if self.FailureResp is not None:
            showIndent(outfile, level)
            outfile.write('FailureResp=model_.FailureRespType(\n')
            self.FailureResp.exportLiteral(outfile, level, name_='FailureResp')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.uR is not None:
            showIndent(outfile, level)
            outfile.write('uR=model_.uRType(\n')
            self.uR.exportLiteral(outfile, level, name_='uR')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.sR is not None:
            showIndent(outfile, level)
            outfile.write('sR=model_.DataResponse(\n')
            self.sR.exportLiteral(outfile, level, name_='sR')
            showIndent(outfile, level)
            outfile.write('),\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.Pport_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.ts is not None:
            dbobj.ts = self.ts
        if self.version is not None:
            dbobj.version = self.version
    def exportSQLAlchemyChildren(self, session, dbobj):
        if self.QueryTimetable is not None:
            dbobj.QueryTimetable = self.QueryTimetable
        if self.TimeTableId is not None:
            child_dbobj = self.TimeTableId.exportSQLAlchemy(session)
            dbobj.TimeTableId = child_dbobj
        if self.GetSnapshotReq is not None:
            child_dbobj = self.GetSnapshotReq.exportSQLAlchemy(session)
            dbobj.GetSnapshotReq = child_dbobj
        if self.GetFullSnapshotReq is not None:
            child_dbobj = self.GetFullSnapshotReq.exportSQLAlchemy(session)
            dbobj.GetFullSnapshotReq = child_dbobj
        if self.SnapshotId is not None:
            dbobj.SnapshotId = self.SnapshotId
        if self.StartUpdateReq is not None:
            dbobj.StartUpdateReq = self.StartUpdateReq
        if self.StopUpdateReq is not None:
            dbobj.StopUpdateReq = self.StopUpdateReq
        if self.FailureResp is not None:
            child_dbobj = self.FailureResp.exportSQLAlchemy(session)
            dbobj.FailureResp = child_dbobj
        if self.uR is not None:
            child_dbobj = self.uR.exportSQLAlchemy(session)
            dbobj.uR = child_dbobj
        if self.sR is not None:
            child_dbobj = self.sR.exportSQLAlchemy(session)
            dbobj.sR = child_dbobj
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('ts', node)
        if value is not None and 'ts' not in already_processed:
            already_processed.add('ts')
            try:
                self.ts = self.gds_parse_datetime(value)
            except ValueError as exp:
                raise ValueError('Bad date-time attribute (ts): %s' % exp)
            self.validate_RTTIDateTimeType(self.ts)    # validate type RTTIDateTimeType
        value = find_attr_value_('version', node)
        if value is not None and 'version' not in already_processed:
            already_processed.add('version')
            self.version = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'QueryTimetable':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'QueryTimetable')
            value_ = self.gds_validate_string(value_, node, 'QueryTimetable')
            self.QueryTimetable = value_
            self.QueryTimetable_nsprefix_ = child_.prefix
        elif nodeName_ == 'TimeTableId':
            obj_ = TimeTableIdType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.TimeTableId = obj_
            obj_.original_tagname_ = 'TimeTableId'
        elif nodeName_ == 'GetSnapshotReq':
            obj_ = GetSnapshotReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.GetSnapshotReq = obj_
            obj_.original_tagname_ = 'GetSnapshotReq'
        elif nodeName_ == 'GetFullSnapshotReq':
            obj_ = GetFullSnapshotReqType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.GetFullSnapshotReq = obj_
            obj_.original_tagname_ = 'GetFullSnapshotReq'
        elif nodeName_ == 'SnapshotId':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'SnapshotId')
            value_ = self.gds_validate_string(value_, node, 'SnapshotId')
            self.SnapshotId = value_
            self.SnapshotId_nsprefix_ = child_.prefix
            # validate type SnapshotIDType
            self.validate_SnapshotIDType(self.SnapshotId)
        elif nodeName_ == 'StartUpdateReq':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'StartUpdateReq')
            value_ = self.gds_validate_string(value_, node, 'StartUpdateReq')
            self.StartUpdateReq = value_
            self.StartUpdateReq_nsprefix_ = child_.prefix
        elif nodeName_ == 'StopUpdateReq':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'StopUpdateReq')
            value_ = self.gds_validate_string(value_, node, 'StopUpdateReq')
            self.StopUpdateReq = value_
            self.StopUpdateReq_nsprefix_ = child_.prefix
        elif nodeName_ == 'FailureResp':
            obj_ = FailureRespType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.FailureResp = obj_
            obj_.original_tagname_ = 'FailureResp'
        elif nodeName_ == 'uR':
            obj_ = uRType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.uR = obj_
            obj_.original_tagname_ = 'uR'
        elif nodeName_ == 'sR':
            class_obj_ = self.get_class_obj_(child_, DataResponse)
            obj_ = class_obj_.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.sR = obj_
            obj_.original_tagname_ = 'sR'
# end class Pport


class QueryTimetable(GeneratedsSuper):
    """Query for the current timetable ID"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, QueryTimetable)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if QueryTimetable.subclass:
            return QueryTimetable.subclass(*args_, **kwargs_)
        else:
            return QueryTimetable(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='QueryTimetable', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('QueryTimetable')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='QueryTimetable')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='QueryTimetable', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='QueryTimetable'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='QueryTimetable', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='QueryTimetable', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='QueryTimetable'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.QueryTimetable_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class QueryTimetable


class StartUpdateReq(GeneratedsSuper):
    """Start sending available updates."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, StartUpdateReq)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if StartUpdateReq.subclass:
            return StartUpdateReq.subclass(*args_, **kwargs_)
        else:
            return StartUpdateReq(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='StartUpdateReq', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('StartUpdateReq')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='StartUpdateReq')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='StartUpdateReq', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='StartUpdateReq'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='StartUpdateReq', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='StartUpdateReq', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='StartUpdateReq'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.StartUpdateReq_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class StartUpdateReq


class StopUpdateReq(GeneratedsSuper):
    """Stop sending available updates."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, StopUpdateReq)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if StopUpdateReq.subclass:
            return StopUpdateReq.subclass(*args_, **kwargs_)
        else:
            return StopUpdateReq(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='StopUpdateReq', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('StopUpdateReq')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='StopUpdateReq')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='StopUpdateReq', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='StopUpdateReq'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='StopUpdateReq', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='StopUpdateReq', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='StopUpdateReq'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.StopUpdateReq_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class StopUpdateReq


class StatusType(GeneratedsSuper):
    """Status Code Type"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, code=None, valueOf_=None, extensiontype_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.code = _cast(None, code)
        self.code_nsprefix_ = None
        self.valueOf_ = valueOf_
        self.anyAttributes_ = {}
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, StatusType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if StatusType.subclass:
            return StatusType.subclass(*args_, **kwargs_)
        else:
            return StatusType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_ErrorCodeType(self, value):
        # Validate type tns:ErrorCodeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 32:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ErrorCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ErrorCodeType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='StatusType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('StatusType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='StatusType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='StatusType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='StatusType'):
        unique_counter = 0
        for name, value in list(self.anyAttributes_.items()):
            xsinamespaceprefix = 'xsi'
            xsinamespace1 = 'http://www.w3.org/2001/XMLSchema-instance'
            xsinamespace2 = '{%s}' % (xsinamespace1, )
            if name.startswith(xsinamespace2):
                name1 = name[len(xsinamespace2):]
                name2 = '%s:%s' % (xsinamespaceprefix, name1, )
                if name2 not in already_processed:
                    already_processed.add(name2)
                    outfile.write(' %s=%s' % (name2, quote_attrib(value), ))
            else:
                mo = re_.match(Namespace_extract_pat_, name)
                if mo is not None:
                    namespace, name = mo.group(1, 2)
                    if name not in already_processed:
                        already_processed.add(name)
                        if namespace == 'http://www.w3.org/XML/1998/namespace':
                            outfile.write(' %s=%s' % (
                                name, quote_attrib(value), ))
                        else:
                            unique_counter += 1
                            outfile.write(' xmlns:%d="%s"' % (
                                unique_counter, namespace, ))
                            outfile.write(' %d:%s=%s' % (
                                unique_counter, name, quote_attrib(value), ))
                else:
                    if name not in already_processed:
                        already_processed.add(name)
                        outfile.write(' %s=%s' % (
                            name, quote_attrib(value), ))
        if 'code' not in already_processed:
            already_processed.add('code')
            outfile.write(' code=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.code), input_name='code')), ))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            outfile.write(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            if ":" not in self.extensiontype_:
                imported_ns_type_prefix_ = GenerateDSNamespaceTypePrefixes_.get(self.extensiontype_, '')
                outfile.write(' xsi:type="%s%s"' % (imported_ns_type_prefix_, self.extensiontype_))
            else:
                outfile.write(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='StatusType', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='StatusType', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.extensiontype_ is not None:
            element.set('{http://www.w3.org/2001/XMLSchema-instance}type', self.extensiontype_)
        if self.code is not None:
            element.set('code', self.gds_format_string(self.code))
        if self.hasContent_():
            element.text = self.gds_format_string(self.get_valueOf_())
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='StatusType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.code is not None and 'code' not in already_processed:
            already_processed.add('code')
            showIndent(outfile, level)
            outfile.write('code=%s,\n' % (self.code,))
        for name, value in list(self.anyAttributes_.items()):
            showIndent(outfile, level)
            outfile.write('%s="%s",\n' % (name, value,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.StatusType_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.code is not None:
            dbobj.code = self.code
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('code', node)
        if value is not None and 'code' not in already_processed:
            already_processed.add('code')
            self.code = value
            self.validate_ErrorCodeType(self.code)    # validate type ErrorCodeType
        self.anyAttributes_ = {}
        for name, value in list(attrs.items()):
            if name not in already_processed:
                self.anyAttributes_[name] = value
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class StatusType


class PPStatus(StatusType):
    """Setup phase status/heartbeat response"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = StatusType
    def __init__(self, code=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(PPStatus, self).__init__(code, valueOf_,  **kwargs_)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PPStatus)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PPStatus.subclass:
            return PPStatus.subclass(*args_, **kwargs_)
        else:
            return PPStatus(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            super(PPStatus, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='PPStatus', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PPStatus')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PPStatus')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PPStatus', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='PPStatus'):
        super(PPStatus, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PPStatus')
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='PPStatus', fromsubclass_=False, pretty_print=True):
        super(PPStatus, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        pass
    def to_etree(self, parent_element=None, name_='PPStatus', mapping_=None):
        element = super(PPStatus, self).to_etree(parent_element, name_, mapping_)
        if self.hasContent_():
            element.text = self.gds_format_string(self.get_valueOf_())
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='PPStatus'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        super(PPStatus, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(PPStatus, self).exportLiteralChildren(outfile, level, name_)
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.PPStatus_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        super(PPStatus, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class PPStatus


class PPReqVersion(GeneratedsSuper):
    """Request the schema versions required by the clientThe namespace of the
    Push Port data schema supported by the client.The namespace of the Push
    Port Timetable schema supported by the client.The namespace of the Push
    Port Timetable Reference data schema supported by the client."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, version=None, ttversion=None, ttrefversion=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.version = _cast(None, version)
        self.version_nsprefix_ = None
        self.ttversion = _cast(None, ttversion)
        self.ttversion_nsprefix_ = None
        self.ttrefversion = _cast(None, ttrefversion)
        self.ttrefversion_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PPReqVersion)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PPReqVersion.subclass:
            return PPReqVersion.subclass(*args_, **kwargs_)
        else:
            return PPReqVersion(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='PPReqVersion', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PPReqVersion')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PPReqVersion')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PPReqVersion', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='PPReqVersion'):
        if 'version' not in already_processed:
            already_processed.add('version')
            outfile.write(' version=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.version), input_name='version')), ))
        if 'ttversion' not in already_processed:
            already_processed.add('ttversion')
            outfile.write(' ttversion=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ttversion), input_name='ttversion')), ))
        if 'ttrefversion' not in already_processed:
            already_processed.add('ttrefversion')
            outfile.write(' ttrefversion=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ttrefversion), input_name='ttrefversion')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='PPReqVersion', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='PPReqVersion', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.version is not None:
            element.set('version', self.gds_format_string(self.version))
        if self.ttversion is not None:
            element.set('ttversion', self.gds_format_string(self.ttversion))
        if self.ttrefversion is not None:
            element.set('ttrefversion', self.gds_format_string(self.ttrefversion))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='PPReqVersion'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.version is not None and 'version' not in already_processed:
            already_processed.add('version')
            showIndent(outfile, level)
            outfile.write('version="%s",\n' % (self.version,))
        if self.ttversion is not None and 'ttversion' not in already_processed:
            already_processed.add('ttversion')
            showIndent(outfile, level)
            outfile.write('ttversion="%s",\n' % (self.ttversion,))
        if self.ttrefversion is not None and 'ttrefversion' not in already_processed:
            already_processed.add('ttrefversion')
            showIndent(outfile, level)
            outfile.write('ttrefversion="%s",\n' % (self.ttrefversion,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.PPReqVersion_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.version is not None:
            dbobj.version = self.version
        if self.ttversion is not None:
            dbobj.ttversion = self.ttversion
        if self.ttrefversion is not None:
            dbobj.ttrefversion = self.ttrefversion
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('version', node)
        if value is not None and 'version' not in already_processed:
            already_processed.add('version')
            self.version = value
        value = find_attr_value_('ttversion', node)
        if value is not None and 'ttversion' not in already_processed:
            already_processed.add('ttversion')
            self.ttversion = value
        value = find_attr_value_('ttrefversion', node)
        if value is not None and 'ttrefversion' not in already_processed:
            already_processed.add('ttrefversion')
            self.ttrefversion = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class PPReqVersion


class PPConnect(GeneratedsSuper):
    """Signal end of the setup phase and switch to use the requested PP data
    schema."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PPConnect)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PPConnect.subclass:
            return PPConnect.subclass(*args_, **kwargs_)
        else:
            return PPConnect(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='PPConnect', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PPConnect')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PPConnect')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PPConnect', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='PPConnect'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='PPConnect', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='PPConnect', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='PPConnect'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.PPConnect_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class PPConnect


class DisruptionReasonType(GeneratedsSuper):
    """Type used to represent a cancellation or late running reasonOptional
    TIPLOC where the reason refers to, e.g. "signalling failure at Cheadle
    Hulme".If true, the tiploc attribute should be interpreted as "near",
    e.g. "signalling failure near Cheadle Hulme"."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, tiploc=None, near=False, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.tiploc = _cast(None, tiploc)
        self.tiploc_nsprefix_ = None
        self.near = _cast(bool, near)
        self.near_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DisruptionReasonType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DisruptionReasonType.subclass:
            return DisruptionReasonType.subclass(*args_, **kwargs_)
        else:
            return DisruptionReasonType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TiplocType(self, value):
        # Validate type tns:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='DisruptionReasonType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DisruptionReasonType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DisruptionReasonType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DisruptionReasonType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='DisruptionReasonType'):
        if self.tiploc is not None and 'tiploc' not in already_processed:
            already_processed.add('tiploc')
            outfile.write(' tiploc=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tiploc), input_name='tiploc')), ))
        if self.near and 'near' not in already_processed:
            already_processed.add('near')
            outfile.write(' near="%s"' % self.gds_format_boolean(self.near, input_name='near'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='DisruptionReasonType', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='DisruptionReasonType', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.tiploc is not None:
            element.set('tiploc', self.gds_format_string(self.tiploc))
        if self.near is not None:
            element.set('near', self.gds_format_boolean(self.near))
        if self.hasContent_():
            element.text = self.gds_format_string(self.get_valueOf_())
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='DisruptionReasonType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.tiploc is not None and 'tiploc' not in already_processed:
            already_processed.add('tiploc')
            showIndent(outfile, level)
            outfile.write('tiploc=%s,\n' % (self.tiploc,))
        if self.near is not None and 'near' not in already_processed:
            already_processed.add('near')
            showIndent(outfile, level)
            outfile.write('near=%s,\n' % (self.near,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.DisruptionReasonType_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.tiploc is not None:
            dbobj.tiploc = self.tiploc
        if self.near is not None:
            dbobj.near = self.near
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('tiploc', node)
        if value is not None and 'tiploc' not in already_processed:
            already_processed.add('tiploc')
            self.tiploc = value
            self.validate_TiplocType(self.tiploc)    # validate type TiplocType
        value = find_attr_value_('near', node)
        if value is not None and 'near' not in already_processed:
            already_processed.add('near')
            if value in ('true', '1'):
                self.near = True
            elif value in ('false', '0'):
                self.near = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DisruptionReasonType


class AssocService(GeneratedsSuper):
    """RTTI Train ID. Note that since this is an RID, the service must already
    exist within Darwin.One or more scheduled times to identify the
    instance of the location in the train schedule where the association
    occurs."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, rid=None, wta=None, wtd=None, wtp=None, pta=None, ptd=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.rid = _cast(None, rid)
        self.rid_nsprefix_ = None
        self.wta = _cast(None, wta)
        self.wta_nsprefix_ = None
        self.wtd = _cast(None, wtd)
        self.wtd_nsprefix_ = None
        self.wtp = _cast(None, wtp)
        self.wtp_nsprefix_ = None
        self.pta = _cast(None, pta)
        self.pta_nsprefix_ = None
        self.ptd = _cast(None, ptd)
        self.ptd_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AssocService)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AssocService.subclass:
            return AssocService.subclass(*args_, **kwargs_)
        else:
            return AssocService(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_RIDType(self, value):
        # Validate type ct:RIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on RIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_WTimeType(self, value):
        # Validate type tns:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_RTTITimeType(self, value):
        # Validate type tns:RTTITimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_RTTITimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_RTTITimeType_patterns_, ))
    validate_RTTITimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9])$']]
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='AssocService', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AssocService')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AssocService')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AssocService', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='AssocService'):
        if 'rid' not in already_processed:
            already_processed.add('rid')
            outfile.write(' rid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.rid), input_name='rid')), ))
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            outfile.write(' wta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wta), input_name='wta')), ))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            outfile.write(' wtd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtd), input_name='wtd')), ))
        if self.wtp is not None and 'wtp' not in already_processed:
            already_processed.add('wtp')
            outfile.write(' wtp=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtp), input_name='wtp')), ))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            outfile.write(' pta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.pta), input_name='pta')), ))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            outfile.write(' ptd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ptd), input_name='ptd')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='AssocService', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='AssocService', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.rid is not None:
            element.set('rid', self.gds_format_string(self.rid))
        if self.wta is not None:
            element.set('wta', self.gds_format_string(self.wta))
        if self.wtd is not None:
            element.set('wtd', self.gds_format_string(self.wtd))
        if self.wtp is not None:
            element.set('wtp', self.gds_format_string(self.wtp))
        if self.pta is not None:
            element.set('pta', self.gds_format_string(self.pta))
        if self.ptd is not None:
            element.set('ptd', self.gds_format_string(self.ptd))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='AssocService'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.rid is not None and 'rid' not in already_processed:
            already_processed.add('rid')
            showIndent(outfile, level)
            outfile.write('rid=%s,\n' % (self.rid,))
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            showIndent(outfile, level)
            outfile.write('wta=%s,\n' % (self.wta,))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            showIndent(outfile, level)
            outfile.write('wtd=%s,\n' % (self.wtd,))
        if self.wtp is not None and 'wtp' not in already_processed:
            already_processed.add('wtp')
            showIndent(outfile, level)
            outfile.write('wtp=%s,\n' % (self.wtp,))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            showIndent(outfile, level)
            outfile.write('pta=%s,\n' % (self.pta,))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            showIndent(outfile, level)
            outfile.write('ptd=%s,\n' % (self.ptd,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.AssocService_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.rid is not None:
            dbobj.rid = self.rid
        if self.wta is not None:
            dbobj.wta = self.wta
        if self.wtd is not None:
            dbobj.wtd = self.wtd
        if self.wtp is not None:
            dbobj.wtp = self.wtp
        if self.pta is not None:
            dbobj.pta = self.pta
        if self.ptd is not None:
            dbobj.ptd = self.ptd
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('rid', node)
        if value is not None and 'rid' not in already_processed:
            already_processed.add('rid')
            self.rid = value
            self.validate_RIDType(self.rid)    # validate type RIDType
        value = find_attr_value_('wta', node)
        if value is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            self.wta = value
            self.validate_WTimeType(self.wta)    # validate type WTimeType
        value = find_attr_value_('wtd', node)
        if value is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            self.wtd = value
            self.validate_WTimeType(self.wtd)    # validate type WTimeType
        value = find_attr_value_('wtp', node)
        if value is not None and 'wtp' not in already_processed:
            already_processed.add('wtp')
            self.wtp = value
            self.validate_WTimeType(self.wtp)    # validate type WTimeType
        value = find_attr_value_('pta', node)
        if value is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            self.pta = value
            self.validate_RTTITimeType(self.pta)    # validate type RTTITimeType
        value = find_attr_value_('ptd', node)
        if value is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            self.ptd = value
            self.validate_RTTITimeType(self.ptd)    # validate type RTTITimeType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class AssocService


class Association(GeneratedsSuper):
    """Type describing an association between schedulesThe TIPLOC of the
    location where the association occurs.Association categoryTrue if this
    association is cancelled, i.e. the association exists but will no
    longer happen.True if this association is deleted, i.e. the association
    no longer exists."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, tiploc=None, category=None, isCancelled=False, isDeleted=False, main=None, assoc=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.tiploc = _cast(None, tiploc)
        self.tiploc_nsprefix_ = None
        self.category = _cast(None, category)
        self.category_nsprefix_ = None
        self.isCancelled = _cast(bool, isCancelled)
        self.isCancelled_nsprefix_ = None
        self.isDeleted = _cast(bool, isDeleted)
        self.isDeleted_nsprefix_ = None
        self.main = main
        self.main_nsprefix_ = None
        self.assoc = assoc
        self.assoc_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Association)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Association.subclass:
            return Association.subclass(*args_, **kwargs_)
        else:
            return Association(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_CategoryType(self, value):
        # Validate type tns:CategoryType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['JJ', 'VV', 'LK', 'NP']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on CategoryType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.main is not None or
            self.assoc is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='Association', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Association')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Association')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Association', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='Association'):
        if 'tiploc' not in already_processed:
            already_processed.add('tiploc')
            outfile.write(' tiploc=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tiploc), input_name='tiploc')), ))
        if 'category' not in already_processed:
            already_processed.add('category')
            outfile.write(' category=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.category), input_name='category')), ))
        if self.isCancelled and 'isCancelled' not in already_processed:
            already_processed.add('isCancelled')
            outfile.write(' isCancelled="%s"' % self.gds_format_boolean(self.isCancelled, input_name='isCancelled'))
        if self.isDeleted and 'isDeleted' not in already_processed:
            already_processed.add('isDeleted')
            outfile.write(' isDeleted="%s"' % self.gds_format_boolean(self.isDeleted, input_name='isDeleted'))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='Association', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.main is not None:
            namespaceprefix_ = self.main_nsprefix_ + ':' if (UseCapturedNS_ and self.main_nsprefix_) else ''
            self.main.export(outfile, level, namespaceprefix_, namespacedef_='', name_='main', pretty_print=pretty_print)
        if self.assoc is not None:
            namespaceprefix_ = self.assoc_nsprefix_ + ':' if (UseCapturedNS_ and self.assoc_nsprefix_) else ''
            self.assoc.export(outfile, level, namespaceprefix_, namespacedef_='', name_='assoc', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Association', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.tiploc is not None:
            element.set('tiploc', self.gds_format_string(self.tiploc))
        if self.category is not None:
            element.set('category', self.gds_format_string(self.category))
        if self.isCancelled is not None:
            element.set('isCancelled', self.gds_format_boolean(self.isCancelled))
        if self.isDeleted is not None:
            element.set('isDeleted', self.gds_format_boolean(self.isDeleted))
        if self.main is not None:
            main_ = self.main
            main_.to_etree(element, name_='main', mapping_=mapping_)
        if self.assoc is not None:
            assoc_ = self.assoc
            assoc_.to_etree(element, name_='assoc', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='Association'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.tiploc is not None and 'tiploc' not in already_processed:
            already_processed.add('tiploc')
            showIndent(outfile, level)
            outfile.write('tiploc=%s,\n' % (self.tiploc,))
        if self.category is not None and 'category' not in already_processed:
            already_processed.add('category')
            showIndent(outfile, level)
            outfile.write('category=%s,\n' % (self.category,))
        if self.isCancelled is not None and 'isCancelled' not in already_processed:
            already_processed.add('isCancelled')
            showIndent(outfile, level)
            outfile.write('isCancelled=%s,\n' % (self.isCancelled,))
        if self.isDeleted is not None and 'isDeleted' not in already_processed:
            already_processed.add('isDeleted')
            showIndent(outfile, level)
            outfile.write('isDeleted=%s,\n' % (self.isDeleted,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.main is not None:
            showIndent(outfile, level)
            outfile.write('main=model_.AssocService(\n')
            self.main.exportLiteral(outfile, level, name_='main')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.assoc is not None:
            showIndent(outfile, level)
            outfile.write('assoc=model_.AssocService(\n')
            self.assoc.exportLiteral(outfile, level, name_='assoc')
            showIndent(outfile, level)
            outfile.write('),\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.Association_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.tiploc is not None:
            dbobj.tiploc = self.tiploc
        if self.category is not None:
            dbobj.category = self.category
        if self.isCancelled is not None:
            dbobj.isCancelled = self.isCancelled
        if self.isDeleted is not None:
            dbobj.isDeleted = self.isDeleted
    def exportSQLAlchemyChildren(self, session, dbobj):
        if self.main is not None:
            child_dbobj = self.main.exportSQLAlchemy(session)
            dbobj.main = child_dbobj
        if self.assoc is not None:
            child_dbobj = self.assoc.exportSQLAlchemy(session)
            dbobj.assoc = child_dbobj
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('tiploc', node)
        if value is not None and 'tiploc' not in already_processed:
            already_processed.add('tiploc')
            self.tiploc = value
            self.validate_TiplocType(self.tiploc)    # validate type TiplocType
        value = find_attr_value_('category', node)
        if value is not None and 'category' not in already_processed:
            already_processed.add('category')
            self.category = value
            self.validate_CategoryType(self.category)    # validate type CategoryType
        value = find_attr_value_('isCancelled', node)
        if value is not None and 'isCancelled' not in already_processed:
            already_processed.add('isCancelled')
            if value in ('true', '1'):
                self.isCancelled = True
            elif value in ('false', '0'):
                self.isCancelled = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('isDeleted', node)
        if value is not None and 'isDeleted' not in already_processed:
            already_processed.add('isDeleted')
            if value in ('true', '1'):
                self.isDeleted = True
            elif value in ('false', '0'):
                self.isDeleted = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'main':
            obj_ = AssocService.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.main = obj_
            obj_.original_tagname_ = 'main'
        elif nodeName_ == 'assoc':
            obj_ = AssocService.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.assoc = obj_
            obj_.original_tagname_ = 'assoc'
# end class Association


class OR(GeneratedsSuper):
    """Defines a Passenger Origin Calling PointWorking Scheduled Time of
    ArrivalWorking Scheduled Time of DepartureTIPLOC of False Destination
    to be used at this location"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, wta=None, wtd=None, fd=None, tpl=None, act='  ', planAct=None, can=False, fid=None, pta=None, ptd=None, avgLoading=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.wta = _cast(None, wta)
        self.wta_nsprefix_ = None
        self.wtd = _cast(None, wtd)
        self.wtd_nsprefix_ = None
        self.fd = _cast(None, fd)
        self.fd_nsprefix_ = None
        self.tpl = _cast(None, tpl)
        self.tpl_nsprefix_ = None
        self.act = _cast(None, act)
        self.act_nsprefix_ = None
        self.planAct = _cast(None, planAct)
        self.planAct_nsprefix_ = None
        self.can = _cast(bool, can)
        self.can_nsprefix_ = None
        self.fid = _cast(None, fid)
        self.fid_nsprefix_ = None
        self.pta = _cast(None, pta)
        self.pta_nsprefix_ = None
        self.ptd = _cast(None, ptd)
        self.ptd_nsprefix_ = None
        self.avgLoading = _cast(None, avgLoading)
        self.avgLoading_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OR)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OR.subclass:
            return OR.subclass(*args_, **kwargs_)
        else:
            return OR(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_WTimeType(self, value):
        # Validate type ct:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ActivityType(self, value):
        # Validate type ct:ActivityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_ActivityType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ActivityType_patterns_, ))
    validate_ActivityType_patterns_ = [['^(([A-Z0-9\\- ][A-Z0-9\\- ]){1,6})$']]
    def validate_FormationIDType(self, value):
        # Validate type ct3:FormationIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_RTTITimeType(self, value):
        # Validate type ct:RTTITimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_RTTITimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_RTTITimeType_patterns_, ))
    validate_RTTITimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9])$']]
    def validate_LoadingValue(self, value):
        # Validate type ct3:LoadingValue, a restriction on xs:unsignedInt.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on LoadingValue' % {"value": value, "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='OR', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OR')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OR')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OR', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='OR'):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            outfile.write(' wta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wta), input_name='wta')), ))
        if 'wtd' not in already_processed:
            already_processed.add('wtd')
            outfile.write(' wtd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtd), input_name='wtd')), ))
        if self.fd is not None and 'fd' not in already_processed:
            already_processed.add('fd')
            outfile.write(' fd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fd), input_name='fd')), ))
        if 'tpl' not in already_processed:
            already_processed.add('tpl')
            outfile.write(' tpl=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tpl), input_name='tpl')), ))
        if self.act != "  " and 'act' not in already_processed:
            already_processed.add('act')
            outfile.write(' act=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.act), input_name='act')), ))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            outfile.write(' planAct=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.planAct), input_name='planAct')), ))
        if self.can and 'can' not in already_processed:
            already_processed.add('can')
            outfile.write(' can="%s"' % self.gds_format_boolean(self.can, input_name='can'))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            outfile.write(' fid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fid), input_name='fid')), ))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            outfile.write(' pta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.pta), input_name='pta')), ))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            outfile.write(' ptd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ptd), input_name='ptd')), ))
        if self.avgLoading is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            outfile.write(' avgLoading="%s"' % self.gds_format_integer(self.avgLoading, input_name='avgLoading'))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='OR', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='OR', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.wta is not None:
            element.set('wta', self.gds_format_string(self.wta))
        if self.wtd is not None:
            element.set('wtd', self.gds_format_string(self.wtd))
        if self.fd is not None:
            element.set('fd', self.gds_format_string(self.fd))
        if self.tpl is not None:
            element.set('tpl', self.gds_format_string(self.tpl))
        if self.act is not None:
            element.set('act', self.gds_format_string(self.act))
        if self.planAct is not None:
            element.set('planAct', self.gds_format_string(self.planAct))
        if self.can is not None:
            element.set('can', self.gds_format_boolean(self.can))
        if self.fid is not None:
            element.set('fid', self.gds_format_string(self.fid))
        if self.pta is not None:
            element.set('pta', self.gds_format_string(self.pta))
        if self.ptd is not None:
            element.set('ptd', self.gds_format_string(self.ptd))
        if self.avgLoading is not None:
            element.set('avgLoading', self.gds_format_integer(self.avgLoading))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='OR'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            showIndent(outfile, level)
            outfile.write('wta=%s,\n' % (self.wta,))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            showIndent(outfile, level)
            outfile.write('wtd=%s,\n' % (self.wtd,))
        if self.fd is not None and 'fd' not in already_processed:
            already_processed.add('fd')
            showIndent(outfile, level)
            outfile.write('fd=%s,\n' % (self.fd,))
        if self.tpl is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            showIndent(outfile, level)
            outfile.write('tpl=%s,\n' % (self.tpl,))
        if self.act is not None and 'act' not in already_processed:
            already_processed.add('act')
            showIndent(outfile, level)
            outfile.write('act=%s,\n' % (self.act,))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            showIndent(outfile, level)
            outfile.write('planAct=%s,\n' % (self.planAct,))
        if self.can is not None and 'can' not in already_processed:
            already_processed.add('can')
            showIndent(outfile, level)
            outfile.write('can=%s,\n' % (self.can,))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            showIndent(outfile, level)
            outfile.write('fid=%s,\n' % (self.fid,))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            showIndent(outfile, level)
            outfile.write('pta=%s,\n' % (self.pta,))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            showIndent(outfile, level)
            outfile.write('ptd=%s,\n' % (self.ptd,))
        if self.avgLoading is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            showIndent(outfile, level)
            outfile.write('avgLoading=%s,\n' % (self.avgLoading,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.OR_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.wta is not None:
            dbobj.wta = self.wta
        if self.wtd is not None:
            dbobj.wtd = self.wtd
        if self.fd is not None:
            dbobj.fd = self.fd
        if self.tpl is not None:
            dbobj.tpl = self.tpl
        if self.act is not None:
            dbobj.act = self.act
        if self.planAct is not None:
            dbobj.planAct = self.planAct
        if self.can is not None:
            dbobj.can = self.can
        if self.fid is not None:
            dbobj.fid = self.fid
        if self.pta is not None:
            dbobj.pta = self.pta
        if self.ptd is not None:
            dbobj.ptd = self.ptd
        if self.avgLoading is not None:
            dbobj.avgLoading = self.avgLoading
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('wta', node)
        if value is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            self.wta = value
            self.validate_WTimeType(self.wta)    # validate type WTimeType
        value = find_attr_value_('wtd', node)
        if value is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            self.wtd = value
            self.validate_WTimeType(self.wtd)    # validate type WTimeType
        value = find_attr_value_('fd', node)
        if value is not None and 'fd' not in already_processed:
            already_processed.add('fd')
            self.fd = value
            self.validate_TiplocType(self.fd)    # validate type TiplocType
        value = find_attr_value_('tpl', node)
        if value is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            self.tpl = value
            self.validate_TiplocType(self.tpl)    # validate type TiplocType
        value = find_attr_value_('act', node)
        if value is not None and 'act' not in already_processed:
            already_processed.add('act')
            self.act = value
            self.validate_ActivityType(self.act)    # validate type ActivityType
        value = find_attr_value_('planAct', node)
        if value is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            self.planAct = value
            self.validate_ActivityType(self.planAct)    # validate type ActivityType
        value = find_attr_value_('can', node)
        if value is not None and 'can' not in already_processed:
            already_processed.add('can')
            if value in ('true', '1'):
                self.can = True
            elif value in ('false', '0'):
                self.can = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('fid', node)
        if value is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            self.fid = value
            self.validate_FormationIDType(self.fid)    # validate type FormationIDType
        value = find_attr_value_('pta', node)
        if value is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            self.pta = value
            self.validate_RTTITimeType(self.pta)    # validate type RTTITimeType
        value = find_attr_value_('ptd', node)
        if value is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            self.ptd = value
            self.validate_RTTITimeType(self.ptd)    # validate type RTTITimeType
        value = find_attr_value_('avgLoading', node)
        if value is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            self.avgLoading = self.gds_parse_integer(value, node, 'avgLoading')
            self.validate_LoadingValue(self.avgLoading)    # validate type LoadingValue
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class OR


class OPOR(GeneratedsSuper):
    """Defines an Operational Origin Calling PointWorking Scheduled Time of
    ArrivalWorking Scheduled Time of Departure"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, wta=None, wtd=None, tpl=None, act='  ', planAct=None, can=False, fid=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.wta = _cast(None, wta)
        self.wta_nsprefix_ = None
        self.wtd = _cast(None, wtd)
        self.wtd_nsprefix_ = None
        self.tpl = _cast(None, tpl)
        self.tpl_nsprefix_ = None
        self.act = _cast(None, act)
        self.act_nsprefix_ = None
        self.planAct = _cast(None, planAct)
        self.planAct_nsprefix_ = None
        self.can = _cast(bool, can)
        self.can_nsprefix_ = None
        self.fid = _cast(None, fid)
        self.fid_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OPOR)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OPOR.subclass:
            return OPOR.subclass(*args_, **kwargs_)
        else:
            return OPOR(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_WTimeType(self, value):
        # Validate type ct:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ActivityType(self, value):
        # Validate type ct:ActivityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_ActivityType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ActivityType_patterns_, ))
    validate_ActivityType_patterns_ = [['^(([A-Z0-9\\- ][A-Z0-9\\- ]){1,6})$']]
    def validate_FormationIDType(self, value):
        # Validate type ct3:FormationIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='OPOR', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OPOR')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OPOR')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OPOR', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='OPOR'):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            outfile.write(' wta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wta), input_name='wta')), ))
        if 'wtd' not in already_processed:
            already_processed.add('wtd')
            outfile.write(' wtd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtd), input_name='wtd')), ))
        if 'tpl' not in already_processed:
            already_processed.add('tpl')
            outfile.write(' tpl=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tpl), input_name='tpl')), ))
        if self.act != "  " and 'act' not in already_processed:
            already_processed.add('act')
            outfile.write(' act=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.act), input_name='act')), ))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            outfile.write(' planAct=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.planAct), input_name='planAct')), ))
        if self.can and 'can' not in already_processed:
            already_processed.add('can')
            outfile.write(' can="%s"' % self.gds_format_boolean(self.can, input_name='can'))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            outfile.write(' fid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fid), input_name='fid')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='OPOR', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='OPOR', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.wta is not None:
            element.set('wta', self.gds_format_string(self.wta))
        if self.wtd is not None:
            element.set('wtd', self.gds_format_string(self.wtd))
        if self.tpl is not None:
            element.set('tpl', self.gds_format_string(self.tpl))
        if self.act is not None:
            element.set('act', self.gds_format_string(self.act))
        if self.planAct is not None:
            element.set('planAct', self.gds_format_string(self.planAct))
        if self.can is not None:
            element.set('can', self.gds_format_boolean(self.can))
        if self.fid is not None:
            element.set('fid', self.gds_format_string(self.fid))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='OPOR'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            showIndent(outfile, level)
            outfile.write('wta=%s,\n' % (self.wta,))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            showIndent(outfile, level)
            outfile.write('wtd=%s,\n' % (self.wtd,))
        if self.tpl is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            showIndent(outfile, level)
            outfile.write('tpl=%s,\n' % (self.tpl,))
        if self.act is not None and 'act' not in already_processed:
            already_processed.add('act')
            showIndent(outfile, level)
            outfile.write('act=%s,\n' % (self.act,))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            showIndent(outfile, level)
            outfile.write('planAct=%s,\n' % (self.planAct,))
        if self.can is not None and 'can' not in already_processed:
            already_processed.add('can')
            showIndent(outfile, level)
            outfile.write('can=%s,\n' % (self.can,))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            showIndent(outfile, level)
            outfile.write('fid=%s,\n' % (self.fid,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.OPOR_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.wta is not None:
            dbobj.wta = self.wta
        if self.wtd is not None:
            dbobj.wtd = self.wtd
        if self.tpl is not None:
            dbobj.tpl = self.tpl
        if self.act is not None:
            dbobj.act = self.act
        if self.planAct is not None:
            dbobj.planAct = self.planAct
        if self.can is not None:
            dbobj.can = self.can
        if self.fid is not None:
            dbobj.fid = self.fid
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('wta', node)
        if value is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            self.wta = value
            self.validate_WTimeType(self.wta)    # validate type WTimeType
        value = find_attr_value_('wtd', node)
        if value is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            self.wtd = value
            self.validate_WTimeType(self.wtd)    # validate type WTimeType
        value = find_attr_value_('tpl', node)
        if value is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            self.tpl = value
            self.validate_TiplocType(self.tpl)    # validate type TiplocType
        value = find_attr_value_('act', node)
        if value is not None and 'act' not in already_processed:
            already_processed.add('act')
            self.act = value
            self.validate_ActivityType(self.act)    # validate type ActivityType
        value = find_attr_value_('planAct', node)
        if value is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            self.planAct = value
            self.validate_ActivityType(self.planAct)    # validate type ActivityType
        value = find_attr_value_('can', node)
        if value is not None and 'can' not in already_processed:
            already_processed.add('can')
            if value in ('true', '1'):
                self.can = True
            elif value in ('false', '0'):
                self.can = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('fid', node)
        if value is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            self.fid = value
            self.validate_FormationIDType(self.fid)    # validate type FormationIDType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class OPOR


class IP(GeneratedsSuper):
    """Defines aPassenger Intermediate Calling PointWorking Scheduled Time of
    ArrivalWorking Scheduled Time of DepartureA delay value that is implied
    by a change to the service's route. This value has been added to the
    forecast lateness of the service at the previous schedule location when
    calculating the expected lateness of arrival at this location.TIPLOC of
    False Destination to be used at this location"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, wta=None, wtd=None, rdelay='0', fd=None, tpl=None, act='  ', planAct=None, can=False, fid=None, pta=None, ptd=None, avgLoading=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.wta = _cast(None, wta)
        self.wta_nsprefix_ = None
        self.wtd = _cast(None, wtd)
        self.wtd_nsprefix_ = None
        self.rdelay = _cast(None, rdelay)
        self.rdelay_nsprefix_ = None
        self.fd = _cast(None, fd)
        self.fd_nsprefix_ = None
        self.tpl = _cast(None, tpl)
        self.tpl_nsprefix_ = None
        self.act = _cast(None, act)
        self.act_nsprefix_ = None
        self.planAct = _cast(None, planAct)
        self.planAct_nsprefix_ = None
        self.can = _cast(bool, can)
        self.can_nsprefix_ = None
        self.fid = _cast(None, fid)
        self.fid_nsprefix_ = None
        self.pta = _cast(None, pta)
        self.pta_nsprefix_ = None
        self.ptd = _cast(None, ptd)
        self.ptd_nsprefix_ = None
        self.avgLoading = _cast(None, avgLoading)
        self.avgLoading_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, IP)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if IP.subclass:
            return IP.subclass(*args_, **kwargs_)
        else:
            return IP(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_WTimeType(self, value):
        # Validate type ct:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_DelayValueType(self, value):
        # Validate type ct:DelayValueType, a restriction on xs:short.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ActivityType(self, value):
        # Validate type ct:ActivityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_ActivityType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ActivityType_patterns_, ))
    validate_ActivityType_patterns_ = [['^(([A-Z0-9\\- ][A-Z0-9\\- ]){1,6})$']]
    def validate_FormationIDType(self, value):
        # Validate type ct3:FormationIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_RTTITimeType(self, value):
        # Validate type ct:RTTITimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_RTTITimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_RTTITimeType_patterns_, ))
    validate_RTTITimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9])$']]
    def validate_LoadingValue(self, value):
        # Validate type ct3:LoadingValue, a restriction on xs:unsignedInt.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on LoadingValue' % {"value": value, "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='IP', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('IP')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='IP')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='IP', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='IP'):
        if 'wta' not in already_processed:
            already_processed.add('wta')
            outfile.write(' wta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wta), input_name='wta')), ))
        if 'wtd' not in already_processed:
            already_processed.add('wtd')
            outfile.write(' wtd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtd), input_name='wtd')), ))
        if self.rdelay != 0 and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            outfile.write(' rdelay="%s"' % self.gds_format_integer(self.rdelay, input_name='rdelay'))
        if self.fd is not None and 'fd' not in already_processed:
            already_processed.add('fd')
            outfile.write(' fd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fd), input_name='fd')), ))
        if 'tpl' not in already_processed:
            already_processed.add('tpl')
            outfile.write(' tpl=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tpl), input_name='tpl')), ))
        if self.act != "  " and 'act' not in already_processed:
            already_processed.add('act')
            outfile.write(' act=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.act), input_name='act')), ))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            outfile.write(' planAct=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.planAct), input_name='planAct')), ))
        if self.can and 'can' not in already_processed:
            already_processed.add('can')
            outfile.write(' can="%s"' % self.gds_format_boolean(self.can, input_name='can'))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            outfile.write(' fid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fid), input_name='fid')), ))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            outfile.write(' pta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.pta), input_name='pta')), ))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            outfile.write(' ptd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ptd), input_name='ptd')), ))
        if self.avgLoading is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            outfile.write(' avgLoading="%s"' % self.gds_format_integer(self.avgLoading, input_name='avgLoading'))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='IP', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='IP', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.wta is not None:
            element.set('wta', self.gds_format_string(self.wta))
        if self.wtd is not None:
            element.set('wtd', self.gds_format_string(self.wtd))
        if self.rdelay is not None:
            element.set('rdelay', self.gds_format_integer(self.rdelay))
        if self.fd is not None:
            element.set('fd', self.gds_format_string(self.fd))
        if self.tpl is not None:
            element.set('tpl', self.gds_format_string(self.tpl))
        if self.act is not None:
            element.set('act', self.gds_format_string(self.act))
        if self.planAct is not None:
            element.set('planAct', self.gds_format_string(self.planAct))
        if self.can is not None:
            element.set('can', self.gds_format_boolean(self.can))
        if self.fid is not None:
            element.set('fid', self.gds_format_string(self.fid))
        if self.pta is not None:
            element.set('pta', self.gds_format_string(self.pta))
        if self.ptd is not None:
            element.set('ptd', self.gds_format_string(self.ptd))
        if self.avgLoading is not None:
            element.set('avgLoading', self.gds_format_integer(self.avgLoading))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='IP'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            showIndent(outfile, level)
            outfile.write('wta=%s,\n' % (self.wta,))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            showIndent(outfile, level)
            outfile.write('wtd=%s,\n' % (self.wtd,))
        if self.rdelay is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            showIndent(outfile, level)
            outfile.write('rdelay=%s,\n' % (self.rdelay,))
        if self.fd is not None and 'fd' not in already_processed:
            already_processed.add('fd')
            showIndent(outfile, level)
            outfile.write('fd=%s,\n' % (self.fd,))
        if self.tpl is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            showIndent(outfile, level)
            outfile.write('tpl=%s,\n' % (self.tpl,))
        if self.act is not None and 'act' not in already_processed:
            already_processed.add('act')
            showIndent(outfile, level)
            outfile.write('act=%s,\n' % (self.act,))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            showIndent(outfile, level)
            outfile.write('planAct=%s,\n' % (self.planAct,))
        if self.can is not None and 'can' not in already_processed:
            already_processed.add('can')
            showIndent(outfile, level)
            outfile.write('can=%s,\n' % (self.can,))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            showIndent(outfile, level)
            outfile.write('fid=%s,\n' % (self.fid,))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            showIndent(outfile, level)
            outfile.write('pta=%s,\n' % (self.pta,))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            showIndent(outfile, level)
            outfile.write('ptd=%s,\n' % (self.ptd,))
        if self.avgLoading is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            showIndent(outfile, level)
            outfile.write('avgLoading=%s,\n' % (self.avgLoading,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.IP_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.wta is not None:
            dbobj.wta = self.wta
        if self.wtd is not None:
            dbobj.wtd = self.wtd
        if self.rdelay is not None:
            dbobj.rdelay = self.rdelay
        if self.fd is not None:
            dbobj.fd = self.fd
        if self.tpl is not None:
            dbobj.tpl = self.tpl
        if self.act is not None:
            dbobj.act = self.act
        if self.planAct is not None:
            dbobj.planAct = self.planAct
        if self.can is not None:
            dbobj.can = self.can
        if self.fid is not None:
            dbobj.fid = self.fid
        if self.pta is not None:
            dbobj.pta = self.pta
        if self.ptd is not None:
            dbobj.ptd = self.ptd
        if self.avgLoading is not None:
            dbobj.avgLoading = self.avgLoading
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('wta', node)
        if value is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            self.wta = value
            self.validate_WTimeType(self.wta)    # validate type WTimeType
        value = find_attr_value_('wtd', node)
        if value is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            self.wtd = value
            self.validate_WTimeType(self.wtd)    # validate type WTimeType
        value = find_attr_value_('rdelay', node)
        if value is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            self.rdelay = self.gds_parse_integer(value, node, 'rdelay')
            self.validate_DelayValueType(self.rdelay)    # validate type DelayValueType
        value = find_attr_value_('fd', node)
        if value is not None and 'fd' not in already_processed:
            already_processed.add('fd')
            self.fd = value
            self.validate_TiplocType(self.fd)    # validate type TiplocType
        value = find_attr_value_('tpl', node)
        if value is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            self.tpl = value
            self.validate_TiplocType(self.tpl)    # validate type TiplocType
        value = find_attr_value_('act', node)
        if value is not None and 'act' not in already_processed:
            already_processed.add('act')
            self.act = value
            self.validate_ActivityType(self.act)    # validate type ActivityType
        value = find_attr_value_('planAct', node)
        if value is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            self.planAct = value
            self.validate_ActivityType(self.planAct)    # validate type ActivityType
        value = find_attr_value_('can', node)
        if value is not None and 'can' not in already_processed:
            already_processed.add('can')
            if value in ('true', '1'):
                self.can = True
            elif value in ('false', '0'):
                self.can = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('fid', node)
        if value is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            self.fid = value
            self.validate_FormationIDType(self.fid)    # validate type FormationIDType
        value = find_attr_value_('pta', node)
        if value is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            self.pta = value
            self.validate_RTTITimeType(self.pta)    # validate type RTTITimeType
        value = find_attr_value_('ptd', node)
        if value is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            self.ptd = value
            self.validate_RTTITimeType(self.ptd)    # validate type RTTITimeType
        value = find_attr_value_('avgLoading', node)
        if value is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            self.avgLoading = self.gds_parse_integer(value, node, 'avgLoading')
            self.validate_LoadingValue(self.avgLoading)    # validate type LoadingValue
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class IP


class OPIP(GeneratedsSuper):
    """Defines an Operational Intermediate Calling PointWorking Scheduled Time
    of ArrivalWorking Scheduled Time of DepartureA delay value that is
    implied by a change to the service's route. This value has been added
    to the forecast lateness of the service at the previous schedule
    location when calculating the expected lateness of arrival at this
    location."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, wta=None, wtd=None, rdelay='0', tpl=None, act='  ', planAct=None, can=False, fid=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.wta = _cast(None, wta)
        self.wta_nsprefix_ = None
        self.wtd = _cast(None, wtd)
        self.wtd_nsprefix_ = None
        self.rdelay = _cast(None, rdelay)
        self.rdelay_nsprefix_ = None
        self.tpl = _cast(None, tpl)
        self.tpl_nsprefix_ = None
        self.act = _cast(None, act)
        self.act_nsprefix_ = None
        self.planAct = _cast(None, planAct)
        self.planAct_nsprefix_ = None
        self.can = _cast(bool, can)
        self.can_nsprefix_ = None
        self.fid = _cast(None, fid)
        self.fid_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OPIP)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OPIP.subclass:
            return OPIP.subclass(*args_, **kwargs_)
        else:
            return OPIP(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_WTimeType(self, value):
        # Validate type ct:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_DelayValueType(self, value):
        # Validate type ct:DelayValueType, a restriction on xs:short.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ActivityType(self, value):
        # Validate type ct:ActivityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_ActivityType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ActivityType_patterns_, ))
    validate_ActivityType_patterns_ = [['^(([A-Z0-9\\- ][A-Z0-9\\- ]){1,6})$']]
    def validate_FormationIDType(self, value):
        # Validate type ct3:FormationIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='OPIP', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OPIP')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OPIP')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OPIP', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='OPIP'):
        if 'wta' not in already_processed:
            already_processed.add('wta')
            outfile.write(' wta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wta), input_name='wta')), ))
        if 'wtd' not in already_processed:
            already_processed.add('wtd')
            outfile.write(' wtd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtd), input_name='wtd')), ))
        if self.rdelay != 0 and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            outfile.write(' rdelay="%s"' % self.gds_format_integer(self.rdelay, input_name='rdelay'))
        if 'tpl' not in already_processed:
            already_processed.add('tpl')
            outfile.write(' tpl=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tpl), input_name='tpl')), ))
        if self.act != "  " and 'act' not in already_processed:
            already_processed.add('act')
            outfile.write(' act=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.act), input_name='act')), ))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            outfile.write(' planAct=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.planAct), input_name='planAct')), ))
        if self.can and 'can' not in already_processed:
            already_processed.add('can')
            outfile.write(' can="%s"' % self.gds_format_boolean(self.can, input_name='can'))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            outfile.write(' fid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fid), input_name='fid')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='OPIP', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='OPIP', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.wta is not None:
            element.set('wta', self.gds_format_string(self.wta))
        if self.wtd is not None:
            element.set('wtd', self.gds_format_string(self.wtd))
        if self.rdelay is not None:
            element.set('rdelay', self.gds_format_integer(self.rdelay))
        if self.tpl is not None:
            element.set('tpl', self.gds_format_string(self.tpl))
        if self.act is not None:
            element.set('act', self.gds_format_string(self.act))
        if self.planAct is not None:
            element.set('planAct', self.gds_format_string(self.planAct))
        if self.can is not None:
            element.set('can', self.gds_format_boolean(self.can))
        if self.fid is not None:
            element.set('fid', self.gds_format_string(self.fid))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='OPIP'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            showIndent(outfile, level)
            outfile.write('wta=%s,\n' % (self.wta,))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            showIndent(outfile, level)
            outfile.write('wtd=%s,\n' % (self.wtd,))
        if self.rdelay is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            showIndent(outfile, level)
            outfile.write('rdelay=%s,\n' % (self.rdelay,))
        if self.tpl is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            showIndent(outfile, level)
            outfile.write('tpl=%s,\n' % (self.tpl,))
        if self.act is not None and 'act' not in already_processed:
            already_processed.add('act')
            showIndent(outfile, level)
            outfile.write('act=%s,\n' % (self.act,))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            showIndent(outfile, level)
            outfile.write('planAct=%s,\n' % (self.planAct,))
        if self.can is not None and 'can' not in already_processed:
            already_processed.add('can')
            showIndent(outfile, level)
            outfile.write('can=%s,\n' % (self.can,))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            showIndent(outfile, level)
            outfile.write('fid=%s,\n' % (self.fid,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.OPIP_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.wta is not None:
            dbobj.wta = self.wta
        if self.wtd is not None:
            dbobj.wtd = self.wtd
        if self.rdelay is not None:
            dbobj.rdelay = self.rdelay
        if self.tpl is not None:
            dbobj.tpl = self.tpl
        if self.act is not None:
            dbobj.act = self.act
        if self.planAct is not None:
            dbobj.planAct = self.planAct
        if self.can is not None:
            dbobj.can = self.can
        if self.fid is not None:
            dbobj.fid = self.fid
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('wta', node)
        if value is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            self.wta = value
            self.validate_WTimeType(self.wta)    # validate type WTimeType
        value = find_attr_value_('wtd', node)
        if value is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            self.wtd = value
            self.validate_WTimeType(self.wtd)    # validate type WTimeType
        value = find_attr_value_('rdelay', node)
        if value is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            self.rdelay = self.gds_parse_integer(value, node, 'rdelay')
            self.validate_DelayValueType(self.rdelay)    # validate type DelayValueType
        value = find_attr_value_('tpl', node)
        if value is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            self.tpl = value
            self.validate_TiplocType(self.tpl)    # validate type TiplocType
        value = find_attr_value_('act', node)
        if value is not None and 'act' not in already_processed:
            already_processed.add('act')
            self.act = value
            self.validate_ActivityType(self.act)    # validate type ActivityType
        value = find_attr_value_('planAct', node)
        if value is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            self.planAct = value
            self.validate_ActivityType(self.planAct)    # validate type ActivityType
        value = find_attr_value_('can', node)
        if value is not None and 'can' not in already_processed:
            already_processed.add('can')
            if value in ('true', '1'):
                self.can = True
            elif value in ('false', '0'):
                self.can = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('fid', node)
        if value is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            self.fid = value
            self.validate_FormationIDType(self.fid)    # validate type FormationIDType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class OPIP


class PP(GeneratedsSuper):
    """Defines an Intermediate Passing PointWorking Scheduled Time of PassingA
    delay value that is implied by a change to the service's route. This
    value has been added to the forecast lateness of the service at the
    previous schedule location when calculating the expected lateness of
    passing this location."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, wtp=None, rdelay='0', tpl=None, act='  ', planAct=None, can=False, fid=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.wtp = _cast(None, wtp)
        self.wtp_nsprefix_ = None
        self.rdelay = _cast(None, rdelay)
        self.rdelay_nsprefix_ = None
        self.tpl = _cast(None, tpl)
        self.tpl_nsprefix_ = None
        self.act = _cast(None, act)
        self.act_nsprefix_ = None
        self.planAct = _cast(None, planAct)
        self.planAct_nsprefix_ = None
        self.can = _cast(bool, can)
        self.can_nsprefix_ = None
        self.fid = _cast(None, fid)
        self.fid_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PP)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PP.subclass:
            return PP.subclass(*args_, **kwargs_)
        else:
            return PP(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_WTimeType(self, value):
        # Validate type ct:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_DelayValueType(self, value):
        # Validate type ct:DelayValueType, a restriction on xs:short.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ActivityType(self, value):
        # Validate type ct:ActivityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_ActivityType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ActivityType_patterns_, ))
    validate_ActivityType_patterns_ = [['^(([A-Z0-9\\- ][A-Z0-9\\- ]){1,6})$']]
    def validate_FormationIDType(self, value):
        # Validate type ct3:FormationIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='PP', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PP')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PP')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PP', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='PP'):
        if 'wtp' not in already_processed:
            already_processed.add('wtp')
            outfile.write(' wtp=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtp), input_name='wtp')), ))
        if self.rdelay != 0 and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            outfile.write(' rdelay="%s"' % self.gds_format_integer(self.rdelay, input_name='rdelay'))
        if 'tpl' not in already_processed:
            already_processed.add('tpl')
            outfile.write(' tpl=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tpl), input_name='tpl')), ))
        if self.act != "  " and 'act' not in already_processed:
            already_processed.add('act')
            outfile.write(' act=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.act), input_name='act')), ))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            outfile.write(' planAct=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.planAct), input_name='planAct')), ))
        if self.can and 'can' not in already_processed:
            already_processed.add('can')
            outfile.write(' can="%s"' % self.gds_format_boolean(self.can, input_name='can'))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            outfile.write(' fid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fid), input_name='fid')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='PP', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='PP', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.wtp is not None:
            element.set('wtp', self.gds_format_string(self.wtp))
        if self.rdelay is not None:
            element.set('rdelay', self.gds_format_integer(self.rdelay))
        if self.tpl is not None:
            element.set('tpl', self.gds_format_string(self.tpl))
        if self.act is not None:
            element.set('act', self.gds_format_string(self.act))
        if self.planAct is not None:
            element.set('planAct', self.gds_format_string(self.planAct))
        if self.can is not None:
            element.set('can', self.gds_format_boolean(self.can))
        if self.fid is not None:
            element.set('fid', self.gds_format_string(self.fid))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='PP'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.wtp is not None and 'wtp' not in already_processed:
            already_processed.add('wtp')
            showIndent(outfile, level)
            outfile.write('wtp=%s,\n' % (self.wtp,))
        if self.rdelay is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            showIndent(outfile, level)
            outfile.write('rdelay=%s,\n' % (self.rdelay,))
        if self.tpl is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            showIndent(outfile, level)
            outfile.write('tpl=%s,\n' % (self.tpl,))
        if self.act is not None and 'act' not in already_processed:
            already_processed.add('act')
            showIndent(outfile, level)
            outfile.write('act=%s,\n' % (self.act,))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            showIndent(outfile, level)
            outfile.write('planAct=%s,\n' % (self.planAct,))
        if self.can is not None and 'can' not in already_processed:
            already_processed.add('can')
            showIndent(outfile, level)
            outfile.write('can=%s,\n' % (self.can,))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            showIndent(outfile, level)
            outfile.write('fid=%s,\n' % (self.fid,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.PP_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.wtp is not None:
            dbobj.wtp = self.wtp
        if self.rdelay is not None:
            dbobj.rdelay = self.rdelay
        if self.tpl is not None:
            dbobj.tpl = self.tpl
        if self.act is not None:
            dbobj.act = self.act
        if self.planAct is not None:
            dbobj.planAct = self.planAct
        if self.can is not None:
            dbobj.can = self.can
        if self.fid is not None:
            dbobj.fid = self.fid
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('wtp', node)
        if value is not None and 'wtp' not in already_processed:
            already_processed.add('wtp')
            self.wtp = value
            self.validate_WTimeType(self.wtp)    # validate type WTimeType
        value = find_attr_value_('rdelay', node)
        if value is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            self.rdelay = self.gds_parse_integer(value, node, 'rdelay')
            self.validate_DelayValueType(self.rdelay)    # validate type DelayValueType
        value = find_attr_value_('tpl', node)
        if value is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            self.tpl = value
            self.validate_TiplocType(self.tpl)    # validate type TiplocType
        value = find_attr_value_('act', node)
        if value is not None and 'act' not in already_processed:
            already_processed.add('act')
            self.act = value
            self.validate_ActivityType(self.act)    # validate type ActivityType
        value = find_attr_value_('planAct', node)
        if value is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            self.planAct = value
            self.validate_ActivityType(self.planAct)    # validate type ActivityType
        value = find_attr_value_('can', node)
        if value is not None and 'can' not in already_processed:
            already_processed.add('can')
            if value in ('true', '1'):
                self.can = True
            elif value in ('false', '0'):
                self.can = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('fid', node)
        if value is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            self.fid = value
            self.validate_FormationIDType(self.fid)    # validate type FormationIDType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class PP


class DT(GeneratedsSuper):
    """Defines a Passenger Destination Calling pointWorking Scheduled Time of
    ArrivalWorking Scheduled Time of DepartureA delay value that is implied
    by a change to the service's route. This value has been added to the
    forecast lateness of the service at the previous schedule location when
    calculating the expected lateness of arrival at this location."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, wta=None, wtd=None, rdelay='0', tpl=None, act='  ', planAct=None, can=False, fid=None, pta=None, ptd=None, avgLoading=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.wta = _cast(None, wta)
        self.wta_nsprefix_ = None
        self.wtd = _cast(None, wtd)
        self.wtd_nsprefix_ = None
        self.rdelay = _cast(None, rdelay)
        self.rdelay_nsprefix_ = None
        self.tpl = _cast(None, tpl)
        self.tpl_nsprefix_ = None
        self.act = _cast(None, act)
        self.act_nsprefix_ = None
        self.planAct = _cast(None, planAct)
        self.planAct_nsprefix_ = None
        self.can = _cast(bool, can)
        self.can_nsprefix_ = None
        self.fid = _cast(None, fid)
        self.fid_nsprefix_ = None
        self.pta = _cast(None, pta)
        self.pta_nsprefix_ = None
        self.ptd = _cast(None, ptd)
        self.ptd_nsprefix_ = None
        self.avgLoading = _cast(None, avgLoading)
        self.avgLoading_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DT)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DT.subclass:
            return DT.subclass(*args_, **kwargs_)
        else:
            return DT(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_WTimeType(self, value):
        # Validate type ct:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_DelayValueType(self, value):
        # Validate type ct:DelayValueType, a restriction on xs:short.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ActivityType(self, value):
        # Validate type ct:ActivityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_ActivityType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ActivityType_patterns_, ))
    validate_ActivityType_patterns_ = [['^(([A-Z0-9\\- ][A-Z0-9\\- ]){1,6})$']]
    def validate_FormationIDType(self, value):
        # Validate type ct3:FormationIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_RTTITimeType(self, value):
        # Validate type ct:RTTITimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_RTTITimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_RTTITimeType_patterns_, ))
    validate_RTTITimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9])$']]
    def validate_LoadingValue(self, value):
        # Validate type ct3:LoadingValue, a restriction on xs:unsignedInt.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on LoadingValue' % {"value": value, "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='DT', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DT')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DT')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DT', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='DT'):
        if 'wta' not in already_processed:
            already_processed.add('wta')
            outfile.write(' wta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wta), input_name='wta')), ))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            outfile.write(' wtd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtd), input_name='wtd')), ))
        if self.rdelay != 0 and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            outfile.write(' rdelay="%s"' % self.gds_format_integer(self.rdelay, input_name='rdelay'))
        if 'tpl' not in already_processed:
            already_processed.add('tpl')
            outfile.write(' tpl=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tpl), input_name='tpl')), ))
        if self.act != "  " and 'act' not in already_processed:
            already_processed.add('act')
            outfile.write(' act=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.act), input_name='act')), ))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            outfile.write(' planAct=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.planAct), input_name='planAct')), ))
        if self.can and 'can' not in already_processed:
            already_processed.add('can')
            outfile.write(' can="%s"' % self.gds_format_boolean(self.can, input_name='can'))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            outfile.write(' fid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fid), input_name='fid')), ))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            outfile.write(' pta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.pta), input_name='pta')), ))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            outfile.write(' ptd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ptd), input_name='ptd')), ))
        if self.avgLoading is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            outfile.write(' avgLoading="%s"' % self.gds_format_integer(self.avgLoading, input_name='avgLoading'))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='DT', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='DT', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.wta is not None:
            element.set('wta', self.gds_format_string(self.wta))
        if self.wtd is not None:
            element.set('wtd', self.gds_format_string(self.wtd))
        if self.rdelay is not None:
            element.set('rdelay', self.gds_format_integer(self.rdelay))
        if self.tpl is not None:
            element.set('tpl', self.gds_format_string(self.tpl))
        if self.act is not None:
            element.set('act', self.gds_format_string(self.act))
        if self.planAct is not None:
            element.set('planAct', self.gds_format_string(self.planAct))
        if self.can is not None:
            element.set('can', self.gds_format_boolean(self.can))
        if self.fid is not None:
            element.set('fid', self.gds_format_string(self.fid))
        if self.pta is not None:
            element.set('pta', self.gds_format_string(self.pta))
        if self.ptd is not None:
            element.set('ptd', self.gds_format_string(self.ptd))
        if self.avgLoading is not None:
            element.set('avgLoading', self.gds_format_integer(self.avgLoading))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='DT'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            showIndent(outfile, level)
            outfile.write('wta=%s,\n' % (self.wta,))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            showIndent(outfile, level)
            outfile.write('wtd=%s,\n' % (self.wtd,))
        if self.rdelay is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            showIndent(outfile, level)
            outfile.write('rdelay=%s,\n' % (self.rdelay,))
        if self.tpl is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            showIndent(outfile, level)
            outfile.write('tpl=%s,\n' % (self.tpl,))
        if self.act is not None and 'act' not in already_processed:
            already_processed.add('act')
            showIndent(outfile, level)
            outfile.write('act=%s,\n' % (self.act,))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            showIndent(outfile, level)
            outfile.write('planAct=%s,\n' % (self.planAct,))
        if self.can is not None and 'can' not in already_processed:
            already_processed.add('can')
            showIndent(outfile, level)
            outfile.write('can=%s,\n' % (self.can,))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            showIndent(outfile, level)
            outfile.write('fid=%s,\n' % (self.fid,))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            showIndent(outfile, level)
            outfile.write('pta=%s,\n' % (self.pta,))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            showIndent(outfile, level)
            outfile.write('ptd=%s,\n' % (self.ptd,))
        if self.avgLoading is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            showIndent(outfile, level)
            outfile.write('avgLoading=%s,\n' % (self.avgLoading,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.DT_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.wta is not None:
            dbobj.wta = self.wta
        if self.wtd is not None:
            dbobj.wtd = self.wtd
        if self.rdelay is not None:
            dbobj.rdelay = self.rdelay
        if self.tpl is not None:
            dbobj.tpl = self.tpl
        if self.act is not None:
            dbobj.act = self.act
        if self.planAct is not None:
            dbobj.planAct = self.planAct
        if self.can is not None:
            dbobj.can = self.can
        if self.fid is not None:
            dbobj.fid = self.fid
        if self.pta is not None:
            dbobj.pta = self.pta
        if self.ptd is not None:
            dbobj.ptd = self.ptd
        if self.avgLoading is not None:
            dbobj.avgLoading = self.avgLoading
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('wta', node)
        if value is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            self.wta = value
            self.validate_WTimeType(self.wta)    # validate type WTimeType
        value = find_attr_value_('wtd', node)
        if value is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            self.wtd = value
            self.validate_WTimeType(self.wtd)    # validate type WTimeType
        value = find_attr_value_('rdelay', node)
        if value is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            self.rdelay = self.gds_parse_integer(value, node, 'rdelay')
            self.validate_DelayValueType(self.rdelay)    # validate type DelayValueType
        value = find_attr_value_('tpl', node)
        if value is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            self.tpl = value
            self.validate_TiplocType(self.tpl)    # validate type TiplocType
        value = find_attr_value_('act', node)
        if value is not None and 'act' not in already_processed:
            already_processed.add('act')
            self.act = value
            self.validate_ActivityType(self.act)    # validate type ActivityType
        value = find_attr_value_('planAct', node)
        if value is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            self.planAct = value
            self.validate_ActivityType(self.planAct)    # validate type ActivityType
        value = find_attr_value_('can', node)
        if value is not None and 'can' not in already_processed:
            already_processed.add('can')
            if value in ('true', '1'):
                self.can = True
            elif value in ('false', '0'):
                self.can = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('fid', node)
        if value is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            self.fid = value
            self.validate_FormationIDType(self.fid)    # validate type FormationIDType
        value = find_attr_value_('pta', node)
        if value is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            self.pta = value
            self.validate_RTTITimeType(self.pta)    # validate type RTTITimeType
        value = find_attr_value_('ptd', node)
        if value is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            self.ptd = value
            self.validate_RTTITimeType(self.ptd)    # validate type RTTITimeType
        value = find_attr_value_('avgLoading', node)
        if value is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            self.avgLoading = self.gds_parse_integer(value, node, 'avgLoading')
            self.validate_LoadingValue(self.avgLoading)    # validate type LoadingValue
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DT


class OPDT(GeneratedsSuper):
    """Defines an Operational Destination Calling pointWorking Scheduled Time
    of ArrivalWorking Scheduled Time of DepartureA delay value that is
    implied by a change to the service's route. This value has been added
    to the forecast lateness of the service at the previous schedule
    location when calculating the expected lateness of arrival at this
    location."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, wta=None, wtd=None, rdelay='0', tpl=None, act='  ', planAct=None, can=False, fid=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.wta = _cast(None, wta)
        self.wta_nsprefix_ = None
        self.wtd = _cast(None, wtd)
        self.wtd_nsprefix_ = None
        self.rdelay = _cast(None, rdelay)
        self.rdelay_nsprefix_ = None
        self.tpl = _cast(None, tpl)
        self.tpl_nsprefix_ = None
        self.act = _cast(None, act)
        self.act_nsprefix_ = None
        self.planAct = _cast(None, planAct)
        self.planAct_nsprefix_ = None
        self.can = _cast(bool, can)
        self.can_nsprefix_ = None
        self.fid = _cast(None, fid)
        self.fid_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OPDT)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OPDT.subclass:
            return OPDT.subclass(*args_, **kwargs_)
        else:
            return OPDT(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_WTimeType(self, value):
        # Validate type ct:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_DelayValueType(self, value):
        # Validate type ct:DelayValueType, a restriction on xs:short.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ActivityType(self, value):
        # Validate type ct:ActivityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_ActivityType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ActivityType_patterns_, ))
    validate_ActivityType_patterns_ = [['^(([A-Z0-9\\- ][A-Z0-9\\- ]){1,6})$']]
    def validate_FormationIDType(self, value):
        # Validate type ct3:FormationIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='OPDT', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OPDT')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OPDT')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OPDT', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='OPDT'):
        if 'wta' not in already_processed:
            already_processed.add('wta')
            outfile.write(' wta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wta), input_name='wta')), ))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            outfile.write(' wtd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtd), input_name='wtd')), ))
        if self.rdelay != 0 and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            outfile.write(' rdelay="%s"' % self.gds_format_integer(self.rdelay, input_name='rdelay'))
        if 'tpl' not in already_processed:
            already_processed.add('tpl')
            outfile.write(' tpl=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tpl), input_name='tpl')), ))
        if self.act != "  " and 'act' not in already_processed:
            already_processed.add('act')
            outfile.write(' act=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.act), input_name='act')), ))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            outfile.write(' planAct=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.planAct), input_name='planAct')), ))
        if self.can and 'can' not in already_processed:
            already_processed.add('can')
            outfile.write(' can="%s"' % self.gds_format_boolean(self.can, input_name='can'))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            outfile.write(' fid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fid), input_name='fid')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='OPDT', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='OPDT', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.wta is not None:
            element.set('wta', self.gds_format_string(self.wta))
        if self.wtd is not None:
            element.set('wtd', self.gds_format_string(self.wtd))
        if self.rdelay is not None:
            element.set('rdelay', self.gds_format_integer(self.rdelay))
        if self.tpl is not None:
            element.set('tpl', self.gds_format_string(self.tpl))
        if self.act is not None:
            element.set('act', self.gds_format_string(self.act))
        if self.planAct is not None:
            element.set('planAct', self.gds_format_string(self.planAct))
        if self.can is not None:
            element.set('can', self.gds_format_boolean(self.can))
        if self.fid is not None:
            element.set('fid', self.gds_format_string(self.fid))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='OPDT'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            showIndent(outfile, level)
            outfile.write('wta=%s,\n' % (self.wta,))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            showIndent(outfile, level)
            outfile.write('wtd=%s,\n' % (self.wtd,))
        if self.rdelay is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            showIndent(outfile, level)
            outfile.write('rdelay=%s,\n' % (self.rdelay,))
        if self.tpl is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            showIndent(outfile, level)
            outfile.write('tpl=%s,\n' % (self.tpl,))
        if self.act is not None and 'act' not in already_processed:
            already_processed.add('act')
            showIndent(outfile, level)
            outfile.write('act=%s,\n' % (self.act,))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            showIndent(outfile, level)
            outfile.write('planAct=%s,\n' % (self.planAct,))
        if self.can is not None and 'can' not in already_processed:
            already_processed.add('can')
            showIndent(outfile, level)
            outfile.write('can=%s,\n' % (self.can,))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            showIndent(outfile, level)
            outfile.write('fid=%s,\n' % (self.fid,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.OPDT_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.wta is not None:
            dbobj.wta = self.wta
        if self.wtd is not None:
            dbobj.wtd = self.wtd
        if self.rdelay is not None:
            dbobj.rdelay = self.rdelay
        if self.tpl is not None:
            dbobj.tpl = self.tpl
        if self.act is not None:
            dbobj.act = self.act
        if self.planAct is not None:
            dbobj.planAct = self.planAct
        if self.can is not None:
            dbobj.can = self.can
        if self.fid is not None:
            dbobj.fid = self.fid
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('wta', node)
        if value is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            self.wta = value
            self.validate_WTimeType(self.wta)    # validate type WTimeType
        value = find_attr_value_('wtd', node)
        if value is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            self.wtd = value
            self.validate_WTimeType(self.wtd)    # validate type WTimeType
        value = find_attr_value_('rdelay', node)
        if value is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            self.rdelay = self.gds_parse_integer(value, node, 'rdelay')
            self.validate_DelayValueType(self.rdelay)    # validate type DelayValueType
        value = find_attr_value_('tpl', node)
        if value is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            self.tpl = value
            self.validate_TiplocType(self.tpl)    # validate type TiplocType
        value = find_attr_value_('act', node)
        if value is not None and 'act' not in already_processed:
            already_processed.add('act')
            self.act = value
            self.validate_ActivityType(self.act)    # validate type ActivityType
        value = find_attr_value_('planAct', node)
        if value is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            self.planAct = value
            self.validate_ActivityType(self.planAct)    # validate type ActivityType
        value = find_attr_value_('can', node)
        if value is not None and 'can' not in already_processed:
            already_processed.add('can')
            if value in ('true', '1'):
                self.can = True
            elif value in ('false', '0'):
                self.can = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('fid', node)
        if value is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            self.fid = value
            self.validate_FormationIDType(self.fid)    # validate type FormationIDType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class OPDT


class Schedule(GeneratedsSuper):
    """Train ScheduleRTTI unique Train IDTrain UIDTrain ID (Headcode)Retail
    Service Identifier. Note that this may be either a full 8-character
    "portion identifier", or a base 6-character identifier, according to
    the available information provided to Darwin.Scheduled Start DateATOC
    CodeType of service, i.e. Train/Bus/Ship.Category of service.True if
    Darwin classifies the train category as a passenger service.Indicates
    if this service is active in Darwin. Note that schedules should be
    assumed to be inactive until a message is received to indicate
    otherwise.Service has been deleted and should not be
    used/displayed.Indicates if this service is a charter service."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, rid=None, uid=None, trainId=None, rsid=None, ssd=None, toc=None, status='P', trainCat='OO', isPassengerSvc=True, isActive=True, deleted=False, isCharter=False, OR=None, OPOR=None, IP=None, OPIP=None, PP=None, DT=None, OPDT=None, cancelReason=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.rid = _cast(None, rid)
        self.rid_nsprefix_ = None
        self.uid = _cast(None, uid)
        self.uid_nsprefix_ = None
        self.trainId = _cast(None, trainId)
        self.trainId_nsprefix_ = None
        self.rsid = _cast(None, rsid)
        self.rsid_nsprefix_ = None
        self.ssd = _cast(None, ssd)
        self.ssd_nsprefix_ = None
        self.toc = _cast(None, toc)
        self.toc_nsprefix_ = None
        self.status = _cast(None, status)
        self.status_nsprefix_ = None
        self.trainCat = _cast(None, trainCat)
        self.trainCat_nsprefix_ = None
        self.isPassengerSvc = _cast(bool, isPassengerSvc)
        self.isPassengerSvc_nsprefix_ = None
        self.isActive = _cast(bool, isActive)
        self.isActive_nsprefix_ = None
        self.deleted = _cast(bool, deleted)
        self.deleted_nsprefix_ = None
        self.isCharter = _cast(bool, isCharter)
        self.isCharter_nsprefix_ = None
        if OR is None:
            self.OR = []
        else:
            self.OR = OR
        self.OR_nsprefix_ = None
        if OPOR is None:
            self.OPOR = []
        else:
            self.OPOR = OPOR
        self.OPOR_nsprefix_ = None
        if IP is None:
            self.IP = []
        else:
            self.IP = IP
        self.IP_nsprefix_ = None
        if OPIP is None:
            self.OPIP = []
        else:
            self.OPIP = OPIP
        self.OPIP_nsprefix_ = None
        if PP is None:
            self.PP = []
        else:
            self.PP = PP
        self.PP_nsprefix_ = None
        if DT is None:
            self.DT = []
        else:
            self.DT = DT
        self.DT_nsprefix_ = None
        if OPDT is None:
            self.OPDT = []
        else:
            self.OPDT = OPDT
        self.OPDT_nsprefix_ = None
        self.cancelReason = cancelReason
        self.cancelReason_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Schedule)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Schedule.subclass:
            return Schedule.subclass(*args_, **kwargs_)
        else:
            return Schedule(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_RIDType(self, value):
        # Validate type ct:RIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on RIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_UIDType(self, value):
        # Validate type ct:UIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 6:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on UIDType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_TrainIdType(self, value):
        # Validate type ct:TrainIdType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on TrainIdType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TrainIdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TrainIdType_patterns_, ))
    validate_TrainIdType_patterns_ = [['^([0-9][A-Z][0-9][0-9])$']]
    def validate_RSIDType(self, value):
        # Validate type ct2:RSIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on RSIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 6:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on RSIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_RTTIDateType(self, value):
        # Validate type ct:RTTIDateType, a restriction on xs:date.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, datetime_.date):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (datetime_.date)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def validate_TOCType(self, value):
        # Validate type ct:TOCType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on TOCType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_CIFTrainStatusType(self, value):
        # Validate type ct:CIFTrainStatusType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on CIFTrainStatusType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_CIFTrainStatusType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_CIFTrainStatusType_patterns_, ))
    validate_CIFTrainStatusType_patterns_ = [['^([BFPST12345])$']]
    def validate_CIFTrainCategoryType(self, value):
        # Validate type ct:CIFTrainCategoryType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CIFTrainCategoryType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CIFTrainCategoryType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.OR or
            self.OPOR or
            self.IP or
            self.OPIP or
            self.PP or
            self.DT or
            self.OPDT or
            self.cancelReason is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:ct="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='Schedule', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Schedule')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Schedule')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Schedule', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='Schedule'):
        if 'rid' not in already_processed:
            already_processed.add('rid')
            outfile.write(' rid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.rid), input_name='rid')), ))
        if 'uid' not in already_processed:
            already_processed.add('uid')
            outfile.write(' uid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.uid), input_name='uid')), ))
        if 'trainId' not in already_processed:
            already_processed.add('trainId')
            outfile.write(' trainId=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.trainId), input_name='trainId')), ))
        if self.rsid is not None and 'rsid' not in already_processed:
            already_processed.add('rsid')
            outfile.write(' rsid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.rsid), input_name='rsid')), ))
        if 'ssd' not in already_processed:
            already_processed.add('ssd')
            outfile.write(' ssd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ssd), input_name='ssd')), ))
        if 'toc' not in already_processed:
            already_processed.add('toc')
            outfile.write(' toc=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.toc), input_name='toc')), ))
        if self.status != "P" and 'status' not in already_processed:
            already_processed.add('status')
            outfile.write(' status=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.status), input_name='status')), ))
        if self.trainCat != "OO" and 'trainCat' not in already_processed:
            already_processed.add('trainCat')
            outfile.write(' trainCat=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.trainCat), input_name='trainCat')), ))
        if not self.isPassengerSvc and 'isPassengerSvc' not in already_processed:
            already_processed.add('isPassengerSvc')
            outfile.write(' isPassengerSvc="%s"' % self.gds_format_boolean(self.isPassengerSvc, input_name='isPassengerSvc'))
        if not self.isActive and 'isActive' not in already_processed:
            already_processed.add('isActive')
            outfile.write(' isActive="%s"' % self.gds_format_boolean(self.isActive, input_name='isActive'))
        if self.deleted and 'deleted' not in already_processed:
            already_processed.add('deleted')
            outfile.write(' deleted="%s"' % self.gds_format_boolean(self.deleted, input_name='deleted'))
        if self.isCharter and 'isCharter' not in already_processed:
            already_processed.add('isCharter')
            outfile.write(' isCharter="%s"' % self.gds_format_boolean(self.isCharter, input_name='isCharter'))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:ct="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='Schedule', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for OR_ in self.OR:
            namespaceprefix_ = self.OR_nsprefix_ + ':' if (UseCapturedNS_ and self.OR_nsprefix_) else ''
            OR_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OR', pretty_print=pretty_print)
        for OPOR_ in self.OPOR:
            namespaceprefix_ = self.OPOR_nsprefix_ + ':' if (UseCapturedNS_ and self.OPOR_nsprefix_) else ''
            OPOR_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OPOR', pretty_print=pretty_print)
        for IP_ in self.IP:
            namespaceprefix_ = self.IP_nsprefix_ + ':' if (UseCapturedNS_ and self.IP_nsprefix_) else ''
            IP_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IP', pretty_print=pretty_print)
        for OPIP_ in self.OPIP:
            namespaceprefix_ = self.OPIP_nsprefix_ + ':' if (UseCapturedNS_ and self.OPIP_nsprefix_) else ''
            OPIP_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OPIP', pretty_print=pretty_print)
        for PP_ in self.PP:
            namespaceprefix_ = self.PP_nsprefix_ + ':' if (UseCapturedNS_ and self.PP_nsprefix_) else ''
            PP_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='PP', pretty_print=pretty_print)
        for DT_ in self.DT:
            namespaceprefix_ = self.DT_nsprefix_ + ':' if (UseCapturedNS_ and self.DT_nsprefix_) else ''
            DT_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DT', pretty_print=pretty_print)
        for OPDT_ in self.OPDT:
            namespaceprefix_ = self.OPDT_nsprefix_ + ':' if (UseCapturedNS_ and self.OPDT_nsprefix_) else ''
            OPDT_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OPDT', pretty_print=pretty_print)
        if self.cancelReason is not None:
            namespaceprefix_ = self.cancelReason_nsprefix_ + ':' if (UseCapturedNS_ and self.cancelReason_nsprefix_) else ''
            self.cancelReason.export(outfile, level, namespaceprefix_, namespacedef_='', name_='cancelReason', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Schedule', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.rid is not None:
            element.set('rid', self.gds_format_string(self.rid))
        if self.uid is not None:
            element.set('uid', self.gds_format_string(self.uid))
        if self.trainId is not None:
            element.set('trainId', self.gds_format_string(self.trainId))
        if self.rsid is not None:
            element.set('rsid', self.gds_format_string(self.rsid))
        if self.ssd is not None:
            element.set('ssd', self.gds_format_date(self.ssd))
        if self.toc is not None:
            element.set('toc', self.gds_format_string(self.toc))
        if self.status is not None:
            element.set('status', self.gds_format_string(self.status))
        if self.trainCat is not None:
            element.set('trainCat', self.gds_format_string(self.trainCat))
        if self.isPassengerSvc is not None:
            element.set('isPassengerSvc', self.gds_format_boolean(self.isPassengerSvc))
        if self.isActive is not None:
            element.set('isActive', self.gds_format_boolean(self.isActive))
        if self.deleted is not None:
            element.set('deleted', self.gds_format_boolean(self.deleted))
        if self.isCharter is not None:
            element.set('isCharter', self.gds_format_boolean(self.isCharter))
        for OR_ in self.OR:
            OR_.to_etree(element, name_='OR', mapping_=mapping_)
        for OPOR_ in self.OPOR:
            OPOR_.to_etree(element, name_='OPOR', mapping_=mapping_)
        for IP_ in self.IP:
            IP_.to_etree(element, name_='IP', mapping_=mapping_)
        for OPIP_ in self.OPIP:
            OPIP_.to_etree(element, name_='OPIP', mapping_=mapping_)
        for PP_ in self.PP:
            PP_.to_etree(element, name_='PP', mapping_=mapping_)
        for DT_ in self.DT:
            DT_.to_etree(element, name_='DT', mapping_=mapping_)
        for OPDT_ in self.OPDT:
            OPDT_.to_etree(element, name_='OPDT', mapping_=mapping_)
        if self.cancelReason is not None:
            cancelReason_ = self.cancelReason
            cancelReason_.to_etree(element, name_='cancelReason', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='Schedule'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.rid is not None and 'rid' not in already_processed:
            already_processed.add('rid')
            showIndent(outfile, level)
            outfile.write('rid=%s,\n' % (self.rid,))
        if self.uid is not None and 'uid' not in already_processed:
            already_processed.add('uid')
            showIndent(outfile, level)
            outfile.write('uid=%s,\n' % (self.uid,))
        if self.trainId is not None and 'trainId' not in already_processed:
            already_processed.add('trainId')
            showIndent(outfile, level)
            outfile.write('trainId=%s,\n' % (self.trainId,))
        if self.rsid is not None and 'rsid' not in already_processed:
            already_processed.add('rsid')
            showIndent(outfile, level)
            outfile.write('rsid=%s,\n' % (self.rsid,))
        if self.ssd is not None and 'ssd' not in already_processed:
            already_processed.add('ssd')
            showIndent(outfile, level)
            outfile.write('ssd=%s,\n' % (self.ssd,))
        if self.toc is not None and 'toc' not in already_processed:
            already_processed.add('toc')
            showIndent(outfile, level)
            outfile.write('toc=%s,\n' % (self.toc,))
        if self.status is not None and 'status' not in already_processed:
            already_processed.add('status')
            showIndent(outfile, level)
            outfile.write('status=%s,\n' % (self.status,))
        if self.trainCat is not None and 'trainCat' not in already_processed:
            already_processed.add('trainCat')
            showIndent(outfile, level)
            outfile.write('trainCat=%s,\n' % (self.trainCat,))
        if self.isPassengerSvc is not None and 'isPassengerSvc' not in already_processed:
            already_processed.add('isPassengerSvc')
            showIndent(outfile, level)
            outfile.write('isPassengerSvc=%s,\n' % (self.isPassengerSvc,))
        if self.isActive is not None and 'isActive' not in already_processed:
            already_processed.add('isActive')
            showIndent(outfile, level)
            outfile.write('isActive=%s,\n' % (self.isActive,))
        if self.deleted is not None and 'deleted' not in already_processed:
            already_processed.add('deleted')
            showIndent(outfile, level)
            outfile.write('deleted=%s,\n' % (self.deleted,))
        if self.isCharter is not None and 'isCharter' not in already_processed:
            already_processed.add('isCharter')
            showIndent(outfile, level)
            outfile.write('isCharter=%s,\n' % (self.isCharter,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('OR=[\n')
        level += 1
        for OR_ in self.OR:
            showIndent(outfile, level)
            outfile.write('model_.OR(\n')
            OR_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('OPOR=[\n')
        level += 1
        for OPOR_ in self.OPOR:
            showIndent(outfile, level)
            outfile.write('model_.OPOR(\n')
            OPOR_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('IP=[\n')
        level += 1
        for IP_ in self.IP:
            showIndent(outfile, level)
            outfile.write('model_.IP(\n')
            IP_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('OPIP=[\n')
        level += 1
        for OPIP_ in self.OPIP:
            showIndent(outfile, level)
            outfile.write('model_.OPIP(\n')
            OPIP_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('PP=[\n')
        level += 1
        for PP_ in self.PP:
            showIndent(outfile, level)
            outfile.write('model_.PP(\n')
            PP_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('DT=[\n')
        level += 1
        for DT_ in self.DT:
            showIndent(outfile, level)
            outfile.write('model_.DT(\n')
            DT_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('OPDT=[\n')
        level += 1
        for OPDT_ in self.OPDT:
            showIndent(outfile, level)
            outfile.write('model_.OPDT(\n')
            OPDT_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.cancelReason is not None:
            showIndent(outfile, level)
            outfile.write('cancelReason=model_.DisruptionReasonType(\n')
            self.cancelReason.exportLiteral(outfile, level, name_='cancelReason')
            showIndent(outfile, level)
            outfile.write('),\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.Schedule_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.rid is not None:
            dbobj.rid = self.rid
        if self.uid is not None:
            dbobj.uid = self.uid
        if self.trainId is not None:
            dbobj.trainId = self.trainId
        if self.rsid is not None:
            dbobj.rsid = self.rsid
        if self.ssd is not None:
            dbobj.ssd = self.ssd
        if self.toc is not None:
            dbobj.toc = self.toc
        if self.status is not None:
            dbobj.status = self.status
        if self.trainCat is not None:
            dbobj.trainCat = self.trainCat
        if self.isPassengerSvc is not None:
            dbobj.isPassengerSvc = self.isPassengerSvc
        if self.isActive is not None:
            dbobj.isActive = self.isActive
        if self.deleted is not None:
            dbobj.deleted = self.deleted
        if self.isCharter is not None:
            dbobj.isCharter = self.isCharter
    def exportSQLAlchemyChildren(self, session, dbobj):
        for child in self.OR:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.OR.append(child_dbobj)
        for child in self.OPOR:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.OPOR.append(child_dbobj)
        for child in self.IP:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.IP.append(child_dbobj)
        for child in self.OPIP:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.OPIP.append(child_dbobj)
        for child in self.PP:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.PP.append(child_dbobj)
        for child in self.DT:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.DT.append(child_dbobj)
        for child in self.OPDT:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.OPDT.append(child_dbobj)
        if self.cancelReason is not None:
            child_dbobj = self.cancelReason.exportSQLAlchemy(session)
            dbobj.cancelReason = child_dbobj
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('rid', node)
        if value is not None and 'rid' not in already_processed:
            already_processed.add('rid')
            self.rid = value
            self.validate_RIDType(self.rid)    # validate type RIDType
        value = find_attr_value_('uid', node)
        if value is not None and 'uid' not in already_processed:
            already_processed.add('uid')
            self.uid = value
            self.validate_UIDType(self.uid)    # validate type UIDType
        value = find_attr_value_('trainId', node)
        if value is not None and 'trainId' not in already_processed:
            already_processed.add('trainId')
            self.trainId = value
            self.validate_TrainIdType(self.trainId)    # validate type TrainIdType
        value = find_attr_value_('rsid', node)
        if value is not None and 'rsid' not in already_processed:
            already_processed.add('rsid')
            self.rsid = value
            self.validate_RSIDType(self.rsid)    # validate type RSIDType
        value = find_attr_value_('ssd', node)
        if value is not None and 'ssd' not in already_processed:
            already_processed.add('ssd')
            try:
                self.ssd = self.gds_parse_date(value)
            except ValueError as exp:
                raise ValueError('Bad date attribute (ssd): %s' % exp)
            self.validate_RTTIDateType(self.ssd)    # validate type RTTIDateType
        value = find_attr_value_('toc', node)
        if value is not None and 'toc' not in already_processed:
            already_processed.add('toc')
            self.toc = value
            self.validate_TOCType(self.toc)    # validate type TOCType
        value = find_attr_value_('status', node)
        if value is not None and 'status' not in already_processed:
            already_processed.add('status')
            self.status = value
            self.validate_CIFTrainStatusType(self.status)    # validate type CIFTrainStatusType
        value = find_attr_value_('trainCat', node)
        if value is not None and 'trainCat' not in already_processed:
            already_processed.add('trainCat')
            self.trainCat = value
            self.validate_CIFTrainCategoryType(self.trainCat)    # validate type CIFTrainCategoryType
        value = find_attr_value_('isPassengerSvc', node)
        if value is not None and 'isPassengerSvc' not in already_processed:
            already_processed.add('isPassengerSvc')
            if value in ('true', '1'):
                self.isPassengerSvc = True
            elif value in ('false', '0'):
                self.isPassengerSvc = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('isActive', node)
        if value is not None and 'isActive' not in already_processed:
            already_processed.add('isActive')
            if value in ('true', '1'):
                self.isActive = True
            elif value in ('false', '0'):
                self.isActive = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('deleted', node)
        if value is not None and 'deleted' not in already_processed:
            already_processed.add('deleted')
            if value in ('true', '1'):
                self.deleted = True
            elif value in ('false', '0'):
                self.deleted = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('isCharter', node)
        if value is not None and 'isCharter' not in already_processed:
            already_processed.add('isCharter')
            if value in ('true', '1'):
                self.isCharter = True
            elif value in ('false', '0'):
                self.isCharter = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'OR':
            obj_ = OR.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OR.append(obj_)
            obj_.original_tagname_ = 'OR'
        elif nodeName_ == 'OPOR':
            obj_ = OPOR.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OPOR.append(obj_)
            obj_.original_tagname_ = 'OPOR'
        elif nodeName_ == 'IP':
            obj_ = IP.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IP.append(obj_)
            obj_.original_tagname_ = 'IP'
        elif nodeName_ == 'OPIP':
            obj_ = OPIP.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OPIP.append(obj_)
            obj_.original_tagname_ = 'OPIP'
        elif nodeName_ == 'PP':
            obj_ = PP.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PP.append(obj_)
            obj_.original_tagname_ = 'PP'
        elif nodeName_ == 'DT':
            obj_ = DT.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DT.append(obj_)
            obj_.original_tagname_ = 'DT'
        elif nodeName_ == 'OPDT':
            obj_ = OPDT.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OPDT.append(obj_)
            obj_.original_tagname_ = 'OPDT'
        elif nodeName_ == 'cancelReason':
            obj_ = DisruptionReasonType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.cancelReason = obj_
            obj_.original_tagname_ = 'cancelReason'
# end class Schedule


class DeactivatedSchedule(GeneratedsSuper):
    """Notification that a Train Schedule is now deactivated in Darwin.RTTI
    unique Train ID"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, rid=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.rid = _cast(None, rid)
        self.rid_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DeactivatedSchedule)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DeactivatedSchedule.subclass:
            return DeactivatedSchedule.subclass(*args_, **kwargs_)
        else:
            return DeactivatedSchedule(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_RIDType(self, value):
        # Validate type ct:RIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on RIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='DeactivatedSchedule', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DeactivatedSchedule')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DeactivatedSchedule')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DeactivatedSchedule', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='DeactivatedSchedule'):
        if 'rid' not in already_processed:
            already_processed.add('rid')
            outfile.write(' rid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.rid), input_name='rid')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='DeactivatedSchedule', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='DeactivatedSchedule', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.rid is not None:
            element.set('rid', self.gds_format_string(self.rid))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='DeactivatedSchedule'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.rid is not None and 'rid' not in already_processed:
            already_processed.add('rid')
            showIndent(outfile, level)
            outfile.write('rid=%s,\n' % (self.rid,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.DeactivatedSchedule_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.rid is not None:
            dbobj.rid = self.rid
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('rid', node)
        if value is not None and 'rid' not in already_processed:
            already_processed.add('rid')
            self.rid = value
            self.validate_RIDType(self.rid)    # validate type RIDType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DeactivatedSchedule


class OR1(GeneratedsSuper):
    """Defines a Passenger Origin Calling PointWorking Scheduled Time of
    ArrivalWorking Scheduled Time of DepartureTIPLOC of False Destination
    to be used at this location"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, wta=None, wtd=None, fd=None, tpl=None, act='  ', planAct=None, can=False, fid=None, pta=None, ptd=None, avgLoading=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.wta = _cast(None, wta)
        self.wta_nsprefix_ = None
        self.wtd = _cast(None, wtd)
        self.wtd_nsprefix_ = None
        self.fd = _cast(None, fd)
        self.fd_nsprefix_ = None
        self.tpl = _cast(None, tpl)
        self.tpl_nsprefix_ = None
        self.act = _cast(None, act)
        self.act_nsprefix_ = None
        self.planAct = _cast(None, planAct)
        self.planAct_nsprefix_ = None
        self.can = _cast(bool, can)
        self.can_nsprefix_ = None
        self.fid = _cast(None, fid)
        self.fid_nsprefix_ = None
        self.pta = _cast(None, pta)
        self.pta_nsprefix_ = None
        self.ptd = _cast(None, ptd)
        self.ptd_nsprefix_ = None
        self.avgLoading = _cast(None, avgLoading)
        self.avgLoading_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OR1)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OR1.subclass:
            return OR1.subclass(*args_, **kwargs_)
        else:
            return OR1(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_WTimeType(self, value):
        # Validate type ct:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ActivityType(self, value):
        # Validate type ct:ActivityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_ActivityType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ActivityType_patterns_, ))
    validate_ActivityType_patterns_ = [['^(([A-Z0-9\\- ][A-Z0-9\\- ]){1,6})$']]
    def validate_FormationIDType(self, value):
        # Validate type ct3:FormationIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_RTTITimeType(self, value):
        # Validate type ct:RTTITimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_RTTITimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_RTTITimeType_patterns_, ))
    validate_RTTITimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9])$']]
    def validate_LoadingValue(self, value):
        # Validate type ct3:LoadingValue, a restriction on xs:unsignedInt.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on LoadingValue' % {"value": value, "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='OR1', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OR1')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OR1')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OR1', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='OR1'):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            outfile.write(' wta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wta), input_name='wta')), ))
        if 'wtd' not in already_processed:
            already_processed.add('wtd')
            outfile.write(' wtd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtd), input_name='wtd')), ))
        if self.fd is not None and 'fd' not in already_processed:
            already_processed.add('fd')
            outfile.write(' fd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fd), input_name='fd')), ))
        if 'tpl' not in already_processed:
            already_processed.add('tpl')
            outfile.write(' tpl=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tpl), input_name='tpl')), ))
        if self.act != "  " and 'act' not in already_processed:
            already_processed.add('act')
            outfile.write(' act=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.act), input_name='act')), ))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            outfile.write(' planAct=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.planAct), input_name='planAct')), ))
        if self.can and 'can' not in already_processed:
            already_processed.add('can')
            outfile.write(' can="%s"' % self.gds_format_boolean(self.can, input_name='can'))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            outfile.write(' fid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fid), input_name='fid')), ))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            outfile.write(' pta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.pta), input_name='pta')), ))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            outfile.write(' ptd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ptd), input_name='ptd')), ))
        if self.avgLoading is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            outfile.write(' avgLoading="%s"' % self.gds_format_integer(self.avgLoading, input_name='avgLoading'))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='OR1', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='OR1', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.wta is not None:
            element.set('wta', self.gds_format_string(self.wta))
        if self.wtd is not None:
            element.set('wtd', self.gds_format_string(self.wtd))
        if self.fd is not None:
            element.set('fd', self.gds_format_string(self.fd))
        if self.tpl is not None:
            element.set('tpl', self.gds_format_string(self.tpl))
        if self.act is not None:
            element.set('act', self.gds_format_string(self.act))
        if self.planAct is not None:
            element.set('planAct', self.gds_format_string(self.planAct))
        if self.can is not None:
            element.set('can', self.gds_format_boolean(self.can))
        if self.fid is not None:
            element.set('fid', self.gds_format_string(self.fid))
        if self.pta is not None:
            element.set('pta', self.gds_format_string(self.pta))
        if self.ptd is not None:
            element.set('ptd', self.gds_format_string(self.ptd))
        if self.avgLoading is not None:
            element.set('avgLoading', self.gds_format_integer(self.avgLoading))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='OR1'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            showIndent(outfile, level)
            outfile.write('wta=%s,\n' % (self.wta,))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            showIndent(outfile, level)
            outfile.write('wtd=%s,\n' % (self.wtd,))
        if self.fd is not None and 'fd' not in already_processed:
            already_processed.add('fd')
            showIndent(outfile, level)
            outfile.write('fd=%s,\n' % (self.fd,))
        if self.tpl is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            showIndent(outfile, level)
            outfile.write('tpl=%s,\n' % (self.tpl,))
        if self.act is not None and 'act' not in already_processed:
            already_processed.add('act')
            showIndent(outfile, level)
            outfile.write('act=%s,\n' % (self.act,))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            showIndent(outfile, level)
            outfile.write('planAct=%s,\n' % (self.planAct,))
        if self.can is not None and 'can' not in already_processed:
            already_processed.add('can')
            showIndent(outfile, level)
            outfile.write('can=%s,\n' % (self.can,))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            showIndent(outfile, level)
            outfile.write('fid=%s,\n' % (self.fid,))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            showIndent(outfile, level)
            outfile.write('pta=%s,\n' % (self.pta,))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            showIndent(outfile, level)
            outfile.write('ptd=%s,\n' % (self.ptd,))
        if self.avgLoading is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            showIndent(outfile, level)
            outfile.write('avgLoading=%s,\n' % (self.avgLoading,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.OR1_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.wta is not None:
            dbobj.wta = self.wta
        if self.wtd is not None:
            dbobj.wtd = self.wtd
        if self.fd is not None:
            dbobj.fd = self.fd
        if self.tpl is not None:
            dbobj.tpl = self.tpl
        if self.act is not None:
            dbobj.act = self.act
        if self.planAct is not None:
            dbobj.planAct = self.planAct
        if self.can is not None:
            dbobj.can = self.can
        if self.fid is not None:
            dbobj.fid = self.fid
        if self.pta is not None:
            dbobj.pta = self.pta
        if self.ptd is not None:
            dbobj.ptd = self.ptd
        if self.avgLoading is not None:
            dbobj.avgLoading = self.avgLoading
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('wta', node)
        if value is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            self.wta = value
            self.validate_WTimeType(self.wta)    # validate type WTimeType
        value = find_attr_value_('wtd', node)
        if value is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            self.wtd = value
            self.validate_WTimeType(self.wtd)    # validate type WTimeType
        value = find_attr_value_('fd', node)
        if value is not None and 'fd' not in already_processed:
            already_processed.add('fd')
            self.fd = value
            self.validate_TiplocType(self.fd)    # validate type TiplocType
        value = find_attr_value_('tpl', node)
        if value is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            self.tpl = value
            self.validate_TiplocType(self.tpl)    # validate type TiplocType
        value = find_attr_value_('act', node)
        if value is not None and 'act' not in already_processed:
            already_processed.add('act')
            self.act = value
            self.validate_ActivityType(self.act)    # validate type ActivityType
        value = find_attr_value_('planAct', node)
        if value is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            self.planAct = value
            self.validate_ActivityType(self.planAct)    # validate type ActivityType
        value = find_attr_value_('can', node)
        if value is not None and 'can' not in already_processed:
            already_processed.add('can')
            if value in ('true', '1'):
                self.can = True
            elif value in ('false', '0'):
                self.can = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('fid', node)
        if value is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            self.fid = value
            self.validate_FormationIDType(self.fid)    # validate type FormationIDType
        value = find_attr_value_('pta', node)
        if value is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            self.pta = value
            self.validate_RTTITimeType(self.pta)    # validate type RTTITimeType
        value = find_attr_value_('ptd', node)
        if value is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            self.ptd = value
            self.validate_RTTITimeType(self.ptd)    # validate type RTTITimeType
        value = find_attr_value_('avgLoading', node)
        if value is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            self.avgLoading = self.gds_parse_integer(value, node, 'avgLoading')
            self.validate_LoadingValue(self.avgLoading)    # validate type LoadingValue
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class OR1


class OPOR2(GeneratedsSuper):
    """Defines an Operational Origin Calling PointWorking Scheduled Time of
    ArrivalWorking Scheduled Time of Departure"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, wta=None, wtd=None, tpl=None, act='  ', planAct=None, can=False, fid=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.wta = _cast(None, wta)
        self.wta_nsprefix_ = None
        self.wtd = _cast(None, wtd)
        self.wtd_nsprefix_ = None
        self.tpl = _cast(None, tpl)
        self.tpl_nsprefix_ = None
        self.act = _cast(None, act)
        self.act_nsprefix_ = None
        self.planAct = _cast(None, planAct)
        self.planAct_nsprefix_ = None
        self.can = _cast(bool, can)
        self.can_nsprefix_ = None
        self.fid = _cast(None, fid)
        self.fid_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OPOR2)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OPOR2.subclass:
            return OPOR2.subclass(*args_, **kwargs_)
        else:
            return OPOR2(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_WTimeType(self, value):
        # Validate type ct:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ActivityType(self, value):
        # Validate type ct:ActivityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_ActivityType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ActivityType_patterns_, ))
    validate_ActivityType_patterns_ = [['^(([A-Z0-9\\- ][A-Z0-9\\- ]){1,6})$']]
    def validate_FormationIDType(self, value):
        # Validate type ct3:FormationIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='OPOR2', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OPOR2')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OPOR2')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OPOR2', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='OPOR2'):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            outfile.write(' wta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wta), input_name='wta')), ))
        if 'wtd' not in already_processed:
            already_processed.add('wtd')
            outfile.write(' wtd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtd), input_name='wtd')), ))
        if 'tpl' not in already_processed:
            already_processed.add('tpl')
            outfile.write(' tpl=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tpl), input_name='tpl')), ))
        if self.act != "  " and 'act' not in already_processed:
            already_processed.add('act')
            outfile.write(' act=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.act), input_name='act')), ))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            outfile.write(' planAct=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.planAct), input_name='planAct')), ))
        if self.can and 'can' not in already_processed:
            already_processed.add('can')
            outfile.write(' can="%s"' % self.gds_format_boolean(self.can, input_name='can'))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            outfile.write(' fid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fid), input_name='fid')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='OPOR2', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='OPOR2', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.wta is not None:
            element.set('wta', self.gds_format_string(self.wta))
        if self.wtd is not None:
            element.set('wtd', self.gds_format_string(self.wtd))
        if self.tpl is not None:
            element.set('tpl', self.gds_format_string(self.tpl))
        if self.act is not None:
            element.set('act', self.gds_format_string(self.act))
        if self.planAct is not None:
            element.set('planAct', self.gds_format_string(self.planAct))
        if self.can is not None:
            element.set('can', self.gds_format_boolean(self.can))
        if self.fid is not None:
            element.set('fid', self.gds_format_string(self.fid))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='OPOR2'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            showIndent(outfile, level)
            outfile.write('wta=%s,\n' % (self.wta,))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            showIndent(outfile, level)
            outfile.write('wtd=%s,\n' % (self.wtd,))
        if self.tpl is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            showIndent(outfile, level)
            outfile.write('tpl=%s,\n' % (self.tpl,))
        if self.act is not None and 'act' not in already_processed:
            already_processed.add('act')
            showIndent(outfile, level)
            outfile.write('act=%s,\n' % (self.act,))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            showIndent(outfile, level)
            outfile.write('planAct=%s,\n' % (self.planAct,))
        if self.can is not None and 'can' not in already_processed:
            already_processed.add('can')
            showIndent(outfile, level)
            outfile.write('can=%s,\n' % (self.can,))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            showIndent(outfile, level)
            outfile.write('fid=%s,\n' % (self.fid,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.OPOR2_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.wta is not None:
            dbobj.wta = self.wta
        if self.wtd is not None:
            dbobj.wtd = self.wtd
        if self.tpl is not None:
            dbobj.tpl = self.tpl
        if self.act is not None:
            dbobj.act = self.act
        if self.planAct is not None:
            dbobj.planAct = self.planAct
        if self.can is not None:
            dbobj.can = self.can
        if self.fid is not None:
            dbobj.fid = self.fid
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('wta', node)
        if value is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            self.wta = value
            self.validate_WTimeType(self.wta)    # validate type WTimeType
        value = find_attr_value_('wtd', node)
        if value is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            self.wtd = value
            self.validate_WTimeType(self.wtd)    # validate type WTimeType
        value = find_attr_value_('tpl', node)
        if value is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            self.tpl = value
            self.validate_TiplocType(self.tpl)    # validate type TiplocType
        value = find_attr_value_('act', node)
        if value is not None and 'act' not in already_processed:
            already_processed.add('act')
            self.act = value
            self.validate_ActivityType(self.act)    # validate type ActivityType
        value = find_attr_value_('planAct', node)
        if value is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            self.planAct = value
            self.validate_ActivityType(self.planAct)    # validate type ActivityType
        value = find_attr_value_('can', node)
        if value is not None and 'can' not in already_processed:
            already_processed.add('can')
            if value in ('true', '1'):
                self.can = True
            elif value in ('false', '0'):
                self.can = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('fid', node)
        if value is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            self.fid = value
            self.validate_FormationIDType(self.fid)    # validate type FormationIDType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class OPOR2


class IP3(GeneratedsSuper):
    """Defines aPassenger Intermediate Calling PointWorking Scheduled Time of
    ArrivalWorking Scheduled Time of DepartureA delay value that is implied
    by a change to the service's route. This value has been added to the
    forecast lateness of the service at the previous schedule location when
    calculating the expected lateness of arrival at this location.TIPLOC of
    False Destination to be used at this location"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, wta=None, wtd=None, rdelay='0', fd=None, tpl=None, act='  ', planAct=None, can=False, fid=None, pta=None, ptd=None, avgLoading=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.wta = _cast(None, wta)
        self.wta_nsprefix_ = None
        self.wtd = _cast(None, wtd)
        self.wtd_nsprefix_ = None
        self.rdelay = _cast(None, rdelay)
        self.rdelay_nsprefix_ = None
        self.fd = _cast(None, fd)
        self.fd_nsprefix_ = None
        self.tpl = _cast(None, tpl)
        self.tpl_nsprefix_ = None
        self.act = _cast(None, act)
        self.act_nsprefix_ = None
        self.planAct = _cast(None, planAct)
        self.planAct_nsprefix_ = None
        self.can = _cast(bool, can)
        self.can_nsprefix_ = None
        self.fid = _cast(None, fid)
        self.fid_nsprefix_ = None
        self.pta = _cast(None, pta)
        self.pta_nsprefix_ = None
        self.ptd = _cast(None, ptd)
        self.ptd_nsprefix_ = None
        self.avgLoading = _cast(None, avgLoading)
        self.avgLoading_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, IP3)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if IP3.subclass:
            return IP3.subclass(*args_, **kwargs_)
        else:
            return IP3(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_WTimeType(self, value):
        # Validate type ct:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_DelayValueType(self, value):
        # Validate type ct:DelayValueType, a restriction on xs:short.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ActivityType(self, value):
        # Validate type ct:ActivityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_ActivityType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ActivityType_patterns_, ))
    validate_ActivityType_patterns_ = [['^(([A-Z0-9\\- ][A-Z0-9\\- ]){1,6})$']]
    def validate_FormationIDType(self, value):
        # Validate type ct3:FormationIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_RTTITimeType(self, value):
        # Validate type ct:RTTITimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_RTTITimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_RTTITimeType_patterns_, ))
    validate_RTTITimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9])$']]
    def validate_LoadingValue(self, value):
        # Validate type ct3:LoadingValue, a restriction on xs:unsignedInt.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on LoadingValue' % {"value": value, "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='IP3', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('IP3')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='IP3')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='IP3', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='IP3'):
        if 'wta' not in already_processed:
            already_processed.add('wta')
            outfile.write(' wta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wta), input_name='wta')), ))
        if 'wtd' not in already_processed:
            already_processed.add('wtd')
            outfile.write(' wtd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtd), input_name='wtd')), ))
        if self.rdelay != 0 and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            outfile.write(' rdelay="%s"' % self.gds_format_integer(self.rdelay, input_name='rdelay'))
        if self.fd is not None and 'fd' not in already_processed:
            already_processed.add('fd')
            outfile.write(' fd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fd), input_name='fd')), ))
        if 'tpl' not in already_processed:
            already_processed.add('tpl')
            outfile.write(' tpl=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tpl), input_name='tpl')), ))
        if self.act != "  " and 'act' not in already_processed:
            already_processed.add('act')
            outfile.write(' act=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.act), input_name='act')), ))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            outfile.write(' planAct=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.planAct), input_name='planAct')), ))
        if self.can and 'can' not in already_processed:
            already_processed.add('can')
            outfile.write(' can="%s"' % self.gds_format_boolean(self.can, input_name='can'))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            outfile.write(' fid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fid), input_name='fid')), ))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            outfile.write(' pta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.pta), input_name='pta')), ))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            outfile.write(' ptd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ptd), input_name='ptd')), ))
        if self.avgLoading is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            outfile.write(' avgLoading="%s"' % self.gds_format_integer(self.avgLoading, input_name='avgLoading'))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='IP3', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='IP3', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.wta is not None:
            element.set('wta', self.gds_format_string(self.wta))
        if self.wtd is not None:
            element.set('wtd', self.gds_format_string(self.wtd))
        if self.rdelay is not None:
            element.set('rdelay', self.gds_format_integer(self.rdelay))
        if self.fd is not None:
            element.set('fd', self.gds_format_string(self.fd))
        if self.tpl is not None:
            element.set('tpl', self.gds_format_string(self.tpl))
        if self.act is not None:
            element.set('act', self.gds_format_string(self.act))
        if self.planAct is not None:
            element.set('planAct', self.gds_format_string(self.planAct))
        if self.can is not None:
            element.set('can', self.gds_format_boolean(self.can))
        if self.fid is not None:
            element.set('fid', self.gds_format_string(self.fid))
        if self.pta is not None:
            element.set('pta', self.gds_format_string(self.pta))
        if self.ptd is not None:
            element.set('ptd', self.gds_format_string(self.ptd))
        if self.avgLoading is not None:
            element.set('avgLoading', self.gds_format_integer(self.avgLoading))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='IP3'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            showIndent(outfile, level)
            outfile.write('wta=%s,\n' % (self.wta,))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            showIndent(outfile, level)
            outfile.write('wtd=%s,\n' % (self.wtd,))
        if self.rdelay is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            showIndent(outfile, level)
            outfile.write('rdelay=%s,\n' % (self.rdelay,))
        if self.fd is not None and 'fd' not in already_processed:
            already_processed.add('fd')
            showIndent(outfile, level)
            outfile.write('fd=%s,\n' % (self.fd,))
        if self.tpl is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            showIndent(outfile, level)
            outfile.write('tpl=%s,\n' % (self.tpl,))
        if self.act is not None and 'act' not in already_processed:
            already_processed.add('act')
            showIndent(outfile, level)
            outfile.write('act=%s,\n' % (self.act,))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            showIndent(outfile, level)
            outfile.write('planAct=%s,\n' % (self.planAct,))
        if self.can is not None and 'can' not in already_processed:
            already_processed.add('can')
            showIndent(outfile, level)
            outfile.write('can=%s,\n' % (self.can,))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            showIndent(outfile, level)
            outfile.write('fid=%s,\n' % (self.fid,))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            showIndent(outfile, level)
            outfile.write('pta=%s,\n' % (self.pta,))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            showIndent(outfile, level)
            outfile.write('ptd=%s,\n' % (self.ptd,))
        if self.avgLoading is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            showIndent(outfile, level)
            outfile.write('avgLoading=%s,\n' % (self.avgLoading,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.IP3_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.wta is not None:
            dbobj.wta = self.wta
        if self.wtd is not None:
            dbobj.wtd = self.wtd
        if self.rdelay is not None:
            dbobj.rdelay = self.rdelay
        if self.fd is not None:
            dbobj.fd = self.fd
        if self.tpl is not None:
            dbobj.tpl = self.tpl
        if self.act is not None:
            dbobj.act = self.act
        if self.planAct is not None:
            dbobj.planAct = self.planAct
        if self.can is not None:
            dbobj.can = self.can
        if self.fid is not None:
            dbobj.fid = self.fid
        if self.pta is not None:
            dbobj.pta = self.pta
        if self.ptd is not None:
            dbobj.ptd = self.ptd
        if self.avgLoading is not None:
            dbobj.avgLoading = self.avgLoading
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('wta', node)
        if value is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            self.wta = value
            self.validate_WTimeType(self.wta)    # validate type WTimeType
        value = find_attr_value_('wtd', node)
        if value is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            self.wtd = value
            self.validate_WTimeType(self.wtd)    # validate type WTimeType
        value = find_attr_value_('rdelay', node)
        if value is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            self.rdelay = self.gds_parse_integer(value, node, 'rdelay')
            self.validate_DelayValueType(self.rdelay)    # validate type DelayValueType
        value = find_attr_value_('fd', node)
        if value is not None and 'fd' not in already_processed:
            already_processed.add('fd')
            self.fd = value
            self.validate_TiplocType(self.fd)    # validate type TiplocType
        value = find_attr_value_('tpl', node)
        if value is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            self.tpl = value
            self.validate_TiplocType(self.tpl)    # validate type TiplocType
        value = find_attr_value_('act', node)
        if value is not None and 'act' not in already_processed:
            already_processed.add('act')
            self.act = value
            self.validate_ActivityType(self.act)    # validate type ActivityType
        value = find_attr_value_('planAct', node)
        if value is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            self.planAct = value
            self.validate_ActivityType(self.planAct)    # validate type ActivityType
        value = find_attr_value_('can', node)
        if value is not None and 'can' not in already_processed:
            already_processed.add('can')
            if value in ('true', '1'):
                self.can = True
            elif value in ('false', '0'):
                self.can = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('fid', node)
        if value is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            self.fid = value
            self.validate_FormationIDType(self.fid)    # validate type FormationIDType
        value = find_attr_value_('pta', node)
        if value is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            self.pta = value
            self.validate_RTTITimeType(self.pta)    # validate type RTTITimeType
        value = find_attr_value_('ptd', node)
        if value is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            self.ptd = value
            self.validate_RTTITimeType(self.ptd)    # validate type RTTITimeType
        value = find_attr_value_('avgLoading', node)
        if value is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            self.avgLoading = self.gds_parse_integer(value, node, 'avgLoading')
            self.validate_LoadingValue(self.avgLoading)    # validate type LoadingValue
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class IP3


class OPIP4(GeneratedsSuper):
    """Defines an Operational Intermediate Calling PointWorking Scheduled Time
    of ArrivalWorking Scheduled Time of DepartureA delay value that is
    implied by a change to the service's route. This value has been added
    to the forecast lateness of the service at the previous schedule
    location when calculating the expected lateness of arrival at this
    location."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, wta=None, wtd=None, rdelay='0', tpl=None, act='  ', planAct=None, can=False, fid=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.wta = _cast(None, wta)
        self.wta_nsprefix_ = None
        self.wtd = _cast(None, wtd)
        self.wtd_nsprefix_ = None
        self.rdelay = _cast(None, rdelay)
        self.rdelay_nsprefix_ = None
        self.tpl = _cast(None, tpl)
        self.tpl_nsprefix_ = None
        self.act = _cast(None, act)
        self.act_nsprefix_ = None
        self.planAct = _cast(None, planAct)
        self.planAct_nsprefix_ = None
        self.can = _cast(bool, can)
        self.can_nsprefix_ = None
        self.fid = _cast(None, fid)
        self.fid_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OPIP4)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OPIP4.subclass:
            return OPIP4.subclass(*args_, **kwargs_)
        else:
            return OPIP4(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_WTimeType(self, value):
        # Validate type ct:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_DelayValueType(self, value):
        # Validate type ct:DelayValueType, a restriction on xs:short.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ActivityType(self, value):
        # Validate type ct:ActivityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_ActivityType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ActivityType_patterns_, ))
    validate_ActivityType_patterns_ = [['^(([A-Z0-9\\- ][A-Z0-9\\- ]){1,6})$']]
    def validate_FormationIDType(self, value):
        # Validate type ct3:FormationIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='OPIP4', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OPIP4')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OPIP4')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OPIP4', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='OPIP4'):
        if 'wta' not in already_processed:
            already_processed.add('wta')
            outfile.write(' wta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wta), input_name='wta')), ))
        if 'wtd' not in already_processed:
            already_processed.add('wtd')
            outfile.write(' wtd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtd), input_name='wtd')), ))
        if self.rdelay != 0 and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            outfile.write(' rdelay="%s"' % self.gds_format_integer(self.rdelay, input_name='rdelay'))
        if 'tpl' not in already_processed:
            already_processed.add('tpl')
            outfile.write(' tpl=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tpl), input_name='tpl')), ))
        if self.act != "  " and 'act' not in already_processed:
            already_processed.add('act')
            outfile.write(' act=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.act), input_name='act')), ))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            outfile.write(' planAct=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.planAct), input_name='planAct')), ))
        if self.can and 'can' not in already_processed:
            already_processed.add('can')
            outfile.write(' can="%s"' % self.gds_format_boolean(self.can, input_name='can'))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            outfile.write(' fid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fid), input_name='fid')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='OPIP4', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='OPIP4', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.wta is not None:
            element.set('wta', self.gds_format_string(self.wta))
        if self.wtd is not None:
            element.set('wtd', self.gds_format_string(self.wtd))
        if self.rdelay is not None:
            element.set('rdelay', self.gds_format_integer(self.rdelay))
        if self.tpl is not None:
            element.set('tpl', self.gds_format_string(self.tpl))
        if self.act is not None:
            element.set('act', self.gds_format_string(self.act))
        if self.planAct is not None:
            element.set('planAct', self.gds_format_string(self.planAct))
        if self.can is not None:
            element.set('can', self.gds_format_boolean(self.can))
        if self.fid is not None:
            element.set('fid', self.gds_format_string(self.fid))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='OPIP4'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            showIndent(outfile, level)
            outfile.write('wta=%s,\n' % (self.wta,))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            showIndent(outfile, level)
            outfile.write('wtd=%s,\n' % (self.wtd,))
        if self.rdelay is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            showIndent(outfile, level)
            outfile.write('rdelay=%s,\n' % (self.rdelay,))
        if self.tpl is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            showIndent(outfile, level)
            outfile.write('tpl=%s,\n' % (self.tpl,))
        if self.act is not None and 'act' not in already_processed:
            already_processed.add('act')
            showIndent(outfile, level)
            outfile.write('act=%s,\n' % (self.act,))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            showIndent(outfile, level)
            outfile.write('planAct=%s,\n' % (self.planAct,))
        if self.can is not None and 'can' not in already_processed:
            already_processed.add('can')
            showIndent(outfile, level)
            outfile.write('can=%s,\n' % (self.can,))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            showIndent(outfile, level)
            outfile.write('fid=%s,\n' % (self.fid,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.OPIP4_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.wta is not None:
            dbobj.wta = self.wta
        if self.wtd is not None:
            dbobj.wtd = self.wtd
        if self.rdelay is not None:
            dbobj.rdelay = self.rdelay
        if self.tpl is not None:
            dbobj.tpl = self.tpl
        if self.act is not None:
            dbobj.act = self.act
        if self.planAct is not None:
            dbobj.planAct = self.planAct
        if self.can is not None:
            dbobj.can = self.can
        if self.fid is not None:
            dbobj.fid = self.fid
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('wta', node)
        if value is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            self.wta = value
            self.validate_WTimeType(self.wta)    # validate type WTimeType
        value = find_attr_value_('wtd', node)
        if value is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            self.wtd = value
            self.validate_WTimeType(self.wtd)    # validate type WTimeType
        value = find_attr_value_('rdelay', node)
        if value is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            self.rdelay = self.gds_parse_integer(value, node, 'rdelay')
            self.validate_DelayValueType(self.rdelay)    # validate type DelayValueType
        value = find_attr_value_('tpl', node)
        if value is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            self.tpl = value
            self.validate_TiplocType(self.tpl)    # validate type TiplocType
        value = find_attr_value_('act', node)
        if value is not None and 'act' not in already_processed:
            already_processed.add('act')
            self.act = value
            self.validate_ActivityType(self.act)    # validate type ActivityType
        value = find_attr_value_('planAct', node)
        if value is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            self.planAct = value
            self.validate_ActivityType(self.planAct)    # validate type ActivityType
        value = find_attr_value_('can', node)
        if value is not None and 'can' not in already_processed:
            already_processed.add('can')
            if value in ('true', '1'):
                self.can = True
            elif value in ('false', '0'):
                self.can = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('fid', node)
        if value is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            self.fid = value
            self.validate_FormationIDType(self.fid)    # validate type FormationIDType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class OPIP4


class PP5(GeneratedsSuper):
    """Defines an Intermediate Passing PointWorking Scheduled Time of PassingA
    delay value that is implied by a change to the service's route. This
    value has been added to the forecast lateness of the service at the
    previous schedule location when calculating the expected lateness of
    passing this location."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, wtp=None, rdelay='0', tpl=None, act='  ', planAct=None, can=False, fid=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.wtp = _cast(None, wtp)
        self.wtp_nsprefix_ = None
        self.rdelay = _cast(None, rdelay)
        self.rdelay_nsprefix_ = None
        self.tpl = _cast(None, tpl)
        self.tpl_nsprefix_ = None
        self.act = _cast(None, act)
        self.act_nsprefix_ = None
        self.planAct = _cast(None, planAct)
        self.planAct_nsprefix_ = None
        self.can = _cast(bool, can)
        self.can_nsprefix_ = None
        self.fid = _cast(None, fid)
        self.fid_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PP5)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PP5.subclass:
            return PP5.subclass(*args_, **kwargs_)
        else:
            return PP5(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_WTimeType(self, value):
        # Validate type ct:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_DelayValueType(self, value):
        # Validate type ct:DelayValueType, a restriction on xs:short.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ActivityType(self, value):
        # Validate type ct:ActivityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_ActivityType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ActivityType_patterns_, ))
    validate_ActivityType_patterns_ = [['^(([A-Z0-9\\- ][A-Z0-9\\- ]){1,6})$']]
    def validate_FormationIDType(self, value):
        # Validate type ct3:FormationIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='PP5', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PP5')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PP5')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PP5', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='PP5'):
        if 'wtp' not in already_processed:
            already_processed.add('wtp')
            outfile.write(' wtp=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtp), input_name='wtp')), ))
        if self.rdelay != 0 and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            outfile.write(' rdelay="%s"' % self.gds_format_integer(self.rdelay, input_name='rdelay'))
        if 'tpl' not in already_processed:
            already_processed.add('tpl')
            outfile.write(' tpl=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tpl), input_name='tpl')), ))
        if self.act != "  " and 'act' not in already_processed:
            already_processed.add('act')
            outfile.write(' act=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.act), input_name='act')), ))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            outfile.write(' planAct=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.planAct), input_name='planAct')), ))
        if self.can and 'can' not in already_processed:
            already_processed.add('can')
            outfile.write(' can="%s"' % self.gds_format_boolean(self.can, input_name='can'))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            outfile.write(' fid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fid), input_name='fid')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='PP5', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='PP5', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.wtp is not None:
            element.set('wtp', self.gds_format_string(self.wtp))
        if self.rdelay is not None:
            element.set('rdelay', self.gds_format_integer(self.rdelay))
        if self.tpl is not None:
            element.set('tpl', self.gds_format_string(self.tpl))
        if self.act is not None:
            element.set('act', self.gds_format_string(self.act))
        if self.planAct is not None:
            element.set('planAct', self.gds_format_string(self.planAct))
        if self.can is not None:
            element.set('can', self.gds_format_boolean(self.can))
        if self.fid is not None:
            element.set('fid', self.gds_format_string(self.fid))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='PP5'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.wtp is not None and 'wtp' not in already_processed:
            already_processed.add('wtp')
            showIndent(outfile, level)
            outfile.write('wtp=%s,\n' % (self.wtp,))
        if self.rdelay is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            showIndent(outfile, level)
            outfile.write('rdelay=%s,\n' % (self.rdelay,))
        if self.tpl is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            showIndent(outfile, level)
            outfile.write('tpl=%s,\n' % (self.tpl,))
        if self.act is not None and 'act' not in already_processed:
            already_processed.add('act')
            showIndent(outfile, level)
            outfile.write('act=%s,\n' % (self.act,))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            showIndent(outfile, level)
            outfile.write('planAct=%s,\n' % (self.planAct,))
        if self.can is not None and 'can' not in already_processed:
            already_processed.add('can')
            showIndent(outfile, level)
            outfile.write('can=%s,\n' % (self.can,))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            showIndent(outfile, level)
            outfile.write('fid=%s,\n' % (self.fid,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.PP5_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.wtp is not None:
            dbobj.wtp = self.wtp
        if self.rdelay is not None:
            dbobj.rdelay = self.rdelay
        if self.tpl is not None:
            dbobj.tpl = self.tpl
        if self.act is not None:
            dbobj.act = self.act
        if self.planAct is not None:
            dbobj.planAct = self.planAct
        if self.can is not None:
            dbobj.can = self.can
        if self.fid is not None:
            dbobj.fid = self.fid
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('wtp', node)
        if value is not None and 'wtp' not in already_processed:
            already_processed.add('wtp')
            self.wtp = value
            self.validate_WTimeType(self.wtp)    # validate type WTimeType
        value = find_attr_value_('rdelay', node)
        if value is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            self.rdelay = self.gds_parse_integer(value, node, 'rdelay')
            self.validate_DelayValueType(self.rdelay)    # validate type DelayValueType
        value = find_attr_value_('tpl', node)
        if value is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            self.tpl = value
            self.validate_TiplocType(self.tpl)    # validate type TiplocType
        value = find_attr_value_('act', node)
        if value is not None and 'act' not in already_processed:
            already_processed.add('act')
            self.act = value
            self.validate_ActivityType(self.act)    # validate type ActivityType
        value = find_attr_value_('planAct', node)
        if value is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            self.planAct = value
            self.validate_ActivityType(self.planAct)    # validate type ActivityType
        value = find_attr_value_('can', node)
        if value is not None and 'can' not in already_processed:
            already_processed.add('can')
            if value in ('true', '1'):
                self.can = True
            elif value in ('false', '0'):
                self.can = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('fid', node)
        if value is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            self.fid = value
            self.validate_FormationIDType(self.fid)    # validate type FormationIDType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class PP5


class DT6(GeneratedsSuper):
    """Defines a Passenger Destination Calling pointWorking Scheduled Time of
    ArrivalWorking Scheduled Time of DepartureA delay value that is implied
    by a change to the service's route. This value has been added to the
    forecast lateness of the service at the previous schedule location when
    calculating the expected lateness of arrival at this location."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, wta=None, wtd=None, rdelay='0', tpl=None, act='  ', planAct=None, can=False, fid=None, pta=None, ptd=None, avgLoading=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.wta = _cast(None, wta)
        self.wta_nsprefix_ = None
        self.wtd = _cast(None, wtd)
        self.wtd_nsprefix_ = None
        self.rdelay = _cast(None, rdelay)
        self.rdelay_nsprefix_ = None
        self.tpl = _cast(None, tpl)
        self.tpl_nsprefix_ = None
        self.act = _cast(None, act)
        self.act_nsprefix_ = None
        self.planAct = _cast(None, planAct)
        self.planAct_nsprefix_ = None
        self.can = _cast(bool, can)
        self.can_nsprefix_ = None
        self.fid = _cast(None, fid)
        self.fid_nsprefix_ = None
        self.pta = _cast(None, pta)
        self.pta_nsprefix_ = None
        self.ptd = _cast(None, ptd)
        self.ptd_nsprefix_ = None
        self.avgLoading = _cast(None, avgLoading)
        self.avgLoading_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, DT6)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if DT6.subclass:
            return DT6.subclass(*args_, **kwargs_)
        else:
            return DT6(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_WTimeType(self, value):
        # Validate type ct:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_DelayValueType(self, value):
        # Validate type ct:DelayValueType, a restriction on xs:short.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ActivityType(self, value):
        # Validate type ct:ActivityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_ActivityType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ActivityType_patterns_, ))
    validate_ActivityType_patterns_ = [['^(([A-Z0-9\\- ][A-Z0-9\\- ]){1,6})$']]
    def validate_FormationIDType(self, value):
        # Validate type ct3:FormationIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_RTTITimeType(self, value):
        # Validate type ct:RTTITimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_RTTITimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_RTTITimeType_patterns_, ))
    validate_RTTITimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9])$']]
    def validate_LoadingValue(self, value):
        # Validate type ct3:LoadingValue, a restriction on xs:unsignedInt.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value > 100:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on LoadingValue' % {"value": value, "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='DT6', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('DT6')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='DT6')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='DT6', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='DT6'):
        if 'wta' not in already_processed:
            already_processed.add('wta')
            outfile.write(' wta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wta), input_name='wta')), ))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            outfile.write(' wtd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtd), input_name='wtd')), ))
        if self.rdelay != 0 and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            outfile.write(' rdelay="%s"' % self.gds_format_integer(self.rdelay, input_name='rdelay'))
        if 'tpl' not in already_processed:
            already_processed.add('tpl')
            outfile.write(' tpl=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tpl), input_name='tpl')), ))
        if self.act != "  " and 'act' not in already_processed:
            already_processed.add('act')
            outfile.write(' act=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.act), input_name='act')), ))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            outfile.write(' planAct=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.planAct), input_name='planAct')), ))
        if self.can and 'can' not in already_processed:
            already_processed.add('can')
            outfile.write(' can="%s"' % self.gds_format_boolean(self.can, input_name='can'))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            outfile.write(' fid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fid), input_name='fid')), ))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            outfile.write(' pta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.pta), input_name='pta')), ))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            outfile.write(' ptd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ptd), input_name='ptd')), ))
        if self.avgLoading is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            outfile.write(' avgLoading="%s"' % self.gds_format_integer(self.avgLoading, input_name='avgLoading'))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='DT6', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='DT6', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.wta is not None:
            element.set('wta', self.gds_format_string(self.wta))
        if self.wtd is not None:
            element.set('wtd', self.gds_format_string(self.wtd))
        if self.rdelay is not None:
            element.set('rdelay', self.gds_format_integer(self.rdelay))
        if self.tpl is not None:
            element.set('tpl', self.gds_format_string(self.tpl))
        if self.act is not None:
            element.set('act', self.gds_format_string(self.act))
        if self.planAct is not None:
            element.set('planAct', self.gds_format_string(self.planAct))
        if self.can is not None:
            element.set('can', self.gds_format_boolean(self.can))
        if self.fid is not None:
            element.set('fid', self.gds_format_string(self.fid))
        if self.pta is not None:
            element.set('pta', self.gds_format_string(self.pta))
        if self.ptd is not None:
            element.set('ptd', self.gds_format_string(self.ptd))
        if self.avgLoading is not None:
            element.set('avgLoading', self.gds_format_integer(self.avgLoading))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='DT6'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            showIndent(outfile, level)
            outfile.write('wta=%s,\n' % (self.wta,))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            showIndent(outfile, level)
            outfile.write('wtd=%s,\n' % (self.wtd,))
        if self.rdelay is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            showIndent(outfile, level)
            outfile.write('rdelay=%s,\n' % (self.rdelay,))
        if self.tpl is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            showIndent(outfile, level)
            outfile.write('tpl=%s,\n' % (self.tpl,))
        if self.act is not None and 'act' not in already_processed:
            already_processed.add('act')
            showIndent(outfile, level)
            outfile.write('act=%s,\n' % (self.act,))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            showIndent(outfile, level)
            outfile.write('planAct=%s,\n' % (self.planAct,))
        if self.can is not None and 'can' not in already_processed:
            already_processed.add('can')
            showIndent(outfile, level)
            outfile.write('can=%s,\n' % (self.can,))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            showIndent(outfile, level)
            outfile.write('fid=%s,\n' % (self.fid,))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            showIndent(outfile, level)
            outfile.write('pta=%s,\n' % (self.pta,))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            showIndent(outfile, level)
            outfile.write('ptd=%s,\n' % (self.ptd,))
        if self.avgLoading is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            showIndent(outfile, level)
            outfile.write('avgLoading=%s,\n' % (self.avgLoading,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.DT6_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.wta is not None:
            dbobj.wta = self.wta
        if self.wtd is not None:
            dbobj.wtd = self.wtd
        if self.rdelay is not None:
            dbobj.rdelay = self.rdelay
        if self.tpl is not None:
            dbobj.tpl = self.tpl
        if self.act is not None:
            dbobj.act = self.act
        if self.planAct is not None:
            dbobj.planAct = self.planAct
        if self.can is not None:
            dbobj.can = self.can
        if self.fid is not None:
            dbobj.fid = self.fid
        if self.pta is not None:
            dbobj.pta = self.pta
        if self.ptd is not None:
            dbobj.ptd = self.ptd
        if self.avgLoading is not None:
            dbobj.avgLoading = self.avgLoading
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('wta', node)
        if value is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            self.wta = value
            self.validate_WTimeType(self.wta)    # validate type WTimeType
        value = find_attr_value_('wtd', node)
        if value is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            self.wtd = value
            self.validate_WTimeType(self.wtd)    # validate type WTimeType
        value = find_attr_value_('rdelay', node)
        if value is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            self.rdelay = self.gds_parse_integer(value, node, 'rdelay')
            self.validate_DelayValueType(self.rdelay)    # validate type DelayValueType
        value = find_attr_value_('tpl', node)
        if value is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            self.tpl = value
            self.validate_TiplocType(self.tpl)    # validate type TiplocType
        value = find_attr_value_('act', node)
        if value is not None and 'act' not in already_processed:
            already_processed.add('act')
            self.act = value
            self.validate_ActivityType(self.act)    # validate type ActivityType
        value = find_attr_value_('planAct', node)
        if value is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            self.planAct = value
            self.validate_ActivityType(self.planAct)    # validate type ActivityType
        value = find_attr_value_('can', node)
        if value is not None and 'can' not in already_processed:
            already_processed.add('can')
            if value in ('true', '1'):
                self.can = True
            elif value in ('false', '0'):
                self.can = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('fid', node)
        if value is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            self.fid = value
            self.validate_FormationIDType(self.fid)    # validate type FormationIDType
        value = find_attr_value_('pta', node)
        if value is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            self.pta = value
            self.validate_RTTITimeType(self.pta)    # validate type RTTITimeType
        value = find_attr_value_('ptd', node)
        if value is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            self.ptd = value
            self.validate_RTTITimeType(self.ptd)    # validate type RTTITimeType
        value = find_attr_value_('avgLoading', node)
        if value is not None and 'avgLoading' not in already_processed:
            already_processed.add('avgLoading')
            self.avgLoading = self.gds_parse_integer(value, node, 'avgLoading')
            self.validate_LoadingValue(self.avgLoading)    # validate type LoadingValue
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class DT6


class OPDT7(GeneratedsSuper):
    """Defines an Operational Destination Calling pointWorking Scheduled Time
    of ArrivalWorking Scheduled Time of DepartureA delay value that is
    implied by a change to the service's route. This value has been added
    to the forecast lateness of the service at the previous schedule
    location when calculating the expected lateness of arrival at this
    location."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, wta=None, wtd=None, rdelay='0', tpl=None, act='  ', planAct=None, can=False, fid=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.wta = _cast(None, wta)
        self.wta_nsprefix_ = None
        self.wtd = _cast(None, wtd)
        self.wtd_nsprefix_ = None
        self.rdelay = _cast(None, rdelay)
        self.rdelay_nsprefix_ = None
        self.tpl = _cast(None, tpl)
        self.tpl_nsprefix_ = None
        self.act = _cast(None, act)
        self.act_nsprefix_ = None
        self.planAct = _cast(None, planAct)
        self.planAct_nsprefix_ = None
        self.can = _cast(bool, can)
        self.can_nsprefix_ = None
        self.fid = _cast(None, fid)
        self.fid_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, OPDT7)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if OPDT7.subclass:
            return OPDT7.subclass(*args_, **kwargs_)
        else:
            return OPDT7(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_WTimeType(self, value):
        # Validate type ct:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_DelayValueType(self, value):
        # Validate type ct:DelayValueType, a restriction on xs:short.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_ActivityType(self, value):
        # Validate type ct:ActivityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 12:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on ActivityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_ActivityType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_ActivityType_patterns_, ))
    validate_ActivityType_patterns_ = [['^(([A-Z0-9\\- ][A-Z0-9\\- ]){1,6})$']]
    def validate_FormationIDType(self, value):
        # Validate type ct3:FormationIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='OPDT7', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('OPDT7')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='OPDT7')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='OPDT7', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='OPDT7'):
        if 'wta' not in already_processed:
            already_processed.add('wta')
            outfile.write(' wta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wta), input_name='wta')), ))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            outfile.write(' wtd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtd), input_name='wtd')), ))
        if self.rdelay != 0 and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            outfile.write(' rdelay="%s"' % self.gds_format_integer(self.rdelay, input_name='rdelay'))
        if 'tpl' not in already_processed:
            already_processed.add('tpl')
            outfile.write(' tpl=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tpl), input_name='tpl')), ))
        if self.act != "  " and 'act' not in already_processed:
            already_processed.add('act')
            outfile.write(' act=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.act), input_name='act')), ))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            outfile.write(' planAct=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.planAct), input_name='planAct')), ))
        if self.can and 'can' not in already_processed:
            already_processed.add('can')
            outfile.write(' can="%s"' % self.gds_format_boolean(self.can, input_name='can'))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            outfile.write(' fid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fid), input_name='fid')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='OPDT7', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='OPDT7', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.wta is not None:
            element.set('wta', self.gds_format_string(self.wta))
        if self.wtd is not None:
            element.set('wtd', self.gds_format_string(self.wtd))
        if self.rdelay is not None:
            element.set('rdelay', self.gds_format_integer(self.rdelay))
        if self.tpl is not None:
            element.set('tpl', self.gds_format_string(self.tpl))
        if self.act is not None:
            element.set('act', self.gds_format_string(self.act))
        if self.planAct is not None:
            element.set('planAct', self.gds_format_string(self.planAct))
        if self.can is not None:
            element.set('can', self.gds_format_boolean(self.can))
        if self.fid is not None:
            element.set('fid', self.gds_format_string(self.fid))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='OPDT7'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            showIndent(outfile, level)
            outfile.write('wta=%s,\n' % (self.wta,))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            showIndent(outfile, level)
            outfile.write('wtd=%s,\n' % (self.wtd,))
        if self.rdelay is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            showIndent(outfile, level)
            outfile.write('rdelay=%s,\n' % (self.rdelay,))
        if self.tpl is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            showIndent(outfile, level)
            outfile.write('tpl=%s,\n' % (self.tpl,))
        if self.act is not None and 'act' not in already_processed:
            already_processed.add('act')
            showIndent(outfile, level)
            outfile.write('act=%s,\n' % (self.act,))
        if self.planAct is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            showIndent(outfile, level)
            outfile.write('planAct=%s,\n' % (self.planAct,))
        if self.can is not None and 'can' not in already_processed:
            already_processed.add('can')
            showIndent(outfile, level)
            outfile.write('can=%s,\n' % (self.can,))
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            showIndent(outfile, level)
            outfile.write('fid=%s,\n' % (self.fid,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.OPDT7_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.wta is not None:
            dbobj.wta = self.wta
        if self.wtd is not None:
            dbobj.wtd = self.wtd
        if self.rdelay is not None:
            dbobj.rdelay = self.rdelay
        if self.tpl is not None:
            dbobj.tpl = self.tpl
        if self.act is not None:
            dbobj.act = self.act
        if self.planAct is not None:
            dbobj.planAct = self.planAct
        if self.can is not None:
            dbobj.can = self.can
        if self.fid is not None:
            dbobj.fid = self.fid
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('wta', node)
        if value is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            self.wta = value
            self.validate_WTimeType(self.wta)    # validate type WTimeType
        value = find_attr_value_('wtd', node)
        if value is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            self.wtd = value
            self.validate_WTimeType(self.wtd)    # validate type WTimeType
        value = find_attr_value_('rdelay', node)
        if value is not None and 'rdelay' not in already_processed:
            already_processed.add('rdelay')
            self.rdelay = self.gds_parse_integer(value, node, 'rdelay')
            self.validate_DelayValueType(self.rdelay)    # validate type DelayValueType
        value = find_attr_value_('tpl', node)
        if value is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            self.tpl = value
            self.validate_TiplocType(self.tpl)    # validate type TiplocType
        value = find_attr_value_('act', node)
        if value is not None and 'act' not in already_processed:
            already_processed.add('act')
            self.act = value
            self.validate_ActivityType(self.act)    # validate type ActivityType
        value = find_attr_value_('planAct', node)
        if value is not None and 'planAct' not in already_processed:
            already_processed.add('planAct')
            self.planAct = value
            self.validate_ActivityType(self.planAct)    # validate type ActivityType
        value = find_attr_value_('can', node)
        if value is not None and 'can' not in already_processed:
            already_processed.add('can')
            if value in ('true', '1'):
                self.can = True
            elif value in ('false', '0'):
                self.can = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('fid', node)
        if value is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            self.fid = value
            self.validate_FormationIDType(self.fid)    # validate type FormationIDType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class OPDT7


class Schedule8(GeneratedsSuper):
    """Train ScheduleRTTI unique Train IDTrain UIDTrain ID (Headcode)Retail
    Service Identifier. Note that this may be either a full 8-character
    "portion identifier", or a base 6-character identifier, according to
    the available information provided to Darwin.Scheduled Start DateATOC
    CodeType of service, i.e. Train/Bus/Ship.Category of service.True if
    Darwin classifies the train category as a passenger service.Indicates
    if this service is active in Darwin. Note that schedules should be
    assumed to be inactive until a message is received to indicate
    otherwise.Service has been deleted and should not be
    used/displayed.Indicates if this service is a charter service."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, rid=None, uid=None, trainId=None, rsid=None, ssd=None, toc=None, status='P', trainCat='OO', isPassengerSvc=True, isActive=True, deleted=False, isCharter=False, OR=None, OPOR=None, IP=None, OPIP=None, PP=None, DT=None, OPDT=None, cancelReason=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.rid = _cast(None, rid)
        self.rid_nsprefix_ = None
        self.uid = _cast(None, uid)
        self.uid_nsprefix_ = None
        self.trainId = _cast(None, trainId)
        self.trainId_nsprefix_ = None
        self.rsid = _cast(None, rsid)
        self.rsid_nsprefix_ = None
        self.ssd = _cast(None, ssd)
        self.ssd_nsprefix_ = None
        self.toc = _cast(None, toc)
        self.toc_nsprefix_ = None
        self.status = _cast(None, status)
        self.status_nsprefix_ = None
        self.trainCat = _cast(None, trainCat)
        self.trainCat_nsprefix_ = None
        self.isPassengerSvc = _cast(bool, isPassengerSvc)
        self.isPassengerSvc_nsprefix_ = None
        self.isActive = _cast(bool, isActive)
        self.isActive_nsprefix_ = None
        self.deleted = _cast(bool, deleted)
        self.deleted_nsprefix_ = None
        self.isCharter = _cast(bool, isCharter)
        self.isCharter_nsprefix_ = None
        if OR is None:
            self.OR = []
        else:
            self.OR = OR
        self.OR_nsprefix_ = None
        if OPOR is None:
            self.OPOR = []
        else:
            self.OPOR = OPOR
        self.OPOR_nsprefix_ = None
        if IP is None:
            self.IP = []
        else:
            self.IP = IP
        self.IP_nsprefix_ = None
        if OPIP is None:
            self.OPIP = []
        else:
            self.OPIP = OPIP
        self.OPIP_nsprefix_ = None
        if PP is None:
            self.PP = []
        else:
            self.PP = PP
        self.PP_nsprefix_ = None
        if DT is None:
            self.DT = []
        else:
            self.DT = DT
        self.DT_nsprefix_ = None
        if OPDT is None:
            self.OPDT = []
        else:
            self.OPDT = OPDT
        self.OPDT_nsprefix_ = None
        self.cancelReason = cancelReason
        self.cancelReason_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Schedule8)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Schedule8.subclass:
            return Schedule8.subclass(*args_, **kwargs_)
        else:
            return Schedule8(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_RIDType(self, value):
        # Validate type ct:RIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on RIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_UIDType(self, value):
        # Validate type ct:UIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 6:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on UIDType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_TrainIdType(self, value):
        # Validate type ct:TrainIdType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on TrainIdType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TrainIdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TrainIdType_patterns_, ))
    validate_TrainIdType_patterns_ = [['^([0-9][A-Z][0-9][0-9])$']]
    def validate_RSIDType(self, value):
        # Validate type ct2:RSIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 8:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on RSIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 6:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on RSIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_RTTIDateType(self, value):
        # Validate type ct:RTTIDateType, a restriction on xs:date.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, datetime_.date):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (datetime_.date)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def validate_TOCType(self, value):
        # Validate type ct:TOCType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on TOCType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_CIFTrainStatusType(self, value):
        # Validate type ct:CIFTrainStatusType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on CIFTrainStatusType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_CIFTrainStatusType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_CIFTrainStatusType_patterns_, ))
    validate_CIFTrainStatusType_patterns_ = [['^([BFPST12345])$']]
    def validate_CIFTrainCategoryType(self, value):
        # Validate type ct:CIFTrainCategoryType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CIFTrainCategoryType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 0:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CIFTrainCategoryType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.OR or
            self.OPOR or
            self.IP or
            self.OPIP or
            self.PP or
            self.DT or
            self.OPDT or
            self.cancelReason is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1"  xmlns:ct="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='Schedule8', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Schedule8')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Schedule8')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Schedule8', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='Schedule8'):
        if 'rid' not in already_processed:
            already_processed.add('rid')
            outfile.write(' rid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.rid), input_name='rid')), ))
        if 'uid' not in already_processed:
            already_processed.add('uid')
            outfile.write(' uid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.uid), input_name='uid')), ))
        if 'trainId' not in already_processed:
            already_processed.add('trainId')
            outfile.write(' trainId=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.trainId), input_name='trainId')), ))
        if self.rsid is not None and 'rsid' not in already_processed:
            already_processed.add('rsid')
            outfile.write(' rsid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.rsid), input_name='rsid')), ))
        if 'ssd' not in already_processed:
            already_processed.add('ssd')
            outfile.write(' ssd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ssd), input_name='ssd')), ))
        if 'toc' not in already_processed:
            already_processed.add('toc')
            outfile.write(' toc=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.toc), input_name='toc')), ))
        if self.status != "P" and 'status' not in already_processed:
            already_processed.add('status')
            outfile.write(' status=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.status), input_name='status')), ))
        if self.trainCat != "OO" and 'trainCat' not in already_processed:
            already_processed.add('trainCat')
            outfile.write(' trainCat=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.trainCat), input_name='trainCat')), ))
        if not self.isPassengerSvc and 'isPassengerSvc' not in already_processed:
            already_processed.add('isPassengerSvc')
            outfile.write(' isPassengerSvc="%s"' % self.gds_format_boolean(self.isPassengerSvc, input_name='isPassengerSvc'))
        if not self.isActive and 'isActive' not in already_processed:
            already_processed.add('isActive')
            outfile.write(' isActive="%s"' % self.gds_format_boolean(self.isActive, input_name='isActive'))
        if self.deleted and 'deleted' not in already_processed:
            already_processed.add('deleted')
            outfile.write(' deleted="%s"' % self.gds_format_boolean(self.deleted, input_name='deleted'))
        if self.isCharter and 'isCharter' not in already_processed:
            already_processed.add('isCharter')
            outfile.write(' isCharter="%s"' % self.gds_format_boolean(self.isCharter, input_name='isCharter'))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1"  xmlns:ct="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='Schedule8', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for OR_ in self.OR:
            namespaceprefix_ = self.OR_nsprefix_ + ':' if (UseCapturedNS_ and self.OR_nsprefix_) else ''
            OR_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OR', pretty_print=pretty_print)
        for OPOR_ in self.OPOR:
            namespaceprefix_ = self.OPOR_nsprefix_ + ':' if (UseCapturedNS_ and self.OPOR_nsprefix_) else ''
            OPOR_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OPOR', pretty_print=pretty_print)
        for IP_ in self.IP:
            namespaceprefix_ = self.IP_nsprefix_ + ':' if (UseCapturedNS_ and self.IP_nsprefix_) else ''
            IP_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='IP', pretty_print=pretty_print)
        for OPIP_ in self.OPIP:
            namespaceprefix_ = self.OPIP_nsprefix_ + ':' if (UseCapturedNS_ and self.OPIP_nsprefix_) else ''
            OPIP_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OPIP', pretty_print=pretty_print)
        for PP_ in self.PP:
            namespaceprefix_ = self.PP_nsprefix_ + ':' if (UseCapturedNS_ and self.PP_nsprefix_) else ''
            PP_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='PP', pretty_print=pretty_print)
        for DT_ in self.DT:
            namespaceprefix_ = self.DT_nsprefix_ + ':' if (UseCapturedNS_ and self.DT_nsprefix_) else ''
            DT_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='DT', pretty_print=pretty_print)
        for OPDT_ in self.OPDT:
            namespaceprefix_ = self.OPDT_nsprefix_ + ':' if (UseCapturedNS_ and self.OPDT_nsprefix_) else ''
            OPDT_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='OPDT', pretty_print=pretty_print)
        if self.cancelReason is not None:
            namespaceprefix_ = self.cancelReason_nsprefix_ + ':' if (UseCapturedNS_ and self.cancelReason_nsprefix_) else ''
            self.cancelReason.export(outfile, level, namespaceprefix_, namespacedef_='', name_='cancelReason', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Schedule8', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.rid is not None:
            element.set('rid', self.gds_format_string(self.rid))
        if self.uid is not None:
            element.set('uid', self.gds_format_string(self.uid))
        if self.trainId is not None:
            element.set('trainId', self.gds_format_string(self.trainId))
        if self.rsid is not None:
            element.set('rsid', self.gds_format_string(self.rsid))
        if self.ssd is not None:
            element.set('ssd', self.gds_format_date(self.ssd))
        if self.toc is not None:
            element.set('toc', self.gds_format_string(self.toc))
        if self.status is not None:
            element.set('status', self.gds_format_string(self.status))
        if self.trainCat is not None:
            element.set('trainCat', self.gds_format_string(self.trainCat))
        if self.isPassengerSvc is not None:
            element.set('isPassengerSvc', self.gds_format_boolean(self.isPassengerSvc))
        if self.isActive is not None:
            element.set('isActive', self.gds_format_boolean(self.isActive))
        if self.deleted is not None:
            element.set('deleted', self.gds_format_boolean(self.deleted))
        if self.isCharter is not None:
            element.set('isCharter', self.gds_format_boolean(self.isCharter))
        for OR_ in self.OR:
            OR_.to_etree(element, name_='OR', mapping_=mapping_)
        for OPOR_ in self.OPOR:
            OPOR_.to_etree(element, name_='OPOR', mapping_=mapping_)
        for IP_ in self.IP:
            IP_.to_etree(element, name_='IP', mapping_=mapping_)
        for OPIP_ in self.OPIP:
            OPIP_.to_etree(element, name_='OPIP', mapping_=mapping_)
        for PP_ in self.PP:
            PP_.to_etree(element, name_='PP', mapping_=mapping_)
        for DT_ in self.DT:
            DT_.to_etree(element, name_='DT', mapping_=mapping_)
        for OPDT_ in self.OPDT:
            OPDT_.to_etree(element, name_='OPDT', mapping_=mapping_)
        if self.cancelReason is not None:
            cancelReason_ = self.cancelReason
            cancelReason_.to_etree(element, name_='cancelReason', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='Schedule8'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.rid is not None and 'rid' not in already_processed:
            already_processed.add('rid')
            showIndent(outfile, level)
            outfile.write('rid=%s,\n' % (self.rid,))
        if self.uid is not None and 'uid' not in already_processed:
            already_processed.add('uid')
            showIndent(outfile, level)
            outfile.write('uid=%s,\n' % (self.uid,))
        if self.trainId is not None and 'trainId' not in already_processed:
            already_processed.add('trainId')
            showIndent(outfile, level)
            outfile.write('trainId=%s,\n' % (self.trainId,))
        if self.rsid is not None and 'rsid' not in already_processed:
            already_processed.add('rsid')
            showIndent(outfile, level)
            outfile.write('rsid=%s,\n' % (self.rsid,))
        if self.ssd is not None and 'ssd' not in already_processed:
            already_processed.add('ssd')
            showIndent(outfile, level)
            outfile.write('ssd=%s,\n' % (self.ssd,))
        if self.toc is not None and 'toc' not in already_processed:
            already_processed.add('toc')
            showIndent(outfile, level)
            outfile.write('toc=%s,\n' % (self.toc,))
        if self.status is not None and 'status' not in already_processed:
            already_processed.add('status')
            showIndent(outfile, level)
            outfile.write('status=%s,\n' % (self.status,))
        if self.trainCat is not None and 'trainCat' not in already_processed:
            already_processed.add('trainCat')
            showIndent(outfile, level)
            outfile.write('trainCat=%s,\n' % (self.trainCat,))
        if self.isPassengerSvc is not None and 'isPassengerSvc' not in already_processed:
            already_processed.add('isPassengerSvc')
            showIndent(outfile, level)
            outfile.write('isPassengerSvc=%s,\n' % (self.isPassengerSvc,))
        if self.isActive is not None and 'isActive' not in already_processed:
            already_processed.add('isActive')
            showIndent(outfile, level)
            outfile.write('isActive=%s,\n' % (self.isActive,))
        if self.deleted is not None and 'deleted' not in already_processed:
            already_processed.add('deleted')
            showIndent(outfile, level)
            outfile.write('deleted=%s,\n' % (self.deleted,))
        if self.isCharter is not None and 'isCharter' not in already_processed:
            already_processed.add('isCharter')
            showIndent(outfile, level)
            outfile.write('isCharter=%s,\n' % (self.isCharter,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('OR=[\n')
        level += 1
        for OR_ in self.OR:
            showIndent(outfile, level)
            outfile.write('model_.OR1(\n')
            OR_.exportLiteral(outfile, level, name_='OR1')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('OPOR=[\n')
        level += 1
        for OPOR_ in self.OPOR:
            showIndent(outfile, level)
            outfile.write('model_.OPOR2(\n')
            OPOR_.exportLiteral(outfile, level, name_='OPOR2')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('IP=[\n')
        level += 1
        for IP_ in self.IP:
            showIndent(outfile, level)
            outfile.write('model_.IP3(\n')
            IP_.exportLiteral(outfile, level, name_='IP3')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('OPIP=[\n')
        level += 1
        for OPIP_ in self.OPIP:
            showIndent(outfile, level)
            outfile.write('model_.OPIP4(\n')
            OPIP_.exportLiteral(outfile, level, name_='OPIP4')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('PP=[\n')
        level += 1
        for PP_ in self.PP:
            showIndent(outfile, level)
            outfile.write('model_.PP5(\n')
            PP_.exportLiteral(outfile, level, name_='PP5')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('DT=[\n')
        level += 1
        for DT_ in self.DT:
            showIndent(outfile, level)
            outfile.write('model_.DT6(\n')
            DT_.exportLiteral(outfile, level, name_='DT6')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('OPDT=[\n')
        level += 1
        for OPDT_ in self.OPDT:
            showIndent(outfile, level)
            outfile.write('model_.OPDT7(\n')
            OPDT_.exportLiteral(outfile, level, name_='OPDT7')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.cancelReason is not None:
            showIndent(outfile, level)
            outfile.write('cancelReason=model_.DisruptionReasonType(\n')
            self.cancelReason.exportLiteral(outfile, level, name_='cancelReason')
            showIndent(outfile, level)
            outfile.write('),\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.Schedule8_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.rid is not None:
            dbobj.rid = self.rid
        if self.uid is not None:
            dbobj.uid = self.uid
        if self.trainId is not None:
            dbobj.trainId = self.trainId
        if self.rsid is not None:
            dbobj.rsid = self.rsid
        if self.ssd is not None:
            dbobj.ssd = self.ssd
        if self.toc is not None:
            dbobj.toc = self.toc
        if self.status is not None:
            dbobj.status = self.status
        if self.trainCat is not None:
            dbobj.trainCat = self.trainCat
        if self.isPassengerSvc is not None:
            dbobj.isPassengerSvc = self.isPassengerSvc
        if self.isActive is not None:
            dbobj.isActive = self.isActive
        if self.deleted is not None:
            dbobj.deleted = self.deleted
        if self.isCharter is not None:
            dbobj.isCharter = self.isCharter
    def exportSQLAlchemyChildren(self, session, dbobj):
        for child in self.OR:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.OR.append(child_dbobj)
        for child in self.OPOR:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.OPOR.append(child_dbobj)
        for child in self.IP:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.IP.append(child_dbobj)
        for child in self.OPIP:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.OPIP.append(child_dbobj)
        for child in self.PP:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.PP.append(child_dbobj)
        for child in self.DT:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.DT.append(child_dbobj)
        for child in self.OPDT:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.OPDT.append(child_dbobj)
        if self.cancelReason is not None:
            child_dbobj = self.cancelReason.exportSQLAlchemy(session)
            dbobj.cancelReason = child_dbobj
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('rid', node)
        if value is not None and 'rid' not in already_processed:
            already_processed.add('rid')
            self.rid = value
            self.validate_RIDType(self.rid)    # validate type RIDType
        value = find_attr_value_('uid', node)
        if value is not None and 'uid' not in already_processed:
            already_processed.add('uid')
            self.uid = value
            self.validate_UIDType(self.uid)    # validate type UIDType
        value = find_attr_value_('trainId', node)
        if value is not None and 'trainId' not in already_processed:
            already_processed.add('trainId')
            self.trainId = value
            self.validate_TrainIdType(self.trainId)    # validate type TrainIdType
        value = find_attr_value_('rsid', node)
        if value is not None and 'rsid' not in already_processed:
            already_processed.add('rsid')
            self.rsid = value
            self.validate_RSIDType(self.rsid)    # validate type RSIDType
        value = find_attr_value_('ssd', node)
        if value is not None and 'ssd' not in already_processed:
            already_processed.add('ssd')
            try:
                self.ssd = self.gds_parse_date(value)
            except ValueError as exp:
                raise ValueError('Bad date attribute (ssd): %s' % exp)
            self.validate_RTTIDateType(self.ssd)    # validate type RTTIDateType
        value = find_attr_value_('toc', node)
        if value is not None and 'toc' not in already_processed:
            already_processed.add('toc')
            self.toc = value
            self.validate_TOCType(self.toc)    # validate type TOCType
        value = find_attr_value_('status', node)
        if value is not None and 'status' not in already_processed:
            already_processed.add('status')
            self.status = value
            self.validate_CIFTrainStatusType(self.status)    # validate type CIFTrainStatusType
        value = find_attr_value_('trainCat', node)
        if value is not None and 'trainCat' not in already_processed:
            already_processed.add('trainCat')
            self.trainCat = value
            self.validate_CIFTrainCategoryType(self.trainCat)    # validate type CIFTrainCategoryType
        value = find_attr_value_('isPassengerSvc', node)
        if value is not None and 'isPassengerSvc' not in already_processed:
            already_processed.add('isPassengerSvc')
            if value in ('true', '1'):
                self.isPassengerSvc = True
            elif value in ('false', '0'):
                self.isPassengerSvc = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('isActive', node)
        if value is not None and 'isActive' not in already_processed:
            already_processed.add('isActive')
            if value in ('true', '1'):
                self.isActive = True
            elif value in ('false', '0'):
                self.isActive = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('deleted', node)
        if value is not None and 'deleted' not in already_processed:
            already_processed.add('deleted')
            if value in ('true', '1'):
                self.deleted = True
            elif value in ('false', '0'):
                self.deleted = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('isCharter', node)
        if value is not None and 'isCharter' not in already_processed:
            already_processed.add('isCharter')
            if value in ('true', '1'):
                self.isCharter = True
            elif value in ('false', '0'):
                self.isCharter = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'OR':
            obj_ = OR1.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OR.append(obj_)
            obj_.original_tagname_ = 'OR'
        elif nodeName_ == 'OPOR':
            obj_ = OPOR2.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OPOR.append(obj_)
            obj_.original_tagname_ = 'OPOR'
        elif nodeName_ == 'IP':
            obj_ = IP3.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.IP.append(obj_)
            obj_.original_tagname_ = 'IP'
        elif nodeName_ == 'OPIP':
            obj_ = OPIP4.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OPIP.append(obj_)
            obj_.original_tagname_ = 'OPIP'
        elif nodeName_ == 'PP':
            obj_ = PP5.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.PP.append(obj_)
            obj_.original_tagname_ = 'PP'
        elif nodeName_ == 'DT':
            obj_ = DT6.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.DT.append(obj_)
            obj_.original_tagname_ = 'DT'
        elif nodeName_ == 'OPDT':
            obj_ = OPDT7.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.OPDT.append(obj_)
            obj_.original_tagname_ = 'OPDT'
        elif nodeName_ == 'cancelReason':
            obj_ = DisruptionReasonType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.cancelReason = obj_
            obj_.original_tagname_ = 'cancelReason'
# end class Schedule8


class PlatformData(GeneratedsSuper):
    """Platform number with associated flagsPlatform number is suppressed and
    should not be displayed.Whether a CIS, or Darwin Workstation, has set
    platform suppression at this location.The source of the platfom number.
    P = Planned, A = Automatic, M = Manual.True if the platform number is
    confirmed."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, platsup=False, cisPlatsup=False, platsrc='P', conf=False, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.platsup = _cast(bool, platsup)
        self.platsup_nsprefix_ = None
        self.cisPlatsup = _cast(bool, cisPlatsup)
        self.cisPlatsup_nsprefix_ = None
        self.platsrc = _cast(None, platsrc)
        self.platsrc_nsprefix_ = None
        self.conf = _cast(bool, conf)
        self.conf_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, PlatformData)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if PlatformData.subclass:
            return PlatformData.subclass(*args_, **kwargs_)
        else:
            return PlatformData(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='PlatformData', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('PlatformData')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='PlatformData')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='PlatformData', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='PlatformData'):
        if self.platsup and 'platsup' not in already_processed:
            already_processed.add('platsup')
            outfile.write(' platsup="%s"' % self.gds_format_boolean(self.platsup, input_name='platsup'))
        if self.cisPlatsup and 'cisPlatsup' not in already_processed:
            already_processed.add('cisPlatsup')
            outfile.write(' cisPlatsup="%s"' % self.gds_format_boolean(self.cisPlatsup, input_name='cisPlatsup'))
        if self.platsrc != "P" and 'platsrc' not in already_processed:
            already_processed.add('platsrc')
            outfile.write(' platsrc=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.platsrc), input_name='platsrc')), ))
        if self.conf and 'conf' not in already_processed:
            already_processed.add('conf')
            outfile.write(' conf="%s"' % self.gds_format_boolean(self.conf, input_name='conf'))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='PlatformData', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='PlatformData', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.platsup is not None:
            element.set('platsup', self.gds_format_boolean(self.platsup))
        if self.cisPlatsup is not None:
            element.set('cisPlatsup', self.gds_format_boolean(self.cisPlatsup))
        if self.platsrc is not None:
            element.set('platsrc', self.gds_format_string(self.platsrc))
        if self.conf is not None:
            element.set('conf', self.gds_format_boolean(self.conf))
        if self.hasContent_():
            element.text = self.gds_format_string(self.get_valueOf_())
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='PlatformData'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.platsup is not None and 'platsup' not in already_processed:
            already_processed.add('platsup')
            showIndent(outfile, level)
            outfile.write('platsup=%s,\n' % (self.platsup,))
        if self.cisPlatsup is not None and 'cisPlatsup' not in already_processed:
            already_processed.add('cisPlatsup')
            showIndent(outfile, level)
            outfile.write('cisPlatsup=%s,\n' % (self.cisPlatsup,))
        if self.platsrc is not None and 'platsrc' not in already_processed:
            already_processed.add('platsrc')
            showIndent(outfile, level)
            outfile.write('platsrc="%s",\n' % (self.platsrc,))
        if self.conf is not None and 'conf' not in already_processed:
            already_processed.add('conf')
            showIndent(outfile, level)
            outfile.write('conf=%s,\n' % (self.conf,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.PlatformData_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.platsup is not None:
            dbobj.platsup = self.platsup
        if self.cisPlatsup is not None:
            dbobj.cisPlatsup = self.cisPlatsup
        if self.platsrc is not None:
            dbobj.platsrc = self.platsrc
        if self.conf is not None:
            dbobj.conf = self.conf
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('platsup', node)
        if value is not None and 'platsup' not in already_processed:
            already_processed.add('platsup')
            if value in ('true', '1'):
                self.platsup = True
            elif value in ('false', '0'):
                self.platsup = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('cisPlatsup', node)
        if value is not None and 'cisPlatsup' not in already_processed:
            already_processed.add('cisPlatsup')
            if value in ('true', '1'):
                self.cisPlatsup = True
            elif value in ('false', '0'):
                self.cisPlatsup = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('platsrc', node)
        if value is not None and 'platsrc' not in already_processed:
            already_processed.add('platsrc')
            self.platsrc = value
        value = find_attr_value_('conf', node)
        if value is not None and 'conf' not in already_processed:
            already_processed.add('conf')
            if value in ('true', '1'):
                self.conf = True
            elif value in ('false', '0'):
                self.conf = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class PlatformData


class TSTimeData(GeneratedsSuper):
    """Type describing time-based forecast attributes for a TS
    arrival/departure/passEstimated Time. For locations that are public
    stops, this will be based on the "public schedule". For operational
    stops and passing locations, it will be based on the "working
    schedule". It is only published where there is a corresponding
    "activity" for the service.The estimated time based on the "working
    schedule". This will only be set for public stops when (i) it also
    differs from the estimated time based on the "public schedule", or (ii)
    where there is an operational "activity" but no public
    "activity".Actual TimeIf true, indicates that an actual time ("at")
    value has just been removed and replaced by an estimated time ("et").
    Note that this attribute will only be set to "true" once, when the
    actual time is removed, and will not be set in any snapshot.The class
    of the actual time.The manually applied lower limit that has been
    applied to the estimated time at this location. The estimated time will
    not be set lower than this value, but may be set higher.Indicates that
    an unknown delay forecast has been set for the estimated time at this
    location. Note that this value indicates where a manual unknown delay
    forecast has been set, whereas it is the "delayed" attribute that
    indicates that the actual forecast is "unknown delay".Indicates that
    this estimated time is a forecast of "unknown delay". Displayed as
    "Delayed" in LDB. Note that this value indicates that this forecast is
    "unknown delay", whereas it is the "etUnknown" attribute that indicates
    where the manual unknown delay forecast has been set.The source of the
    forecast or actual time.The RTTI CIS code of the CIS instance if the
    src is a CIS."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, et=None, wet=None, at=None, atRemoved=False, atClass=None, etmin=None, etUnknown=False, delayed=False, src=None, srcInst=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.et = _cast(None, et)
        self.et_nsprefix_ = None
        self.wet = _cast(None, wet)
        self.wet_nsprefix_ = None
        self.at = _cast(None, at)
        self.at_nsprefix_ = None
        self.atRemoved = _cast(bool, atRemoved)
        self.atRemoved_nsprefix_ = None
        self.atClass = _cast(None, atClass)
        self.atClass_nsprefix_ = None
        self.etmin = _cast(None, etmin)
        self.etmin_nsprefix_ = None
        self.etUnknown = _cast(bool, etUnknown)
        self.etUnknown_nsprefix_ = None
        self.delayed = _cast(bool, delayed)
        self.delayed_nsprefix_ = None
        self.src = _cast(None, src)
        self.src_nsprefix_ = None
        self.srcInst = _cast(None, srcInst)
        self.srcInst_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TSTimeData)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TSTimeData.subclass:
            return TSTimeData.subclass(*args_, **kwargs_)
        else:
            return TSTimeData(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_RTTITimeType(self, value):
        # Validate type ct:RTTITimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_RTTITimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_RTTITimeType_patterns_, ))
    validate_RTTITimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9])$']]
    def validate_SourceTypeInst(self, value):
        # Validate type ct:SourceTypeInst, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on SourceTypeInst' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='TSTimeData', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TSTimeData')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TSTimeData')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TSTimeData', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='TSTimeData'):
        if self.et is not None and 'et' not in already_processed:
            already_processed.add('et')
            outfile.write(' et=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.et), input_name='et')), ))
        if self.wet is not None and 'wet' not in already_processed:
            already_processed.add('wet')
            outfile.write(' wet=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wet), input_name='wet')), ))
        if self.at is not None and 'at' not in already_processed:
            already_processed.add('at')
            outfile.write(' at=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.at), input_name='at')), ))
        if self.atRemoved and 'atRemoved' not in already_processed:
            already_processed.add('atRemoved')
            outfile.write(' atRemoved="%s"' % self.gds_format_boolean(self.atRemoved, input_name='atRemoved'))
        if self.atClass is not None and 'atClass' not in already_processed:
            already_processed.add('atClass')
            outfile.write(' atClass=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.atClass), input_name='atClass')), ))
        if self.etmin is not None and 'etmin' not in already_processed:
            already_processed.add('etmin')
            outfile.write(' etmin=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.etmin), input_name='etmin')), ))
        if self.etUnknown and 'etUnknown' not in already_processed:
            already_processed.add('etUnknown')
            outfile.write(' etUnknown="%s"' % self.gds_format_boolean(self.etUnknown, input_name='etUnknown'))
        if self.delayed and 'delayed' not in already_processed:
            already_processed.add('delayed')
            outfile.write(' delayed="%s"' % self.gds_format_boolean(self.delayed, input_name='delayed'))
        if self.src is not None and 'src' not in already_processed:
            already_processed.add('src')
            outfile.write(' src=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.src), input_name='src')), ))
        if self.srcInst is not None and 'srcInst' not in already_processed:
            already_processed.add('srcInst')
            outfile.write(' srcInst=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.srcInst), input_name='srcInst')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='TSTimeData', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='TSTimeData', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.et is not None:
            element.set('et', self.gds_format_string(self.et))
        if self.wet is not None:
            element.set('wet', self.gds_format_string(self.wet))
        if self.at is not None:
            element.set('at', self.gds_format_string(self.at))
        if self.atRemoved is not None:
            element.set('atRemoved', self.gds_format_boolean(self.atRemoved))
        if self.atClass is not None:
            element.set('atClass', self.gds_format_string(self.atClass))
        if self.etmin is not None:
            element.set('etmin', self.gds_format_string(self.etmin))
        if self.etUnknown is not None:
            element.set('etUnknown', self.gds_format_boolean(self.etUnknown))
        if self.delayed is not None:
            element.set('delayed', self.gds_format_boolean(self.delayed))
        if self.src is not None:
            element.set('src', self.gds_format_string(self.src))
        if self.srcInst is not None:
            element.set('srcInst', self.gds_format_string(self.srcInst))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='TSTimeData'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.et is not None and 'et' not in already_processed:
            already_processed.add('et')
            showIndent(outfile, level)
            outfile.write('et=%s,\n' % (self.et,))
        if self.wet is not None and 'wet' not in already_processed:
            already_processed.add('wet')
            showIndent(outfile, level)
            outfile.write('wet=%s,\n' % (self.wet,))
        if self.at is not None and 'at' not in already_processed:
            already_processed.add('at')
            showIndent(outfile, level)
            outfile.write('at=%s,\n' % (self.at,))
        if self.atRemoved is not None and 'atRemoved' not in already_processed:
            already_processed.add('atRemoved')
            showIndent(outfile, level)
            outfile.write('atRemoved=%s,\n' % (self.atRemoved,))
        if self.atClass is not None and 'atClass' not in already_processed:
            already_processed.add('atClass')
            showIndent(outfile, level)
            outfile.write('atClass="%s",\n' % (self.atClass,))
        if self.etmin is not None and 'etmin' not in already_processed:
            already_processed.add('etmin')
            showIndent(outfile, level)
            outfile.write('etmin=%s,\n' % (self.etmin,))
        if self.etUnknown is not None and 'etUnknown' not in already_processed:
            already_processed.add('etUnknown')
            showIndent(outfile, level)
            outfile.write('etUnknown=%s,\n' % (self.etUnknown,))
        if self.delayed is not None and 'delayed' not in already_processed:
            already_processed.add('delayed')
            showIndent(outfile, level)
            outfile.write('delayed=%s,\n' % (self.delayed,))
        if self.src is not None and 'src' not in already_processed:
            already_processed.add('src')
            showIndent(outfile, level)
            outfile.write('src="%s",\n' % (self.src,))
        if self.srcInst is not None and 'srcInst' not in already_processed:
            already_processed.add('srcInst')
            showIndent(outfile, level)
            outfile.write('srcInst=%s,\n' % (self.srcInst,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.TSTimeData_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.et is not None:
            dbobj.et = self.et
        if self.wet is not None:
            dbobj.wet = self.wet
        if self.at is not None:
            dbobj.at = self.at
        if self.atRemoved is not None:
            dbobj.atRemoved = self.atRemoved
        if self.atClass is not None:
            dbobj.atClass = self.atClass
        if self.etmin is not None:
            dbobj.etmin = self.etmin
        if self.etUnknown is not None:
            dbobj.etUnknown = self.etUnknown
        if self.delayed is not None:
            dbobj.delayed = self.delayed
        if self.src is not None:
            dbobj.src = self.src
        if self.srcInst is not None:
            dbobj.srcInst = self.srcInst
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('et', node)
        if value is not None and 'et' not in already_processed:
            already_processed.add('et')
            self.et = value
            self.validate_RTTITimeType(self.et)    # validate type RTTITimeType
        value = find_attr_value_('wet', node)
        if value is not None and 'wet' not in already_processed:
            already_processed.add('wet')
            self.wet = value
            self.validate_RTTITimeType(self.wet)    # validate type RTTITimeType
        value = find_attr_value_('at', node)
        if value is not None and 'at' not in already_processed:
            already_processed.add('at')
            self.at = value
            self.validate_RTTITimeType(self.at)    # validate type RTTITimeType
        value = find_attr_value_('atRemoved', node)
        if value is not None and 'atRemoved' not in already_processed:
            already_processed.add('atRemoved')
            if value in ('true', '1'):
                self.atRemoved = True
            elif value in ('false', '0'):
                self.atRemoved = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('atClass', node)
        if value is not None and 'atClass' not in already_processed:
            already_processed.add('atClass')
            self.atClass = value
        value = find_attr_value_('etmin', node)
        if value is not None and 'etmin' not in already_processed:
            already_processed.add('etmin')
            self.etmin = value
            self.validate_RTTITimeType(self.etmin)    # validate type RTTITimeType
        value = find_attr_value_('etUnknown', node)
        if value is not None and 'etUnknown' not in already_processed:
            already_processed.add('etUnknown')
            if value in ('true', '1'):
                self.etUnknown = True
            elif value in ('false', '0'):
                self.etUnknown = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('delayed', node)
        if value is not None and 'delayed' not in already_processed:
            already_processed.add('delayed')
            if value in ('true', '1'):
                self.delayed = True
            elif value in ('false', '0'):
                self.delayed = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('src', node)
        if value is not None and 'src' not in already_processed:
            already_processed.add('src')
            self.src = value
        value = find_attr_value_('srcInst', node)
        if value is not None and 'srcInst' not in already_processed:
            already_processed.add('srcInst')
            self.srcInst = value
            self.validate_SourceTypeInst(self.srcInst)    # validate type SourceTypeInst
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class TSTimeData


class TSLocation(GeneratedsSuper):
    """Forecast data for an individual location in the service's
    scheduleTIPLOC"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, tpl=None, wta=None, wtd=None, wtp=None, pta=None, ptd=None, arr=None, dep=None, pass_=None, plat=None, suppr=False, length=0, detachFront=False, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.tpl = _cast(None, tpl)
        self.tpl_nsprefix_ = None
        self.wta = _cast(None, wta)
        self.wta_nsprefix_ = None
        self.wtd = _cast(None, wtd)
        self.wtd_nsprefix_ = None
        self.wtp = _cast(None, wtp)
        self.wtp_nsprefix_ = None
        self.pta = _cast(None, pta)
        self.pta_nsprefix_ = None
        self.ptd = _cast(None, ptd)
        self.ptd_nsprefix_ = None
        self.arr = arr
        self.arr_nsprefix_ = None
        self.dep = dep
        self.dep_nsprefix_ = None
        self.pass_ = pass_
        self.pass__nsprefix_ = None
        self.plat = plat
        self.plat_nsprefix_ = None
        self.suppr = suppr
        self.suppr_nsprefix_ = None
        self.length = length
        self.validate_TrainLengthType(self.length)
        self.length_nsprefix_ = None
        self.detachFront = detachFront
        self.detachFront_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TSLocation)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TSLocation.subclass:
            return TSLocation.subclass(*args_, **kwargs_)
        else:
            return TSLocation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TrainLengthType(self, value):
        result = True
        # Validate type TrainLengthType, a restriction on xs:unsignedShort.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, int):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (int)' % {"value": value, "lineno": lineno, })
                return False
            if value > 99:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxInclusive restriction on TrainLengthType' % {"value": value, "lineno": lineno} )
                result = False
        return result
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_WTimeType(self, value):
        # Validate type tns:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_RTTITimeType(self, value):
        # Validate type tns:RTTITimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_RTTITimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_RTTITimeType_patterns_, ))
    validate_RTTITimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9])$']]
    def hasContent_(self):
        if (
            self.arr is not None or
            self.dep is not None or
            self.pass_ is not None or
            self.plat is not None or
            self.suppr or
            self.length != 0 or
            self.detachFront
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1"  xmlns:ct="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='TSLocation', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TSLocation')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TSLocation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TSLocation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='TSLocation'):
        if 'tpl' not in already_processed:
            already_processed.add('tpl')
            outfile.write(' tpl=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tpl), input_name='tpl')), ))
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            outfile.write(' wta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wta), input_name='wta')), ))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            outfile.write(' wtd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtd), input_name='wtd')), ))
        if self.wtp is not None and 'wtp' not in already_processed:
            already_processed.add('wtp')
            outfile.write(' wtp=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtp), input_name='wtp')), ))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            outfile.write(' pta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.pta), input_name='pta')), ))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            outfile.write(' ptd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ptd), input_name='ptd')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1"  xmlns:ct="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='TSLocation', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.arr is not None:
            namespaceprefix_ = self.arr_nsprefix_ + ':' if (UseCapturedNS_ and self.arr_nsprefix_) else ''
            self.arr.export(outfile, level, namespaceprefix_, namespacedef_='', name_='arr', pretty_print=pretty_print)
        if self.dep is not None:
            namespaceprefix_ = self.dep_nsprefix_ + ':' if (UseCapturedNS_ and self.dep_nsprefix_) else ''
            self.dep.export(outfile, level, namespaceprefix_, namespacedef_='', name_='dep', pretty_print=pretty_print)
        if self.pass_ is not None:
            namespaceprefix_ = self.pass__nsprefix_ + ':' if (UseCapturedNS_ and self.pass__nsprefix_) else ''
            self.pass_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='pass', pretty_print=pretty_print)
        if self.plat is not None:
            namespaceprefix_ = self.plat_nsprefix_ + ':' if (UseCapturedNS_ and self.plat_nsprefix_) else ''
            self.plat.export(outfile, level, namespaceprefix_, namespacedef_='', name_='plat', pretty_print=pretty_print)
        if self.suppr:
            namespaceprefix_ = self.suppr_nsprefix_ + ':' if (UseCapturedNS_ and self.suppr_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%ssuppr>%s</%ssuppr>%s' % (namespaceprefix_ , self.gds_format_boolean(self.suppr, input_name='suppr'), namespaceprefix_ , eol_))
        if self.length != 0:
            namespaceprefix_ = self.length_nsprefix_ + ':' if (UseCapturedNS_ and self.length_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%slength>%s</%slength>%s' % (namespaceprefix_ , self.gds_format_integer(self.length, input_name='length'), namespaceprefix_ , eol_))
        if self.detachFront:
            namespaceprefix_ = self.detachFront_nsprefix_ + ':' if (UseCapturedNS_ and self.detachFront_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sdetachFront>%s</%sdetachFront>%s' % (namespaceprefix_ , self.gds_format_boolean(self.detachFront, input_name='detachFront'), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='TSLocation', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.tpl is not None:
            element.set('tpl', self.gds_format_string(self.tpl))
        if self.wta is not None:
            element.set('wta', self.gds_format_string(self.wta))
        if self.wtd is not None:
            element.set('wtd', self.gds_format_string(self.wtd))
        if self.wtp is not None:
            element.set('wtp', self.gds_format_string(self.wtp))
        if self.pta is not None:
            element.set('pta', self.gds_format_string(self.pta))
        if self.ptd is not None:
            element.set('ptd', self.gds_format_string(self.ptd))
        if self.arr is not None:
            arr_ = self.arr
            arr_.to_etree(element, name_='arr', mapping_=mapping_)
        if self.dep is not None:
            dep_ = self.dep
            dep_.to_etree(element, name_='dep', mapping_=mapping_)
        if self.pass_ is not None:
            pass__ = self.pass_
            pass__.to_etree(element, name_='pass', mapping_=mapping_)
        if self.plat is not None:
            plat_ = self.plat
            plat_.to_etree(element, name_='plat', mapping_=mapping_)
        if self.suppr is not None:
            suppr_ = self.suppr
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}suppr').text = self.gds_format_boolean(suppr_)
        if self.length is not None:
            length_ = self.length
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}length').text = self.gds_format_integer(length_)
        if self.detachFront is not None:
            detachFront_ = self.detachFront
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}detachFront').text = self.gds_format_boolean(detachFront_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='TSLocation'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.tpl is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            showIndent(outfile, level)
            outfile.write('tpl=%s,\n' % (self.tpl,))
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            showIndent(outfile, level)
            outfile.write('wta=%s,\n' % (self.wta,))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            showIndent(outfile, level)
            outfile.write('wtd=%s,\n' % (self.wtd,))
        if self.wtp is not None and 'wtp' not in already_processed:
            already_processed.add('wtp')
            showIndent(outfile, level)
            outfile.write('wtp=%s,\n' % (self.wtp,))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            showIndent(outfile, level)
            outfile.write('pta=%s,\n' % (self.pta,))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            showIndent(outfile, level)
            outfile.write('ptd=%s,\n' % (self.ptd,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.arr is not None:
            showIndent(outfile, level)
            outfile.write('arr=model_.TSTimeData(\n')
            self.arr.exportLiteral(outfile, level, name_='arr')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.dep is not None:
            showIndent(outfile, level)
            outfile.write('dep=model_.TSTimeData(\n')
            self.dep.exportLiteral(outfile, level, name_='dep')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.pass_ is not None:
            showIndent(outfile, level)
            outfile.write('pass_=model_.TSTimeData(\n')
            self.pass_.exportLiteral(outfile, level, name_='pass')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.plat is not None:
            showIndent(outfile, level)
            outfile.write('plat=model_.PlatformData(\n')
            self.plat.exportLiteral(outfile, level, name_='plat')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.suppr is not None:
            showIndent(outfile, level)
            outfile.write('suppr=%s,\n' % self.suppr)
        if self.length is not None:
            showIndent(outfile, level)
            outfile.write('length=%d,\n' % self.length)
        if self.detachFront is not None:
            showIndent(outfile, level)
            outfile.write('detachFront=%s,\n' % self.detachFront)
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.TSLocation_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.tpl is not None:
            dbobj.tpl = self.tpl
        if self.wta is not None:
            dbobj.wta = self.wta
        if self.wtd is not None:
            dbobj.wtd = self.wtd
        if self.wtp is not None:
            dbobj.wtp = self.wtp
        if self.pta is not None:
            dbobj.pta = self.pta
        if self.ptd is not None:
            dbobj.ptd = self.ptd
    def exportSQLAlchemyChildren(self, session, dbobj):
        if self.arr is not None:
            child_dbobj = self.arr.exportSQLAlchemy(session)
            dbobj.arr = child_dbobj
        if self.dep is not None:
            child_dbobj = self.dep.exportSQLAlchemy(session)
            dbobj.dep = child_dbobj
        if self.pass_ is not None:
            child_dbobj = self.pass_.exportSQLAlchemy(session)
            dbobj.pass_x = child_dbobj
        if self.plat is not None:
            child_dbobj = self.plat.exportSQLAlchemy(session)
            dbobj.plat = child_dbobj
        if self.suppr is not None:
            dbobj.suppr = self.suppr
        if self.length is not None:
            dbobj.length = self.length
        if self.detachFront is not None:
            dbobj.detachFront = self.detachFront
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('tpl', node)
        if value is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            self.tpl = value
            self.validate_TiplocType(self.tpl)    # validate type TiplocType
        value = find_attr_value_('wta', node)
        if value is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            self.wta = value
            self.validate_WTimeType(self.wta)    # validate type WTimeType
        value = find_attr_value_('wtd', node)
        if value is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            self.wtd = value
            self.validate_WTimeType(self.wtd)    # validate type WTimeType
        value = find_attr_value_('wtp', node)
        if value is not None and 'wtp' not in already_processed:
            already_processed.add('wtp')
            self.wtp = value
            self.validate_WTimeType(self.wtp)    # validate type WTimeType
        value = find_attr_value_('pta', node)
        if value is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            self.pta = value
            self.validate_RTTITimeType(self.pta)    # validate type RTTITimeType
        value = find_attr_value_('ptd', node)
        if value is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            self.ptd = value
            self.validate_RTTITimeType(self.ptd)    # validate type RTTITimeType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'arr':
            obj_ = TSTimeData.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.arr = obj_
            obj_.original_tagname_ = 'arr'
        elif nodeName_ == 'dep':
            obj_ = TSTimeData.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.dep = obj_
            obj_.original_tagname_ = 'dep'
        elif nodeName_ == 'pass':
            obj_ = TSTimeData.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.pass_ = obj_
            obj_.original_tagname_ = 'pass'
        elif nodeName_ == 'plat':
            obj_ = PlatformData.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.plat = obj_
            obj_.original_tagname_ = 'plat'
        elif nodeName_ == 'suppr':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'suppr')
            ival_ = self.gds_validate_boolean(ival_, node, 'suppr')
            self.suppr = ival_
            self.suppr_nsprefix_ = child_.prefix
        elif nodeName_ == 'length' and child_.text:
            sval_ = child_.text
            ival_ = self.gds_parse_integer(sval_, node, 'length')
            ival_ = self.gds_validate_integer(ival_, node, 'length')
            self.length = ival_
            self.length_nsprefix_ = child_.prefix
            # validate type TrainLengthType
            self.validate_TrainLengthType(self.length)
        elif nodeName_ == 'detachFront':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'detachFront')
            ival_ = self.gds_validate_boolean(ival_, node, 'detachFront')
            self.detachFront = ival_
            self.detachFront_nsprefix_ = child_.prefix
# end class TSLocation


class TS(GeneratedsSuper):
    """Train Status. Update to the "real time" forecast data for a service.RTTI
    unique Train IdentifierTrain UIDScheduled Start DateIndicates whether a
    train that divides is working with portions in reverse to their normal
    formation. The value applies to the whole train. Darwin will not
    validate that a divide association actually exists for this service."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, rid=None, uid=None, ssd=None, isReverseFormation=False, LateReason=None, Location=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.rid = _cast(None, rid)
        self.rid_nsprefix_ = None
        self.uid = _cast(None, uid)
        self.uid_nsprefix_ = None
        self.ssd = _cast(None, ssd)
        self.ssd_nsprefix_ = None
        self.isReverseFormation = _cast(bool, isReverseFormation)
        self.isReverseFormation_nsprefix_ = None
        self.LateReason = LateReason
        self.LateReason_nsprefix_ = None
        if Location is None:
            self.Location = []
        else:
            self.Location = Location
        self.Location_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TS)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TS.subclass:
            return TS.subclass(*args_, **kwargs_)
        else:
            return TS(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_RIDType(self, value):
        # Validate type ct:RIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on RIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_UIDType(self, value):
        # Validate type ct:UIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 6:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on UIDType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_RTTIDateType(self, value):
        # Validate type ct:RTTIDateType, a restriction on xs:date.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, datetime_.date):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (datetime_.date)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def hasContent_(self):
        if (
            self.LateReason is not None or
            self.Location
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:ct="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='TS', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TS')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TS')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TS', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='TS'):
        if 'rid' not in already_processed:
            already_processed.add('rid')
            outfile.write(' rid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.rid), input_name='rid')), ))
        if 'uid' not in already_processed:
            already_processed.add('uid')
            outfile.write(' uid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.uid), input_name='uid')), ))
        if 'ssd' not in already_processed:
            already_processed.add('ssd')
            outfile.write(' ssd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ssd), input_name='ssd')), ))
        if self.isReverseFormation and 'isReverseFormation' not in already_processed:
            already_processed.add('isReverseFormation')
            outfile.write(' isReverseFormation="%s"' % self.gds_format_boolean(self.isReverseFormation, input_name='isReverseFormation'))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:ct="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='TS', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.LateReason is not None:
            namespaceprefix_ = self.LateReason_nsprefix_ + ':' if (UseCapturedNS_ and self.LateReason_nsprefix_) else ''
            self.LateReason.export(outfile, level, namespaceprefix_, namespacedef_='', name_='LateReason', pretty_print=pretty_print)
        for Location_ in self.Location:
            namespaceprefix_ = self.Location_nsprefix_ + ':' if (UseCapturedNS_ and self.Location_nsprefix_) else ''
            Location_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Location', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='TS', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.rid is not None:
            element.set('rid', self.gds_format_string(self.rid))
        if self.uid is not None:
            element.set('uid', self.gds_format_string(self.uid))
        if self.ssd is not None:
            element.set('ssd', self.gds_format_date(self.ssd))
        if self.isReverseFormation is not None:
            element.set('isReverseFormation', self.gds_format_boolean(self.isReverseFormation))
        if self.LateReason is not None:
            LateReason_ = self.LateReason
            LateReason_.to_etree(element, name_='LateReason', mapping_=mapping_)
        for Location_ in self.Location:
            Location_.to_etree(element, name_='Location', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='TS'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.rid is not None and 'rid' not in already_processed:
            already_processed.add('rid')
            showIndent(outfile, level)
            outfile.write('rid=%s,\n' % (self.rid,))
        if self.uid is not None and 'uid' not in already_processed:
            already_processed.add('uid')
            showIndent(outfile, level)
            outfile.write('uid=%s,\n' % (self.uid,))
        if self.ssd is not None and 'ssd' not in already_processed:
            already_processed.add('ssd')
            showIndent(outfile, level)
            outfile.write('ssd=%s,\n' % (self.ssd,))
        if self.isReverseFormation is not None and 'isReverseFormation' not in already_processed:
            already_processed.add('isReverseFormation')
            showIndent(outfile, level)
            outfile.write('isReverseFormation=%s,\n' % (self.isReverseFormation,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.LateReason is not None:
            showIndent(outfile, level)
            outfile.write('LateReason=model_.DisruptionReasonType(\n')
            self.LateReason.exportLiteral(outfile, level, name_='LateReason')
            showIndent(outfile, level)
            outfile.write('),\n')
        showIndent(outfile, level)
        outfile.write('Location=[\n')
        level += 1
        for Location_ in self.Location:
            showIndent(outfile, level)
            outfile.write('model_.TSLocation(\n')
            Location_.exportLiteral(outfile, level, name_='TSLocation')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.TS_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.rid is not None:
            dbobj.rid = self.rid
        if self.uid is not None:
            dbobj.uid = self.uid
        if self.ssd is not None:
            dbobj.ssd = self.ssd
        if self.isReverseFormation is not None:
            dbobj.isReverseFormation = self.isReverseFormation
    def exportSQLAlchemyChildren(self, session, dbobj):
        if self.LateReason is not None:
            child_dbobj = self.LateReason.exportSQLAlchemy(session)
            dbobj.LateReason = child_dbobj
        for child in self.Location:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.Location.append(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('rid', node)
        if value is not None and 'rid' not in already_processed:
            already_processed.add('rid')
            self.rid = value
            self.validate_RIDType(self.rid)    # validate type RIDType
        value = find_attr_value_('uid', node)
        if value is not None and 'uid' not in already_processed:
            already_processed.add('uid')
            self.uid = value
            self.validate_UIDType(self.uid)    # validate type UIDType
        value = find_attr_value_('ssd', node)
        if value is not None and 'ssd' not in already_processed:
            already_processed.add('ssd')
            try:
                self.ssd = self.gds_parse_date(value)
            except ValueError as exp:
                raise ValueError('Bad date attribute (ssd): %s' % exp)
            self.validate_RTTIDateType(self.ssd)    # validate type RTTIDateType
        value = find_attr_value_('isReverseFormation', node)
        if value is not None and 'isReverseFormation' not in already_processed:
            already_processed.add('isReverseFormation')
            if value in ('true', '1'):
                self.isReverseFormation = True
            elif value in ('false', '0'):
                self.isReverseFormation = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'LateReason':
            obj_ = DisruptionReasonType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.LateReason = obj_
            obj_.original_tagname_ = 'LateReason'
        elif nodeName_ == 'Location':
            obj_ = TSLocation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Location.append(obj_)
            obj_.original_tagname_ = 'Location'
# end class TS


class TrainOrderItem(GeneratedsSuper):
    """Describes the identifier of a train in the train order"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, rid=None, trainID=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.rid = rid
        self.rid_nsprefix_ = None
        self.trainID = trainID
        self.validate_TrainIdType(self.trainID)
        self.trainID_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TrainOrderItem)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TrainOrderItem.subclass:
            return TrainOrderItem.subclass(*args_, **kwargs_)
        else:
            return TrainOrderItem(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TrainIdType(self, value):
        result = True
        # Validate type TrainIdType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on TrainIdType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TrainIdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TrainIdType_patterns_, ))
                result = False
        return result
    validate_TrainIdType_patterns_ = [['^([0-9][A-Z][0-9][0-9])$']]
    def hasContent_(self):
        if (
            self.rid is not None or
            self.trainID is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1"  xmlns:ct="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='TrainOrderItem', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TrainOrderItem')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TrainOrderItem')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TrainOrderItem', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='TrainOrderItem'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1"  xmlns:ct="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='TrainOrderItem', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.rid is not None:
            namespaceprefix_ = self.rid_nsprefix_ + ':' if (UseCapturedNS_ and self.rid_nsprefix_) else ''
            self.rid.export(outfile, level, namespaceprefix_, namespacedef_='', name_='rid', pretty_print=pretty_print)
        if self.trainID is not None:
            namespaceprefix_ = self.trainID_nsprefix_ + ':' if (UseCapturedNS_ and self.trainID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%strainID>%s</%strainID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.trainID), input_name='trainID')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='TrainOrderItem', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.rid is not None:
            rid_ = self.rid
            rid_.to_etree(element, name_='rid', mapping_=mapping_)
        if self.trainID is not None:
            trainID_ = self.trainID
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}trainID').text = self.gds_format_string(trainID_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='TrainOrderItem'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.rid is not None:
            showIndent(outfile, level)
            outfile.write('rid=model_.ridType(\n')
            self.rid.exportLiteral(outfile, level, name_='rid')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.trainID is not None:
            showIndent(outfile, level)
            outfile.write('trainID=%s,\n' % self.gds_encode(quote_python(self.trainID)))
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.TrainOrderItem_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        if self.rid is not None:
            child_dbobj = self.rid.exportSQLAlchemy(session)
            dbobj.rid = child_dbobj
        if self.trainID is not None:
            dbobj.trainID = self.trainID
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'rid':
            obj_ = ridType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.rid = obj_
            obj_.original_tagname_ = 'rid'
        elif nodeName_ == 'trainID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'trainID')
            value_ = self.gds_validate_string(value_, node, 'trainID')
            self.trainID = value_
            self.trainID_nsprefix_ = child_.prefix
            # validate type TrainIdType
            self.validate_TrainIdType(self.trainID)
# end class TrainOrderItem


class TrainOrderData(GeneratedsSuper):
    """Defines the sequence of trains making up the train order"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, first=None, second=None, third=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.first = first
        self.first_nsprefix_ = None
        self.second = second
        self.second_nsprefix_ = None
        self.third = third
        self.third_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TrainOrderData)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TrainOrderData.subclass:
            return TrainOrderData.subclass(*args_, **kwargs_)
        else:
            return TrainOrderData(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.first is not None or
            self.second is not None or
            self.third is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='TrainOrderData', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TrainOrderData')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TrainOrderData')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TrainOrderData', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='TrainOrderData'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='TrainOrderData', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.first is not None:
            namespaceprefix_ = self.first_nsprefix_ + ':' if (UseCapturedNS_ and self.first_nsprefix_) else ''
            self.first.export(outfile, level, namespaceprefix_, namespacedef_='', name_='first', pretty_print=pretty_print)
        if self.second is not None:
            namespaceprefix_ = self.second_nsprefix_ + ':' if (UseCapturedNS_ and self.second_nsprefix_) else ''
            self.second.export(outfile, level, namespaceprefix_, namespacedef_='', name_='second', pretty_print=pretty_print)
        if self.third is not None:
            namespaceprefix_ = self.third_nsprefix_ + ':' if (UseCapturedNS_ and self.third_nsprefix_) else ''
            self.third.export(outfile, level, namespaceprefix_, namespacedef_='', name_='third', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='TrainOrderData', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.first is not None:
            first_ = self.first
            first_.to_etree(element, name_='first', mapping_=mapping_)
        if self.second is not None:
            second_ = self.second
            second_.to_etree(element, name_='second', mapping_=mapping_)
        if self.third is not None:
            third_ = self.third
            third_.to_etree(element, name_='third', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='TrainOrderData'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.first is not None:
            showIndent(outfile, level)
            outfile.write('first=model_.TrainOrderItem(\n')
            self.first.exportLiteral(outfile, level, name_='first')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.second is not None:
            showIndent(outfile, level)
            outfile.write('second=model_.TrainOrderItem(\n')
            self.second.exportLiteral(outfile, level, name_='second')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.third is not None:
            showIndent(outfile, level)
            outfile.write('third=model_.TrainOrderItem(\n')
            self.third.exportLiteral(outfile, level, name_='third')
            showIndent(outfile, level)
            outfile.write('),\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.TrainOrderData_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        if self.first is not None:
            child_dbobj = self.first.exportSQLAlchemy(session)
            dbobj.first = child_dbobj
        if self.second is not None:
            child_dbobj = self.second.exportSQLAlchemy(session)
            dbobj.second = child_dbobj
        if self.third is not None:
            child_dbobj = self.third.exportSQLAlchemy(session)
            dbobj.third = child_dbobj
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'first':
            obj_ = TrainOrderItem.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.first = obj_
            obj_.original_tagname_ = 'first'
        elif nodeName_ == 'second':
            obj_ = TrainOrderItem.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.second = obj_
            obj_.original_tagname_ = 'second'
        elif nodeName_ == 'third':
            obj_ = TrainOrderItem.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.third = obj_
            obj_.original_tagname_ = 'third'
# end class TrainOrderData


class TrainOrder(GeneratedsSuper):
    """Defines the expected Train order at a platformThe tiploc where the train
    order appliesThe CRS code of the station where the train order
    appliesThe platform number where the train order applies"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, tiploc=None, crs=None, platform=None, set=None, clear=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.tiploc = _cast(None, tiploc)
        self.tiploc_nsprefix_ = None
        self.crs = _cast(None, crs)
        self.crs_nsprefix_ = None
        self.platform = _cast(None, platform)
        self.platform_nsprefix_ = None
        self.set = set
        self.set_nsprefix_ = None
        self.clear = clear
        self.clear_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TrainOrder)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TrainOrder.subclass:
            return TrainOrder.subclass(*args_, **kwargs_)
        else:
            return TrainOrder(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_CrsType(self, value):
        # Validate type ct:CrsType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on CrsType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_PlatformType(self, value):
        # Validate type ct:PlatformType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on PlatformType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on PlatformType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.set is not None or
            self.clear is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='TrainOrder', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TrainOrder')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TrainOrder')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TrainOrder', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='TrainOrder'):
        if 'tiploc' not in already_processed:
            already_processed.add('tiploc')
            outfile.write(' tiploc=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tiploc), input_name='tiploc')), ))
        if 'crs' not in already_processed:
            already_processed.add('crs')
            outfile.write(' crs=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.crs), input_name='crs')), ))
        if 'platform' not in already_processed:
            already_processed.add('platform')
            outfile.write(' platform=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.platform), input_name='platform')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='TrainOrder', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.set is not None:
            namespaceprefix_ = self.set_nsprefix_ + ':' if (UseCapturedNS_ and self.set_nsprefix_) else ''
            self.set.export(outfile, level, namespaceprefix_, namespacedef_='', name_='set', pretty_print=pretty_print)
        if self.clear is not None:
            namespaceprefix_ = self.clear_nsprefix_ + ':' if (UseCapturedNS_ and self.clear_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sclear>%s</%sclear>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.clear), input_name='clear')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='TrainOrder', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.tiploc is not None:
            element.set('tiploc', self.gds_format_string(self.tiploc))
        if self.crs is not None:
            element.set('crs', self.gds_format_string(self.crs))
        if self.platform is not None:
            element.set('platform', self.gds_format_string(self.platform))
        if self.set is not None:
            set_ = self.set
            set_.to_etree(element, name_='set', mapping_=mapping_)
        if self.clear is not None:
            clear_ = self.clear
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}clear').text = self.gds_format_string(clear_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='TrainOrder'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.tiploc is not None and 'tiploc' not in already_processed:
            already_processed.add('tiploc')
            showIndent(outfile, level)
            outfile.write('tiploc=%s,\n' % (self.tiploc,))
        if self.crs is not None and 'crs' not in already_processed:
            already_processed.add('crs')
            showIndent(outfile, level)
            outfile.write('crs=%s,\n' % (self.crs,))
        if self.platform is not None and 'platform' not in already_processed:
            already_processed.add('platform')
            showIndent(outfile, level)
            outfile.write('platform=%s,\n' % (self.platform,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.set is not None:
            showIndent(outfile, level)
            outfile.write('set=model_.TrainOrderData(\n')
            self.set.exportLiteral(outfile, level, name_='set')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.clear is not None:
            showIndent(outfile, level)
            outfile.write('clear=%s,\n' % self.gds_encode(quote_python(self.clear)))
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.TrainOrder_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.tiploc is not None:
            dbobj.tiploc = self.tiploc
        if self.crs is not None:
            dbobj.crs = self.crs
        if self.platform is not None:
            dbobj.platform = self.platform
    def exportSQLAlchemyChildren(self, session, dbobj):
        if self.set is not None:
            child_dbobj = self.set.exportSQLAlchemy(session)
            dbobj.set = child_dbobj
        if self.clear is not None:
            dbobj.clear = self.clear
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('tiploc', node)
        if value is not None and 'tiploc' not in already_processed:
            already_processed.add('tiploc')
            self.tiploc = value
            self.validate_TiplocType(self.tiploc)    # validate type TiplocType
        value = find_attr_value_('crs', node)
        if value is not None and 'crs' not in already_processed:
            already_processed.add('crs')
            self.crs = value
            self.validate_CrsType(self.crs)    # validate type CrsType
        value = find_attr_value_('platform', node)
        if value is not None and 'platform' not in already_processed:
            already_processed.add('platform')
            self.platform = value
            self.validate_PlatformType(self.platform)    # validate type PlatformType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'set':
            obj_ = TrainOrderData.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.set = obj_
            obj_.original_tagname_ = 'set'
        elif nodeName_ == 'clear':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'clear')
            value_ = self.gds_validate_string(value_, node, 'clear')
            self.clear = value_
            self.clear_nsprefix_ = child_.prefix
# end class TrainOrder


class clear(GeneratedsSuper):
    """Clear the current train order"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, clear)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if clear.subclass:
            return clear.subclass(*args_, **kwargs_)
        else:
            return clear(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='clear', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('clear')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='clear')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='clear', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='clear'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='clear', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='clear', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='clear'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.clear_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class clear


class StationMessage(GeneratedsSuper):
    """Darwin Workstation Station MessageThe category of messageThe severity of
    the messageWhether the train running information is suppressed to the
    public"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, cat=None, sev=None, suppress=False, Station=None, Msg=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(int, id)
        self.id_nsprefix_ = None
        self.cat = _cast(None, cat)
        self.cat_nsprefix_ = None
        self.sev = _cast(None, sev)
        self.sev_nsprefix_ = None
        self.suppress = _cast(bool, suppress)
        self.suppress_nsprefix_ = None
        if Station is None:
            self.Station = []
        else:
            self.Station = Station
        self.Station_nsprefix_ = None
        self.Msg = Msg
        self.Msg_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, StationMessage)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if StationMessage.subclass:
            return StationMessage.subclass(*args_, **kwargs_)
        else:
            return StationMessage(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_MsgCategoryType(self, value):
        # Validate type tns:MsgCategoryType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Train', 'Station', 'Connections', 'System', 'Misc', 'PriorTrains', 'PriorOther']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on MsgCategoryType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_MsgSeverityType(self, value):
        # Validate type tns:MsgSeverityType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['0', '1', '2', '3']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on MsgSeverityType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.Station or
            self.Msg is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='StationMessage', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('StationMessage')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='StationMessage')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='StationMessage', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='StationMessage'):
        if 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id="%s"' % self.gds_format_integer(self.id, input_name='id'))
        if 'cat' not in already_processed:
            already_processed.add('cat')
            outfile.write(' cat=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.cat), input_name='cat')), ))
        if 'sev' not in already_processed:
            already_processed.add('sev')
            outfile.write(' sev=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.sev), input_name='sev')), ))
        if self.suppress and 'suppress' not in already_processed:
            already_processed.add('suppress')
            outfile.write(' suppress="%s"' % self.gds_format_boolean(self.suppress, input_name='suppress'))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='StationMessage', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Station_ in self.Station:
            namespaceprefix_ = self.Station_nsprefix_ + ':' if (UseCapturedNS_ and self.Station_nsprefix_) else ''
            Station_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Station', pretty_print=pretty_print)
        if self.Msg is not None:
            namespaceprefix_ = self.Msg_nsprefix_ + ':' if (UseCapturedNS_ and self.Msg_nsprefix_) else ''
            self.Msg.export(outfile, level, namespaceprefix_, namespacedef_='', name_='Msg', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='StationMessage', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.id is not None:
            element.set('id', self.gds_format_integer(self.id))
        if self.cat is not None:
            element.set('cat', self.gds_format_string(self.cat))
        if self.sev is not None:
            element.set('sev', self.gds_format_string(self.sev))
        if self.suppress is not None:
            element.set('suppress', self.gds_format_boolean(self.suppress))
        for Station_ in self.Station:
            Station_.to_etree(element, name_='Station', mapping_=mapping_)
        if self.Msg is not None:
            Msg_ = self.Msg
            Msg_.to_etree(element, name_='Msg', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='StationMessage'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            showIndent(outfile, level)
            outfile.write('id=%d,\n' % (self.id,))
        if self.cat is not None and 'cat' not in already_processed:
            already_processed.add('cat')
            showIndent(outfile, level)
            outfile.write('cat=%s,\n' % (self.cat,))
        if self.sev is not None and 'sev' not in already_processed:
            already_processed.add('sev')
            showIndent(outfile, level)
            outfile.write('sev=%s,\n' % (self.sev,))
        if self.suppress is not None and 'suppress' not in already_processed:
            already_processed.add('suppress')
            showIndent(outfile, level)
            outfile.write('suppress=%s,\n' % (self.suppress,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Station=[\n')
        level += 1
        for Station_ in self.Station:
            showIndent(outfile, level)
            outfile.write('model_.StationType(\n')
            Station_.exportLiteral(outfile, level, name_='StationType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Msg is not None:
            showIndent(outfile, level)
            outfile.write('Msg=model_.MsgType(\n')
            self.Msg.exportLiteral(outfile, level, name_='Msg')
            showIndent(outfile, level)
            outfile.write('),\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.StationMessage_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.id is not None:
            dbobj.id_x = self.id
        if self.cat is not None:
            dbobj.cat = self.cat
        if self.sev is not None:
            dbobj.sev = self.sev
        if self.suppress is not None:
            dbobj.suppress = self.suppress
    def exportSQLAlchemyChildren(self, session, dbobj):
        for child in self.Station:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.Station.append(child_dbobj)
        if self.Msg is not None:
            child_dbobj = self.Msg.exportSQLAlchemy(session)
            dbobj.Msg = child_dbobj
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = self.gds_parse_integer(value, node, 'id')
        value = find_attr_value_('cat', node)
        if value is not None and 'cat' not in already_processed:
            already_processed.add('cat')
            self.cat = value
            self.validate_MsgCategoryType(self.cat)    # validate type MsgCategoryType
        value = find_attr_value_('sev', node)
        if value is not None and 'sev' not in already_processed:
            already_processed.add('sev')
            self.sev = value
            self.validate_MsgSeverityType(self.sev)    # validate type MsgSeverityType
        value = find_attr_value_('suppress', node)
        if value is not None and 'suppress' not in already_processed:
            already_processed.add('suppress')
            if value in ('true', '1'):
                self.suppress = True
            elif value in ('false', '0'):
                self.suppress = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Station':
            obj_ = StationType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Station.append(obj_)
            obj_.original_tagname_ = 'Station'
        elif nodeName_ == 'Msg':
            obj_ = MsgType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.Msg = obj_
            obj_.original_tagname_ = 'Msg'
# end class StationMessage


class p(GeneratedsSuper):
    """Defines an HTML paragraph"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, a=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if a is None:
            self.a = []
        else:
            self.a = a
        self.a_nsprefix_ = None
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, p)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if p.subclass:
            return p.subclass(*args_, **kwargs_)
        else:
            return p(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.a or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='p', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('p')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='p')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='p', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='p'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='p', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for a_ in self.a:
            namespaceprefix_ = self.a_nsprefix_ + ':' if (UseCapturedNS_ and self.a_nsprefix_) else ''
            a_.export(outfile, level, namespaceprefix_='tns:', namespacedef_='', name_='a', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='p', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        for item_ in self.content_:
            item_.to_etree(element)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='p'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('],\n')
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.p_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        for child in self.a:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.a.append(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'a':
            obj_ = a.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'a', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_a'):
              self.add_a(obj_.value)
            elif hasattr(self, 'set_a'):
              self.set_a(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class p


class a(GeneratedsSuper):
    """Defines an HTML anchor"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, href=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.href = _cast(None, href)
        self.href_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, a)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if a.subclass:
            return a.subclass(*args_, **kwargs_)
        else:
            return a(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='a', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('a')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='a')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='a', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='a'):
        if 'href' not in already_processed:
            already_processed.add('href')
            outfile.write(' href=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.href), input_name='href')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='a', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='a', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.href is not None:
            element.set('href', self.gds_format_string(self.href))
        if self.hasContent_():
            element.text = self.gds_format_string(self.get_valueOf_())
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='a'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.href is not None and 'href' not in already_processed:
            already_processed.add('href')
            showIndent(outfile, level)
            outfile.write('href="%s",\n' % (self.href,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.a_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.href is not None:
            dbobj.href = self.href
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('href', node)
        if value is not None and 'href' not in already_processed:
            already_processed.add('href')
            self.href = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class a


class TrainAlert(GeneratedsSuper):
    """Train Alert"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, AlertID=None, AlertServices=None, SendAlertBySMS=None, SendAlertByEmail=None, SendAlertByTwitter=None, Source=None, AlertText=None, Audience=None, AlertType=None, CopiedFromAlertID=None, CopiedFromSource=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.AlertID = AlertID
        self.AlertID_nsprefix_ = None
        self.AlertServices = AlertServices
        self.AlertServices_nsprefix_ = None
        self.SendAlertBySMS = SendAlertBySMS
        self.SendAlertBySMS_nsprefix_ = None
        self.SendAlertByEmail = SendAlertByEmail
        self.SendAlertByEmail_nsprefix_ = None
        self.SendAlertByTwitter = SendAlertByTwitter
        self.SendAlertByTwitter_nsprefix_ = None
        self.Source = Source
        self.Source_nsprefix_ = None
        self.AlertText = AlertText
        self.AlertText_nsprefix_ = None
        self.Audience = Audience
        self.validate_AlertAudienceType(self.Audience)
        self.Audience_nsprefix_ = None
        self.AlertType = AlertType
        self.validate_AlertType(self.AlertType)
        self.AlertType_nsprefix_ = None
        self.CopiedFromAlertID = CopiedFromAlertID
        self.CopiedFromAlertID_nsprefix_ = None
        self.CopiedFromSource = CopiedFromSource
        self.CopiedFromSource_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TrainAlert)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TrainAlert.subclass:
            return TrainAlert.subclass(*args_, **kwargs_)
        else:
            return TrainAlert(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_AlertAudienceType(self, value):
        result = True
        # Validate type AlertAudienceType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Customer', 'Staff', 'Operations']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on AlertAudienceType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_AlertType(self, value):
        result = True
        # Validate type AlertType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Normal', 'Forced']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on AlertType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def hasContent_(self):
        if (
            self.AlertID is not None or
            self.AlertServices is not None or
            self.SendAlertBySMS is not None or
            self.SendAlertByEmail is not None or
            self.SendAlertByTwitter is not None or
            self.Source is not None or
            self.AlertText is not None or
            self.Audience is not None or
            self.AlertType is not None or
            self.CopiedFromAlertID is not None or
            self.CopiedFromSource is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='TrainAlert', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TrainAlert')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TrainAlert')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TrainAlert', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='TrainAlert'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='TrainAlert', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.AlertID is not None:
            namespaceprefix_ = self.AlertID_nsprefix_ + ':' if (UseCapturedNS_ and self.AlertID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAlertID>%s</%sAlertID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.AlertID), input_name='AlertID')), namespaceprefix_ , eol_))
        if self.AlertServices is not None:
            namespaceprefix_ = self.AlertServices_nsprefix_ + ':' if (UseCapturedNS_ and self.AlertServices_nsprefix_) else ''
            self.AlertServices.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AlertServices', pretty_print=pretty_print)
        if self.SendAlertBySMS is not None:
            namespaceprefix_ = self.SendAlertBySMS_nsprefix_ + ':' if (UseCapturedNS_ and self.SendAlertBySMS_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSendAlertBySMS>%s</%sSendAlertBySMS>%s' % (namespaceprefix_ , self.gds_format_boolean(self.SendAlertBySMS, input_name='SendAlertBySMS'), namespaceprefix_ , eol_))
        if self.SendAlertByEmail is not None:
            namespaceprefix_ = self.SendAlertByEmail_nsprefix_ + ':' if (UseCapturedNS_ and self.SendAlertByEmail_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSendAlertByEmail>%s</%sSendAlertByEmail>%s' % (namespaceprefix_ , self.gds_format_boolean(self.SendAlertByEmail, input_name='SendAlertByEmail'), namespaceprefix_ , eol_))
        if self.SendAlertByTwitter is not None:
            namespaceprefix_ = self.SendAlertByTwitter_nsprefix_ + ':' if (UseCapturedNS_ and self.SendAlertByTwitter_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSendAlertByTwitter>%s</%sSendAlertByTwitter>%s' % (namespaceprefix_ , self.gds_format_boolean(self.SendAlertByTwitter, input_name='SendAlertByTwitter'), namespaceprefix_ , eol_))
        if self.Source is not None:
            namespaceprefix_ = self.Source_nsprefix_ + ':' if (UseCapturedNS_ and self.Source_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sSource>%s</%sSource>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Source), input_name='Source')), namespaceprefix_ , eol_))
        if self.AlertText is not None:
            namespaceprefix_ = self.AlertText_nsprefix_ + ':' if (UseCapturedNS_ and self.AlertText_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAlertText>%s</%sAlertText>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.AlertText), input_name='AlertText')), namespaceprefix_ , eol_))
        if self.Audience is not None:
            namespaceprefix_ = self.Audience_nsprefix_ + ':' if (UseCapturedNS_ and self.Audience_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAudience>%s</%sAudience>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.Audience), input_name='Audience')), namespaceprefix_ , eol_))
        if self.AlertType is not None:
            namespaceprefix_ = self.AlertType_nsprefix_ + ':' if (UseCapturedNS_ and self.AlertType_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sAlertType>%s</%sAlertType>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.AlertType), input_name='AlertType')), namespaceprefix_ , eol_))
        if self.CopiedFromAlertID is not None:
            namespaceprefix_ = self.CopiedFromAlertID_nsprefix_ + ':' if (UseCapturedNS_ and self.CopiedFromAlertID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCopiedFromAlertID>%s</%sCopiedFromAlertID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CopiedFromAlertID), input_name='CopiedFromAlertID')), namespaceprefix_ , eol_))
        if self.CopiedFromSource is not None:
            namespaceprefix_ = self.CopiedFromSource_nsprefix_ + ':' if (UseCapturedNS_ and self.CopiedFromSource_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sCopiedFromSource>%s</%sCopiedFromSource>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.CopiedFromSource), input_name='CopiedFromSource')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='TrainAlert', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.AlertID is not None:
            AlertID_ = self.AlertID
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}AlertID').text = self.gds_format_string(AlertID_)
        if self.AlertServices is not None:
            AlertServices_ = self.AlertServices
            AlertServices_.to_etree(element, name_='AlertServices', mapping_=mapping_)
        if self.SendAlertBySMS is not None:
            SendAlertBySMS_ = self.SendAlertBySMS
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}SendAlertBySMS').text = self.gds_format_boolean(SendAlertBySMS_)
        if self.SendAlertByEmail is not None:
            SendAlertByEmail_ = self.SendAlertByEmail
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}SendAlertByEmail').text = self.gds_format_boolean(SendAlertByEmail_)
        if self.SendAlertByTwitter is not None:
            SendAlertByTwitter_ = self.SendAlertByTwitter
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}SendAlertByTwitter').text = self.gds_format_boolean(SendAlertByTwitter_)
        if self.Source is not None:
            Source_ = self.Source
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}Source').text = self.gds_format_string(Source_)
        if self.AlertText is not None:
            AlertText_ = self.AlertText
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}AlertText').text = self.gds_format_string(AlertText_)
        if self.Audience is not None:
            Audience_ = self.Audience
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}Audience').text = self.gds_format_string(Audience_)
        if self.AlertType is not None:
            AlertType_ = self.AlertType
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}AlertType').text = self.gds_format_string(AlertType_)
        if self.CopiedFromAlertID is not None:
            CopiedFromAlertID_ = self.CopiedFromAlertID
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}CopiedFromAlertID').text = self.gds_format_string(CopiedFromAlertID_)
        if self.CopiedFromSource is not None:
            CopiedFromSource_ = self.CopiedFromSource
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}CopiedFromSource').text = self.gds_format_string(CopiedFromSource_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='TrainAlert'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.AlertID is not None:
            showIndent(outfile, level)
            outfile.write('AlertID=%s,\n' % self.gds_encode(quote_python(self.AlertID)))
        if self.AlertServices is not None:
            showIndent(outfile, level)
            outfile.write('AlertServices=model_.AlertServices(\n')
            self.AlertServices.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.SendAlertBySMS is not None:
            showIndent(outfile, level)
            outfile.write('SendAlertBySMS=%s,\n' % self.SendAlertBySMS)
        if self.SendAlertByEmail is not None:
            showIndent(outfile, level)
            outfile.write('SendAlertByEmail=%s,\n' % self.SendAlertByEmail)
        if self.SendAlertByTwitter is not None:
            showIndent(outfile, level)
            outfile.write('SendAlertByTwitter=%s,\n' % self.SendAlertByTwitter)
        if self.Source is not None:
            showIndent(outfile, level)
            outfile.write('Source=%s,\n' % self.gds_encode(quote_python(self.Source)))
        if self.AlertText is not None:
            showIndent(outfile, level)
            outfile.write('AlertText=%s,\n' % self.gds_encode(quote_python(self.AlertText)))
        if self.Audience is not None:
            showIndent(outfile, level)
            outfile.write('Audience=%s,\n' % self.gds_encode(quote_python(self.Audience)))
        if self.AlertType is not None:
            showIndent(outfile, level)
            outfile.write('AlertType=%s,\n' % self.gds_encode(quote_python(self.AlertType)))
        if self.CopiedFromAlertID is not None:
            showIndent(outfile, level)
            outfile.write('CopiedFromAlertID=%s,\n' % self.gds_encode(quote_python(self.CopiedFromAlertID)))
        if self.CopiedFromSource is not None:
            showIndent(outfile, level)
            outfile.write('CopiedFromSource=%s,\n' % self.gds_encode(quote_python(self.CopiedFromSource)))
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.TrainAlert_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        if self.AlertID is not None:
            dbobj.AlertID = self.AlertID
        if self.AlertServices is not None:
            child_dbobj = self.AlertServices.exportSQLAlchemy(session)
            dbobj.AlertServices = child_dbobj
        if self.SendAlertBySMS is not None:
            dbobj.SendAlertBySMS = self.SendAlertBySMS
        if self.SendAlertByEmail is not None:
            dbobj.SendAlertByEmail = self.SendAlertByEmail
        if self.SendAlertByTwitter is not None:
            dbobj.SendAlertByTwitter = self.SendAlertByTwitter
        if self.Source is not None:
            dbobj.Source = self.Source
        if self.AlertText is not None:
            dbobj.AlertText = self.AlertText
        if self.Audience is not None:
            dbobj.Audience = self.Audience
        if self.AlertType is not None:
            dbobj.AlertType = self.AlertType
        if self.CopiedFromAlertID is not None:
            dbobj.CopiedFromAlertID = self.CopiedFromAlertID
        if self.CopiedFromSource is not None:
            dbobj.CopiedFromSource = self.CopiedFromSource
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'AlertID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'AlertID')
            value_ = self.gds_validate_string(value_, node, 'AlertID')
            self.AlertID = value_
            self.AlertID_nsprefix_ = child_.prefix
        elif nodeName_ == 'AlertServices':
            obj_ = AlertServices.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AlertServices = obj_
            obj_.original_tagname_ = 'AlertServices'
        elif nodeName_ == 'SendAlertBySMS':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'SendAlertBySMS')
            ival_ = self.gds_validate_boolean(ival_, node, 'SendAlertBySMS')
            self.SendAlertBySMS = ival_
            self.SendAlertBySMS_nsprefix_ = child_.prefix
        elif nodeName_ == 'SendAlertByEmail':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'SendAlertByEmail')
            ival_ = self.gds_validate_boolean(ival_, node, 'SendAlertByEmail')
            self.SendAlertByEmail = ival_
            self.SendAlertByEmail_nsprefix_ = child_.prefix
        elif nodeName_ == 'SendAlertByTwitter':
            sval_ = child_.text
            ival_ = self.gds_parse_boolean(sval_, node, 'SendAlertByTwitter')
            ival_ = self.gds_validate_boolean(ival_, node, 'SendAlertByTwitter')
            self.SendAlertByTwitter = ival_
            self.SendAlertByTwitter_nsprefix_ = child_.prefix
        elif nodeName_ == 'Source':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Source')
            value_ = self.gds_validate_string(value_, node, 'Source')
            self.Source = value_
            self.Source_nsprefix_ = child_.prefix
        elif nodeName_ == 'AlertText':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'AlertText')
            value_ = self.gds_validate_string(value_, node, 'AlertText')
            self.AlertText = value_
            self.AlertText_nsprefix_ = child_.prefix
        elif nodeName_ == 'Audience':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Audience')
            value_ = self.gds_validate_string(value_, node, 'Audience')
            self.Audience = value_
            self.Audience_nsprefix_ = child_.prefix
            # validate type AlertAudienceType
            self.validate_AlertAudienceType(self.Audience)
        elif nodeName_ == 'AlertType':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'AlertType')
            value_ = self.gds_validate_string(value_, node, 'AlertType')
            self.AlertType = value_
            self.AlertType_nsprefix_ = child_.prefix
            # validate type AlertType
            self.validate_AlertType(self.AlertType)
        elif nodeName_ == 'CopiedFromAlertID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CopiedFromAlertID')
            value_ = self.gds_validate_string(value_, node, 'CopiedFromAlertID')
            self.CopiedFromAlertID = value_
            self.CopiedFromAlertID_nsprefix_ = child_.prefix
        elif nodeName_ == 'CopiedFromSource':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'CopiedFromSource')
            value_ = self.gds_validate_string(value_, node, 'CopiedFromSource')
            self.CopiedFromSource = value_
            self.CopiedFromSource_nsprefix_ = child_.prefix
# end class TrainAlert


class AlertService(GeneratedsSuper):
    """TODOTODOTODOTODO"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, RID=None, UID=None, SSD=None, Location=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.RID = _cast(None, RID)
        self.RID_nsprefix_ = None
        self.UID = _cast(None, UID)
        self.UID_nsprefix_ = None
        if isinstance(SSD, BaseStrType_):
            initvalue_ = datetime_.datetime.strptime(SSD, '%Y-%m-%d').date()
        else:
            initvalue_ = SSD
        self.SSD = initvalue_
        if Location is None:
            self.Location = []
        else:
            self.Location = Location
        self.Location_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AlertService)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AlertService.subclass:
            return AlertService.subclass(*args_, **kwargs_)
        else:
            return AlertService(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_RIDType(self, value):
        # Validate type ct:RIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on RIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_UIDType(self, value):
        # Validate type ct:UIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 6:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on UIDType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.Location
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='AlertService', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AlertService')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AlertService')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AlertService', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='AlertService'):
        if self.RID is not None and 'RID' not in already_processed:
            already_processed.add('RID')
            outfile.write(' RID=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.RID), input_name='RID')), ))
        if self.UID is not None and 'UID' not in already_processed:
            already_processed.add('UID')
            outfile.write(' UID=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.UID), input_name='UID')), ))
        if self.SSD is not None and 'SSD' not in already_processed:
            already_processed.add('SSD')
            outfile.write(' SSD="%s"' % self.gds_format_date(self.SSD, input_name='SSD'))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='AlertService', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Location_ in self.Location:
            namespaceprefix_ = self.Location_nsprefix_ + ':' if (UseCapturedNS_ and self.Location_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sLocation>%s</%sLocation>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(Location_), input_name='Location')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='AlertService', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.RID is not None:
            element.set('RID', self.gds_format_string(self.RID))
        if self.UID is not None:
            element.set('UID', self.gds_format_string(self.UID))
        if self.SSD is not None:
            element.set('SSD', self.gds_format_date(self.SSD))
        for Location_ in self.Location:
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}Location').text = self.gds_format_string(Location_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='AlertService'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.RID is not None and 'RID' not in already_processed:
            already_processed.add('RID')
            showIndent(outfile, level)
            outfile.write('RID=%s,\n' % (self.RID,))
        if self.UID is not None and 'UID' not in already_processed:
            already_processed.add('UID')
            showIndent(outfile, level)
            outfile.write('UID=%s,\n' % (self.UID,))
        if self.SSD is not None and 'SSD' not in already_processed:
            already_processed.add('SSD')
            showIndent(outfile, level)
            outfile.write('SSD=model_.GeneratedsSuper.gds_parse_date("%s"),\n' % self.gds_format_date(self.SSD, input_name='SSD'))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Location=[\n')
        level += 1
        for Location_ in self.Location:
            showIndent(outfile, level)
            outfile.write('%s,\n' % self.gds_encode(quote_python(Location_)))
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.AlertService_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.RID is not None:
            dbobj.RID = self.RID
        if self.UID is not None:
            dbobj.UID = self.UID
        if self.SSD is not None:
            dbobj.SSD = self.SSD
    def exportSQLAlchemyChildren(self, session, dbobj):
        dbobj.Location = json_.dumps(self.Location, separators=(',', ':'))
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('RID', node)
        if value is not None and 'RID' not in already_processed:
            already_processed.add('RID')
            self.RID = value
            self.validate_RIDType(self.RID)    # validate type RIDType
        value = find_attr_value_('UID', node)
        if value is not None and 'UID' not in already_processed:
            already_processed.add('UID')
            self.UID = value
            self.validate_UIDType(self.UID)    # validate type UIDType
        value = find_attr_value_('SSD', node)
        if value is not None and 'SSD' not in already_processed:
            already_processed.add('SSD')
            try:
                self.SSD = self.gds_parse_date(value)
            except ValueError as exp:
                raise ValueError('Bad date attribute (SSD): %s' % exp)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'Location':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'Location')
            value_ = self.gds_validate_string(value_, node, 'Location')
            self.Location.append(value_)
            self.Location_nsprefix_ = child_.prefix
# end class AlertService


class AlertServices(GeneratedsSuper):
    """A list of services to which the alert applies"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, AlertService=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if AlertService is None:
            self.AlertService = []
        else:
            self.AlertService = AlertService
        self.AlertService_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, AlertServices)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if AlertServices.subclass:
            return AlertServices.subclass(*args_, **kwargs_)
        else:
            return AlertServices(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.AlertService
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='AlertServices', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('AlertServices')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='AlertServices')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='AlertServices', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='AlertServices'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='AlertServices', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for AlertService_ in self.AlertService:
            namespaceprefix_ = self.AlertService_nsprefix_ + ':' if (UseCapturedNS_ and self.AlertService_nsprefix_) else ''
            AlertService_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='AlertService', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='AlertServices', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        for AlertService_ in self.AlertService:
            AlertService_.to_etree(element, name_='AlertService', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='AlertServices'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('AlertService=[\n')
        level += 1
        for AlertService_ in self.AlertService:
            showIndent(outfile, level)
            outfile.write('model_.AlertService(\n')
            AlertService_.exportLiteral(outfile, level)
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.AlertServices_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        for child in self.AlertService:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.AlertService.append(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'AlertService':
            obj_ = AlertService.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.AlertService.append(obj_)
            obj_.original_tagname_ = 'AlertService'
# end class AlertServices


class FullTDBerthID(GeneratedsSuper):
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, area=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.area = _cast(None, area)
        self.area_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, FullTDBerthID)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if FullTDBerthID.subclass:
            return FullTDBerthID.subclass(*args_, **kwargs_)
        else:
            return FullTDBerthID(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TDAreaIDType(self, value):
        # Validate type ct:TDAreaIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on TDAreaIDType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='FullTDBerthID', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('FullTDBerthID')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='FullTDBerthID')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='FullTDBerthID', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='FullTDBerthID'):
        if 'area' not in already_processed:
            already_processed.add('area')
            outfile.write(' area=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.area), input_name='area')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='FullTDBerthID', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='FullTDBerthID', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.area is not None:
            element.set('area', self.gds_format_string(self.area))
        if self.hasContent_():
            element.text = self.gds_format_string(self.get_valueOf_())
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='FullTDBerthID'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.area is not None and 'area' not in already_processed:
            already_processed.add('area')
            showIndent(outfile, level)
            outfile.write('area=%s,\n' % (self.area,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.FullTDBerthID_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.area is not None:
            dbobj.area = self.area
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('area', node)
        if value is not None and 'area' not in already_processed:
            already_processed.add('area')
            self.area = value
            self.validate_TDAreaIDType(self.area)    # validate type TDAreaIDType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class FullTDBerthID


class TrackingID(GeneratedsSuper):
    """Indicate a corrected Tracking ID (headcode) for a service in a TD
    berth."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, berth=None, incorrectTrainID=None, correctTrainID=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.berth = berth
        self.berth_nsprefix_ = None
        self.incorrectTrainID = incorrectTrainID
        self.validate_TrainIdType(self.incorrectTrainID)
        self.incorrectTrainID_nsprefix_ = None
        self.correctTrainID = correctTrainID
        self.validate_TrainIdType(self.correctTrainID)
        self.correctTrainID_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TrackingID)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TrackingID.subclass:
            return TrackingID.subclass(*args_, **kwargs_)
        else:
            return TrackingID(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TrainIdType(self, value):
        result = True
        # Validate type TrainIdType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on TrainIdType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_TrainIdType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_TrainIdType_patterns_, ))
                result = False
        return result
    validate_TrainIdType_patterns_ = [['^([0-9][A-Z][0-9][0-9])$']]
    def hasContent_(self):
        if (
            self.berth is not None or
            self.incorrectTrainID is not None or
            self.correctTrainID is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:ct="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='TrackingID', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TrackingID')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TrackingID')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TrackingID', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='TrackingID'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:ct="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='TrackingID', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.berth is not None:
            namespaceprefix_ = self.berth_nsprefix_ + ':' if (UseCapturedNS_ and self.berth_nsprefix_) else ''
            self.berth.export(outfile, level, namespaceprefix_, namespacedef_='', name_='berth', pretty_print=pretty_print)
        if self.incorrectTrainID is not None:
            namespaceprefix_ = self.incorrectTrainID_nsprefix_ + ':' if (UseCapturedNS_ and self.incorrectTrainID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sincorrectTrainID>%s</%sincorrectTrainID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.incorrectTrainID), input_name='incorrectTrainID')), namespaceprefix_ , eol_))
        if self.correctTrainID is not None:
            namespaceprefix_ = self.correctTrainID_nsprefix_ + ':' if (UseCapturedNS_ and self.correctTrainID_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%scorrectTrainID>%s</%scorrectTrainID>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.correctTrainID), input_name='correctTrainID')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='TrackingID', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.berth is not None:
            berth_ = self.berth
            berth_.to_etree(element, name_='berth', mapping_=mapping_)
        if self.incorrectTrainID is not None:
            incorrectTrainID_ = self.incorrectTrainID
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}incorrectTrainID').text = self.gds_format_string(incorrectTrainID_)
        if self.correctTrainID is not None:
            correctTrainID_ = self.correctTrainID
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}correctTrainID').text = self.gds_format_string(correctTrainID_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='TrackingID'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.berth is not None:
            showIndent(outfile, level)
            outfile.write('berth=model_.FullTDBerthID(\n')
            self.berth.exportLiteral(outfile, level, name_='berth')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.incorrectTrainID is not None:
            showIndent(outfile, level)
            outfile.write('incorrectTrainID=%s,\n' % self.gds_encode(quote_python(self.incorrectTrainID)))
        if self.correctTrainID is not None:
            showIndent(outfile, level)
            outfile.write('correctTrainID=%s,\n' % self.gds_encode(quote_python(self.correctTrainID)))
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.TrackingID_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        if self.berth is not None:
            child_dbobj = self.berth.exportSQLAlchemy(session)
            dbobj.berth = child_dbobj
        if self.incorrectTrainID is not None:
            dbobj.incorrectTrainID = self.incorrectTrainID
        if self.correctTrainID is not None:
            dbobj.correctTrainID = self.correctTrainID
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'berth':
            obj_ = FullTDBerthID.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.berth = obj_
            obj_.original_tagname_ = 'berth'
        elif nodeName_ == 'incorrectTrainID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'incorrectTrainID')
            value_ = self.gds_validate_string(value_, node, 'incorrectTrainID')
            self.incorrectTrainID = value_
            self.incorrectTrainID_nsprefix_ = child_.prefix
            # validate type TrainIdType
            self.validate_TrainIdType(self.incorrectTrainID)
        elif nodeName_ == 'correctTrainID':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'correctTrainID')
            value_ = self.gds_validate_string(value_, node, 'correctTrainID')
            self.correctTrainID = value_
            self.correctTrainID_nsprefix_ = child_.prefix
            # validate type TrainIdType
            self.validate_TrainIdType(self.correctTrainID)
# end class TrackingID


class RTTIAlarmData(GeneratedsSuper):
    """Type describing each type of alarm that can be set.Unique identifier for
    this alarm"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, id=None, tdAreaFail=None, tdFeedFail=None, tyrellFeedFail=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.id = _cast(None, id)
        self.id_nsprefix_ = None
        self.tdAreaFail = tdAreaFail
        self.validate_TDAreaIDType(self.tdAreaFail)
        self.tdAreaFail_nsprefix_ = None
        self.tdFeedFail = tdFeedFail
        self.tdFeedFail_nsprefix_ = None
        self.tyrellFeedFail = tyrellFeedFail
        self.tyrellFeedFail_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RTTIAlarmData)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RTTIAlarmData.subclass:
            return RTTIAlarmData.subclass(*args_, **kwargs_)
        else:
            return RTTIAlarmData(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TDAreaIDType(self, value):
        result = True
        # Validate type TDAreaIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on TDAreaIDType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
        return result
    def validate_AlarmID(self, value):
        # Validate type tns:AlarmID, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def hasContent_(self):
        if (
            self.tdAreaFail is not None or
            self.tdFeedFail is not None or
            self.tyrellFeedFail is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:ct="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1"  xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='RTTIAlarmData', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RTTIAlarmData')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RTTIAlarmData')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RTTIAlarmData', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='RTTIAlarmData'):
        if 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.id), input_name='id')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:ct="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1"  xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='RTTIAlarmData', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.tdAreaFail is not None:
            namespaceprefix_ = self.tdAreaFail_nsprefix_ + ':' if (UseCapturedNS_ and self.tdAreaFail_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stdAreaFail>%s</%stdAreaFail>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tdAreaFail), input_name='tdAreaFail')), namespaceprefix_ , eol_))
        if self.tdFeedFail is not None:
            namespaceprefix_ = self.tdFeedFail_nsprefix_ + ':' if (UseCapturedNS_ and self.tdFeedFail_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%stdFeedFail>%s</%stdFeedFail>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tdFeedFail), input_name='tdFeedFail')), namespaceprefix_ , eol_))
        if self.tyrellFeedFail is not None:
            namespaceprefix_ = self.tyrellFeedFail_nsprefix_ + ':' if (UseCapturedNS_ and self.tyrellFeedFail_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%styrellFeedFail>%s</%styrellFeedFail>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.tyrellFeedFail), input_name='tyrellFeedFail')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='RTTIAlarmData', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.id is not None:
            element.set('id', self.gds_format_string(self.id))
        if self.tdAreaFail is not None:
            tdAreaFail_ = self.tdAreaFail
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}tdAreaFail').text = self.gds_format_string(tdAreaFail_)
        if self.tdFeedFail is not None:
            tdFeedFail_ = self.tdFeedFail
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}tdFeedFail').text = self.gds_format_string(tdFeedFail_)
        if self.tyrellFeedFail is not None:
            tyrellFeedFail_ = self.tyrellFeedFail
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}tyrellFeedFail').text = self.gds_format_string(tyrellFeedFail_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='RTTIAlarmData'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            showIndent(outfile, level)
            outfile.write('id=%s,\n' % (self.id,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.tdAreaFail is not None:
            showIndent(outfile, level)
            outfile.write('tdAreaFail=%s,\n' % self.gds_encode(quote_python(self.tdAreaFail)))
        if self.tdFeedFail is not None:
            showIndent(outfile, level)
            outfile.write('tdFeedFail=%s,\n' % self.gds_encode(quote_python(self.tdFeedFail)))
        if self.tyrellFeedFail is not None:
            showIndent(outfile, level)
            outfile.write('tyrellFeedFail=%s,\n' % self.gds_encode(quote_python(self.tyrellFeedFail)))
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.RTTIAlarmData_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.id is not None:
            dbobj.id_x = self.id
    def exportSQLAlchemyChildren(self, session, dbobj):
        if self.tdAreaFail is not None:
            dbobj.tdAreaFail = self.tdAreaFail
        if self.tdFeedFail is not None:
            dbobj.tdFeedFail = self.tdFeedFail
        if self.tyrellFeedFail is not None:
            dbobj.tyrellFeedFail = self.tyrellFeedFail
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
            self.validate_AlarmID(self.id)    # validate type AlarmID
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'tdAreaFail':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tdAreaFail')
            value_ = self.gds_validate_string(value_, node, 'tdAreaFail')
            self.tdAreaFail = value_
            self.tdAreaFail_nsprefix_ = child_.prefix
            # validate type TDAreaIDType
            self.validate_TDAreaIDType(self.tdAreaFail)
        elif nodeName_ == 'tdFeedFail':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tdFeedFail')
            value_ = self.gds_validate_string(value_, node, 'tdFeedFail')
            self.tdFeedFail = value_
            self.tdFeedFail_nsprefix_ = child_.prefix
        elif nodeName_ == 'tyrellFeedFail':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'tyrellFeedFail')
            value_ = self.gds_validate_string(value_, node, 'tyrellFeedFail')
            self.tyrellFeedFail = value_
            self.tyrellFeedFail_nsprefix_ = child_.prefix
# end class RTTIAlarmData


class tdFeedFail(GeneratedsSuper):
    """Alarm for the failure of the entire TD feed into Darwin."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tdFeedFail)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tdFeedFail.subclass:
            return tdFeedFail.subclass(*args_, **kwargs_)
        else:
            return tdFeedFail(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='tdFeedFail', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tdFeedFail')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tdFeedFail')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tdFeedFail', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tdFeedFail'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='tdFeedFail', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='tdFeedFail', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='tdFeedFail'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.tdFeedFail_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class tdFeedFail


class tyrellFeedFail(GeneratedsSuper):
    """Alarm for the failure of the Tyrell feed into Darwin."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, tyrellFeedFail)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if tyrellFeedFail.subclass:
            return tyrellFeedFail.subclass(*args_, **kwargs_)
        else:
            return tyrellFeedFail(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='tyrellFeedFail', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('tyrellFeedFail')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='tyrellFeedFail')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='tyrellFeedFail', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='tyrellFeedFail'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='tyrellFeedFail', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='tyrellFeedFail', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='tyrellFeedFail'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.tyrellFeedFail_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class tyrellFeedFail


class RTTIAlarm(GeneratedsSuper):
    """An update to a Darwin alarm."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, set=None, clear=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.set = set
        self.set_nsprefix_ = None
        self.clear = clear
        self.validate_AlarmID(self.clear)
        self.clear_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, RTTIAlarm)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if RTTIAlarm.subclass:
            return RTTIAlarm.subclass(*args_, **kwargs_)
        else:
            return RTTIAlarm(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_AlarmID(self, value):
        result = True
        # Validate type AlarmID, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
        return result
    def hasContent_(self):
        if (
            self.set is not None or
            self.clear is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='RTTIAlarm', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('RTTIAlarm')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='RTTIAlarm')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='RTTIAlarm', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='RTTIAlarm'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='RTTIAlarm', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.set is not None:
            namespaceprefix_ = self.set_nsprefix_ + ':' if (UseCapturedNS_ and self.set_nsprefix_) else ''
            self.set.export(outfile, level, namespaceprefix_, namespacedef_='', name_='set', pretty_print=pretty_print)
        if self.clear is not None:
            namespaceprefix_ = self.clear_nsprefix_ + ':' if (UseCapturedNS_ and self.clear_nsprefix_) else ''
            showIndent(outfile, level, pretty_print)
            outfile.write('<%sclear>%s</%sclear>%s' % (namespaceprefix_ , self.gds_encode(self.gds_format_string(quote_xml(self.clear), input_name='clear')), namespaceprefix_ , eol_))
    def to_etree(self, parent_element=None, name_='RTTIAlarm', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.set is not None:
            set_ = self.set
            set_.to_etree(element, name_='set', mapping_=mapping_)
        if self.clear is not None:
            clear_ = self.clear
            etree_.SubElement(element, '{http://www.thalesgroup.com/rtti/PushPort/v16}clear').text = self.gds_format_string(clear_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='RTTIAlarm'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.set is not None:
            showIndent(outfile, level)
            outfile.write('set=model_.RTTIAlarmData(\n')
            self.set.exportLiteral(outfile, level, name_='set')
            showIndent(outfile, level)
            outfile.write('),\n')
        if self.clear is not None:
            showIndent(outfile, level)
            outfile.write('clear=%s,\n' % self.gds_encode(quote_python(self.clear)))
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.RTTIAlarm_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        if self.set is not None:
            child_dbobj = self.set.exportSQLAlchemy(session)
            dbobj.set = child_dbobj
        if self.clear is not None:
            dbobj.clear = self.clear
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'set':
            obj_ = RTTIAlarmData.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.set = obj_
            obj_.original_tagname_ = 'set'
        elif nodeName_ == 'clear':
            value_ = child_.text
            value_ = self.gds_parse_string(value_, node, 'clear')
            value_ = self.gds_validate_string(value_, node, 'clear')
            self.clear = value_
            self.clear_nsprefix_ = child_.prefix
            # validate type AlarmID
            self.validate_AlarmID(self.clear)
# end class RTTIAlarm


class ScheduleFormations(GeneratedsSuper):
    """Type describing all of the Train Formations set for a Schedule.RTTI
    unique Train Identifier"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, rid=None, formation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.rid = _cast(None, rid)
        self.rid_nsprefix_ = None
        if formation is None:
            self.formation = []
        else:
            self.formation = formation
        self.formation_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ScheduleFormations)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ScheduleFormations.subclass:
            return ScheduleFormations.subclass(*args_, **kwargs_)
        else:
            return ScheduleFormations(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_RIDType(self, value):
        # Validate type ct:RIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on RIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.formation
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='ScheduleFormations', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ScheduleFormations')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ScheduleFormations')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ScheduleFormations', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='ScheduleFormations'):
        if 'rid' not in already_processed:
            already_processed.add('rid')
            outfile.write(' rid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.rid), input_name='rid')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='ScheduleFormations', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for formation_ in self.formation:
            namespaceprefix_ = self.formation_nsprefix_ + ':' if (UseCapturedNS_ and self.formation_nsprefix_) else ''
            formation_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='formation', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ScheduleFormations', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.rid is not None:
            element.set('rid', self.gds_format_string(self.rid))
        for formation_ in self.formation:
            formation_.to_etree(element, name_='formation', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ScheduleFormations'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.rid is not None and 'rid' not in already_processed:
            already_processed.add('rid')
            showIndent(outfile, level)
            outfile.write('rid=%s,\n' % (self.rid,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('formation=[\n')
        level += 1
        for formation_ in self.formation:
            showIndent(outfile, level)
            outfile.write('model_.Formation(\n')
            formation_.exportLiteral(outfile, level, name_='Formation')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.ScheduleFormations_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.rid is not None:
            dbobj.rid = self.rid
    def exportSQLAlchemyChildren(self, session, dbobj):
        for child in self.formation:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.formation.append(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('rid', node)
        if value is not None and 'rid' not in already_processed:
            already_processed.add('rid')
            self.rid = value
            self.validate_RIDType(self.rid)    # validate type RIDType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'formation':
            obj_ = Formation.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.formation.append(obj_)
            obj_.original_tagname_ = 'formation'
# end class ScheduleFormations


class Formation(GeneratedsSuper):
    """Type describing a Train Formation for a Schedule.The unique identifier
    of this formation data.The source of the formation data.The RTTI
    instance ID of the src (if any)."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, fid=None, src=None, srcInst=None, coaches=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.fid = _cast(None, fid)
        self.fid_nsprefix_ = None
        self.src = _cast(None, src)
        self.src_nsprefix_ = None
        self.srcInst = _cast(None, srcInst)
        self.srcInst_nsprefix_ = None
        self.coaches = coaches
        self.coaches_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Formation)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Formation.subclass:
            return Formation.subclass(*args_, **kwargs_)
        else:
            return Formation(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_FormationIDType(self, value):
        # Validate type ct3:FormationIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_SourceTypeInst(self, value):
        # Validate type ct:SourceTypeInst, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on SourceTypeInst' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.coaches is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='Formation', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Formation')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Formation')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Formation', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='Formation'):
        if 'fid' not in already_processed:
            already_processed.add('fid')
            outfile.write(' fid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fid), input_name='fid')), ))
        if self.src is not None and 'src' not in already_processed:
            already_processed.add('src')
            outfile.write(' src=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.src), input_name='src')), ))
        if self.srcInst is not None and 'srcInst' not in already_processed:
            already_processed.add('srcInst')
            outfile.write(' srcInst=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.srcInst), input_name='srcInst')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='Formation', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.coaches is not None:
            namespaceprefix_ = self.coaches_nsprefix_ + ':' if (UseCapturedNS_ and self.coaches_nsprefix_) else ''
            self.coaches.export(outfile, level, namespaceprefix_, namespacedef_='', name_='coaches', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Formation', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.fid is not None:
            element.set('fid', self.gds_format_string(self.fid))
        if self.src is not None:
            element.set('src', self.gds_format_string(self.src))
        if self.srcInst is not None:
            element.set('srcInst', self.gds_format_string(self.srcInst))
        if self.coaches is not None:
            coaches_ = self.coaches
            coaches_.to_etree(element, name_='coaches', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='Formation'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            showIndent(outfile, level)
            outfile.write('fid=%s,\n' % (self.fid,))
        if self.src is not None and 'src' not in already_processed:
            already_processed.add('src')
            showIndent(outfile, level)
            outfile.write('src="%s",\n' % (self.src,))
        if self.srcInst is not None and 'srcInst' not in already_processed:
            already_processed.add('srcInst')
            showIndent(outfile, level)
            outfile.write('srcInst=%s,\n' % (self.srcInst,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.coaches is not None:
            showIndent(outfile, level)
            outfile.write('coaches=model_.CoachList(\n')
            self.coaches.exportLiteral(outfile, level, name_='coaches')
            showIndent(outfile, level)
            outfile.write('),\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.Formation_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.fid is not None:
            dbobj.fid = self.fid
        if self.src is not None:
            dbobj.src = self.src
        if self.srcInst is not None:
            dbobj.srcInst = self.srcInst
    def exportSQLAlchemyChildren(self, session, dbobj):
        if self.coaches is not None:
            child_dbobj = self.coaches.exportSQLAlchemy(session)
            dbobj.coaches = child_dbobj
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('fid', node)
        if value is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            self.fid = value
            self.validate_FormationIDType(self.fid)    # validate type FormationIDType
        value = find_attr_value_('src', node)
        if value is not None and 'src' not in already_processed:
            already_processed.add('src')
            self.src = value
        value = find_attr_value_('srcInst', node)
        if value is not None and 'srcInst' not in already_processed:
            already_processed.add('srcInst')
            self.srcInst = value
            self.validate_SourceTypeInst(self.srcInst)    # validate type SourceTypeInst
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'coaches':
            obj_ = CoachList.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.coaches = obj_
            obj_.original_tagname_ = 'coaches'
# end class Formation


class Loading(GeneratedsSuper):
    """Loading data for an individual location in a schedule linked to a
    formation.The unique identifier of the formation data.RTTI unique Train
    IDTIPLOC where the loading data applies."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, fid=None, rid=None, tpl=None, wta=None, wtd=None, wtp=None, pta=None, ptd=None, loading=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.fid = _cast(None, fid)
        self.fid_nsprefix_ = None
        self.rid = _cast(None, rid)
        self.rid_nsprefix_ = None
        self.tpl = _cast(None, tpl)
        self.tpl_nsprefix_ = None
        self.wta = _cast(None, wta)
        self.wta_nsprefix_ = None
        self.wtd = _cast(None, wtd)
        self.wtd_nsprefix_ = None
        self.wtp = _cast(None, wtp)
        self.wtp_nsprefix_ = None
        self.pta = _cast(None, pta)
        self.pta_nsprefix_ = None
        self.ptd = _cast(None, ptd)
        self.ptd_nsprefix_ = None
        if loading is None:
            self.loading = []
        else:
            self.loading = loading
        self.loading_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Loading)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Loading.subclass:
            return Loading.subclass(*args_, **kwargs_)
        else:
            return Loading(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_FormationIDType(self, value):
        # Validate type ct3:FormationIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_RIDType(self, value):
        # Validate type ct:RIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on RIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_TiplocType(self, value):
        # Validate type ct:TiplocType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 7:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TiplocType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_WTimeType(self, value):
        # Validate type tns:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_RTTITimeType(self, value):
        # Validate type tns:RTTITimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_RTTITimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_RTTITimeType_patterns_, ))
    validate_RTTITimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9])$']]
    def hasContent_(self):
        if (
            self.loading
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='Loading', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Loading')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Loading')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Loading', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='Loading'):
        if 'fid' not in already_processed:
            already_processed.add('fid')
            outfile.write(' fid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fid), input_name='fid')), ))
        if 'rid' not in already_processed:
            already_processed.add('rid')
            outfile.write(' rid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.rid), input_name='rid')), ))
        if 'tpl' not in already_processed:
            already_processed.add('tpl')
            outfile.write(' tpl=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.tpl), input_name='tpl')), ))
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            outfile.write(' wta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wta), input_name='wta')), ))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            outfile.write(' wtd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtd), input_name='wtd')), ))
        if self.wtp is not None and 'wtp' not in already_processed:
            already_processed.add('wtp')
            outfile.write(' wtp=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtp), input_name='wtp')), ))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            outfile.write(' pta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.pta), input_name='pta')), ))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            outfile.write(' ptd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ptd), input_name='ptd')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='Loading', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for loading_ in self.loading:
            namespaceprefix_ = self.loading_nsprefix_ + ':' if (UseCapturedNS_ and self.loading_nsprefix_) else ''
            loading_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='loading', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Loading', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.fid is not None:
            element.set('fid', self.gds_format_string(self.fid))
        if self.rid is not None:
            element.set('rid', self.gds_format_string(self.rid))
        if self.tpl is not None:
            element.set('tpl', self.gds_format_string(self.tpl))
        if self.wta is not None:
            element.set('wta', self.gds_format_string(self.wta))
        if self.wtd is not None:
            element.set('wtd', self.gds_format_string(self.wtd))
        if self.wtp is not None:
            element.set('wtp', self.gds_format_string(self.wtp))
        if self.pta is not None:
            element.set('pta', self.gds_format_string(self.pta))
        if self.ptd is not None:
            element.set('ptd', self.gds_format_string(self.ptd))
        for loading_ in self.loading:
            loading_.to_etree(element, name_='loading', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='Loading'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            showIndent(outfile, level)
            outfile.write('fid=%s,\n' % (self.fid,))
        if self.rid is not None and 'rid' not in already_processed:
            already_processed.add('rid')
            showIndent(outfile, level)
            outfile.write('rid=%s,\n' % (self.rid,))
        if self.tpl is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            showIndent(outfile, level)
            outfile.write('tpl=%s,\n' % (self.tpl,))
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            showIndent(outfile, level)
            outfile.write('wta=%s,\n' % (self.wta,))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            showIndent(outfile, level)
            outfile.write('wtd=%s,\n' % (self.wtd,))
        if self.wtp is not None and 'wtp' not in already_processed:
            already_processed.add('wtp')
            showIndent(outfile, level)
            outfile.write('wtp=%s,\n' % (self.wtp,))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            showIndent(outfile, level)
            outfile.write('pta=%s,\n' % (self.pta,))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            showIndent(outfile, level)
            outfile.write('ptd=%s,\n' % (self.ptd,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('loading=[\n')
        level += 1
        for loading_ in self.loading:
            showIndent(outfile, level)
            outfile.write('model_.CoachLoadingData(\n')
            loading_.exportLiteral(outfile, level, name_='CoachLoadingData')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.Loading_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.fid is not None:
            dbobj.fid = self.fid
        if self.rid is not None:
            dbobj.rid = self.rid
        if self.tpl is not None:
            dbobj.tpl = self.tpl
        if self.wta is not None:
            dbobj.wta = self.wta
        if self.wtd is not None:
            dbobj.wtd = self.wtd
        if self.wtp is not None:
            dbobj.wtp = self.wtp
        if self.pta is not None:
            dbobj.pta = self.pta
        if self.ptd is not None:
            dbobj.ptd = self.ptd
    def exportSQLAlchemyChildren(self, session, dbobj):
        for child in self.loading:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.loading.append(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('fid', node)
        if value is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            self.fid = value
            self.validate_FormationIDType(self.fid)    # validate type FormationIDType
        value = find_attr_value_('rid', node)
        if value is not None and 'rid' not in already_processed:
            already_processed.add('rid')
            self.rid = value
            self.validate_RIDType(self.rid)    # validate type RIDType
        value = find_attr_value_('tpl', node)
        if value is not None and 'tpl' not in already_processed:
            already_processed.add('tpl')
            self.tpl = value
            self.validate_TiplocType(self.tpl)    # validate type TiplocType
        value = find_attr_value_('wta', node)
        if value is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            self.wta = value
            self.validate_WTimeType(self.wta)    # validate type WTimeType
        value = find_attr_value_('wtd', node)
        if value is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            self.wtd = value
            self.validate_WTimeType(self.wtd)    # validate type WTimeType
        value = find_attr_value_('wtp', node)
        if value is not None and 'wtp' not in already_processed:
            already_processed.add('wtp')
            self.wtp = value
            self.validate_WTimeType(self.wtp)    # validate type WTimeType
        value = find_attr_value_('pta', node)
        if value is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            self.pta = value
            self.validate_RTTITimeType(self.pta)    # validate type RTTITimeType
        value = find_attr_value_('ptd', node)
        if value is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            self.ptd = value
            self.validate_RTTITimeType(self.ptd)    # validate type RTTITimeType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'loading':
            obj_ = CoachLoadingData.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.loading.append(obj_)
            obj_.original_tagname_ = 'loading'
# end class Loading


class CoachList(GeneratedsSuper):
    """A list of coach data for a formation."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, coach=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if coach is None:
            self.coach = []
        else:
            self.coach = coach
        self.coach_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CoachList)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CoachList.subclass:
            return CoachList.subclass(*args_, **kwargs_)
        else:
            return CoachList(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.coach
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='CoachList', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CoachList')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CoachList')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CoachList', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='CoachList'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='CoachList', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for coach_ in self.coach:
            namespaceprefix_ = self.coach_nsprefix_ + ':' if (UseCapturedNS_ and self.coach_nsprefix_) else ''
            coach_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='coach', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='CoachList', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        for coach_ in self.coach:
            coach_.to_etree(element, name_='coach', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='CoachList'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('coach=[\n')
        level += 1
        for coach_ in self.coach:
            showIndent(outfile, level)
            outfile.write('model_.CoachData(\n')
            coach_.exportLiteral(outfile, level, name_='CoachData')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.CoachList_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        for child in self.coach:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.coach.append(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'coach':
            obj_ = CoachData.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.coach.append(obj_)
            obj_.original_tagname_ = 'coach'
# end class CoachList


class CoachData(GeneratedsSuper):
    """Data for an individual coach in a formation.The number/identifier for
    this coach, e.g. "A".The class of the coach, e.g. "First" or
    "Standard"."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, coachNumber=None, coachClass=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.coachNumber = _cast(None, coachNumber)
        self.coachNumber_nsprefix_ = None
        self.coachClass = _cast(None, coachClass)
        self.coachClass_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CoachData)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CoachData.subclass:
            return CoachData.subclass(*args_, **kwargs_)
        else:
            return CoachData(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_CoachNumberType(self, value):
        # Validate type ct3:CoachNumberType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CoachNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CoachNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_CoachClassType(self, value):
        # Validate type ct3:CoachClassType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='CoachData', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CoachData')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CoachData')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CoachData', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='CoachData'):
        if 'coachNumber' not in already_processed:
            already_processed.add('coachNumber')
            outfile.write(' coachNumber=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.coachNumber), input_name='coachNumber')), ))
        if self.coachClass is not None and 'coachClass' not in already_processed:
            already_processed.add('coachClass')
            outfile.write(' coachClass=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.coachClass), input_name='coachClass')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='CoachData', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='CoachData', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.coachNumber is not None:
            element.set('coachNumber', self.gds_format_string(self.coachNumber))
        if self.coachClass is not None:
            element.set('coachClass', self.gds_format_string(self.coachClass))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='CoachData'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.coachNumber is not None and 'coachNumber' not in already_processed:
            already_processed.add('coachNumber')
            showIndent(outfile, level)
            outfile.write('coachNumber=%s,\n' % (self.coachNumber,))
        if self.coachClass is not None and 'coachClass' not in already_processed:
            already_processed.add('coachClass')
            showIndent(outfile, level)
            outfile.write('coachClass=%s,\n' % (self.coachClass,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.CoachData_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.coachNumber is not None:
            dbobj.coachNumber = self.coachNumber
        if self.coachClass is not None:
            dbobj.coachClass = self.coachClass
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('coachNumber', node)
        if value is not None and 'coachNumber' not in already_processed:
            already_processed.add('coachNumber')
            self.coachNumber = value
            self.validate_CoachNumberType(self.coachNumber)    # validate type CoachNumberType
        value = find_attr_value_('coachClass', node)
        if value is not None and 'coachClass' not in already_processed:
            already_processed.add('coachClass')
            self.coachClass = value
            self.validate_CoachClassType(self.coachClass)    # validate type CoachClassType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class CoachData


class CoachLoadingData(GeneratedsSuper):
    """Type describing the loading data for an identified coach.The
    number/identifier for this coach, e.g. "A".The source of the loading
    data.The RTTI instance ID of the src (if any)."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, coachNumber=None, src=None, srcInst=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.coachNumber = _cast(None, coachNumber)
        self.coachNumber_nsprefix_ = None
        self.src = _cast(None, src)
        self.src_nsprefix_ = None
        self.srcInst = _cast(None, srcInst)
        self.srcInst_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CoachLoadingData)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CoachLoadingData.subclass:
            return CoachLoadingData.subclass(*args_, **kwargs_)
        else:
            return CoachLoadingData(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_CoachNumberType(self, value):
        # Validate type ct3:CoachNumberType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CoachNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CoachNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_SourceTypeInst(self, value):
        # Validate type ct:SourceTypeInst, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on SourceTypeInst' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='CoachLoadingData', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CoachLoadingData')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CoachLoadingData')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CoachLoadingData', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='CoachLoadingData'):
        if 'coachNumber' not in already_processed:
            already_processed.add('coachNumber')
            outfile.write(' coachNumber=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.coachNumber), input_name='coachNumber')), ))
        if self.src is not None and 'src' not in already_processed:
            already_processed.add('src')
            outfile.write(' src=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.src), input_name='src')), ))
        if self.srcInst is not None and 'srcInst' not in already_processed:
            already_processed.add('srcInst')
            outfile.write(' srcInst=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.srcInst), input_name='srcInst')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='CoachLoadingData', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='CoachLoadingData', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.coachNumber is not None:
            element.set('coachNumber', self.gds_format_string(self.coachNumber))
        if self.src is not None:
            element.set('src', self.gds_format_string(self.src))
        if self.srcInst is not None:
            element.set('srcInst', self.gds_format_string(self.srcInst))
        if self.hasContent_():
            element.text = self.gds_format_string(self.get_valueOf_())
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='CoachLoadingData'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.coachNumber is not None and 'coachNumber' not in already_processed:
            already_processed.add('coachNumber')
            showIndent(outfile, level)
            outfile.write('coachNumber=%s,\n' % (self.coachNumber,))
        if self.src is not None and 'src' not in already_processed:
            already_processed.add('src')
            showIndent(outfile, level)
            outfile.write('src="%s",\n' % (self.src,))
        if self.srcInst is not None and 'srcInst' not in already_processed:
            already_processed.add('srcInst')
            showIndent(outfile, level)
            outfile.write('srcInst=%s,\n' % (self.srcInst,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.CoachLoadingData_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.coachNumber is not None:
            dbobj.coachNumber = self.coachNumber
        if self.src is not None:
            dbobj.src = self.src
        if self.srcInst is not None:
            dbobj.srcInst = self.srcInst
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('coachNumber', node)
        if value is not None and 'coachNumber' not in already_processed:
            already_processed.add('coachNumber')
            self.coachNumber = value
            self.validate_CoachNumberType(self.coachNumber)    # validate type CoachNumberType
        value = find_attr_value_('src', node)
        if value is not None and 'src' not in already_processed:
            already_processed.add('src')
            self.src = value
        value = find_attr_value_('srcInst', node)
        if value is not None and 'srcInst' not in already_processed:
            already_processed.add('srcInst')
            self.srcInst = value
            self.validate_SourceTypeInst(self.srcInst)    # validate type SourceTypeInst
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class CoachLoadingData


class ScheduleFormations9(GeneratedsSuper):
    """Type describing all of the Train Formations set for a Schedule.RTTI
    unique Train Identifier"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, rid=None, formation=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.rid = _cast(None, rid)
        self.rid_nsprefix_ = None
        if formation is None:
            self.formation = []
        else:
            self.formation = formation
        self.formation_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ScheduleFormations9)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ScheduleFormations9.subclass:
            return ScheduleFormations9.subclass(*args_, **kwargs_)
        else:
            return ScheduleFormations9(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_RIDType(self, value):
        # Validate type ct:RIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on RIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.formation
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='ScheduleFormations9', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ScheduleFormations9')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ScheduleFormations9')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ScheduleFormations9', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='ScheduleFormations9'):
        if 'rid' not in already_processed:
            already_processed.add('rid')
            outfile.write(' rid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.rid), input_name='rid')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='ScheduleFormations9', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for formation_ in self.formation:
            namespaceprefix_ = self.formation_nsprefix_ + ':' if (UseCapturedNS_ and self.formation_nsprefix_) else ''
            formation_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='formation', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='ScheduleFormations9', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.rid is not None:
            element.set('rid', self.gds_format_string(self.rid))
        for formation_ in self.formation:
            formation_.to_etree(element, name_='formation', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ScheduleFormations9'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.rid is not None and 'rid' not in already_processed:
            already_processed.add('rid')
            showIndent(outfile, level)
            outfile.write('rid=%s,\n' % (self.rid,))
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('formation=[\n')
        level += 1
        for formation_ in self.formation:
            showIndent(outfile, level)
            outfile.write('model_.Formation10(\n')
            formation_.exportLiteral(outfile, level, name_='Formation10')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.ScheduleFormations9_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.rid is not None:
            dbobj.rid = self.rid
    def exportSQLAlchemyChildren(self, session, dbobj):
        for child in self.formation:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.formation.append(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('rid', node)
        if value is not None and 'rid' not in already_processed:
            already_processed.add('rid')
            self.rid = value
            self.validate_RIDType(self.rid)    # validate type RIDType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'formation':
            obj_ = Formation10.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.formation.append(obj_)
            obj_.original_tagname_ = 'formation'
# end class ScheduleFormations9


class Formation10(GeneratedsSuper):
    """Type describing a Train Formation for a Schedule.The unique identifier
    of this formation data.The source of the formation data.The RTTI
    instance ID of the src (if any)."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, fid=None, src=None, srcInst=None, coaches=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.fid = _cast(None, fid)
        self.fid_nsprefix_ = None
        self.src = _cast(None, src)
        self.src_nsprefix_ = None
        self.srcInst = _cast(None, srcInst)
        self.srcInst_nsprefix_ = None
        self.coaches = coaches
        self.coaches_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, Formation10)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if Formation10.subclass:
            return Formation10.subclass(*args_, **kwargs_)
        else:
            return Formation10(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_FormationIDType(self, value):
        # Validate type ct3:FormationIDType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 20:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on FormationIDType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_SourceTypeInst(self, value):
        # Validate type ct:SourceTypeInst, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on SourceTypeInst' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            self.coaches is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='Formation10', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('Formation10')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='Formation10')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='Formation10', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='Formation10'):
        if 'fid' not in already_processed:
            already_processed.add('fid')
            outfile.write(' fid=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.fid), input_name='fid')), ))
        if self.src is not None and 'src' not in already_processed:
            already_processed.add('src')
            outfile.write(' src=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.src), input_name='src')), ))
        if self.srcInst is not None and 'srcInst' not in already_processed:
            already_processed.add('srcInst')
            outfile.write(' srcInst=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.srcInst), input_name='srcInst')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='Formation10', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.coaches is not None:
            namespaceprefix_ = self.coaches_nsprefix_ + ':' if (UseCapturedNS_ and self.coaches_nsprefix_) else ''
            self.coaches.export(outfile, level, namespaceprefix_, namespacedef_='', name_='coaches', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='Formation10', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.fid is not None:
            element.set('fid', self.gds_format_string(self.fid))
        if self.src is not None:
            element.set('src', self.gds_format_string(self.src))
        if self.srcInst is not None:
            element.set('srcInst', self.gds_format_string(self.srcInst))
        if self.coaches is not None:
            coaches_ = self.coaches
            coaches_.to_etree(element, name_='coaches', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='Formation10'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.fid is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            showIndent(outfile, level)
            outfile.write('fid=%s,\n' % (self.fid,))
        if self.src is not None and 'src' not in already_processed:
            already_processed.add('src')
            showIndent(outfile, level)
            outfile.write('src="%s",\n' % (self.src,))
        if self.srcInst is not None and 'srcInst' not in already_processed:
            already_processed.add('srcInst')
            showIndent(outfile, level)
            outfile.write('srcInst=%s,\n' % (self.srcInst,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.coaches is not None:
            showIndent(outfile, level)
            outfile.write('coaches=model_.CoachList11(\n')
            self.coaches.exportLiteral(outfile, level, name_='coaches')
            showIndent(outfile, level)
            outfile.write('),\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.Formation10_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.fid is not None:
            dbobj.fid = self.fid
        if self.src is not None:
            dbobj.src = self.src
        if self.srcInst is not None:
            dbobj.srcInst = self.srcInst
    def exportSQLAlchemyChildren(self, session, dbobj):
        if self.coaches is not None:
            child_dbobj = self.coaches.exportSQLAlchemy(session)
            dbobj.coaches = child_dbobj
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('fid', node)
        if value is not None and 'fid' not in already_processed:
            already_processed.add('fid')
            self.fid = value
            self.validate_FormationIDType(self.fid)    # validate type FormationIDType
        value = find_attr_value_('src', node)
        if value is not None and 'src' not in already_processed:
            already_processed.add('src')
            self.src = value
        value = find_attr_value_('srcInst', node)
        if value is not None and 'srcInst' not in already_processed:
            already_processed.add('srcInst')
            self.srcInst = value
            self.validate_SourceTypeInst(self.srcInst)    # validate type SourceTypeInst
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'coaches':
            obj_ = CoachList11.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.coaches = obj_
            obj_.original_tagname_ = 'coaches'
# end class Formation10


class CoachList11(GeneratedsSuper):
    """A list of coach data for a formation."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, coach=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if coach is None:
            self.coach = []
        else:
            self.coach = coach
        self.coach_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CoachList11)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CoachList11.subclass:
            return CoachList11.subclass(*args_, **kwargs_)
        else:
            return CoachList11(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.coach
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='CoachList11', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CoachList11')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CoachList11')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CoachList11', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='CoachList11'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:None="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v1" ', name_='CoachList11', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for coach_ in self.coach:
            namespaceprefix_ = self.coach_nsprefix_ + ':' if (UseCapturedNS_ and self.coach_nsprefix_) else ''
            coach_.export(outfile, level, namespaceprefix_, namespacedef_='', name_='coach', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='CoachList11', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        for coach_ in self.coach:
            coach_.to_etree(element, name_='coach', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='CoachList11'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('coach=[\n')
        level += 1
        for coach_ in self.coach:
            showIndent(outfile, level)
            outfile.write('model_.CoachData12(\n')
            coach_.exportLiteral(outfile, level, name_='CoachData12')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.CoachList11_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        for child in self.coach:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.coach.append(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'coach':
            obj_ = CoachData12.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.coach.append(obj_)
            obj_.original_tagname_ = 'coach'
# end class CoachList11


class CoachData12(GeneratedsSuper):
    """Data for an individual coach in a formation.The number/identifier for
    this coach, e.g. "A".The class of the coach, e.g. "First" or
    "Standard"."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, coachNumber=None, coachClass=None, toilet=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.coachNumber = _cast(None, coachNumber)
        self.coachNumber_nsprefix_ = None
        self.coachClass = _cast(None, coachClass)
        self.coachClass_nsprefix_ = None
        self.toilet = toilet
        self.toilet_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, CoachData12)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if CoachData12.subclass:
            return CoachData12.subclass(*args_, **kwargs_)
        else:
            return CoachData12(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_CoachNumberType(self, value):
        # Validate type ct3:CoachNumberType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 2:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on CoachNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on CoachNumberType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_CoachClassType(self, value):
        # Validate type ct3:CoachClassType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            pass
    def hasContent_(self):
        if (
            self.toilet is not None
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:ct4="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v4" ', name_='CoachData12', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('CoachData12')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='CoachData12')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='CoachData12', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='CoachData12'):
        if 'coachNumber' not in already_processed:
            already_processed.add('coachNumber')
            outfile.write(' coachNumber=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.coachNumber), input_name='coachNumber')), ))
        if self.coachClass is not None and 'coachClass' not in already_processed:
            already_processed.add('coachClass')
            outfile.write(' coachClass=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.coachClass), input_name='coachClass')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16" xmlns:ct4="http://www.thalesgroup.com/rtti/PushPort/CommonTypes/v4" ', name_='CoachData12', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.toilet is not None:
            namespaceprefix_ = self.toilet_nsprefix_ + ':' if (UseCapturedNS_ and self.toilet_nsprefix_) else ''
            self.toilet.export(outfile, level, namespaceprefix_, namespacedef_='', name_='toilet', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='CoachData12', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.coachNumber is not None:
            element.set('coachNumber', self.gds_format_string(self.coachNumber))
        if self.coachClass is not None:
            element.set('coachClass', self.gds_format_string(self.coachClass))
        if self.toilet is not None:
            toilet_ = self.toilet
            toilet_.to_etree(element, name_='toilet', mapping_=mapping_)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='CoachData12'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.coachNumber is not None and 'coachNumber' not in already_processed:
            already_processed.add('coachNumber')
            showIndent(outfile, level)
            outfile.write('coachNumber=%s,\n' % (self.coachNumber,))
        if self.coachClass is not None and 'coachClass' not in already_processed:
            already_processed.add('coachClass')
            showIndent(outfile, level)
            outfile.write('coachClass=%s,\n' % (self.coachClass,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.toilet is not None:
            showIndent(outfile, level)
            outfile.write('toilet=model_.ToiletAvailabilityType(\n')
            self.toilet.exportLiteral(outfile, level, name_='toilet')
            showIndent(outfile, level)
            outfile.write('),\n')
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.CoachData12_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.coachNumber is not None:
            dbobj.coachNumber = self.coachNumber
        if self.coachClass is not None:
            dbobj.coachClass = self.coachClass
    def exportSQLAlchemyChildren(self, session, dbobj):
        if self.toilet is not None:
            child_dbobj = self.toilet.exportSQLAlchemy(session)
            dbobj.toilet = child_dbobj
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('coachNumber', node)
        if value is not None and 'coachNumber' not in already_processed:
            already_processed.add('coachNumber')
            self.coachNumber = value
            self.validate_CoachNumberType(self.coachNumber)    # validate type CoachNumberType
        value = find_attr_value_('coachClass', node)
        if value is not None and 'coachClass' not in already_processed:
            already_processed.add('coachClass')
            self.coachClass = value
            self.validate_CoachClassType(self.coachClass)    # validate type CoachClassType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'toilet':
            obj_ = ToiletAvailabilityType.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            self.toilet = obj_
            obj_.original_tagname_ = 'toilet'
# end class CoachData12


class ToiletAvailabilityType(GeneratedsSuper):
    """The availability of a toilet in coach formation data. If no availability
    is supplied, it should be assumed to have the value "Unknown".The
    service status of this toilet. E.g. "Unknown", "InService" or
    "NotInService"."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, status='InService', valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.status = _cast(None, status)
        self.status_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ToiletAvailabilityType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ToiletAvailabilityType.subclass:
            return ToiletAvailabilityType.subclass(*args_, **kwargs_)
        else:
            return ToiletAvailabilityType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_ToiletStatus(self, value):
        # Validate type tns:ToiletStatus, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            value = value
            enumerations = ['Unknown', 'InService', 'NotInService']
            if value not in enumerations:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd enumeration restriction on ToiletStatus' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='ToiletAvailabilityType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ToiletAvailabilityType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ToiletAvailabilityType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ToiletAvailabilityType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='tns:', name_='ToiletAvailabilityType'):
        if self.status != "InService" and 'status' not in already_processed:
            already_processed.add('status')
            outfile.write(' status=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.status), input_name='status')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='tns:', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='ToiletAvailabilityType', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='ToiletAvailabilityType', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.status is not None:
            element.set('status', self.gds_format_string(self.status))
        if self.hasContent_():
            element.text = self.gds_format_string(self.get_valueOf_())
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ToiletAvailabilityType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.status is not None and 'status' not in already_processed:
            already_processed.add('status')
            showIndent(outfile, level)
            outfile.write('status=%s,\n' % (self.status,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.ToiletAvailabilityType_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.status is not None:
            dbobj.status = self.status
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('status', node)
        if value is not None and 'status' not in already_processed:
            already_processed.add('status')
            self.status = value
            self.validate_ToiletStatus(self.status)    # validate type ToiletStatus
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ToiletAvailabilityType


class TimeTableIdType(GeneratedsSuper):
    """Response for the current timetable ID"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, ttfile=None, ttreffile=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.ttfile = _cast(None, ttfile)
        self.ttfile_nsprefix_ = None
        self.ttreffile = _cast(None, ttreffile)
        self.ttreffile_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, TimeTableIdType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if TimeTableIdType.subclass:
            return TimeTableIdType.subclass(*args_, **kwargs_)
        else:
            return TimeTableIdType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_TimetableFilenameType(self, value):
        # Validate type ct:TimetableFilenameType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 128:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on TimetableFilenameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on TimetableFilenameType' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='TimeTableIdType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('TimeTableIdType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='TimeTableIdType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='TimeTableIdType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='TimeTableIdType'):
        if self.ttfile is not None and 'ttfile' not in already_processed:
            already_processed.add('ttfile')
            outfile.write(' ttfile=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ttfile), input_name='ttfile')), ))
        if self.ttreffile is not None and 'ttreffile' not in already_processed:
            already_processed.add('ttreffile')
            outfile.write(' ttreffile=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ttreffile), input_name='ttreffile')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='TimeTableIdType', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='TimeTableIdType', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.ttfile is not None:
            element.set('ttfile', self.gds_format_string(self.ttfile))
        if self.ttreffile is not None:
            element.set('ttreffile', self.gds_format_string(self.ttreffile))
        if self.hasContent_():
            element.text = self.gds_format_string(self.get_valueOf_())
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='TimeTableIdType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.ttfile is not None and 'ttfile' not in already_processed:
            already_processed.add('ttfile')
            showIndent(outfile, level)
            outfile.write('ttfile=%s,\n' % (self.ttfile,))
        if self.ttreffile is not None and 'ttreffile' not in already_processed:
            already_processed.add('ttreffile')
            showIndent(outfile, level)
            outfile.write('ttreffile=%s,\n' % (self.ttreffile,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.TimeTableIdType_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.ttfile is not None:
            dbobj.ttfile = self.ttfile
        if self.ttreffile is not None:
            dbobj.ttreffile = self.ttreffile
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('ttfile', node)
        if value is not None and 'ttfile' not in already_processed:
            already_processed.add('ttfile')
            self.ttfile = value
            self.validate_TimetableFilenameType(self.ttfile)    # validate type TimetableFilenameType
        value = find_attr_value_('ttreffile', node)
        if value is not None and 'ttreffile' not in already_processed:
            already_processed.add('ttreffile')
            self.ttreffile = value
            self.validate_TimetableFilenameType(self.ttreffile)    # validate type TimetableFilenameType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class TimeTableIdType


class GetSnapshotReqType(GeneratedsSuper):
    """Request a standard snapshot of current databaseIf true, then resulting
    snapshot data is fetched by the client via FTP"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, viaftp=False, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.viaftp = _cast(bool, viaftp)
        self.viaftp_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GetSnapshotReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GetSnapshotReqType.subclass:
            return GetSnapshotReqType.subclass(*args_, **kwargs_)
        else:
            return GetSnapshotReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='GetSnapshotReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GetSnapshotReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GetSnapshotReqType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GetSnapshotReqType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GetSnapshotReqType'):
        if self.viaftp and 'viaftp' not in already_processed:
            already_processed.add('viaftp')
            outfile.write(' viaftp="%s"' % self.gds_format_boolean(self.viaftp, input_name='viaftp'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='GetSnapshotReqType', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='GetSnapshotReqType', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.viaftp is not None:
            element.set('viaftp', self.gds_format_boolean(self.viaftp))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='GetSnapshotReqType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.viaftp is not None and 'viaftp' not in already_processed:
            already_processed.add('viaftp')
            showIndent(outfile, level)
            outfile.write('viaftp=%s,\n' % (self.viaftp,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.GetSnapshotReqType_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.viaftp is not None:
            dbobj.viaftp = self.viaftp
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('viaftp', node)
        if value is not None and 'viaftp' not in already_processed:
            already_processed.add('viaftp')
            if value in ('true', '1'):
                self.viaftp = True
            elif value in ('false', '0'):
                self.viaftp = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class GetSnapshotReqType


class GetFullSnapshotReqType(GeneratedsSuper):
    """Request a full snapshot of current databaseIf true, then resulting
    snapshot data is fetched by the client via FTP"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, viaftp=False, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.viaftp = _cast(bool, viaftp)
        self.viaftp_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, GetFullSnapshotReqType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if GetFullSnapshotReqType.subclass:
            return GetFullSnapshotReqType.subclass(*args_, **kwargs_)
        else:
            return GetFullSnapshotReqType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='GetFullSnapshotReqType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('GetFullSnapshotReqType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='GetFullSnapshotReqType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='GetFullSnapshotReqType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='GetFullSnapshotReqType'):
        if self.viaftp and 'viaftp' not in already_processed:
            already_processed.add('viaftp')
            outfile.write(' viaftp="%s"' % self.gds_format_boolean(self.viaftp, input_name='viaftp'))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='GetFullSnapshotReqType', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='GetFullSnapshotReqType', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.viaftp is not None:
            element.set('viaftp', self.gds_format_boolean(self.viaftp))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='GetFullSnapshotReqType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.viaftp is not None and 'viaftp' not in already_processed:
            already_processed.add('viaftp')
            showIndent(outfile, level)
            outfile.write('viaftp=%s,\n' % (self.viaftp,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.GetFullSnapshotReqType_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.viaftp is not None:
            dbobj.viaftp = self.viaftp
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('viaftp', node)
        if value is not None and 'viaftp' not in already_processed:
            already_processed.add('viaftp')
            if value in ('true', '1'):
                self.viaftp = True
            elif value in ('false', '0'):
                self.viaftp = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class GetFullSnapshotReqType


class FailureRespType(StatusType):
    """Failure ResponseThe DCIS source that generated this updateThe
    DCISRequestID value provided by the originator of this update. Used in
    conjunction with the updateSource attribute to ensure uniqueness"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = StatusType
    def __init__(self, code=None, requestSource=None, requestID=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(FailureRespType, self).__init__(code, valueOf_,  **kwargs_)
        self.requestSource = _cast(None, requestSource)
        self.requestSource_nsprefix_ = None
        self.requestID = _cast(None, requestID)
        self.requestID_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, FailureRespType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if FailureRespType.subclass:
            return FailureRespType.subclass(*args_, **kwargs_)
        else:
            return FailureRespType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_SourceTypeInst(self, value):
        # Validate type ct:SourceTypeInst, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on SourceTypeInst' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_DCISRequestID(self, value):
        # Validate type ct:DCISRequestID, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on DCISRequestID' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on DCISRequestID' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_DCISRequestID_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_DCISRequestID_patterns_, ))
    validate_DCISRequestID_patterns_ = [['^([-_A-Za-z0-9]{1,16})$']]
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_) or
            super(FailureRespType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='FailureRespType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('FailureRespType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='FailureRespType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='FailureRespType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='FailureRespType'):
        super(FailureRespType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='FailureRespType')
        if self.requestSource is not None and 'requestSource' not in already_processed:
            already_processed.add('requestSource')
            outfile.write(' requestSource=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.requestSource), input_name='requestSource')), ))
        if self.requestID is not None and 'requestID' not in already_processed:
            already_processed.add('requestID')
            outfile.write(' requestID=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.requestID), input_name='requestID')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='FailureRespType', fromsubclass_=False, pretty_print=True):
        super(FailureRespType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
        pass
    def to_etree(self, parent_element=None, name_='FailureRespType', mapping_=None):
        element = super(FailureRespType, self).to_etree(parent_element, name_, mapping_)
        if self.requestSource is not None:
            element.set('requestSource', self.gds_format_string(self.requestSource))
        if self.requestID is not None:
            element.set('requestID', self.gds_format_string(self.requestID))
        if self.hasContent_():
            element.text = self.gds_format_string(self.get_valueOf_())
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='FailureRespType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.requestSource is not None and 'requestSource' not in already_processed:
            already_processed.add('requestSource')
            showIndent(outfile, level)
            outfile.write('requestSource=%s,\n' % (self.requestSource,))
        if self.requestID is not None and 'requestID' not in already_processed:
            already_processed.add('requestID')
            showIndent(outfile, level)
            outfile.write('requestID=%s,\n' % (self.requestID,))
        super(FailureRespType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(FailureRespType, self).exportLiteralChildren(outfile, level, name_)
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.FailureRespType_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.requestSource is not None:
            dbobj.requestSource = self.requestSource
        if self.requestID is not None:
            dbobj.requestID = self.requestID
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('requestSource', node)
        if value is not None and 'requestSource' not in already_processed:
            already_processed.add('requestSource')
            self.requestSource = value
            self.validate_SourceTypeInst(self.requestSource)    # validate type SourceTypeInst
        value = find_attr_value_('requestID', node)
        if value is not None and 'requestID' not in already_processed:
            already_processed.add('requestID')
            self.requestID = value
            self.validate_DCISRequestID(self.requestID)    # validate type DCISRequestID
        super(FailureRespType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class FailureRespType


class uRType(DataResponse):
    """Update ResponseA string describing the type of system that originated
    this update, e.g. "CIS" or "Darwin".The source instance that generated
    this update, usually a CIS instance.The DCISRequestID value provided by
    the originator of this update. Used in conjunction with the
    requestSource attribute to ensure uniqueness"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = DataResponse
    def __init__(self, schedule=None, deactivated=None, association=None, scheduleFormations=None, TS=None, formationLoading=None, OW=None, trainAlert=None, trainOrder=None, trackingID=None, alarm=None, updateOrigin=None, requestSource=None, requestID=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        super(uRType, self).__init__(schedule, deactivated, association, scheduleFormations, TS, formationLoading, OW, trainAlert, trainOrder, trackingID, alarm,  **kwargs_)
        self.updateOrigin = _cast(None, updateOrigin)
        self.updateOrigin_nsprefix_ = None
        self.requestSource = _cast(None, requestSource)
        self.requestSource_nsprefix_ = None
        self.requestID = _cast(None, requestID)
        self.requestID_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, uRType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if uRType.subclass:
            return uRType.subclass(*args_, **kwargs_)
        else:
            return uRType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_SourceTypeInst(self, value):
        # Validate type ct:SourceTypeInst, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 4:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on SourceTypeInst' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
    def validate_DCISRequestID(self, value):
        # Validate type ct:DCISRequestID, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) > 16:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd maxLength restriction on DCISRequestID' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if len(value) < 1:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd minLength restriction on DCISRequestID' % {"value" : encode_str_2_3(value), "lineno": lineno} )
                result = False
            if not self.gds_validate_simple_patterns(
                    self.validate_DCISRequestID_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_DCISRequestID_patterns_, ))
    validate_DCISRequestID_patterns_ = [['^([-_A-Za-z0-9]{1,16})$']]
    def hasContent_(self):
        if (
            super(uRType, self).hasContent_()
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='uRType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('uRType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='uRType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='uRType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='uRType'):
        super(uRType, self).exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='uRType')
        if self.updateOrigin is not None and 'updateOrigin' not in already_processed:
            already_processed.add('updateOrigin')
            outfile.write(' updateOrigin=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.updateOrigin), input_name='updateOrigin')), ))
        if self.requestSource is not None and 'requestSource' not in already_processed:
            already_processed.add('requestSource')
            outfile.write(' requestSource=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.requestSource), input_name='requestSource')), ))
        if self.requestID is not None and 'requestID' not in already_processed:
            already_processed.add('requestID')
            outfile.write(' requestID=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.requestID), input_name='requestID')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='uRType', fromsubclass_=False, pretty_print=True):
        super(uRType, self).exportChildren(outfile, level, namespaceprefix_, namespacedef_, name_, True, pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='uRType', mapping_=None):
        element = super(uRType, self).to_etree(parent_element, name_, mapping_)
        if self.updateOrigin is not None:
            element.set('updateOrigin', self.gds_format_string(self.updateOrigin))
        if self.requestSource is not None:
            element.set('requestSource', self.gds_format_string(self.requestSource))
        if self.requestID is not None:
            element.set('requestID', self.gds_format_string(self.requestID))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='uRType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.updateOrigin is not None and 'updateOrigin' not in already_processed:
            already_processed.add('updateOrigin')
            showIndent(outfile, level)
            outfile.write('updateOrigin="%s",\n' % (self.updateOrigin,))
        if self.requestSource is not None and 'requestSource' not in already_processed:
            already_processed.add('requestSource')
            showIndent(outfile, level)
            outfile.write('requestSource=%s,\n' % (self.requestSource,))
        if self.requestID is not None and 'requestID' not in already_processed:
            already_processed.add('requestID')
            showIndent(outfile, level)
            outfile.write('requestID=%s,\n' % (self.requestID,))
        super(uRType, self).exportLiteralAttributes(outfile, level, already_processed, name_)
    def exportLiteralChildren(self, outfile, level, name_):
        super(uRType, self).exportLiteralChildren(outfile, level, name_)
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.uRType_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.updateOrigin is not None:
            dbobj.updateOrigin = self.updateOrigin
        if self.requestSource is not None:
            dbobj.requestSource = self.requestSource
        if self.requestID is not None:
            dbobj.requestID = self.requestID
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('updateOrigin', node)
        if value is not None and 'updateOrigin' not in already_processed:
            already_processed.add('updateOrigin')
            self.updateOrigin = value
        value = find_attr_value_('requestSource', node)
        if value is not None and 'requestSource' not in already_processed:
            already_processed.add('requestSource')
            self.requestSource = value
            self.validate_SourceTypeInst(self.requestSource)    # validate type SourceTypeInst
        value = find_attr_value_('requestID', node)
        if value is not None and 'requestID' not in already_processed:
            already_processed.add('requestID')
            self.requestID = value
            self.validate_DCISRequestID(self.requestID)    # validate type DCISRequestID
        super(uRType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        super(uRType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class uRType


class ridType(GeneratedsSuper):
    """For trains in the train order where the train is the Darwin timetable,
    it will be identified by its RIDOne or more scheduled times to identify
    the instance of the location in the train schedule for which the train
    order is set."""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, wta=None, wtd=None, wtp=None, pta=None, ptd=None, valueOf_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.wta = _cast(None, wta)
        self.wta_nsprefix_ = None
        self.wtd = _cast(None, wtd)
        self.wtd_nsprefix_ = None
        self.wtp = _cast(None, wtp)
        self.wtp_nsprefix_ = None
        self.pta = _cast(None, pta)
        self.pta_nsprefix_ = None
        self.ptd = _cast(None, ptd)
        self.ptd_nsprefix_ = None
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, ridType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if ridType.subclass:
            return ridType.subclass(*args_, **kwargs_)
        else:
            return ridType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_WTimeType(self, value):
        # Validate type tns:WTimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_WTimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_WTimeType_patterns_, ))
    validate_WTimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9](:[0-5][0-9])?)$']]
    def validate_RTTITimeType(self, value):
        # Validate type tns:RTTITimeType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if not self.gds_validate_simple_patterns(
                    self.validate_RTTITimeType_patterns_, value):
                self.gds_collector_.add_message('Value "%s" does not match xsd pattern restrictions: %s' % (encode_str_2_3(value), self.validate_RTTITimeType_patterns_, ))
    validate_RTTITimeType_patterns_ = [['^(([0-1][0-9]|2[0-3]):[0-5][0-9])$']]
    def hasContent_(self):
        if (
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='ridType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('ridType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='ridType')
        if self.hasContent_():
            outfile.write('>')
            outfile.write(self.convert_unicode(self.valueOf_))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='ridType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='ridType'):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            outfile.write(' wta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wta), input_name='wta')), ))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            outfile.write(' wtd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtd), input_name='wtd')), ))
        if self.wtp is not None and 'wtp' not in already_processed:
            already_processed.add('wtp')
            outfile.write(' wtp=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.wtp), input_name='wtp')), ))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            outfile.write(' pta=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.pta), input_name='pta')), ))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            outfile.write(' ptd=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.ptd), input_name='ptd')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='ridType', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='ridType', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.wta is not None:
            element.set('wta', self.gds_format_string(self.wta))
        if self.wtd is not None:
            element.set('wtd', self.gds_format_string(self.wtd))
        if self.wtp is not None:
            element.set('wtp', self.gds_format_string(self.wtp))
        if self.pta is not None:
            element.set('pta', self.gds_format_string(self.pta))
        if self.ptd is not None:
            element.set('ptd', self.gds_format_string(self.ptd))
        if self.hasContent_():
            element.text = self.gds_format_string(self.get_valueOf_())
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='ridType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.wta is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            showIndent(outfile, level)
            outfile.write('wta=%s,\n' % (self.wta,))
        if self.wtd is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            showIndent(outfile, level)
            outfile.write('wtd=%s,\n' % (self.wtd,))
        if self.wtp is not None and 'wtp' not in already_processed:
            already_processed.add('wtp')
            showIndent(outfile, level)
            outfile.write('wtp=%s,\n' % (self.wtp,))
        if self.pta is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            showIndent(outfile, level)
            outfile.write('pta=%s,\n' % (self.pta,))
        if self.ptd is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            showIndent(outfile, level)
            outfile.write('ptd=%s,\n' % (self.ptd,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.ridType_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.wta is not None:
            dbobj.wta = self.wta
        if self.wtd is not None:
            dbobj.wtd = self.wtd
        if self.wtp is not None:
            dbobj.wtp = self.wtp
        if self.pta is not None:
            dbobj.pta = self.pta
        if self.ptd is not None:
            dbobj.ptd = self.ptd
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('wta', node)
        if value is not None and 'wta' not in already_processed:
            already_processed.add('wta')
            self.wta = value
            self.validate_WTimeType(self.wta)    # validate type WTimeType
        value = find_attr_value_('wtd', node)
        if value is not None and 'wtd' not in already_processed:
            already_processed.add('wtd')
            self.wtd = value
            self.validate_WTimeType(self.wtd)    # validate type WTimeType
        value = find_attr_value_('wtp', node)
        if value is not None and 'wtp' not in already_processed:
            already_processed.add('wtp')
            self.wtp = value
            self.validate_WTimeType(self.wtp)    # validate type WTimeType
        value = find_attr_value_('pta', node)
        if value is not None and 'pta' not in already_processed:
            already_processed.add('pta')
            self.pta = value
            self.validate_RTTITimeType(self.pta)    # validate type RTTITimeType
        value = find_attr_value_('ptd', node)
        if value is not None and 'ptd' not in already_processed:
            already_processed.add('ptd')
            self.ptd = value
            self.validate_RTTITimeType(self.ptd)    # validate type RTTITimeType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class ridType


class StationType(GeneratedsSuper):
    """The Stations the message is being applied to"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, crs=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        self.crs = _cast(None, crs)
        self.crs_nsprefix_ = None
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, StationType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if StationType.subclass:
            return StationType.subclass(*args_, **kwargs_)
        else:
            return StationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def validate_CrsType(self, value):
        # Validate type ct:CrsType, a restriction on xs:string.
        if value is not None and Validate_simpletypes_ and self.gds_collector_ is not None:
            if not isinstance(value, str):
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s is not of the correct base simple type (str)' % {"value": value, "lineno": lineno, })
                return False
            if len(value) != 3:
                lineno = self.gds_get_node_lineno_()
                self.gds_collector_.add_message('Value "%(value)s"%(lineno)s does not match xsd length restriction on CrsType' % {"value": encode_str_2_3(value), "lineno": lineno} )
                result = False
    def hasContent_(self):
        if (

        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='StationType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('StationType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='StationType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='StationType', pretty_print=pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='StationType'):
        if 'crs' not in already_processed:
            already_processed.add('crs')
            outfile.write(' crs=%s' % (self.gds_encode(self.gds_format_string(quote_attrib(self.crs), input_name='crs')), ))
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='StationType', fromsubclass_=False, pretty_print=True):
        pass
    def to_etree(self, parent_element=None, name_='StationType', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        if self.crs is not None:
            element.set('crs', self.gds_format_string(self.crs))
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='StationType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.crs is not None and 'crs' not in already_processed:
            already_processed.add('crs')
            showIndent(outfile, level)
            outfile.write('crs=%s,\n' % (self.crs,))
    def exportLiteralChildren(self, outfile, level, name_):
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.StationType_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        if self.crs is not None:
            dbobj.crs = self.crs
    def exportSQLAlchemyChildren(self, session, dbobj):
        pass
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('crs', node)
        if value is not None and 'crs' not in already_processed:
            already_processed.add('crs')
            self.crs = value
            self.validate_CrsType(self.crs)    # validate type CrsType
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        pass
# end class StationType


class MsgType(GeneratedsSuper):
    """The content of the message"""
    __hash__ = GeneratedsSuper.__hash__
    subclass = None
    superclass = None
    def __init__(self, p=None, a=None, valueOf_=None, mixedclass_=None, content_=None, gds_collector_=None, **kwargs_):
        self.gds_collector_ = gds_collector_
        self.gds_elementtree_node_ = None
        self.original_tagname_ = None
        self.parent_object_ = kwargs_.get('parent_object_')
        self.ns_prefix_ = None
        if p is None:
            self.p = []
        else:
            self.p = p
        self.p_nsprefix_ = None
        if a is None:
            self.a = []
        else:
            self.a = a
        self.a_nsprefix_ = None
        self.valueOf_ = valueOf_
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, MsgType)
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if MsgType.subclass:
            return MsgType.subclass(*args_, **kwargs_)
        else:
            return MsgType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (
            self.p or
            self.a or
            (1 if type(self.valueOf_) in [int,float] else self.valueOf_)
        ):
            return True
        else:
            return False
    def export(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='MsgType', pretty_print=True):
        imported_ns_def_ = GenerateDSNamespaceDefs_.get('MsgType')
        if imported_ns_def_ is not None:
            namespacedef_ = imported_ns_def_
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.original_tagname_ is not None:
            name_ = self.original_tagname_
        if UseCapturedNS_ and self.ns_prefix_:
            namespaceprefix_ = self.ns_prefix_ + ':'
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s%s%s' % (namespaceprefix_, name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespaceprefix_, name_='MsgType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, namespaceprefix_, namespacedef_, name_='MsgType', pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s%s>%s' % (namespaceprefix_, name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespaceprefix_='', name_='MsgType'):
        pass
    def exportChildren(self, outfile, level, namespaceprefix_='', namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"', name_='MsgType', fromsubclass_=False, pretty_print=True):
        if not fromsubclass_:
            for item_ in self.content_:
                item_.export(outfile, level, item_.name, namespaceprefix_, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for p_ in self.p:
            namespaceprefix_ = self.p_nsprefix_ + ':' if (UseCapturedNS_ and self.p_nsprefix_) else ''
            p_.export(outfile, level, namespaceprefix_='tns:', namespacedef_='', name_='p', pretty_print=pretty_print)
        for a_ in self.a:
            namespaceprefix_ = self.a_nsprefix_ + ':' if (UseCapturedNS_ and self.a_nsprefix_) else ''
            a_.export(outfile, level, namespaceprefix_='tns:', namespacedef_='', name_='a', pretty_print=pretty_print)
    def to_etree(self, parent_element=None, name_='MsgType', mapping_=None):
        if parent_element is None:
            element = etree_.Element('{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        else:
            element = etree_.SubElement(parent_element, '{http://www.thalesgroup.com/rtti/PushPort/v16}' + name_)
        for item_ in self.content_:
            item_.to_etree(element)
        if mapping_ is not None:
            mapping_[id(self)] = element
        return element
    def exportLiteral(self, outfile, level, name_='MsgType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('valueOf_ = """%s""",\n' % (self.valueOf_,))
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('],\n')
        showIndent(outfile, level)
        outfile.write('content_ = [\n')
        for item_ in self.content_:
            item_.exportLiteral(outfile, level, name_)
        showIndent(outfile, level)
        outfile.write('],\n')
        pass
    def exportSQLAlchemy(self, session):
        """Export to SQLAlchemy database/ORM.
        For help with running this code, see:
            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
        """
        status, dbobj = self.gds_sqa_etl_transform()
        if status == 1:
            return dbobj
        if dbobj is None:
            dbobj = models_sqa_.MsgType_model()
        session.add(dbobj)
        self.exportSQLAlchemyAttributes(dbobj)
        self.exportSQLAlchemyChildren(session, dbobj)
        self.gds_sqa_etl_transform_db_obj(dbobj)
        return dbobj
    def exportSQLAlchemyAttributes(self, dbobj):
        pass
    def exportSQLAlchemyChildren(self, session, dbobj):
        for child in self.p:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.p.append(child_dbobj)
        for child in self.a:
            child_dbobj = child.exportSQLAlchemy(session)
            dbobj.a.append(child_dbobj)
    def build(self, node, gds_collector_=None):
        self.gds_collector_ = gds_collector_
        if SaveElementTreeNode:
            self.gds_elementtree_node_ = node
        already_processed = set()
        self.ns_prefix_ = node.prefix
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        if node.text is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', node.text)
            self.content_.append(obj_)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_, gds_collector_=gds_collector_)
        return self
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False, gds_collector_=None):
        if nodeName_ == 'p':
            obj_ = p.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'p', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_p'):
              self.add_p(obj_.value)
            elif hasattr(self, 'set_p'):
              self.set_p(obj_.value)
        elif nodeName_ == 'a':
            obj_ = a.factory(parent_object_=self)
            obj_.build(child_, gds_collector_=gds_collector_)
            obj_ = self.mixedclass_(MixedContainer.CategoryComplex,
                MixedContainer.TypeNone, 'a', obj_)
            self.content_.append(obj_)
            if hasattr(self, 'add_a'):
              self.add_a(obj_.value)
            elif hasattr(self, 'set_a'):
              self.set_a(obj_.value)
        if not fromsubclass_ and child_.tail is not None:
            obj_ = self.mixedclass_(MixedContainer.CategoryText,
                MixedContainer.TypeNone, '', child_.tail)
            self.content_.append(obj_)
# end class MsgType


GDSClassesMapping = {
}


USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in list(node.nsmap.items())
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in list(nsmap.items())
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
    parser = None
    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DataResponse'
        rootClass = DataResponse
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_=namespacedefs,
            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DataResponse'
        rootClass = DataResponse
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(str(content))
        sys.stdout.write('\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
    parser = None
    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DataResponse'
        rootClass = DataResponse
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:tns="http://www.thalesgroup.com/rtti/PushPort/v16"')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
    parser = None
    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DataResponse'
        rootClass = DataResponse
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
    if not silence:
        sys.stdout.write('#from schema_v16_py2 import *\n\n')
        sys.stdout.write('import schema_v16_py2 as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

RenameMappings_ = {
    "{http://www.thalesgroup.com/rtti/PushPort/Formations/v2}CoachData": "CoachData12",
    "{http://www.thalesgroup.com/rtti/PushPort/Formations/v2}CoachList": "CoachList11",
    "{http://www.thalesgroup.com/rtti/PushPort/Formations/v2}Formation": "Formation10",
    "{http://www.thalesgroup.com/rtti/PushPort/Formations/v2}ScheduleFormations": "ScheduleFormations9",
    "{http://www.thalesgroup.com/rtti/PushPort/Schedules/v3}DT": "DT6",
    "{http://www.thalesgroup.com/rtti/PushPort/Schedules/v3}IP": "IP3",
    "{http://www.thalesgroup.com/rtti/PushPort/Schedules/v3}OPDT": "OPDT7",
    "{http://www.thalesgroup.com/rtti/PushPort/Schedules/v3}OPIP": "OPIP4",
    "{http://www.thalesgroup.com/rtti/PushPort/Schedules/v3}OPOR": "OPOR2",
    "{http://www.thalesgroup.com/rtti/PushPort/Schedules/v3}OR": "OR1",
    "{http://www.thalesgroup.com/rtti/PushPort/Schedules/v3}PP": "PP5",
    "{http://www.thalesgroup.com/rtti/PushPort/Schedules/v3}Schedule": "Schedule8",
}

__all__ = [
    "AlertService",
    "AlertServices",
    "AssocService",
    "Association",
    "CoachData",
    "CoachData12",
    "CoachList",
    "CoachList11",
    "CoachLoadingData",
    "DT",
    "DT6",
    "DataResponse",
    "DeactivatedSchedule",
    "DisruptionReasonType",
    "FailureRespType",
    "Formation",
    "Formation10",
    "FullTDBerthID",
    "GetFullSnapshotReqType",
    "GetSnapshotReqType",
    "IP",
    "IP3",
    "Loading",
    "MsgType",
    "OPDT",
    "OPDT7",
    "OPIP",
    "OPIP4",
    "OPOR",
    "OPOR2",
    "OR",
    "OR1",
    "PP",
    "PP5",
    "PPConnect",
    "PPReqVersion",
    "PPStatus",
    "PlatformData",
    "Pport",
    "RTTIAlarm",
    "RTTIAlarmData",
    "Schedule",
    "Schedule8",
    "ScheduleFormations",
    "ScheduleFormations9",
    "StationMessage",
    "StationType",
    "StatusType",
    "TS",
    "TSLocation",
    "TSTimeData",
    "TimeTableIdType",
    "ToiletAvailabilityType",
    "TrackingID",
    "TrainAlert",
    "TrainOrder",
    "TrainOrderData",
    "TrainOrderItem",
    "a",
    "p",
    "ridType",
    "uRType"
]
