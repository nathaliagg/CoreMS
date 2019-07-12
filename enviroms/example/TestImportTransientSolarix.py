import pickle, sys

sys.path.append(".")
from enviroms.emsl.yec.transient.input.BrukerSolarix import ReadBrukerSolarix


__author__ = "Yuri E. Corilo"
__date__ = "Jun 19, 2019"


if __name__ == "__main__":
    # from enviroms.emsl.yec.structure.input.MidasDatFile import ReadMidasDatFile
    filelocation = "C:\\Users\\eber373\\Desktop\\data\\20190616_WK_ESFA_0pt2mgml_ESI_Neg_0pt8sFID_000001.d\\"
    filelocation = "C:\\Users\\eber373\\Desktop\\data\\20190205_WK_SRFA_opt_000001.d\\"

    apodization_method = "Hanning"
    number_of_truncations = 0
    number_of_zero_fills = 1

    bruker_transient = ReadBrukerSolarix(filelocation)
    bruker_transient.set_processing_parameter(
        apodization_method, number_of_truncations, number_of_zero_fills
    )
    
    #need implement manual check
    mass_spec = bruker_transient.generate_mass_spec(plot_result=False)
    
    #need implement  check already processed
    #mass_spec.cal_noise_treshould()
    #need implement  check already processed
    #mass_spec.find_peaks()
    
    mass_spec.plot_mz_domain_profile_and_noise_threshold()
   
    print(mass_spec.mspeaks[0].exp_mz, mass_spec.mspeaks[-1].exp_mz)

    with open("test.pkl", "wb") as file:
        pickle.dump(bruker_transient, file, protocol=pickle.HIGHEST_PROTOCOL)

    # transient = pickle.load( open( 'test.pkl', "rb" ) )
    # do_something
