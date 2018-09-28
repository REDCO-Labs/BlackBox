# TEC Driver Documentation (MTD415T)



## Circuit information

### MTD415T

- 4.5 to 5.5 V

- 1.5 A max

  ![MTD415 Pin Layout](https://www.thorlabs.com/images/tabimages/MTD_Pin_Diagram-400.gif)

![img](https://www.thorlabs.com/images/TabImages/MTD415T_Block_Diagram_D2-780.gif)


### N.B.

- Make sure UART TX-RX connects to MTD RX-TX  (look up uart color-code)
- CONNECT UART GND TO MTD415T GND !!!





## Usage

### Thorlabs MTD Software

Download the software from thorlabs website.

Plug&Play. Easy control of all settings.

**N.B. :**  If you restart the MTD board or something goes wrong, you might have to restart the software and re-plug the UART connection. 



### Thorlabs MTD Python API

Requires Thorlabs MTD415 API :

```
pip install pyserial
pip install git+git://github.com/nelsond/thorlabs-mtd415t.git
```

The API example has been copied here to `tecDriver.py`

Nothing has been developed with this API yet.

