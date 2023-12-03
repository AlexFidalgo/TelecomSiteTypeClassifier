import pandas as pd

def get_rid_of_problematic_columns(anatel):

    anatel = anatel.drop('SiglaUf_max', axis = 1) #CATEGORICAL: would yield 27 new columns - too high dimensionality
    anatel = anatel.drop('CodMunicipio_max', axis = 1) #NUMERICAL: but not really a number; if converted to str, same problem as SiglaUf
    anatel = anatel.drop('CodTipoClasseEstacao_max', axis = 1) #CATEGORICAL: ended up with a single value for all rows
    anatel = anatel.drop('CodDebitoTFI_max', axis = 1) #CATEGORICAL: overwhelming majority are of one specific value