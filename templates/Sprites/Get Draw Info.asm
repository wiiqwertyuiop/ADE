;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; GET_DRAW_INFO
; This is a helper for the graphics routine.  It sets off screen flags, and sets up
; variables.  It will return with the following:
;
;       Y = index to sprite OAM ($300)
;       $00 = sprite x position relative to screen boarder
;       $01 = sprite y position relative to screen boarder  
;
; It is adapted from the subroutine at $03B760
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

SPR_T1:              db $0C,$1C
SPR_T2:              db $01,$02

GET_DRAW_INFO:       STZ $186C,x             ; reset sprite offscreen flag, vertical
	STZ $15A0,x             ; reset sprite offscreen flag, horizontal
	LDA $E4,x               ; \
	CMP $1A                 ;  | set horizontal offscreen if necessary
	LDA $14E0,x             ;  |
	SBC $1B                 ;  |
	BEQ ON_SCREEN_X         ;  |
	INC $15A0,x             ; /

ON_SCREEN_X:         LDA $14E0,x             ; \
	XBA	 ;  |
	LDA $E4,x               ;  |
	REP #$20                ;  |
	SEC	 ;  |
	SBC $1A                 ;  | mark sprite invalid if far enough off screen
	CLC	 ;  |
	ADC.w #$0040            ;  |
	CMP.w #$0180            ;  |
	SEP #$20                ;  |
	ROL A                   ;  |
	AND #$01                ;  |
	STA $15C4,x             ; / 
	BNE INVALID             ; 
	
	LDY #$00                ; \ set up loop:
	LDA $1662,x             ;  | 
	AND #$20                ;  | if not smushed (1662 & 0x20), go through loop twice
	BEQ ON_SCREEN_LOOP      ;  | else, go through loop once
	INY	 ; / 
ON_SCREEN_LOOP:      LDA $D8,x               ; \ 
	CLC	 ;  | set vertical offscreen if necessary
	ADC SPR_T1,y            ;  |
	PHP	 ;  |
	CMP $1C                 ;  | (vert screen boundry)
	ROL $00                 ;  |
	PLP	 ;  |
	LDA $14D4,x             ;  | 
	ADC #$00                ;  |
	LSR $00                 ;  |
	SBC $1D                 ;  |
	BEQ ON_SCREEN_Y         ;  |
	LDA $186C,x             ;  | (vert offscreen)
	ORA SPR_T2,y            ;  |
	STA $186C,x             ;  |
ON_SCREEN_Y:         DEY	 ;  |
	BPL ON_SCREEN_LOOP      ; /

	LDY $15EA,x             ; get offset to sprite OAM
	LDA $E4,x               ; \ 
	SEC	 ;  | 
	SBC $1A                 ;  | $00 = sprite x position relative to screen boarder
	STA $00                 ; / 
	LDA $D8,x               ; \ 
	SEC	 ;  | 
	SBC $1C                 ;  | $01 = sprite y position relative to screen boarder
	STA $01                 ; / 
	RTS	 ; return

INVALID:             PLA	 ; \ return from *main gfx routine* subroutine...
	PLA	 ;  |    ...(not just this subroutine)
	RTS	 ; /