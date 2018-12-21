;==================;
;Proximity Vertical;
;==================;

;Store the proximity range to 02 and then all this routine, 00 is returned if it's not in range while 01 is returned if it's in range.

ProxVert:
	STA $02
	LDA $D8,x		;\
	SEC				; |
	SBC $96			; |
	PHA				; |
	JSR SUB_VERT_POS		; | Check sprite range ..
	PLA				; |
	EOR DirFix,y		; |
	CMP $02			; | ; If Range > !Temp return. 
	BCS +			; |
	LDA #$01			; | A = #$01.
	RTS				; |
+	LDA #$00			; | A = #$00 if not in range.
	RTS				;/
