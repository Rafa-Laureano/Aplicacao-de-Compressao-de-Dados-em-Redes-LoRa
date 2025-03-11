#include <Wire.h>
#include <Adafruit_INA219.h>

Adafruit_INA219 ina219; // Inicialização com endereço padrão 0x40

void setup(void) 
{
  Serial.begin(115200);
  while (!Serial) {
      delay(10); // Pausa até a abertura do monitor serial
  }

  //Serial.println("Adafruit INA219 Test");

  if (!ina219.begin()) {
    Serial.println("Failed to find INA219 chip");
    while (1) { delay(10); }
  }
  // Para usar um ganho diferente, descomente uma das linhas seguintes:
   //ina219.setCalibration_32V_2A();
   //ina219.setCalibration_32V_1A();
   //ina219.setCalibration_16V_400mA();
}

float peakAvgPower = 0;

void loop(void) 
{
  float shuntvoltage = 0;
  float current_mA = 0;
  float power_mW = 0;
  float avg_power_mW = 0;
  float busVoltage = 0;
  float peakCurrent = 0;
  float peakPower = 0;
  float teste = 0;



  int numOfMeasurements = 100;
  
  for(int j=0; j<numOfMeasurements;j++){
    shuntvoltage = ina219.getShuntVoltage_mV();
    current_mA = ina219.getCurrent_mA();
    power_mW = ina219.getPower_mW();
    busVoltage = ina219.getBusVoltage_V();

    

    if(current_mA > peakCurrent){
      peakCurrent = current_mA;
    }

    if(power_mW > peakPower){
      peakPower = power_mW;
    }

    avg_power_mW += power_mW;

  }

  avg_power_mW /= numOfMeasurements;

  if(avg_power_mW > peakAvgPower){
    peakAvgPower = avg_power_mW;
  }
 
  
  Serial.print(avg_power_mW); Serial.print(",");
  Serial.print(peakPower); Serial.print(",");
  Serial.print(peakAvgPower); Serial.print(",");
  Serial.println(peakCurrent);
  

  /*Serial.print(shuntvoltage); Serial.print(",");
  Serial.print(current_mA); Serial.print(",");
  Serial.println(power_mW); 
  
delay(400);*/

}