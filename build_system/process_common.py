import string
import types

def replace_common_identifier(s0):
  s0 = s0.replace(" ","_")
  s0 = s0.replace("'","_")
  s0 = s0.replace("`","_")
  s0 = s0.replace("(","_")
  s0 = s0.replace(")","_")
  s0 = s0.replace("-","_")
  s0 = s0.replace(",","")
  s0 = s0.replace("|","")
  s0 = s0.replace("\t","_") #Tab
  return s0

def convert_to_identifier(s0):
  s0 = replace_common_identifier(s0)
  s0 = s0.lower()
  return s0

def convert_to_identifier_with_no_lowercase(s0):
  s0 = replace_common_identifier(s0)
  return s0

def replace_spaces(s0):
  s0 = s0.replace("\t","_")
  return s0.replace(" ","_")
