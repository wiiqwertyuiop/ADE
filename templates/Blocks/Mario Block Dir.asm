	LDA $77
	AND #$01
	BNE Left
	AND #$04
	BNE Right
MarioSide:
	LDA $9A
	AND #$08
	BNE Right
Left:
	;[Left code here]
	RTL
Right:
	;[Right code here]
	RTL