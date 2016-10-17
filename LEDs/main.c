#include <wiringPi.h>
#include <stdio.h>
#include <wiringPiI2C.h>

#define N 6
#define PCF8591 (0x90 >> 1)
#define AIn0 0x00
#define Samples 25

int leds[6] = {0,2,3,21,22,23};

void setup(void)
{
   int i;
   wiringPiSetup();
   for(i=0;i<N;i++)
   	pinMode(leds[i], OUTPUT); 	
}

void leds_blink(unsigned char a)
{
   int i;
   if(a>N)
	a = N;
   if(a<0)
	a = 0;
   for(i=0;i<a;i++)
	digitalWrite(leds[i], HIGH);
   for(i=a;i<N;i++)
	digitalWrite(leds[i], LOW); 	
}

unsigned char maxchar(unsigned char a, unsigned char b){
  if(a>=b)
    return a;
  else
    return b;
}

unsigned char minchar(unsigned char a, unsigned char b){
  if(a<=b)
    return a;
  else
    return b;
}

int main (void)
{
  int i,fd;
  unsigned char value[Samples];
  unsigned char diff,blink;
  unsigned char inputMax = 0;
  unsigned char inputMin = 255;

  setup();
  if ((fd = wiringPiI2CSetup(PCF8591)) < 0) {
    printf("wiringPiI2CSetup failed:\n");
  }

  while(1)
  {
    inputMax = 0;
    inputMin = 255;
    wiringPiI2CWrite(fd,0x40 | AIn0);

    value[0] = wiringPiI2CRead(fd);
    for(i=0;i<Samples;i++)
    {
	value[i] = wiringPiI2CRead(fd);
	inputMin = minchar(inputMin, value[i]);
    	inputMax = maxchar(inputMax, value[i]);
    }

    diff = (inputMax - inputMin);
    blink = diff/8;
    leds_blink(blink);
   
    printf("\nInput Max: 0x%X\tInput Min: 0x%X\tDiff: %6d\tBlink: %2d\t",inputMax,inputMin,diff,blink);
     
  }
  return 0 ;
}
