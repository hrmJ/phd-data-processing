import sys
import os
import glob
import json
import time
import searchutils
import menus
import utils
import groups.fi
import groups.ru
result_data_address = '/root/results'
final_data_address = '/'

if __name__ == "__main__":

    groupname = sys.argv[1]
    lang = sys.argv[2]

    if lang == "fi":
        subgroups = groups.fi.subgroups
    elif lang=="ru":
        subgroups = groups.ru.subgroups

    res_filename = '{}/{}/{}_SVO_quantdata.json'.format(result_data_address, lang, groupname)
    res_filename2 = '{}/{}/{}_svo_quantdata.json'.format(result_data_address, lang, groupname)
    subgroup = subgroup[groupname]
    if not os.path.isfile(res_filename):
        searchutils.logging.info("STARTING "  + groupname)
        subgroup.Analyze(True)
        searchutils.logging.info(subgroup.name + "DONE.")
