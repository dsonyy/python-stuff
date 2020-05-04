#include "SerialCommand.h"
#include <LiquidCrystal_I2C.h>

#if defined(ARDUINO) && ARDUINO >= 100
#define printByte(args)  write(args);
#else
#define printByte(args)  print(args,BYTE);
#endif

LiquidCrystal_I2C lcd(0x27,20,4);
SerialCommand sCmd;
int x = 0, y = 0;

void setup() 
{
  Serial.begin(9600);
  Serial.println("READY");

  lcd.init();
  lcd.backlight();
  sCmd.addCommand("SYMBOL", symbolCmd);
  sCmd.addCommand("PRINT", printCmd);
  sCmd.addCommand("PRINTB", printbCmd);
  sCmd.addCommand("HOME", homeCmd);
  sCmd.addCommand("CURSOR", cursorCmd);
}

void loop() 
{
  sCmd.readSerial();
}

void homeCmd()
{
  lcd.home();
}

void cursorCmd()
{
  int x = atoi(sCmd.next());
  int y = atoi(sCmd.next());

  lcd.setCursor(x, y);
}

void symbolCmd()
{
  uint8_t symbol[8];
  int b;
  for (int i = 0; i < 8; i++)
  {
    symbol[i] = atoi(sCmd.next());
  }
  b = atoi(sCmd.next());
  lcd.createChar(b, symbol);
}

void printCmd()
{
  char * txt = sCmd.next();
  lcd.print(txt);
}

void printbCmd()
{
  int b = atoi(sCmd.next());
  lcd.printByte(b);
}
