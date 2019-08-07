import json
from os import system
from rateVsLumError_v5 import rate_lumi_fit 

def main():
    message = extend_info(4)
    system(' say "Hecho!"')
    return

def extend_info(number_of_chambers):
    """
    This function will make fits and add result to the written json file
    """
    i = 0
    with open('lumi_fit_by_chamber.json', 'r') as fp:
        info_prev = json.load(fp)
    fit_info_manager = rate_lumi_fit(info_prev)
    accumulated_fit_information_dictionary = fit_info_manager.fit_info
    all_chambers = fit_info_manager.all_chambers
    accumulated_chambers = [k for k,v in accumulated_fit_information_dictionary.items()]
    missing_chambers = [item for item in all_chambers if item not in accumulated_chambers]
    extention_chambers = missing_chambers[:number_of_chambers]
    for chamber in extention_chambers:
        fit_info_manager.fit_chamber_and_append_result(chamber)
        with open('lumi_fit_by_chamber.json', 'w') as fp:
            json.dump(accumulated_fit_information_dictionary, fp, indent=4)
        continue
    return "done"


if __name__ == "__main__":
  test = main()

