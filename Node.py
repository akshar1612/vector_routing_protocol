#Akshar Patel 200561850 pate6185 and Devarsh Patwa 190417940 patw7940
from common import *

class Node:
    def __init__(self, ID, networksimulator, costs):
        self.myID = ID
        self.ns = networksimulator
        num = self.ns.NUM_NODES        
        self.distanceTable = [[0 for i in range(num)] for j in range(num)]
        self.routes = [i for i in range(num)]
        
        #loop through 0 to nums
        for nums_1 in range(num):
            #second loop through 0 to num
            for nums_2 in range(num):
                #compare nums
                if nums_1 != nums_2:
                    #set table at index [num_1][num_2] to ns.infin
                    self.distanceTable[nums_1][nums_2] = self.ns.INFINITY
                else:
                    #set to 0
                    self.distanceTable[nums_1][nums_2] = 0
            #compare num1 to id and costs at index num1 to ns.infin        
            if((nums_1 != self.myID) and (costs[nums_1] != self.ns.INFINITY)):
                #make packet
                packet = RTPacket(self.myID, nums_1, costs)
                self.ns.tolayer2(packet)

        self.distanceTable[self.myID] = costs

    def recvUpdate(self, pkt):
       
       self.distanceTable[pkt.sourceid] = pkt.mincosts
       #set a new variable 
       cstchnd = False
        
        #loop through range 0 to num nodes
       for nds in range(self.ns.NUM_NODES):
           #set new variable to table index
           distInti = self.distanceTable[self.myID][pkt.sourceid]
           
           #INNER loop through 0 to nodes
           for nds_2 in range(self.ns.NUM_NODES):
               #set new variable to index of table
               dis_rw = self.distanceTable[pkt.sourceid][nds_2]
               #set new variable to index of table
               cstcurr = self.distanceTable[self.myID][nds_2]
                #comapre node2, id and check if distInti + is less than cst
               if( (nds_2 != self.myID) and (distInti + dis_rw < cstcurr) ):
                   self.distanceTable[self.myID][nds_2] = distInti + dis_rw
                   self.routes[nds_2] = self.routes[pkt.sourceid]
                   #change cstchnd to true
                   cstchnd = True
       #check cst             
       if(cstchnd == True):
           for nds in range(self.ns.NUM_NODES):
               if (nds != self.myID and self.routes[nds] != self.ns.INFINITY):
                   new_packet = RTPacket(self.myID, nds, self.distanceTable[self.myID])
                   self.ns.tolayer2(new_packet)
        
       return 
    
    def printdt(self):
        print("   D"+str(self.myID)+" |  ", end="")
        for i in range(self.ns.NUM_NODES):
            print("{:3d}   ".format(i), end="")
        print()
        print("  ----|-", end="")
        for i in range(self.ns.NUM_NODES):            
            print("------", end="")
        print()    
        for i in range(self.ns.NUM_NODES):
            print("     {}|  ".format(i), end="" )
            
            for j in range(self.ns.NUM_NODES):
                print("{:3d}   ".format(self.distanceTable[i][j]), end="" )
            print()            
        print()
        
