

#ifndef UART_H
#define UART_H

#include <stdint.h>
#include <avr/pgmspace.h>


/* some mcus have multiple uarts */
#ifdef UDR0
#define UBRRH UBRR0H
#define UBRRL UBRR0L
#define UDR UDR0

#define UCSRA UCSR0A
#define UDRE UDRE0
#define RXC RXC0

#define UCSRB UCSR0B
#define RXEN RXEN0
#define TXEN TXEN0
#define RXCIE RXCIE0

#define UCSRC UCSR0C
#define URSEL
#define UCSZ0 UCSZ00
#define UCSZ1 UCSZ01
#define UCSRC_SELECT 0
#else
#define UCSRC_SELECT (1 << URSEL)
#endif

#ifndef USART_RXC_vect
#if defined(UART0_RX_vect)
#define USART_RXC_vect UART0_RX_vect
#elif defined(UART_RX_vect)
#define USART_RXC_vect UART_RX_vect
#elif defined(USART0_RX_vect)
#define USART_RXC_vect USART0_RX_vect
#elif defined(USART_RX_vect)
#define USART_RXC_vect USART_RX_vect
#elif defined(USART0_RXC_vect)
#define USART_RXC_vect USART0_RXC_vect
#elif defined(USART_RXC_vect)
#define USART_RXC_vect USART_RXC_vect
#else
#error "Uart receive complete interrupt not defined!"
#endif
#endif

#define BAUD 9600ul
#define UBRRVAL ((F_CPU/(BAUD<<4))-1)
//#define UBRRVAL 412UL
#define USE_SLEEP 1


/* Recieve buffer size */
#define RX_BUFFER_SIZE 60
/* Increase ring buffer macro: */
#define INC_RING(var, bsize) if (var == ((bsize)-1)) var=0; else var++

#ifndef TRUE
#define TRUE 1
#endif
#ifndef FALSE
#define FALSE 0
#endif


void uart_init();

void uart_putc(uint8_t c);

void uart_putc_hex(uint8_t b);
void uart_putw_hex(uint16_t w);
void uart_putdw_hex(uint32_t dw);

void uart_putw_dec(uint16_t w);
void uart_putdw_dec(uint32_t dw);

void uart_puts(const char* str);
void uart_puts_p(PGM_P str);

uint8_t uart_getc();
unsigned char uart_buffer_empty(void);


#endif

