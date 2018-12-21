	LDA $186C,x
	BNE EndSpawn
	JSL $02A9DE
	BMI EndSpawn
	LDA #$01				; Sprite state ($14C8,x).
	STA $14C8,y
	PHX
	TYX
	LDA #!SpriteNumber	; This the sprite number to spawn.
	STA $7FAB9E,x
	PLX
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
	JSL $0187A7
	LDA #$08
	STA $7FAB10,x
	PLX
EndSpawn:
	RTS

