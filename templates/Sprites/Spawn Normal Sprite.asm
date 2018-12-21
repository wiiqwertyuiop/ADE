	;Spawn a normal sprite.
	;Replace !SpriteNumber with the number of the sprite.
	LDA $186C,x
	BNE EndSpawn
	JSL $02A9DE
	BMI EndSpawn
	LDA #$01
	STA $14C8,y
	LDA #!SpriteNumber
	STA $009E,y
	LDA $E4,x
	STA $00E4,y
	LDA $14E0,x
	STA $14E0,y
	LDA $D8,x
	STA $00D8,y
	LDA $14D4,x
	STA $14D4,y
	PHX
	TYX
	JSL $07F7D2
	PLX
EndSpawn:
	RTS
