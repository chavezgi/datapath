lw_test:
	nop
	li $sp, 0xf800
	li $s0, 5
	lw $s1, 0($s0)

bne_test:
	nop
	li $s0, 1
	li $s1, 1
	bne $s0, $s1, beq_test
	nop
	li $s1, 0
	bne $s0, $s1, beq_test
	nop
	add $s2, $s1, $s0
beq_test:
	nop
	li $s0, 5
	li $s1, 3
	beq $s0, $s1, jump_test
	nop
	li $s1, 5
	beq $s0, $s1, jump_test
	nop
	add $s1, $s1, $s1
	add $s1, $s1, $s1
	
jump_test:
	nop
	j bne_test   	 #jump to subi
	nop	
sub_test:
  li $t0, 3          # Load a 3 into $t0                                        
  sub $s1, $s0, $s0  # Store $s0 - $s0 into $s1  ($s1 = 0)                      
  sub $s2, $s0, $s1  # Store $s0 - $s1 into $s2  ($s2 = 3)                      
  li  $s0, 1         # Load a 1 to $s0                                          
  sub $s1, $s2, $s0  # Store $s2 - $s0 into $s1  ($s1 = 2)  

