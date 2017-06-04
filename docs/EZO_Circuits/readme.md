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

## EZO PMP
<img src="https://scontent-cdg2-1.cdninstagram.com/t50.2886-16/18785726_212682725908972_7723313300947075072_n.mp4" width="600">
<video controls="controls" poster="http://distilleryimage3.ak.instagram.com/2f7c10d8d9e911e28df922000a9f1991_7.jpg" width="640" height="640">
	<source src="https://distilleryimage3.s3.amazonaws.com/2f7c10d8d9e911e28df922000a9f1991_101.mp4" type="video/mp4" />
	<img alt="5th Ave" src="http://distilleryimage3.ak.instagram.com/2f7c10d8d9e911e28df922000a9f1991_7.jpg" width="640" height="640" title="No video playback capabilities, please download the video below" />
</video>

```python
s = "Python syntax highlighting"
print s
```
