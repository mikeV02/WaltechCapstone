#include <stdio.h>
#include <string.h>
#include <avr/interrupt.h>
#include <avr/io.h>
#include <avr/pgmspace.h>
#include <avr/sfr_defs.h>
#include <avr/sleep.h>

#include "uart.h"


unsigned char rx_buffer[RX_BUFFER_SIZE];
volatile unsigned char rx_buffer_head;
volatile unsigned char rx_buffer_tail;
volatile char tx_complete;
//int receivingCounter = 0;

// UART recieve interrupt handler.
//   
// If the buffer overflows, data will be overwritten without warning
//

ISR(USART_RXC_vect) // before: SIGNAL(SIG_USART_RECV)
{
    //commented out in order to handle the receiving of data
    //in other part of code
    /*char c = UDR;
    rx_buffer[rx_buffer_head] = c;
    INC_RING(rx_buffer_head, RX_BUFFER_SIZE);*/
    
    // one might deal with head==tail here (buffer full)
}



void uart_init()
{
    
    /* set baud rate */
    UBRRH = UBRRVAL >> 8;
    UBRRL = UBRRVAL & 0xff;
    /* set frame format: 8 bit, no parity, 1 bit */
    UCSRC = UCSRC_SELECT | (1 << UCSZ1) | (1 << UCSZ0);
    /* enable serial receiver and transmitter */
#if !USE_SLEEP
    UCSRB = (1 << RXEN) | (1 << TXEN);
#else
    UCSRB = (1 << RXEN) | (1 << TXEN) | (1 << RXCIE);
#endif
/* Reset buffers */
  rx_buffer_head = 0;
  rx_buffer_tail = 0;
  tx_complete = TRUE;
}

void uart_putc(uint8_t c)
{
    if(c == '\n')
        uart_putc('\r');

    /* wait until transmit buffer is empty */
    while(!(UCSRA & (1 << UDRE)));

    /* send next byte */
    UDR = c;
}

void uart_putc_hex(uint8_t b)
{
    /* upper nibble */
    if((b >> 4) < 0x0a)
        uart_putc((b >> 4) + '0');
    else
        uart_putc((b >> 4) - 0x0a + 'a');

    /* lower nibble */
    if((b & 0x0f) < 0x0a)
        uart_putc((b & 0x0f) + '0');
    else
        uart_putc((b & 0x0f) - 0x0a + 'a');
}

void uart_putw_hex(uint16_t w)
{
    uart_putc_hex((uint8_t) (w >> 8));
    uart_putc_hex((uint8_t) (w & 0xff));
}

void uart_putdw_hex(uint32_t dw)
{
    uart_putw_hex((uint16_t) (dw >> 16));
    uart_putw_hex((uint16_t) (dw & 0xffff));
}

void uart_putw_dec(uint16_t w)
{
    uint16_t num = 10000;
    uint8_t started = 0;

    while(num > 0)
    {
        uint8_t b = w / num;
        if(b > 0 || started || num == 1)
        {
            uart_putc('0' + b);
            started = 1;
        }
        w -= b * num;

        num /= 10;
    }
}

void uart_putdw_dec(uint32_t dw)
{
    uint32_t num = 1000000000;
    uint8_t started = 0;

    while(num > 0)
    {
        uint8_t b = dw / num;
        if(b > 0 || started || num == 1)
        {
            uart_putc('0' + b);
            started = 1;
        }
        dw -= b * num;

        num /= 10;
    }
}

void uart_puts(const char* str)
{
    while(*str)
        uart_putc(*str++);
}

void uart_puts_p(PGM_P str)
{
    while(1)
    {
        uint8_t b = pgm_read_byte_near(str++);
        if(!b)
            break;

        uart_putc(b);
    }
}



// Returns true if recieve buffer is empty 
//
unsigned char uart_buffer_empty(void)
{
    return (UCSRA & (1 << RXC));
}


// Get char from buffer. 
// Note that this function BLOCKS until a char is recieved. 
//

unsigned char uart_getc(void) 
{
  unsigned char c;
  
  loop_until_bit_is_set(UCSR0A,RXC0);
  
  c = UDR;
  
  return c;
}

void padToBuffer(char* str)
{
    int len = strlen(str);
    int current = 0;
    
    while((len + current) < RX_BUFFER_SIZE)
    {
        str[(current + len)] = '0';
        current = current + 1;
    }
    
}

/*
uint8_t uart_getc()
{
    //wait until receive buffer is full 
#if USE_SLEEP
    uint8_t sreg = SREG;
    sei();

    while(!(UCSRA & (1 << RXC)))
        sleep_mode();

    SREG = sreg;
#else
    while(!(UCSRA & (1 << RXC)));
#endif

    uint8_t b = UDR;
    if(b == '\r')
        b = '\n';

    return b;
}

EMPTY_INTERRUPT(USART_RXC_vect)

*/
