	LDA #$15
	STA $1887	; shake the ground
	LDA #$0D		;/
	STA $9E,x	;\ Sprite = Bob-omb.
	LDA #$08		;/
	STA $14C8,x	;\ Set status for new sprite.
	JSL $07F7D2	;/ Reset sprite tables (sprite becomes bob-omb)..
	LDA #$01		;\ .. and flag explosion status.
	STA $1534,x	;/
	LDA #$40		;\ Time for explosion.
	STA $1540,x
	LDA #$09		;\
	STA $1DFC	;/ Sound effect.
	LDA #$1B
	STA $167A,x
	RTS
