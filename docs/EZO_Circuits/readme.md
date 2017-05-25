# EZO EC (Electrical Conductivity)

## Data type (EC,TDS,SAL,SG)
- EC	Electrical Conductivity (μS - microSiemens)
- TDS 	Total Dissolved solids (PPM)
- SAL	Salinity (PSU - practical salinity uni)
- SG	Specific Gravity

## Dynamic set Temperature compensation

T,19.5 (i2cset -y 1 0x64 0x54 0x31 0x39 0x2e 0x35)

## Set type of probe

K,0.1 K,1.0 K,10
