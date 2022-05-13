/*Arduino Code
 * Thomas Wick, Elizibeth Woodard, Andrew Posey, Garrett Sepulvado
 */
#include <HX711_ADC.h>
#if defined(ESP8266)|| defined(ESP32) || defined(AVR)
#include <EEPROM.h>
#endif

//pins:
const int HX711_dout_1 = 3; 
const int HX711_sck_1 = 4;
const int HX711_dout_2 = 6; 
const int HX711_sck_2 = 7; 
const int HX711_dout_3 = 9; 
const int HX711_sck_3 = 10;
const int HX711_dout_4 = 12; 
const int HX711_sck_4 = 13;



//HX711 constructor (dout pin, sck pin)
HX711_ADC LoadCell_1(HX711_dout_1, HX711_sck_1); //HX711 1
HX711_ADC LoadCell_2(HX711_dout_2, HX711_sck_2); //HX711 2
HX711_ADC LoadCell_3(HX711_dout_3, HX711_sck_3); //HX711 3
HX711_ADC LoadCell_4(HX711_dout_4, HX711_sck_4); //HX711 4

const int calVal_eepromAdress_1 = 0; // eeprom adress for calibration value load cell 1 (4 bytes)
const int calVal_eepromAdress_2 = 4; // eeprom adress for calibration value load cell 2 (4 bytes)
unsigned long t = 0;

void setup() {
  Serial.begin(57600); delay(10);
  Serial.println();
  Serial.println("Starting...");

  float calibrationValue_1; 
  float calibrationValue_2; 
  float calibrationValue_3;  
  float calibrationValue_4;
  

  calibrationValue_1 = 2005.0; 
  calibrationValue_2 = 1818.0;  //calibration values
  calibrationValue_3 = 1975.0; 
  calibrationValue_4 = 1840.0; 
  
#if defined(ESP8266) || defined(ESP32)
 
#endif


  LoadCell_1.begin();
  LoadCell_2.begin();
  LoadCell_3.begin(); //begins loadcells to get values
  LoadCell_4.begin();
  
  unsigned long stabilizingtime = 2000; 
  boolean _tare = true; 
  byte loadcell_1_rdy = 0;
  byte loadcell_2_rdy = 0;
  byte loadcell_3_rdy = 0;
  byte loadcell_4_rdy = 0;
  
  while ((loadcell_1_rdy + loadcell_2_rdy + loadcell_3_rdy) < 3) { //run startup, stabilization and tare, both modules simultaniously
    if (!loadcell_1_rdy) loadcell_1_rdy = LoadCell_1.startMultiple(stabilizingtime, _tare);
    if (!loadcell_2_rdy) loadcell_2_rdy = LoadCell_2.startMultiple(stabilizingtime, _tare);
    if (!loadcell_3_rdy) loadcell_3_rdy = LoadCell_3.startMultiple(stabilizingtime, _tare);
    if (!loadcell_4_rdy) loadcell_4_rdy = LoadCell_4.startMultiple(stabilizingtime, _tare);       //tests for wiring
  }
  if (LoadCell_1.getTareTimeoutFlag()) {
    Serial.println("Timeout, check MCU>HX711 no.1 wiring and pin designations");
  }
  if (LoadCell_2.getTareTimeoutFlag()) {
    Serial.println("Timeout, check MCU>HX711 no.2 wiring and pin designations");
  }
  if (LoadCell_3.getTareTimeoutFlag()) {
    Serial.println("Timeout, check MCU>HX711 no.3 wiring and pin designations");
  }
  if (LoadCell_4.getTareTimeoutFlag()) {
    Serial.println("Timeout, check MCU>HX711 no.4 wiring and pin designations");
  }
  LoadCell_1.setCalFactor(calibrationValue_1); 
  LoadCell_2.setCalFactor(calibrationValue_2);
  LoadCell_3.setCalFactor(calibrationValue_3); 
  LoadCell_4.setCalFactor(calibrationValue_4);  //gives the okay to start
  Serial.println("Startup is complete");
}

void loop() {
  static boolean newDataReady = 0;
  const int serialPrintInterval = 3000; //increase value to slow down serial print activity

  
  
  // check for new data/start next conversion:
  if (LoadCell_1.update() || LoadCell_2.update() || LoadCell_3.update() || LoadCell_4.update()) newDataReady = true;

  //get smoothed value from data set
  
  //if (newDataReady) {
    
    if (Serial.read() == 'p') {
      float a = LoadCell_1.getData();
      float b = LoadCell_2.getData();
      float c = LoadCell_3.getData();
      float d = LoadCell_4.getData();

      Serial.println(a);
      Serial.println(b);  //values of all load cells
      Serial.println(c);
      Serial.println(d);
      //Serial.println('p');
    }
    newDataReady = 0;
    t = millis();
      
  //}


  // receive command from serial terminal, send 't' to initiate tare operation:
  if (Serial.available() > 0) {
    char inByte = Serial.read();
    if (inByte == 't') {
      LoadCell_1.tareNoDelay();
      LoadCell_2.tareNoDelay();
      LoadCell_3.tareNoDelay();
      LoadCell_4.tareNoDelay();
    }
  }

  //check if last tare operation is complete
  if (LoadCell_1.getTareStatus() == true) {
    Serial.println("Tare load cell 1 complete");
  }
  if (LoadCell_2.getTareStatus() == true) {
    Serial.println("Tare load cell 2 complete");     //lets us know when the load cells have zeroe'd out
  }
  if (LoadCell_3.getTareStatus() == true) {
    Serial.println("Tare load cell 3 complete");
  }
  if (LoadCell_4.getTareStatus() == true) {
    Serial.println("Tare load cell 4 complete");
  }

}
