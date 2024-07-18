# initialize block variable to store user input
# set height to 0
# declare variable to hold needed blocks and set to 1
# while loop to handle adding layers to the pyramid
# subtract needed block from block(-=)
# increment height by 1 to  increase pyramid height
# increment counter for needed blocks to account for extra layer
# outside the loop, print current height of the pyramid

block = int(input("Enter number of available blocks: "))
height = 0
neededBlock = 1

while block >= neededBlock:
    block -= neededBlock
    height += 1
    neededBlock += 1
print("Height of the pyramid is:", height)