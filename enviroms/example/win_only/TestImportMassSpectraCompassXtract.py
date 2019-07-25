import sys

sys.path.append(".")

from enviroms.emsl.yec.mass_spectra.input.win_only.BrukerCompassXtract import (
    ImportLCMSBrukerCompassXtract,
)

if __name__ == "__main__":
    file_location = "C:\\Users\\eber373\\Desktop\\Data\\20190205_WK_SRFA_opt_000001.d"

    lcms_reader = ImportLCMSBrukerCompassXtract(file_location)

    all_scans = lcms_reader.get_scans_numbers()

    print("There are a total of %i scans" % all_scans)
    # a.initial_scan_number = 100
    # a.final_scan_number = 103

    lcms = lcms_reader.get_mass_spectra(auto_process=True)
    """to use the thread
    lcmc_reader.start()
    do something 
    lcmc_reader.join()
    lcms = lcmc_reader.get_lcms"""
    kendrick_base = {"C" : 1, "H" : 1, "O" :1}
    
    for mass_spec in lcms:
       
       print(mass_spec.number_average_molecular_weight)
       mass_spec.change_kendrick_base_all_mspeaks(kendrick_base)
       for ms_peak in mass_spec:
           
           print(ms_peak.exp_mz)
           print(ms_peak.abundance)
           print(ms_peak.kendrick_mass)
           kendrick_base = {"C" : 1, "H" : 0, "O" :1}
           print(ms_peak.kendrick_mass)
           ms_peak.change_kendrick_base(kendrick_base)
    
    mass_spec = lcms.get_mass_spec_by_scan_number(1)
    mass_spec.plot_mz_domain_profile()
    mass_spec.plot_mz_domain_profile_and_noise_threshold()
