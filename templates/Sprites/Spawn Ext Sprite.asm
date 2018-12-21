;Spawn an extended sprite.
;!ExSpriteNumber being the sprite number.
GenExtra:
	LDY #$07
ExtraLoop:
	LDA $170B,y
	BEQ Extra1
	DEY
	BPL ExtraLoop
	RTS
Extra1:
	LDA #!ExSpriteNumber
	STA $170B,y
	LDA $E4,x
	STA $171F,y
	LDA $14E0,x
	STA $1733,y
	LDA $D8,x
	STA $1715,y
	LDA $14D4,x
	STA $1729,y
	LDA #!ExSpriteYSpeed
	STA $173D,y
	LDA #!ExSpriteXSpeed
	STA $1747,y
	LDA #$FF
	STA $176F,y
	RTS
