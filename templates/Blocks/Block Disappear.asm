	LDA #$02 	; Replace block with block # 1E6
	STA $9C
	JSL $00BEB0 	; Make the block disappear.