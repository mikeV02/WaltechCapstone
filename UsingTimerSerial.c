#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <avr/io.h>
#include <avr/interrupt.h>
#include "uart.c"
#include <util/delay.h>

volatile uint8_t timerOF=0;
#define OVERSAMPLES 10
int testCount = 0;
unsigned long int TimerSetup = 0;
static volatile uint16_t adcData;
static volatile uint16_t ADCtotal;
static volatile uint8_t adcDataL;
static volatile uint8_t adcDataH;
static volatile uint8_t sample_count;

inline ISR(TIMER0_OVF_vect)
{
    timerOF=1;
    
    TimerSetup = TimerSetup + 1;
    
    if(TimerSetup > (61035/4))  //sets speed to a quarter of a second
    {    
        if(uart_buffer_empty())
        {
            char temp[50];// = "hello world, from inside loop";
            
            //strcat(temp,"received: ");
            //
            //temp[strlen(temp) + 1] = uart_getc();
            //
            //strcat(temp,"\n\0");
            uart_getc();
            
            itoa(PINC,temp,2);
            strcat(temp,"\n\0");
            
            uart_puts(temp);
        }
        TimerSetup = 0;
    }
    
}

inline ISR(ADC_vect)
{
    adcDataL = ADCL;
    adcDataH = ADCH;
    adcData = 0;
    adcData = adcData | adcDataH;
    adcData = adcData << 8;
    adcData = adcData | adcDataL;
    ADCtotal = ADCtotal+adcData;
    sample_count ++;
}
int16_t do_math(int16_t A,int16_t B,char operator)
{
    int32_t result = 0;
    if (operator == '+'){result = A+B;}
    if (operator == '-'){result = A-B;}
    if (operator == '*'){result = A*B;}
    if (operator == '/'){result = A/B;}
//    if (operator == '='){result = A = B;}
    int16_t i =  ((result >> 0) & 0xffff);
   return i;
}
uint16_t read_adc(uint8_t channel)
{
    ADMUX = channel;// set channel
    ADMUX |=  (1<<REFS0);// sets ref volts to Vcc
    ADCSRA |= (1<<ADEN); // enable the ADC
    sample_count = 0; ADCtotal = 0;//clear sample count
    ADCSRA |= (1<<ADSC);//start conversion
    //read adcData done in interrupt
    while (sample_count < OVERSAMPLES){asm volatile ("nop"::);}//wait for completion
    ADCSRA &=~ (1<<ADEN); // stop the ADC
    return (ADCtotal/OVERSAMPLES); //mx osamples = 63  othewise will overflow total register with 10 bit adc results
}
int main()
{
//set up ADC
    ADCSRA |= ( (1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0) );//  sets adc clock prescaler to 128 //checked
    ADCSRA |= (1<<ADIE); // enable ADC conversion complete interrupt
    ADCSRA |= (1<<ADATE);// set to auto trigger (free running by default)
   DDRD |= (1<<5);
   DDRD |= (1<<6);
   DDRD |= (1<<7);
   DDRB |= (1<<0);
   DDRB |= (1<<3);
   DDRB |= (1<<4);
   DDRB |= (1<<5);

   DDRC &= 0b0000000;
   //PORTC |= (1<<4);
   //PORTC |= (1<<5);
   PORTD |= (1<<2);
   PORTD |= (1<<3);
   PORTD |= (1<<4);

   //PCICR &= 0b000;
   //PCICR |= 0b010;
   //
   //PCMSK1 &= 0b00000000; 
   //PCMSK1 |= 0b00111111; 
   
    //set up loop timer:
    /*TIMSK0 |= (1<<TOIE0);// overflow capture enable
    TCNT0 = 101;// start at this
    TCCR0B &= ((1<<CS10)|(1<<CS12));// timer started with /1024 prescaler
    sei();*/
    
    //OCR0A = 0xAF;
    //TIMSK0 |= _BV(OCIE0A);
    
    //set up loop timer:

    TIMSK0 |= (1<<TOIE0);// overflow capture enable*/
    TCNT0 = 0;//101;// start at this
    TCCR0B |= (1<<CS10);//((1<<CS10)|(1<<CS12));// timer started with /1024 prescaler
    sei();
    //uint8_t cont_Name_2_NO = 0;

    //uint8_t output_Name_1 = 0;





    //uint8_t W = 1;
	uart_init();




    while (1)
    {

        /*if (timerOF == 1)
        {
           timerOF=0;//reset timer flag
           TCNT0 = 101;// start at this
           //inputs:
           cont_Name_2_NO = PINC &(1<<4);

            //Start of Ladder:

            //rung at 0
             W = 1;
             if(cont_Name_2_NO == 0){
				W = 0;

			 }else{
					uart_puts("Hello ALL");			 
			 }
			 
              output_Name_1 = W;


            //end rung

           //outputs:
         if(output_Name_1 == 0){PORTD &=~ (1<<5);}
         else {PORTD |= (1<<5);}

       }*/
   }
}