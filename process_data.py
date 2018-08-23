import sys
import os
import glob
import json
import time
import searchutils
import menus
import utils
result_data_address = '/root/results'
final_data_address = '/'

if __name__ == "__main__":

    groupname = sys.argv[1]
    lang = sys.argv[2]

    if lang == "fi":
        import groups.fi
        subgroups = groups.fi.subgroups
    elif lang=="ru":
        import groups.ru
        subgroups = groups.ru.subgroups

    res_filename = '{}/{}/{}_SVO_quantdata.json'.format(result_data_address, lang, groupname)
    res_filename2 = '{}/{}/{}_svo_quantdata.json'.format(result_data_address, lang, groupname)
    subgroup = subgroups[groupname]
    if not os.path.isfile(res_filename):
        searchutils.logging.info("STARTING "  + groupname)
        subgroup.Analyze(True)
        searchutils.logging.info(subgroup.name + "DONE.")
    else:
        with open("/tmp/already_processed.log","a") as f:
            f.write(groupname)
