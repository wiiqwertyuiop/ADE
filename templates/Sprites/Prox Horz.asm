;=========================================;
;Proximity (horizontal)		      
;A will have 1 if the sprite is in range
;Otherwise it's 0			     
;=========================================;

;Store the range to check from in 00, then jump to this routine.
;E.g.
;LDA #$12
;STA $00
;JSR Proximity

DirFix: db $FF,$00

Proximity:
	LDA $E4,x		;\
	SEC				; |
	SBC $94			; |
	PHA				; |
	JSR SUB_HORZ_POS	; | Check sprite range ..
	PLA				; |
	EOR DirFix,y		; |
	CMP $00			; | If Range > !Temp return.
	BCC +			; | If in RANGE.. branch.
	RTS				;/
+	LDA #$01
	RTS