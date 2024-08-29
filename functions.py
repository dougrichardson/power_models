import xarray as xr

def load_hourly_cf(year, gen_type, method="van_der_Wiel", chunks=None):
    """
    Load one year of hourly generation data.
    
    year: int, year to load
    gen_type: str, 'wind' or 'solar'
    method: str, method used to compute capacity factor, e.g. 'van_der_Wiel'
    chunks: dict, how to chunk. Default is None
    """
    cf_path = "/g/data/w42/dr6273/work/projects/Aus_energy/production_metrics/" + gen_type + "/capacity_factor/" + method + "/"
    return xr.open_mfdataset(cf_path + gen_type + "_capacity_factor_" + method + "_era5_hourly_" + str(year) + "_Aus.nc", chunks=chunks)