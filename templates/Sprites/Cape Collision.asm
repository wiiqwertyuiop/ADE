;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;Spinning Cape Contact Routine by Bio(mostly ripped from the original wich start at $93BE);
;If contact is found, $01 is returned, if it isn't, $00 is returned                       ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
SCCR
                     LDA $13E8
		     BEQ SCCRNOCONTACT
                     LDA $15D0,x
                     ORA $154C,x
                     ORA $1FE2,x
                     BNE SCCRNOCONTACT
                     LDA $1632,x
                     PHY    
                     LDY $74  
                     BEQ SCCRLABEL1
                     EOR #$01  
SCCRLABEL1           PLY   
                     EOR $13F9 
                     BNE SCCRNOCONTACT
                     JSL $03B69F
                     LDA $13E9
                     SEC         
                     SBC #$02               
                     STA $00   
                     LDA $13EA  
                     SBC #$00             
                     STA $08    
                     LDA #$14          
                     STA $02    
                     LDA $13EB 
                     STA $01    
                     LDA $13EC  
                     STA $09    
                     LDA #$10       
                     STA $03
SCCRFINNISH          JSL $03B72B
                     BCC SCCRNOCONTACT
                     LDA #$01
		     RTS
SCCRNOCONTACT       
                     LDA #$00
		     RTS