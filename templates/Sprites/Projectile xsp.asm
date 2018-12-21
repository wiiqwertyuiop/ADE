;AXY = 8-bit.
!Type = $1747		;$1747 = Extended sprites,
			;$B6 = Regular sprites.
			;$182C = Minor extended sprites.

		STZ $00	;initialize scratch RAM
		LDA $76
		CLC
		ROR A
		ROR A
		EOR $7B
		BPL +
		LDA $7B
		STA $00
+		LDA #$10
		LDY $76
		BNE +
		EOR #$FF
		INC A
+		CLC
		ADC $00
		STA !Type,x;Store into somespritetype's X speed