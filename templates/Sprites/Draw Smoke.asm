DrawSmoke:
	LDY #$03
-
	LDA $17C0,y
	BEQ +
	DEY
	BPL -
	RTS
+
	LDA #$01
	STA $17C0,y
	LDA #$1C     
	STA $17CC,y
	LDA $D8,x
	STA $17C4,y
	LDA $E4,x
	STA $17C8,y
	RTS