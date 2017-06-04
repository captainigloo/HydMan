# Specifications & I²C commands (ASCII)

## EZO I²C Address :

|| EZO  | HEX  | ASCII  | Circuit |
|:-:|:-:|:-:|:-:|:-:|
|<img src="https://github.com/captainigloo/HydMan/blob/master/docs/EZO_Circuits/do.png">| DO  | 0x60  | 97  ||
|<img src="https://github.com/captainigloo/HydMan/blob/master/docs/EZO_Circuits/orp.png">| ORP  | 0x61  | 98  ||
|<img src="https://github.com/captainigloo/HydMan/blob/master/docs/EZO_Circuits/ph.png">| pH  | 0x63  | 99  |<img src="https://github.com/captainigloo/HydMan/blob/master/docs/EZO_Circuits/EZO-PH.png" width="100">|
|<img src="https://github.com/captainigloo/HydMan/blob/master/docs/EZO_Circuits/ec.png">| EC  | 0x64  | 100  |<img src="https://github.com/captainigloo/HydMan/blob/master/docs/EZO_Circuits/EZO-EC.png" width="100">|
|<img src="https://github.com/captainigloo/HydMan/blob/master/docs/EZO_Circuits/rtd.png">| RTD  | 0x66  | 102  |<img src="https://github.com/captainigloo/HydMan/blob/master/docs/EZO_Circuits/EZO_RTD.png" width="100">|
|<img src="https://github.com/captainigloo/HydMan/blob/master/docs/EZO_Circuits/peristaltic.png">| PMP  | 0x67  | 103  |<img src="https://github.com/captainigloo/HydMan/blob/master/docs/EZO_Circuits/EZO-PMP.png" width="100">|

## EZO EC (Electrical Conductivity)

### Data type (EC,TDS,SAL,SG)
- EC	Electrical Conductivity (μS - microSiemens)
- TDS 	Total Dissolved solids (PPM)
- SAL	Salinity (PSU - practical salinity uni)
- SG	Specific Gravity

### Dynamic set Temperature compensation

T,19.5

### Set type of probe

K,0.1 K,1.0 K,10

## EZO RTD (PT-1000 : °C, °F, °K)
### Dynamic set Temperature compensation
<img src="https://github.com/captainigloo/HydMan/blob/master/docs/EZO_Circuits/Dynamic%20Temerature%20compensation.png" width="600">


- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item
- [ ] this is an incomplete item
- [ ] this is an incomplete item
- [ ] this is an incomplete item


```python
s = "Python syntax highlighting"
print s
```
