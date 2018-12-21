	LDA $0A 		;\
	AND #$F0 	;| Update the position
	STA $9A 		;| of the block
	LDA $0B 		;| so it doesn't shatter
	STA $9B 		;| where the players at
	LDA $0C 		;|
	AND #$F0 	;|
	STA $98 		;|
	LDA $0D 		;|
	STA $99 		;/

	LDA #$02 	; Replace block with blank tile
	STA $9C
	JSL $00BEB0

	PHB
	LDA #$02
	PHA
	PLB
	LDA #$00 	;set to 0 for normal explosion, 1 for rainbow (throw blocks)
	JSL $028663 	;breaking effect
	PLB
