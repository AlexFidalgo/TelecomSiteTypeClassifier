import pandas as pd

def rename_anatel_cols(anatel):

    d = {
        'NumEstacao_': 'Station',
        'FreqTxMHz_min': 'MinTxFreq',
        'FreqTxMHz_max': 'MaxTxFreq',
        'FreqRxMHz_min': 'MinRxFreq',
        'FreqRxMHz_max': 'MaxRxFreq',
        'ClassInfraFisica_agg_non_none': 'SiteType',
        'CodTipoAntena_max': 'AntennaCode',
        'GanhoAntena_agg_non_none': 'AntennaGain',
        'FrenteCostaAntena_max': 'FrontBackAntennaRation',
        'AnguloMeiaPotencialAntena_max': 'HalfPowerAngleAntenna',
        'AnguloElevacao_min': 'ElevationAngle',
        'Polarizacao_max': 'Polarization',
        'AlturaAntena_max': 'AntennaHeight',
        'PotenciaTransmissorWatts_max': 'TransmitterPower',
        'LarguraFaixaNecessaria_max': 'NecessaryBandwidth',
        'CaracteristicasBasicas_agg_non_none': 'BasicFeatures',
        'LTE_max': 'LTE', 
        'WCDMA_max': 'WCDMA', 
        'GSM_max': 'GSM', 
        'NR_NSA_max': 'NR_NSA', 
        'NR_SA-NSA_max': 'NR_SA-NSA',
        'DMR_max': 'DMR', 
        'Digital_max': 'Digital',
        'DiasDesdeLicenciamento_max': 'DaysSinceLicensing',
        'DiasDesdePrimeiroLicenciamento_max': 'DaysSinceFirstLicensing', 
        'DiasAteExpirar_min': 'DaysUntilExpiration'
    }

    anatel.rename(columns = d, inplace = True)

def get_rid_of_problematic_columns(anatel):

    anatel.drop('CompartilhamentoInfraFisica_agg_non_none', axis = 1, inplace=True) # too many NaN values (>70%)
    anatel.drop('SiglaUf_max', axis = 1, inplace=True) #CATEGORICAL: would yield 27 new columns - too high dimensionality
    anatel.drop('CodMunicipio_max', axis = 1, inplace=True) #NUMERICAL: but not really a number; if converted to str, same problem as SiglaUf
    anatel.drop('CodTipoClasseEstacao_max', axis = 1, inplace=True) #CATEGORICAL: ended up with a single value for all rows
    anatel.drop('CodDebitoTFI_max', axis = 1, inplace=True) #CATEGORICAL: overwhelming majority are of one specific value

    