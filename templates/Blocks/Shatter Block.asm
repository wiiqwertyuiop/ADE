	LDA #$02
	STA $9C
	JSL $00BEB0
	PHB
	LDA #$02
	PHA
	PLB
	LDA #$00             ; Set to 01 for rainbow explosion.
	JSL $028663
	PLB