'''
https://www.codewars.com/kata/51fda2d95d6efda45e00004e
4 kyu
'''
class User:
    #define maximum rank
    MAXRANK = 8
    #create dictionary with rankings and "score"
    LEVELS = {-8:1,-7:2,-6:3,-5:4,-4:5,-3:6,-2:7,-1:8,
             1:9,2:10,3:11,4:12,5:13,6:14,7:15,8:16}
    
    #initialize class
    def __init__(self,rank=-8):
        self.rank = rank
        self.progress = 0
        
    #return current rank    
    def rank(self):
        return self.rank
    
    #return current progress
    def progress(self):
        return self.progress
    
    
    #apply progress based on completed activity and rank up based on progress
    def inc_progress(self,activity_level):
        #check for valid activity level
        if activity_level not in User.LEVELS:
            raise Error
        #check if user is already max rank
        if self.rank == User.MAXRANK:
            return
          
        #print("Starting Rank:",self.rank)
        #print("Activity Level: ",activity_level)
        
        #apply points when activity is greater than user level
        if User.LEVELS[activity_level] > User.LEVELS[self.rank]:
            #print ("Activity higher than rank.")
            #print ("Starting progress ",self.progress)
            self.progress += 10 *  (User.LEVELS[activity_level] - User.LEVELS[self.rank]) **2
            #print ("Ending progress ",self.progress)
            
        #apply points when activity is less than user level
        elif User.LEVELS[activity_level] < User.LEVELS[self.rank]:
            #print ("Activity lower than rank.")
            #print ("Starting progress ",self.progress)
            if (User.LEVELS[self.rank] - User.LEVELS[activity_level]) == 1:
                self.progress += 1
                #print ("Ending progress ",self.progress)
            else:
                #print ("Activity too low.")
                pass
            
        #apply points when activity is equal user level    
        elif User.LEVELS[activity_level] == User.LEVELS[self.rank]:
            #print ("Activity equals rank.")
            #print ("Starting progress ",self.progress)
            self.progress += 3
            #print ("Ending progress ",self.progress)
        
        #check if current progress warrants a rank up
        #print ("Checking progress...")
        while self.progress >= 100:
            #print ("Current progress ",self.progress)
            self.progress -= 100
            #if rank is -1, skip 0 and go to 1
            if self.rank == -1:
                self.rank += 2
                #print("New Rank ",self.rank)
                #print("New Progress ",self.progress)
            else:
                self.rank += 1
                #print("New Rank ",self.rank)
                #print("New Progress ",self.progress)
            if self.rank == User.MAXRANK:
                self.progress = 0
                #print("Max rank reach.")
                break
        #print("Ending Rank:",self.rank)