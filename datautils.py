import yaml
import json as jsonmod
import toml
import csv
import io
import os
#import crutils
import sys
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo
# Crutils and datautils was written by KoffiDev in 2019/2022
# If you are going to use our product for commercial purposes please specify us as library developers
# Copyright KoffiDev
# Datautils can open: json, yaml, toml, ssb256 (our format), ini
class notDictionary(Exception):
    def __init__(self, text):
        self.txt = text
class notJson(Exception):
    def __init__(self, text):
        self.txt = text
class notYaml(Exception):
    def __init__(self, text):
        self.txt = text
class notToml(Exception):
    def __init__(self, text):
        self.txt = text
class yamlGroupExcept(Exception):
    def __init__(self, text):
        self.txt = text
class yamlSaveExcept(Exception):
    def __init__(self, text):
        self.txt = text
class yamlAddExcept(Exception):
    def __init__(self, text):
        self.txt = text
class yamlKeyExists(Exception):
    def __init__(self, text):
        self.txt = text
class SSBTextNotSupporting(Exception):
    def __init__(self, text):
        self.txt = text
class SSBParserError(Exception):
    def __init__(self, text):
        self.txt = text
class SSBFuncError(Exception):
    def __init__(self, text):
        self.txt = text
class CleanMemoryException(Exception):
    def __init__(self, text):
        self.txt = text
class jsonData:
    def __init__(self,json):
        self.json = json
        self.dictionary_class = type({})
    def load(self):

        if os.path.isfile(self.json) == False:
            try:
                self.json_profile = jsonmod.load(self.json)
            except:
                raise notJson('The returned value is not a json-format.')
        else:
            self.f = open(self.json)
            self.json_profile = jsonmod.load(self.f)
    def loadcustom(self, customload):
        self.customload = customload
        if os.path.isfile(self.json) == False:
            try:
                self.json_profile = jsonmod.loads([self.customload])
            except:
                raise notJson('The returned value is not a json-format.')
        else:
            self.f = open(self.json)
            self.json_profile = jsonmod.loads([self.customload])
    def getalldata(self):
        return self.json_profile
    def getonedata(self, param):
        self.param = param
        return self.json_profile[self.param]
    def add_data(self, data_dict):
        self.data_dict = data_dict
        if type(self.data_dict) != self.dictionary_class:
            raise notDictionary('The returned value is not a dictionary: '+str(type(self.data_dict)))
        else:
            self.json_tmp_1 = self.json_profile
            self.json_profile = {}
            self.json_profile = {**self.json_tmp_1, **self.data_dict}
    def save(self, fn):
        self.fn = fn
        with open(self.fn, 'w') as f:
            jsonmod.dump(self.json_profile, f)
class yamlData:
    def __init__(self,yamlf):
        self.yamlf = yamlf
        self.dictionary_class = type({})
    def load(self):
        if os.path.isfile(self.yamlf) == False:
            try:
                self.yaml_profile = yaml.safe_load(self.yamlf)
            except:
                raise notYaml('The returned value is not a yaml-format.')
        else:
            self.f = open(self.yamlf)
            self.yaml_profile = yaml.safe_load(self.f)
    def getalldata(self):
        return self.yaml_profile
    def getgroup(self, dest):
        self.dest = dest
        try:
            return self.yaml_profile[self.dest]
        except:
            raise yamlGroupExcept('Group doesnt exists:'+self.dest)
    def getonedata(self, group, dest):
        self.dest = dest
        self.group = group
        try:
            self.yaml_tmp_god_1 = self.yaml_profile[self.group]
            return self.yaml_tmp_god_1[self.dest]
        except:
            raise yamlGroupExcept('Error with group or dictionary index:'+self.group+","+self.dest)
    def add_data(self, data_to_add, key):
        self.data_to_add = data_to_add
        self.key = key
        if type(self.data_to_add) != self.dictionary_class:
            raise notDictionary('The returned value is not a dictionary: '+str(type(self.data_to_add)))
        else:
            try:
                self.yaml_1 = {**self.yaml_profile[key], **self.data_to_add}
                self.yaml_profile[key] = self.yaml_1
            except:
                raise yamlAddExcept('Datautils cant add data to yaml dictionary, key doesnt exists!')
    def add_key(self, key_name):
        self.key_name = key_name
        try:
            self.yaml_ak_tmp = {self.key_name:{}}
            self.yaml_ak_2 = self.yaml_profile
            self.yaml_profile = {**self.yaml_ak_2, **self.yaml_ak_tmp}
        except:
            yamlKeyExists('Key for yaml dictionary already exists!')
    def save(self, yfn):
        self.yfn = yfn
        try:
            with io.open(self.yfn, 'w', encoding='utf8') as self.outfile:
                yaml.dump(self.yaml_profile, self.outfile, default_flow_style=False, allow_unicode=True)
        except:
            raise yamlSaveExcept('Saving error has been occured!')
class tomlData:
    def __init__(self, toml_profile2):
        self.toml_profile2 = toml_profile2
        self.dictionary_class = type({})
    def load(self):
        if os.path.isfile(self.toml_profile2) == False:
            try:
                self.toml_profile2 = toml.load(self.toml_profile2)
            except:
                raise notToml('The returned value is not a toml-format.')
        else:
            self.f = open(self.toml_profile2)
            self.toml_profile = toml.load(self.f)
    def getalldata(self):
        return self.toml_profile
class ssb256Data:
    # sha256 have 64 
    def __init__(self, ssb256_profile):
        self.ssb256_profile = ssb256_profile
        self.dictionary_class = type({})
        self.loady = False
        self.godl = False
        self.enc = False
    def load(self):
        self.blank_cnt = 0
        self.temp_cnt_1_ = 0
        self.ssb_256type_dict = {}
        if os.path.isfile(self.ssb256_profile) == False:
            raise SSBTextNotSupporting('SSB256 Strings not supported.')
        else:
            self.filename, self.file_extension = os.path.splitext(self.ssb256_profile)
            if self.file_extension == '.ssb':
                with open(self.ssb256_profile, 'r') as f:
                    self.lines = f.readlines()
                    self.blank_cnt = len([l for l in self.lines if l.strip(' \n') != ''])
                with open(self.ssb256_profile) as file_in:
                    for line in file_in:
                        i = 0
                        self.temp_cnt_1_ += 1
                        self.sha256 = ''
                        self.signame = ''
                        self.signamelen = len(line)
                        if line[64] != "=":
                            raise SSBParserError('An assignment operator was expected but was not found.')
                            
                        for i in range(0, 64):
                            if line[i] == "#":
                                raise SSBParserError('On a 64 character long line where sha256 was expected but a comment was found')
                            else:
                                self.sha256 += line[i]
                        for i2 in range(65, self.signamelen):
                            if line[i2] == "#":
                                break
                            else:
                                self.signame += line[i2]
                        self.ssb_256type_tmp = {self.temp_cnt_1_:{'sha256':self.sha256,'sig':self.signame}}
                        self.ssb_256type_tmp2 = self.ssb_256type_dict
                        self.ssb_256type_dict = {**self.ssb_256type_tmp2, **self.ssb_256type_tmp}
                        self.ssb256_check1 = self.ssb_256type_dict[self.temp_cnt_1_]
                        self.ssb256_check2 = self.ssb256_check1['sig']
                        if "\n" in self.ssb256_check2:
                            self.newsig = self.signame.replace("\n", "")
                            self.ssb_256type_tmp = {self.temp_cnt_1_:{'sha256':self.sha256,'sig':self.newsig}}
                            self.ssb_256type_tmp2 = self.ssb_256type_dict
                            self.ssb_256type_dict = {**self.ssb_256type_tmp2, **self.ssb_256type_tmp}
                    self.loady = True
            else:
                raise SSBParserError('An unprotected type ssb256 was expected, but a different format was given.')
    def cleanmemory(self):
        if self.loady == True:
            del self.ssb_256type_tmp2
            del self.ssb_256type_tmp
            del self.ssb256_check2
            del self.ssb256_check1
            del self.temp_cnt_1_
            del self.sha256
            del self.signame
            del self.signamelen
            if self.godl == True:
                del self.godl_tmp
                self.godl = False

        else:
            raise CleanMemoryException('An attempt was made to clear the work memory but the load was not carried out.')
    def getalldata(self):
        if self.loady == True:
            return self.ssb_256type_dict
        else:
            raise SSBFuncError('An attempt was made to receive data but the load was not carried out.')
    def getgroup(self, group):
        if self.loady == True:
            self.group = group
            try:
                return self.ssb_256type_dict[self.group]
            except:
                raise SSBFuncError('An attempt was made to receive data but group doesnt exists.')
        else:
            raise SSBFuncError('An attempt was made to receive data but the load was not carried out.')
    def getonedata(self, group, val):
        if self.loady == True:
            self.group = group
            self.val = val
            try:
                try:
                    self.godl_tmp = self.ssb_256type_dict[self.group]
                    self.godl = True
                    return self.godl_tmp[self.val]
                except:
                    raise SSBFuncError('An attempt was made to receive data but value doesnt exists.')
            except:
                raise SSBFuncError('An attempt was made to receive data but group doesnt exists.')
        else:
            raise SSBFuncError('An attempt was made to receive data but the load was not carried out.')
class ssbEvrData:
    # sha256 have 64 
    def __init__(self, ssb256_profile):
        self.ssb256_profile = ssb256_profile
        self.dictionary_class = type({})
        self.loady = False
        self.godl = False
        self.enc = False
    def load(self):
        self.blank_cnt = 0
        self.temp_cnt_1_ = 0
        self.ssb_256type_dict = {}
        if os.path.isfile(self.ssb256_profile) == False:
            raise SSBTextNotSupporting('SSBEvr Strings not supported.')
        else:
            self.filename, self.file_extension = os.path.splitext(self.ssb256_profile)
            if self.file_extension == '.ssb':
                with open(self.ssb256_profile, 'r') as f:
                    self.lines = f.readlines()
                    self.blank_cnt = len([l for l in self.lines if l.strip(' \n') != ''])
                with open(self.ssb256_profile) as file_in:
                    for line in file_in:
                        self.whereoperator = line.find("=")
                        
                        i = 0
                        self.temp_cnt_1_ += 1
                        self.badcode = ''
                        self.signame = ''
                        self.signamelen = len(line)
                        if line[self.whereoperator] != "=":
                            raise SSBParserError('An assignment operator was expected but was not found.')
                            
                        for i in range(0, self.whereoperator):
                            if line[i] == "#":
                                raise SSBParserError('On a character long line where bad code was expected but a comment was found')
                            else:
                                self.badcode += line[i]
                        for i2 in range(self.whereoperator+1, self.signamelen):
                            if line[i2] == "#":
                                break
                            else:
                                self.signame += line[i2]
                        self.ssb_256type_tmp = {self.temp_cnt_1_:{'badcode':self.badcode,'sig':self.signame}}
                        self.ssb_256type_tmp2 = self.ssb_256type_dict
                        self.ssb_256type_dict = {**self.ssb_256type_tmp2, **self.ssb_256type_tmp}
                        self.ssb256_check1 = self.ssb_256type_dict[self.temp_cnt_1_]
                        self.ssb256_check2 = self.ssb256_check1['sig']
                        if "\n" in self.ssb256_check2:
                            self.newsig = self.signame.replace("\n", "")
                            self.ssb_256type_tmp = {self.temp_cnt_1_:{'badcode':self.badcode,'sig':self.newsig}}
                            self.ssb_256type_tmp2 = self.ssb_256type_dict
                            self.ssb_256type_dict = {**self.ssb_256type_tmp2, **self.ssb_256type_tmp}
                    self.loady = True
            else:
                raise SSBParserError('An unprotected type ssb256 was expected, but a different format was given.')
    def cleanmemory(self):
        if self.loady == True:
            del self.ssb_256type_tmp2
            del self.ssb_256type_tmp
            del self.ssb256_check2
            del self.ssb256_check1
            del self.temp_cnt_1_
            del self.badcode
            del self.signame
            del self.signamelen
            if self.godl == True:
                del self.godl_tmp
                self.godl = False

        else:
            raise CleanMemoryException('An attempt was made to clear the work memory but the load was not carried out.')
    def getalldata(self):
        if self.loady == True:
            return self.ssb_256type_dict
        else:
            raise SSBFuncError('An attempt was made to receive data but the load was not carried out.')
    def getgroup(self, group):
        if self.loady == True:
            self.group = group
            try:
                return self.ssb_256type_dict[self.group]
            except:
                raise SSBFuncError('An attempt was made to receive data but group doesnt exists.')
        else:
            raise SSBFuncError('An attempt was made to receive data but the load was not carried out.')
    def getonedata(self, group, val):
        if self.loady == True:
            self.group = group
            self.val = val
            try:
                try:
                    self.godl_tmp = self.ssb_256type_dict[self.group]
                    self.godl = True
                    return self.godl_tmp[self.val]
                except:
                    raise SSBFuncError('An attempt was made to receive data but value doesnt exists.')
            except:
                raise SSBFuncError('An attempt was made to receive data but group doesnt exists.')
        else:
            raise SSBFuncError('An attempt was made to receive data but the load was not carried out.')
