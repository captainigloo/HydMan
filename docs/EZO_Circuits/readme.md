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

<blockquote class="instagram-media" data-instgrm-version="7" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:658px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:8px;"> <div style=" background:#F8F8F8; line-height:0; margin-top:40px; padding:50.0% 0; text-align:center; width:100%;"> <div style=" background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAsCAMAAAApWqozAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAAMUExURczMzPf399fX1+bm5mzY9AMAAADiSURBVDjLvZXbEsMgCES5/P8/t9FuRVCRmU73JWlzosgSIIZURCjo/ad+EQJJB4Hv8BFt+IDpQoCx1wjOSBFhh2XssxEIYn3ulI/6MNReE07UIWJEv8UEOWDS88LY97kqyTliJKKtuYBbruAyVh5wOHiXmpi5we58Ek028czwyuQdLKPG1Bkb4NnM+VeAnfHqn1k4+GPT6uGQcvu2h2OVuIf/gWUFyy8OWEpdyZSa3aVCqpVoVvzZZ2VTnn2wU8qzVjDDetO90GSy9mVLqtgYSy231MxrY6I2gGqjrTY0L8fxCxfCBbhWrsYYAAAAAElFTkSuQmCC); display:block; height:44px; margin:0 auto -44px; position:relative; top:-22px; width:44px;"></div></div><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/p/BUkorWeFYo7/" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">Une publication partagée par AtlasScientific (@atlasscientific)</a> le <time style=" font-family:Arial,sans-serif; font-size:14px; line-height:17px;" datetime="2017-05-26T22:32:14+00:00">26 Mai 2017 à 15h32 PDT</time></p></div></blockquote>
<script async defer src="//platform.instagram.com/en_US/embeds.js"></script>

```python
s = "Python syntax highlighting"
print s
```
