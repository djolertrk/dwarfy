#!/usr/bin/python
#
# This file is part of 'dwarfy' project.
#
# The program evaluates debugging user experience.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# Author: Djordje Todorovic djolertrk@gmail.com

import re

def process_backtrace(frames_bt):
  optimized_out_bt = 0
  num_entry_values_bt = 0
  num_params = 0
  i = 0
  frames_len = len (frames_bt)
  while i < frames_len:
    f = frames_bt[i]
    full_call_frame = ""
    first_param = f.find('(')
    last_param = f.find(')')
    if first_param != -1 and last_param != -1:
      # Found whole frame in one line.
      full_call_frame  += f
    elif first_param != -1 and last_param == -1:
      # Found frame in multiple lines.
      full_call_frame  += f
      i += 1
      if i >= frames_len:
        break
      next_line = frames_bt [i]
      while 1:
        full_call_frame += next_line
        last_param = next_line.find(')')
        if last_param != -1:
          break
        i += 1
        if i >= frames_len:
          break
        next_line = frames_bt [i]
    else:
      i += 1
      continue

    i += 1

    # Rearranging all params in one line.
    full_call_frame = full_call_frame.replace ("\n", "")
    full_call_frame = re.sub(' +', ' ', full_call_frame)

    first_param = full_call_frame.find('(')
    last_param = full_call_frame.find(')')

    if first_param == -1 or last_param == -1:
      continue

    params = full_call_frame[first_param+1:last_param]
    params_list = params.split(", ")
    for p in params_list:
      if not "=" in p:
        continue
      num_params += 1
      expr = p.partition("=")
      var = expr[0]
      value = expr[2]
      entry_value = ""
      if value.find("@entry") != -1:
        value.partition("=")
        value = value[2]
        entry_value = value
        num_entry_values_bt += 1
      elif var.find("@entry") != -1:
        var.partition("=")
        entry_value = var[2]
        num_entry_values_bt += 1

      if value == "<optimized out>":
        optimized_out_bt += 1

  result = []
  result.append (num_params)
  optimized_out_bt_p = 0.0
  num_entry_values_bt_p = 0.0
  if num_params > 0:
    optimized_out_bt_p = (float(optimized_out_bt)/num_params) * 100;
    num_entry_values_bt_p = (float(num_entry_values_bt)/num_params) * 100;
  result.append (optimized_out_bt_p)
  result.append (num_entry_values_bt_p)

  return result
