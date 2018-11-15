import assembler
import pips

# The instruction decorator tells the assembler to create a new syntax rule for add instructions.
# The "#" spots indicate operands, which are passed in as parameters to the function below.
# The second parameter indicates the number of instructions this rule will create (1 in this case)
@assembler.instruction('add #, #, #', 1)
def add(dest, operand1, operand2):
  return pips.rformat(opcode='add', r0=dest, r1=operand1, r2=operand2)

# Encode an addi instruction
@assembler.instruction('addi #, #, #', 1)
def addi(dest, op1, immediate):
  return pips.iformat(opcode='add', r0=dest, r1=op1, imm=immediate)
  
# Encode the li pseudoinstruction using an addition to zero
@assembler.instruction('li #, #', 1)
def li(dest, immediate):
  return addi(dest, '$zero', immediate)

#Encode the subi instruction
@assembler.instruction('subi #, #, #', 1)
def subi(dest, op1, immediate):
  return pips.iformat(opcode='sub', r0=dest, r1=op1, imm=immediate)

#Encode the sub instruction
@assembler.instruction('sub #, #, #', 1)
def sub(dest, op1, op2):
  return pips.rformat(opcode='sub', r0=dest, r1=op1, r2=op2)

#Encode the nop instruction
@assembler.instruction('nop', 1)
def nop():
  return addi('$zero', '$zero', 0)

#Encode the and instruction
@assembler.instruction('and #, #, #', 1)
def andd(dest, operand1, operand2):
  return pips.rformat(opcode='and', r0=dest, r1=operand1, r2=operand2)

#Encode the andi instruction
@assembler.instruction('andi #, #, #', 1)
def andi(dest, operand1, immediate):
  return pips.iformat(opcode='and', r0=dest, r1=operand1, imm=immediate)

#Encode the or instruction
@assembler.instruction('or #, #, #', 1)
def orr(dest, operand1, operand2):
  return pips.rformat(opcode='or', r0=dest, r1=operand1, r2=operand2)

#Encode the ori instruction
@assembler.instruction('ori #, #, #', 1)
def ori(dest, operand1, immediate):
  return pips.iformat(opcode='or', r0=dest, r1=operand1, imm=immediate)

#Encode the nand instruction
@assembler.instruction('nand #, #, #', 1)
def nand(dest, operand1, operand2):
  return pips.rformat(opcode='nand', r0=dest, r1=operand1, r2=operand2)

#Encode the nandi instruction
@assembler.instruction('nandi #, #, #', 1)
def nandi(dest, operand1, immediate):
  return pips.iformat(opcode='nand', r0=dest, r1=operand1, imm=immediate)

#Encode the nor instruction
@assembler.instruction('nor #, #, #', 1)
def nor(dest, operand1, operand2):
  return pips.rformat(opcode='nor', r0=dest, r1=operand1, r2=operand2)

#Encode the nori instruction
@assembler.instruction('nori #, #, #', 1)
def nori(dest, operand1, immediate):
  return pips.iformat(opcode='nor', r0=dest, r1=operand1, imm=immediate)

#Encode the xor instruction
@assembler.instruction('xor #, #, #', 1)
def xor(dest, operand1, operand2):
  return pips.rformat(opcode='xor', r0=dest, r1=operand1, r2=operand2)

#Encode the xori instruction
@assembler.instruction('xori #, #, #', 1)
def xori(dest, operand1, immediate):
  return pips.iformat(opcode='xor', r0=dest, r1=operand1, imm=immediate)

#Encode the slt instruction
@assembler.instruction('slt #, #, #', 1)
def slt(dest, operand1, operand2):
  return pips.rformat(opcode='slt', r0=dest, r1=operand1, r2=operand2)

#Encode the slti instruction
@assembler.instruction('slti #, #, #', 1)
def slti(dest, operand1, immediate):
  return pips.iformat(opcode='slt', r0=dest, r1=operand1, imm=immediate)

#Encode the sltu instruction
@assembler.instruction('sltu #, #, #', 1)
def sltu(dest, operand1, operand2):
  return pips.rformat(opcode='sltu', r0=dest, r1=operand1, r2=operand2)

#Encode the sltui instruction
@assembler.instruction('sltui #, #, #', 1)
def sltui(dest, operand1, immediate):
  return pips.iformat(opcode='sltu', r0=dest, r1=operand1, imm=immediate)
  
#Encode the j instruction
@assembler.instruction('j #', 1)
def j(dest):
  return pips.iformat(opcode='j', r0='$zero', r1='$zero', imm=dest)
  
#Encode the jal instruction
@assembler.instruction('jal #', 1)
def jal(dest):
  return pips.iformat(opcode='j', link=True, r0='$ra', r1='$zero', imm=dest)  

#Encode the jr instruction
@assembler.instruction('jr #', 1)
def jr(dest):
  return pips.rformat(opcode='j', link=True, r0='$zero', r1='$zero', r2=dest)
    
#Encode the beq instruction
@assembler.instruction('beq #, #, #', 1)
def beq(operand1, operand2, dest):
  return pips.iformat(opcode='beq', r0= operand1, r1= operand2, imm=dest)
  
#Encode the bne instruction
@assembler.instruction('bne #, #, #', 1)
def beq(operand1, operand2, dest):
  return pips.iformat(opcode='bne', r0= operand1, r1= operand2, imm=dest)  
    
#Encode the lw instruction
@assembler.instruction('lb #, #', 1)
def lb(dest, immediate):
  return pips.iformat(opcode='lb', r0=dest, r1= '$sp', imm=immediate)
       
#Encode the lw instruction
@assembler.instruction('lw #, #', 1)
def lw(dest, immediate):
  return pips.iformat(opcode='lw', r0=dest, r1= immediate, imm=immediate) 

#Encode the sw instruction
#@assembler.instruction('sw #, #', 1)
#def sw(dest, immediate):
#  return pips.iformat(opcode='sw', r0=dest, r1= '$sp', imm=immediate)   
