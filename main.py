# Copyright (c) 2020 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#
# Author: Kami Salibayeva
# Indiana University

# set up environment
import os
import json
import mne

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Populate mne_config.py file with brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)

fname = config['raw']

# Read the raw data and info
raw = mne.read_raw_fif(fname)
info = raw.info

#Save the info into a info.txt file
with open(os.path.join('out_dir','info.txt'), 'w') as f:
    print(info, file=f)