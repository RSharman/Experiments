#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.64.00), May 31, 2011, at 11:39
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""
from numpy import * #many different maths functions
from numpy.random import * #maths randomisation functions
import os #handy system and path functions
from psychopy import core, data, event, visual, gui
import psychopy.log #import like this so it doesn't interfere with numpy.log

#User-defined variables = [u'Gabor', 'Instructions', 'Intro', 'key_resp', 'key_resp_2', 'trial', u'trials']
known_name_collisions = None  #(collisions are bad)

#store info about the experiment
expName='StairTest'#from the Builder filename that created this script
expInfo={'participant':'', 'session':'001'}
dlg=gui.DlgFromDict(dictionary=expInfo,title=expName)
if dlg.OK==False: core.quit() #user pressed cancel
expInfo['date']=data.getDateStr()#add a simple timestamp
expInfo['expName']=expName
#setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data') #if this fails (e.g. permissions) we will get error
filename='data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
psychopy.log.console.setLevel(psychopy.log.warning)#this outputs to the screen, not a file
logFile=psychopy.log.LogFile(filename+'.log', level=psychopy.log.EXP)

#setup the Window
win = visual.Window(size=[1024, 768], fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb')

#Initialise components for routine:Intro
IntroClock=core.Clock()
Instructions=visual.TextStim(win=win, ori=0,
    text=u'Some Instructions, press some buttons\n\nPress any key to continue',
    font=u'Arial',
    pos=[0, 0], height=0.1,
    color=u'white', colorSpace=u'rgb')

#set up handler to look after randomisation of trials etc
trials=data.StairHandler(startVal=0.5, extraInfo=expInfo,
    stepSizes=asarray([0.8,0.8,0.4,0.4,0.2]), stepType=u'log',
    nReversals=0, nTrials=50, 
    nUp=1, nDown=3)
level=thisTrial=0.5#initialise some vals

#Initialise components for routine:trial
trialClock=core.Clock()
Gabor=visual.PatchStim(win=win, tex=u'sin', mask=u'gauss',
    ori=0, pos=[0, 0], size=[0.5, 0.5], sf=level, phase=0.0,
    color=[1,1,1], colorSpace=u'rgb',
    texRes=128, interpolate=False)

#update component parameters for each repeat
key_resp = event._BuilderKeyResponse() #create an object of type KeyResponse

#run the trial
continueIntro=True
t=0; IntroClock.reset()
while continueIntro and (t<1000000.0000):
    #get current time
    t=IntroClock.getTime()
    
    #update/draw components on each frame
    if (0.0 <= t < (0.0+1.0)):
        Instructions.draw()
    if (0.0 <= t):
        if key_resp.clockNeedsReset:
            key_resp.clock.reset() # now t=0
            key_resp.clockNeedsReset = False
        theseKeys = event.getKeys()
        if len(theseKeys)>0:#at least one key was pressed
            key_resp.keys=theseKeys[-1]#just the last key pressed
            key_resp.rt = key_resp.clock.getTime()
            #abort routine on response
            continueIntro=False
    
    #check for quit (the [Esc] key)
    if event.getKeys(["escape"]): core.quit()
    #refresh the screen
    win.flip()

#end of this routine (e.g. trial)

for thisTrial in trials:
    level=thisTrial
    
    #update component parameters for each repeat
    key_resp_2 = event._BuilderKeyResponse() #create an object of type KeyResponse
    
    #run the trial
    continueTrial=True
    t=0; trialClock.reset()
    while continueTrial and (t<1000000.0000):
        #get current time
        t=trialClock.getTime()
        
        #update/draw components on each frame
        if (0.0 <= t < (0.0+1.0)):
            Gabor.draw()
        if (0.0 <= t):
            theseKeys = event.getKeys(keyList=u'["left","right"]')
            if len(theseKeys)>0:#at least one key was pressed
                key_resp_2.keys=theseKeys[-1]#just the last key pressed
                #was this 'correct'?
                if (key_resp_2.keys==str(u'left')): key_resp_2.corr=1
                else: key_resp_2.corr=0
                #abort routine on response
                continueTrial=False
        
        #check for quit (the [Esc] key)
        if event.getKeys(["escape"]): core.quit()
        #refresh the screen
        win.flip()
    
    #end of this routine (e.g. trial)
    if len(key_resp_2.keys)>0:#we had a response
        trials.addData(key_resp_2.corr)

#staircase completed

trials.saveAsPickle(filename+'trials')
trials.saveAsExcel(filename+'.xlsx', sheetName='trials')

#Shutting down:
win.close()
core.quit()
