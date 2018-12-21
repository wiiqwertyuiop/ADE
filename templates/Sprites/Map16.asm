
<!-- saved from url=(0041)http://bin.smwcentral.net/u/845/Map16.txt -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1"></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">LDA $E4,x           ; Get X low position of sprite
STA $02             ; store into $02
LDA $14E0,X         ;
STA $03	
LDA $D8,x           ; Get y low position of sprite
STA $00             ; Store into $00
LDA $14D4,x         ; Get y hi
STA $01             ; Store into $01
LDA $00                   
AND #$F0                
STA $06                   
LDA $02                   
LSR                       
LSR                       
LSR                       
LSR                                              
ORA $06                   
PHA                      
LDA $5B     
AND #$01                
BEQ CODE_01D977           
PLA                       
LDX $01                   
CLC                       
ADC $00BA80,X       
STA $05                   
LDA $00BABC,X       
ADC $03                   
STA $06                   
BRA CODE_01D989           

CODE_01D977
PLA                       
LDX $03                   
CLC                       
ADC.l $00BA60,X       
STA $05                   
LDA.l $00BA9C,x       
ADC $01                   
STA $06                   

CODE_01D989
LDA.b #$7E                
STA $07                   
LDX $15E9
; [$05] now contains the Map16 tile number. To access it, do LDA [$05]. This will load the low byte.
; To check a 16-bit Map16 value, do:
; LDA [$05]
; XBA
; INC $07
; LDA [$05]
; XBA
; REP #$20
; A now contains the 16-bit Map16 tile number that the sprite is touching.</pre></body></html>