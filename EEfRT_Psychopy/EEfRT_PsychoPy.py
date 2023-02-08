#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Fri Jul 31 16:20:42 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('latest')


from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'EEfRT_PsychoPy'  # from the Builder filename that created this script
expInfo = {'Subject Number:': '', 'Handedness (r/l):': '', 'Include Practice Trials (y/n):': '', 'Session:': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expName, expInfo['Subject Number:'], expInfo['Session:'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/ehahn6/Desktop/eefrt_online/eefrt_online.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# timer for experiment
max_time = (60*20)

# Initialize components for Routine "Intro"
IntroClock = core.Clock()
handintro = 'In the next screen you will be prompted to press a key as quickly as you can with your non-dominant pinky.\n\nPress the S key if you are right handed, and the left key if you are left handed\n\nPress the space bar when ready.'

intro_text = visual.TextStim(win=win, name='intro_text',
    text='default text',
    font='Arial',
    units='pix', pos=(0, 0), height=36, wrapWidth=900, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
intro_key_resp = keyboard.Keyboard()

# Initialize components for Routine "maxpress"
maxpressClock = core.Clock()
from psychopy.hardware import keyboard
from psychopy import core
max_press_list= []
kb = keyboard.Keyboard()

#determine correct key based on dexterity
if expInfo['Handedness (r/l):'] == 'r':
    handmaxpress = 'Press "s" to fill up the bar.'
    handkeypress = 's'
elif expInfo['Handedness (r/l):'] == 'l':
    handmaxpress = 'Press "l" to fill up the bar.'
    handkeypress = 'l'


maxpress_fillbar = visual.Rect(
    win=win, name='maxpress_fillbar',units='pix', 
    width=(100, 400)[0], height=(100, 400)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
maxpress_text = visual.TextStim(win=win, name='maxpress_text',
    text='default text',
    font='Arial',
    units='pix', pos=(0, -300), height=36, wrapWidth=800, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='RTL',
    depth=-2.0);
maxpress_countdown = visual.TextStim(win=win, name='maxpress_countdown',
    text='default text',
    font='Arial',
    units='pix', pos=(250, 150), height=36, wrapWidth=150, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='RTL',
    depth=-3.0);
maxpress_fillbarshow = visual.Rect(
    win=win, name='maxpress_fillbarshow',units='pix', 
    width=(100, 0)[0], height=(100, 0)[1],
    ori=0, pos=(0, -200),
    lineWidth=1, lineColor=[-1,-1,-1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

# Initialize components for Routine "maxpress_break"
maxpress_breakClock = core.Clock()
break_text = visual.TextStim(win=win, name='break_text',
    text='Press the spacebar to continue',
    font='Arial',
    units='pix', pos=(0, 0), height=36, wrapWidth=500, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
break_keyresp = keyboard.Keyboard()

# Initialize components for Routine "instruct"
instructClock = core.Clock()
instruct_keyresp = keyboard.Keyboard()
right = []
left = []
instruct_imageshow = visual.ImageStim(
    win=win,
    name='instruct_imageshow', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "pracfixation"
pracfixationClock = core.Clock()
prac_fixation_cross = visual.ImageStim(
    win=win,
    name='prac_fixation_cross', 
    image='stim/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "pracchoice"
pracchoiceClock = core.Clock()
pracchoice_keyresp = keyboard.Keyboard()
prob = []
winlose = []
reward = []
choice = []
required_key = []
import random


pracchoice_text = visual.TextStim(win=win, name='pracchoice_text',
    text='default text',
    font='Arial',
    pos=(0, 0), height=36, wrapWidth=600, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "praceasy"
praceasyClock = core.Clock()
#correct keys by dexterity
if expInfo['Handedness (r/l):'] == 'r':
    easyhand = 'Push "l" until bar is full.'
    easy_handkeypress = 'l'
    hardhand = 'Push "s" until bar is full.'
    hard_handkeypress = 's'

if expInfo['Handedness (r/l):'] == 'l':
    easyhand = 'Push "s" until bar is full.'
    easy_handkeypress = 's'
    hardhand = 'Push "l" until bar is full.'
    hard_handkeypress = 'l'
praceasy_fillbar = visual.Rect(
    win=win, name='praceasy_fillbar',units='pix', 
    width=(100, 400)[0], height=(100, 400)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
praceasy_countdown = visual.TextStim(win=win, name='praceasy_countdown',
    text='default text',
    font='Arial',
    units='pix', pos=(250, 150), height=36, wrapWidth=150, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
praceasy_text = visual.TextStim(win=win, name='praceasy_text',
    text='default text',
    font='Arial',
    pos=(0, -300), height=36, wrapWidth=600, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
praceasy_fillbarshow = visual.Rect(
    win=win, name='praceasy_fillbarshow',units='pix', 
    width=(100, 0)[0], height=(100, 0)[1],
    ori=0, pos=(0,-200),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

# Initialize components for Routine "prachard"
prachardClock = core.Clock()
prachard_fillbar = visual.Rect(
    win=win, name='prachard_fillbar',units='pix', 
    width=(100, 400)[0], height=(100, 400)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
prachard_text = visual.TextStim(win=win, name='prachard_text',
    text='default text',
    font='Arial',
    units='pix', pos=(0, -300), height=36, wrapWidth=600, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
prachard_countdown = visual.TextStim(win=win, name='prachard_countdown',
    text='default text',
    font='Arial',
    units='pix', pos=(250, 150), height=36, wrapWidth=150, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
prachard_fillbarshow = visual.Rect(
    win=win, name='prachard_fillbarshow',units='pix', 
    width=(100, 0)[0], height=(100, 0)[1],
    ori=0, pos=(0, -200),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

# Initialize components for Routine "pracfeedback"
pracfeedbackClock = core.Clock()
prac_feedback_text = []
prac_feedback_show = visual.TextStim(win=win, name='prac_feedback_show',
    text='default text',
    font='Arial',
    pos=(0, 0), height=36, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "pracreward"
pracrewardClock = core.Clock()
prac_reward = []
prac_reward_reward = visual.TextStim(win=win, name='prac_reward_reward',
    text='default text',
    font='Arial',
    units='pix', pos=(0, 0), height=36, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instruct2"
instruct2Clock = core.Clock()
instruct2_text = visual.TextStim(win=win, name='instruct2_text',
    text='You have finished the practice trials.\nYou will now begin the actual trials.\n\nPress the spacebar to continue.',
    font='Arial',
    pos=(0, 0), height=36, wrapWidth=600, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instruct2_keyresp = keyboard.Keyboard()

# Initialize components for Routine "clock"
clockClock = core.Clock()

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_cross = visual.ImageStim(
    win=win,
    name='fixation_cross', 
    image='stim/fixation.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)


# Initialize components for Routine "choice"
choiceClock = core.Clock()
choice_keyresp = keyboard.Keyboard()
trial_choice = []
choiceRT = []
choice_textshow = visual.TextStim(win=win, name='choice_textshow',
    text='default text',
    font='Arial',
    pos=[0,0], height=36, wrapWidth=600, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "easy"
easyClock = core.Clock()
easy_fillbar = visual.Rect(
    win=win, name='easy_fillbar',units='pix', 
    width=(100, 400)[0], height=(100, 400)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
easy_countdown = visual.TextStim(win=win, name='easy_countdown',
    text='default text',
    font='Arial',
    units='pix', pos=(250, 150), height=36, wrapWidth=150, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
easy_text = visual.TextStim(win=win, name='easy_text',
    text='default text',
    font='Arial',
    units='pix', pos=(0, -300), height=36, wrapWidth=600, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
easy_fillbarshow = visual.Rect(
    win=win, name='easy_fillbarshow',units='pix', 
    width=(100, 0)[0], height=(100, 0)[1],
    ori=0, pos=(0, -200),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

# Initialize components for Routine "hard"
hardClock = core.Clock()
hard_fillbar = visual.Rect(
    win=win, name='hard_fillbar',units='pix', 
    width=(100, 400)[0], height=(100, 400)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
hard_text = visual.TextStim(win=win, name='hard_text',
    text='default text',
    font='Arial',
    units='pix', pos=(0, -300), height=36, wrapWidth=600, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
hard_countdown = visual.TextStim(win=win, name='hard_countdown',
    text='default text',
    font='Arial',
    units='pix', pos=(250, 150), height=36, wrapWidth=150, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
hard_fillbarshow = visual.Rect(
    win=win, name='hard_fillbarshow',units='pix', 
    width=(100,0)[0], height=(100,0)[1],
    ori=0, pos=(0, -200),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
feedback_text = []
trial_reward = []
feedback_text_show = visual.TextStim(win=win, name='feedback_text_show',
    text='default text',
    font='Arial',
    units='pix', pos=(0, 0), height=36, wrapWidth=600, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "reward"
rewardClock = core.Clock()
earnings = 0
import pandas as pd 
reward_reward = visual.TextStim(win=win, name='reward_reward',
    text='default text',
    font='Arial',
    units='pix', pos=(0, 0), height=36, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Intro"-------
# update component parameters for each repeat
intro_text.setText(handintro )
intro_key_resp.keys = []
intro_key_resp.rt = []
# keep track of which components have finished
IntroComponents = [intro_text, intro_key_resp]
for thisComponent in IntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
IntroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Intro"-------
while continueRoutine:
    # get current time
    t = IntroClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=IntroClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_text* updates
    if intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_text.frameNStart = frameN  # exact frame index
        intro_text.tStart = t  # local t and not account for scr refresh
        intro_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_text, 'tStartRefresh')  # time at next scr refresh
        intro_text.setAutoDraw(True)
    
    # *intro_key_resp* updates
    waitOnFlip = False
    if intro_key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_key_resp.frameNStart = frameN  # exact frame index
        intro_key_resp.tStart = t  # local t and not account for scr refresh
        intro_key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_key_resp, 'tStartRefresh')  # time at next scr refresh
        intro_key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(intro_key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if intro_key_resp.status == STARTED and not waitOnFlip:
        theseKeys = intro_key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Intro"-------
for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
maxpress_trials = data.TrialHandler(nReps=3, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='maxpress_trials')
thisExp.addLoop(maxpress_trials)  # add the loop to the experiment
thisMaxpress_trial = maxpress_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMaxpress_trial.rgb)
if thisMaxpress_trial != None:
    for paramName in thisMaxpress_trial:
        exec('{} = thisMaxpress_trial[paramName]'.format(paramName))

for thisMaxpress_trial in maxpress_trials:
    currentLoop = maxpress_trials
    # abbreviate parameter names if possible (e.g. rgb = thisMaxpress_trial.rgb)
    if thisMaxpress_trial != None:
        for paramName in thisMaxpress_trial:
            exec('{} = thisMaxpress_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "maxpress"-------
    routineTimer.add(21.000000)
    # update component parameters for each repeat
    #reset bar
    maxpress_fillbarshow.height = 0
    maxpress_fillbarshow.pos[1] = -200
    key_count = 0
    max_keys = 400
    maxpress_text.setText(handmaxpress)
    # keep track of which components have finished
    maxpressComponents = [maxpress_fillbar, maxpress_text, maxpress_countdown, maxpress_fillbarshow]
    for thisComponent in maxpressComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    maxpressClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "maxpress"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = maxpressClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=maxpressClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #move bar with key press
        rise_speed = 2
        key_press = kb.getKeys(handkeypress)
        if key_press:
            key_count = key_count + 1
            if key_count <= max_keys:
                maxpress_fillbarshow.height += rise_speed
                maxpress_fillbarshow.pos[1] += (rise_speed/2)
        
        #on-screen countdown
        countdown = round(21.0 - t, ndigits = 2)
        
        
        # *maxpress_fillbar* updates
        if maxpress_fillbar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            maxpress_fillbar.frameNStart = frameN  # exact frame index
            maxpress_fillbar.tStart = t  # local t and not account for scr refresh
            maxpress_fillbar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(maxpress_fillbar, 'tStartRefresh')  # time at next scr refresh
            maxpress_fillbar.setAutoDraw(True)
        if maxpress_fillbar.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > maxpress_fillbar.tStartRefresh + 21-frameTolerance:
                # keep track of stop time/frame for later
                maxpress_fillbar.tStop = t  # not accounting for scr refresh
                maxpress_fillbar.frameNStop = frameN  # exact frame index
                win.timeOnFlip(maxpress_fillbar, 'tStopRefresh')  # time at next scr refresh
                maxpress_fillbar.setAutoDraw(False)
        
        # *maxpress_text* updates
        if maxpress_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            maxpress_text.frameNStart = frameN  # exact frame index
            maxpress_text.tStart = t  # local t and not account for scr refresh
            maxpress_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(maxpress_text, 'tStartRefresh')  # time at next scr refresh
            maxpress_text.setAutoDraw(True)
        if maxpress_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > maxpress_text.tStartRefresh + 21-frameTolerance:
                # keep track of stop time/frame for later
                maxpress_text.tStop = t  # not accounting for scr refresh
                maxpress_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(maxpress_text, 'tStopRefresh')  # time at next scr refresh
                maxpress_text.setAutoDraw(False)
        
        # *maxpress_countdown* updates
        if maxpress_countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            maxpress_countdown.frameNStart = frameN  # exact frame index
            maxpress_countdown.tStart = t  # local t and not account for scr refresh
            maxpress_countdown.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(maxpress_countdown, 'tStartRefresh')  # time at next scr refresh
            maxpress_countdown.setAutoDraw(True)
        if maxpress_countdown.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > maxpress_countdown.tStartRefresh + 21-frameTolerance:
                # keep track of stop time/frame for later
                maxpress_countdown.tStop = t  # not accounting for scr refresh
                maxpress_countdown.frameNStop = frameN  # exact frame index
                win.timeOnFlip(maxpress_countdown, 'tStopRefresh')  # time at next scr refresh
                maxpress_countdown.setAutoDraw(False)
        if maxpress_countdown.status == STARTED:  # only update if drawing
            maxpress_countdown.setText(f'Time left: {str(countdown)}', log=False)
        
        # *maxpress_fillbarshow* updates
        if maxpress_fillbarshow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            maxpress_fillbarshow.frameNStart = frameN  # exact frame index
            maxpress_fillbarshow.tStart = t  # local t and not account for scr refresh
            maxpress_fillbarshow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(maxpress_fillbarshow, 'tStartRefresh')  # time at next scr refresh
            maxpress_fillbarshow.setAutoDraw(True)
        if maxpress_fillbarshow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > maxpress_fillbarshow.tStartRefresh + 21-frameTolerance:
                # keep track of stop time/frame for later
                maxpress_fillbarshow.tStop = t  # not accounting for scr refresh
                maxpress_fillbarshow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(maxpress_fillbarshow, 'tStopRefresh')  # time at next scr refresh
                maxpress_fillbarshow.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in maxpressComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "maxpress"-------
    for thisComponent in maxpressComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #avg max press
    max_press = key_count
    max_press_list.append(max_press)
    
    
    
    # ------Prepare to start Routine "maxpress_break"-------
    # update component parameters for each repeat
    break_keyresp.keys = []
    break_keyresp.rt = []
    #clear previous key queue
    break_keyresp.clearEvents()
    
    
    # keep track of which components have finished
    maxpress_breakComponents = [break_text, break_keyresp]
    for thisComponent in maxpress_breakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    maxpress_breakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "maxpress_break"-------
    while continueRoutine:
        # get current time
        t = maxpress_breakClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=maxpress_breakClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *break_text* updates
        if break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_text.frameNStart = frameN  # exact frame index
            break_text.tStart = t  # local t and not account for scr refresh
            break_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_text, 'tStartRefresh')  # time at next scr refresh
            break_text.setAutoDraw(True)
        
        # *break_keyresp* updates
        waitOnFlip = False
        if break_keyresp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            break_keyresp.frameNStart = frameN  # exact frame index
            break_keyresp.tStart = t  # local t and not account for scr refresh
            break_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_keyresp, 'tStartRefresh')  # time at next scr refresh
            break_keyresp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(break_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if break_keyresp.status == STARTED and not waitOnFlip:
            theseKeys = break_keyresp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in maxpress_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "maxpress_break"-------
    for thisComponent in maxpress_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "maxpress_break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 3 repeats of 'maxpress_trials'


# set up handler to look after randomisation of conditions etc
instructions = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cond/Instructions.xlsx'),
    seed=None, name='instructions')
thisExp.addLoop(instructions)  # add the loop to the experiment
thisInstruction = instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
if thisInstruction != None:
    for paramName in thisInstruction:
        exec('{} = thisInstruction[paramName]'.format(paramName))

for thisInstruction in instructions:
    currentLoop = instructions
    # abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
    if thisInstruction != None:
        for paramName in thisInstruction:
            exec('{} = thisInstruction[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instruct"-------
    # update component parameters for each repeat
    instruct_keyresp.keys = []
    instruct_keyresp.rt = []
    # keep track of which components have finished
    instructComponents = [instruct_keyresp, instruct_imageshow]
    for thisComponent in instructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "instruct"-------
    while continueRoutine:
        # get current time
        t = instructClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruct_keyresp* updates
        waitOnFlip = False
        if instruct_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruct_keyresp.frameNStart = frameN  # exact frame index
            instruct_keyresp.tStart = t  # local t and not account for scr refresh
            instruct_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_keyresp, 'tStartRefresh')  # time at next scr refresh
            instruct_keyresp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(instruct_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instruct_keyresp.status == STARTED and not waitOnFlip:
            theseKeys = instruct_keyresp.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        if expInfo['Include Practice Trials (y/n):'] == 'n':
            continueRoutine = False
        if expInfo['Handedness (r/l):'] == 'r':
            image_show = right
        else:
            image_show = left
           
        
        
        # *instruct_imageshow* updates
        if instruct_imageshow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruct_imageshow.frameNStart = frameN  # exact frame index
            instruct_imageshow.tStart = t  # local t and not account for scr refresh
            instruct_imageshow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruct_imageshow, 'tStartRefresh')  # time at next scr refresh
            instruct_imageshow.setAutoDraw(True)
        if instruct_imageshow.status == STARTED:  # only update if drawing
            instruct_imageshow.setImage(image_show, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruct"-------
    for thisComponent in instructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'instructions'


# set up handler to look after randomisation of conditions etc
prac_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cond/prac_conditions.xlsx'),
    seed=None, name='prac_trials')
thisExp.addLoop(prac_trials)  # add the loop to the experiment
thisPrac_trial = prac_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_trial.rgb)
if thisPrac_trial != None:
    for paramName in thisPrac_trial:
        exec('{} = thisPrac_trial[paramName]'.format(paramName))

for thisPrac_trial in prac_trials:
    currentLoop = prac_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial.rgb)
    if thisPrac_trial != None:
        for paramName in thisPrac_trial:
            exec('{} = thisPrac_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "pracfixation"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    pracfixationComponents = [prac_fixation_cross]
    for thisComponent in pracfixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pracfixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "pracfixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pracfixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pracfixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_fixation_cross* updates
        if prac_fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_fixation_cross.frameNStart = frameN  # exact frame index
            prac_fixation_cross.tStart = t  # local t and not account for scr refresh
            prac_fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_fixation_cross, 'tStartRefresh')  # time at next scr refresh
            prac_fixation_cross.setAutoDraw(True)
        if prac_fixation_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_fixation_cross.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                prac_fixation_cross.tStop = t  # not accounting for scr refresh
                prac_fixation_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prac_fixation_cross, 'tStopRefresh')  # time at next scr refresh
                prac_fixation_cross.setAutoDraw(False)
        if expInfo['Include Practice Trials (y/n):'] == 'n':
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracfixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pracfixation"-------
    for thisComponent in pracfixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "pracchoice"-------
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    pracchoice_keyresp.keys = []
    pracchoice_keyresp.rt = []
    #reset timeout
    timeout = 0
    # keep track of which components have finished
    pracchoiceComponents = [pracchoice_keyresp, pracchoice_text]
    for thisComponent in pracchoiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pracchoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "pracchoice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pracchoiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pracchoiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *pracchoice_keyresp* updates
        waitOnFlip = False
        if pracchoice_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracchoice_keyresp.frameNStart = frameN  # exact frame index
            pracchoice_keyresp.tStart = t  # local t and not account for scr refresh
            pracchoice_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracchoice_keyresp, 'tStartRefresh')  # time at next scr refresh
            pracchoice_keyresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(pracchoice_keyresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(pracchoice_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if pracchoice_keyresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracchoice_keyresp.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                pracchoice_keyresp.tStop = t  # not accounting for scr refresh
                pracchoice_keyresp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pracchoice_keyresp, 'tStopRefresh')  # time at next scr refresh
                pracchoice_keyresp.status = FINISHED
        if pracchoice_keyresp.status == STARTED and not waitOnFlip:
            theseKeys = pracchoice_keyresp.getKeys(keyList=['s', 'l'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if pracchoice_keyresp.keys == []:  # then this was the first keypress
                    pracchoice_keyresp.keys = theseKeys.name  # just the first key pressed
                    pracchoice_keyresp.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
        if expInfo['Include Practice Trials (y/n):'] == 'n':
            continueRoutine = False
        
        # *pracchoice_text* updates
        if pracchoice_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            pracchoice_text.frameNStart = frameN  # exact frame index
            pracchoice_text.tStart = t  # local t and not account for scr refresh
            pracchoice_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pracchoice_text, 'tStartRefresh')  # time at next scr refresh
            pracchoice_text.setAutoDraw(True)
        if pracchoice_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > pracchoice_text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                pracchoice_text.tStop = t  # not accounting for scr refresh
                pracchoice_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(pracchoice_text, 'tStopRefresh')  # time at next scr refresh
                pracchoice_text.setAutoDraw(False)
        if pracchoice_text.status == STARTED:  # only update if drawing
            pracchoice_text.setText(f'The easy task is worth: $1.00 \n\n The hard task is worth: ${str(reward)} \n\n The probability of winning is {str(prob)}%', log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracchoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pracchoice"-------
    for thisComponent in pracchoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if pracchoice_keyresp.keys in ['', [], None]:  # No response was made
        pracchoice_keyresp.keys = None
    prac_trials.addData('pracchoice_keyresp.keys',pracchoice_keyresp.keys)
    if pracchoice_keyresp.keys != None:  # we had a response
        prac_trials.addData('pracchoice_keyresp.rt', pracchoice_keyresp.rt)
    #add prac choice and required key press info to datafile
    #coinflip for easy or hard if timeout
    
    prac_choice = pracchoice_keyresp.keys
    if prac_choice == hard_handkeypress:
            choice = 'hard'
            required_key = 98
    if prac_choice == easy_handkeypress:
            choice = 'easy'
            required_key = 30
    if not prac_choice:
        timeout = 1
        coin_flip = round(random.random())
        if coin_flip == 1:
            choice = 'hard'
            required_key = 98
        if coin_flip == 0:
            choice = 'easy'
            required_key = 30
    
    #calc avg max press
    average_max_press = round(((max_press_list[0]+max_press_list[1]+max_press_list[2])/3),0)
    thisExp.addData('average_max_press', average_max_press)
    
    
    # ------Prepare to start Routine "praceasy"-------
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    #reset bar
    praceasy_fillbarshow.height = 0
    praceasy_fillbarshow.pos[1] = -200
    prachard_fillbarshow.height = 0
    prachard_fillbarshow.pos[1] = -200
    key_count = 0
    completed = 0
    
    
    
    # keep track of which components have finished
    praceasyComponents = [praceasy_fillbar, praceasy_countdown, praceasy_text, praceasy_fillbarshow]
    for thisComponent in praceasyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    praceasyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "praceasy"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = praceasyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=praceasyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #skip if hard choice, if none use coin flip
        if expInfo['Include Practice Trials (y/n):'] == 'n':
            continueRoutine = False
        if choice == 'hard':
            continueRoutine = False
        
        #move bar with key press
        key_press = kb.getKeys(easy_handkeypress)
        if key_press:
                key_count = key_count + 1
                if key_count < 31:
                    praceasy_fillbarshow.height += 400/30
                    praceasy_fillbarshow.pos[1] += (((400/30))/2)
                if key_count >= 30:
                    completed = 1
                    continueRoutine = False
        
        #on-screen countdown
        countdown = round(7.0 - t, ndigits = 2)
        
        
        # *praceasy_fillbar* updates
        if praceasy_fillbar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            praceasy_fillbar.frameNStart = frameN  # exact frame index
            praceasy_fillbar.tStart = t  # local t and not account for scr refresh
            praceasy_fillbar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(praceasy_fillbar, 'tStartRefresh')  # time at next scr refresh
            praceasy_fillbar.setAutoDraw(True)
        if praceasy_fillbar.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > praceasy_fillbar.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                praceasy_fillbar.tStop = t  # not accounting for scr refresh
                praceasy_fillbar.frameNStop = frameN  # exact frame index
                win.timeOnFlip(praceasy_fillbar, 'tStopRefresh')  # time at next scr refresh
                praceasy_fillbar.setAutoDraw(False)
        
        # *praceasy_countdown* updates
        if praceasy_countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            praceasy_countdown.frameNStart = frameN  # exact frame index
            praceasy_countdown.tStart = t  # local t and not account for scr refresh
            praceasy_countdown.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(praceasy_countdown, 'tStartRefresh')  # time at next scr refresh
            praceasy_countdown.setAutoDraw(True)
        if praceasy_countdown.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > praceasy_countdown.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                praceasy_countdown.tStop = t  # not accounting for scr refresh
                praceasy_countdown.frameNStop = frameN  # exact frame index
                win.timeOnFlip(praceasy_countdown, 'tStopRefresh')  # time at next scr refresh
                praceasy_countdown.setAutoDraw(False)
        if praceasy_countdown.status == STARTED:  # only update if drawing
            praceasy_countdown.setText(f'Time left: {str(countdown)}', log=False)
        
        # *praceasy_text* updates
        if praceasy_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            praceasy_text.frameNStart = frameN  # exact frame index
            praceasy_text.tStart = t  # local t and not account for scr refresh
            praceasy_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(praceasy_text, 'tStartRefresh')  # time at next scr refresh
            praceasy_text.setAutoDraw(True)
        if praceasy_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > praceasy_text.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                praceasy_text.tStop = t  # not accounting for scr refresh
                praceasy_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(praceasy_text, 'tStopRefresh')  # time at next scr refresh
                praceasy_text.setAutoDraw(False)
        if praceasy_text.status == STARTED:  # only update if drawing
            praceasy_text.setText(easyhand, log=False)
        
        # *praceasy_fillbarshow* updates
        if praceasy_fillbarshow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            praceasy_fillbarshow.frameNStart = frameN  # exact frame index
            praceasy_fillbarshow.tStart = t  # local t and not account for scr refresh
            praceasy_fillbarshow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(praceasy_fillbarshow, 'tStartRefresh')  # time at next scr refresh
            praceasy_fillbarshow.setAutoDraw(True)
        if praceasy_fillbarshow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > praceasy_fillbarshow.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                praceasy_fillbarshow.tStop = t  # not accounting for scr refresh
                praceasy_fillbarshow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(praceasy_fillbarshow, 'tStopRefresh')  # time at next scr refresh
                praceasy_fillbarshow.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in praceasyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "praceasy"-------
    for thisComponent in praceasyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "prachard"-------
    routineTimer.add(21.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    prachardComponents = [prachard_fillbar, prachard_text, prachard_countdown, prachard_fillbarshow]
    for thisComponent in prachardComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    prachardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "prachard"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = prachardClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prachardClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #skip if easy choice
        if expInfo['Include Practice Trials (y/n):'] == 'n':
            continueRoutine = False
        if choice == 'easy':
            continueRoutine = False
        
        #move bar with keypress
        key_press = kb.getKeys(hard_handkeypress)
        if key_press:
                key_count = key_count + 1
                if key_count < 99:
                    prachard_fillbarshow.height += 400/98
                    prachard_fillbarshow.pos[1] += ((400/98)/2)
        #determine if completed
                if key_count >= 98:
                    completed = 1
                    continueRoutine = False
        
        #on-screen countdown
        countdown = round(21.0 - t, ndigits = 2)
        
        
        # *prachard_fillbar* updates
        if prachard_fillbar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prachard_fillbar.frameNStart = frameN  # exact frame index
            prachard_fillbar.tStart = t  # local t and not account for scr refresh
            prachard_fillbar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prachard_fillbar, 'tStartRefresh')  # time at next scr refresh
            prachard_fillbar.setAutoDraw(True)
        if prachard_fillbar.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prachard_fillbar.tStartRefresh + 21-frameTolerance:
                # keep track of stop time/frame for later
                prachard_fillbar.tStop = t  # not accounting for scr refresh
                prachard_fillbar.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prachard_fillbar, 'tStopRefresh')  # time at next scr refresh
                prachard_fillbar.setAutoDraw(False)
        
        # *prachard_text* updates
        if prachard_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prachard_text.frameNStart = frameN  # exact frame index
            prachard_text.tStart = t  # local t and not account for scr refresh
            prachard_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prachard_text, 'tStartRefresh')  # time at next scr refresh
            prachard_text.setAutoDraw(True)
        if prachard_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prachard_text.tStartRefresh + 21-frameTolerance:
                # keep track of stop time/frame for later
                prachard_text.tStop = t  # not accounting for scr refresh
                prachard_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prachard_text, 'tStopRefresh')  # time at next scr refresh
                prachard_text.setAutoDraw(False)
        if prachard_text.status == STARTED:  # only update if drawing
            prachard_text.setText(hardhand, log=False)
        
        # *prachard_countdown* updates
        if prachard_countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prachard_countdown.frameNStart = frameN  # exact frame index
            prachard_countdown.tStart = t  # local t and not account for scr refresh
            prachard_countdown.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prachard_countdown, 'tStartRefresh')  # time at next scr refresh
            prachard_countdown.setAutoDraw(True)
        if prachard_countdown.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prachard_countdown.tStartRefresh + 21-frameTolerance:
                # keep track of stop time/frame for later
                prachard_countdown.tStop = t  # not accounting for scr refresh
                prachard_countdown.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prachard_countdown, 'tStopRefresh')  # time at next scr refresh
                prachard_countdown.setAutoDraw(False)
        if prachard_countdown.status == STARTED:  # only update if drawing
            prachard_countdown.setText(f'Time left: {str(countdown)}', log=False)
        
        # *prachard_fillbarshow* updates
        if prachard_fillbarshow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prachard_fillbarshow.frameNStart = frameN  # exact frame index
            prachard_fillbarshow.tStart = t  # local t and not account for scr refresh
            prachard_fillbarshow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prachard_fillbarshow, 'tStartRefresh')  # time at next scr refresh
            prachard_fillbarshow.setAutoDraw(True)
        if prachard_fillbarshow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prachard_fillbarshow.tStartRefresh + 21-frameTolerance:
                # keep track of stop time/frame for later
                prachard_fillbarshow.tStop = t  # not accounting for scr refresh
                prachard_fillbarshow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prachard_fillbarshow, 'tStopRefresh')  # time at next scr refresh
                prachard_fillbarshow.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prachardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prachard"-------
    for thisComponent in prachardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "pracfeedback"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    pracfeedbackComponents = [prac_feedback_show]
    for thisComponent in pracfeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pracfeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "pracfeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pracfeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pracfeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if expInfo['Include Practice Trials (y/n):'] == 'n':
            continueRoutine = False
            
            #display feedback
        if completed == 1:
            prac_feedback_text = 'You completed the task!'
        if completed == 0:
            prac_feedback_text = 'You failed to complete the task.'
        
        # *prac_feedback_show* updates
        if prac_feedback_show.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_feedback_show.frameNStart = frameN  # exact frame index
            prac_feedback_show.tStart = t  # local t and not account for scr refresh
            prac_feedback_show.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_feedback_show, 'tStartRefresh')  # time at next scr refresh
            prac_feedback_show.setAutoDraw(True)
        if prac_feedback_show.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_feedback_show.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                prac_feedback_show.tStop = t  # not accounting for scr refresh
                prac_feedback_show.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prac_feedback_show, 'tStopRefresh')  # time at next scr refresh
                prac_feedback_show.setAutoDraw(False)
        if prac_feedback_show.status == STARTED:  # only update if drawing
            prac_feedback_show.setText(prac_feedback_text, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracfeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pracfeedback"-------
    for thisComponent in pracfeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "pracreward"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    #pick correct reward by winlose/choice
    if completed == 1:
        if winlose == 'w':
            if choice == 'hard':
                prac_reward = f'You won: ${reward}' %(reward)
            if choice == 'easy':
                prac_reward = 'You won: $1.00'
        if winlose == 'l':
            prac_reward = 'No money this trial'
    prac_reward_reward.setText(prac_reward)
    # keep track of which components have finished
    pracrewardComponents = [prac_reward_reward]
    for thisComponent in pracrewardComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pracrewardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "pracreward"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pracrewardClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pracrewardClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #skip if not reward
        if expInfo['Include Practice Trials (y/n):'] == 'n':
            continueRoutine = False
        if completed == 0:
            continueRoutine = False
        
        # *prac_reward_reward* updates
        if prac_reward_reward.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            prac_reward_reward.frameNStart = frameN  # exact frame index
            prac_reward_reward.tStart = t  # local t and not account for scr refresh
            prac_reward_reward.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_reward_reward, 'tStartRefresh')  # time at next scr refresh
            prac_reward_reward.setAutoDraw(True)
        if prac_reward_reward.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_reward_reward.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                prac_reward_reward.tStop = t  # not accounting for scr refresh
                prac_reward_reward.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prac_reward_reward, 'tStopRefresh')  # time at next scr refresh
                prac_reward_reward.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pracrewardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pracreward"-------
    for thisComponent in pracrewardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1 repeats of 'prac_trials'


# ------Prepare to start Routine "instruct2"-------
# update component parameters for each repeat
instruct2_keyresp.keys = []
instruct2_keyresp.rt = []
# keep track of which components have finished
instruct2Components = [instruct2_text, instruct2_keyresp]
for thisComponent in instruct2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instruct2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "instruct2"-------
while continueRoutine:
    # get current time
    t = instruct2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instruct2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct2_text* updates
    if instruct2_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct2_text.frameNStart = frameN  # exact frame index
        instruct2_text.tStart = t  # local t and not account for scr refresh
        instruct2_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct2_text, 'tStartRefresh')  # time at next scr refresh
        instruct2_text.setAutoDraw(True)
    
    # *instruct2_keyresp* updates
    waitOnFlip = False
    if instruct2_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruct2_keyresp.frameNStart = frameN  # exact frame index
        instruct2_keyresp.tStart = t  # local t and not account for scr refresh
        instruct2_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruct2_keyresp, 'tStartRefresh')  # time at next scr refresh
        instruct2_keyresp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instruct2_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instruct2_keyresp.status == STARTED and not waitOnFlip:
        theseKeys = instruct2_keyresp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruct2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct2"-------
for thisComponent in instruct2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruct2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "clock"-------
# update component parameters for each repeat
#create loopClock
loopClock = core.Clock() 
# keep track of which components have finished
clockComponents = []
for thisComponent in clockComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
clockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "clock"-------
while continueRoutine:
    # get current time
    t = clockClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=clockClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in clockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "clock"-------
for thisComponent in clockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "clock" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('cond/trial_conditions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation"-------
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [fixation_cross]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "fixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixationClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixationClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross* updates
        if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.tStart = t  # local t and not account for scr refresh
            fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(True)
        if fixation_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_cross.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                fixation_cross.tStop = t  # not accounting for scr refresh
                fixation_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_cross, 'tStopRefresh')  # time at next scr refresh
                fixation_cross.setAutoDraw(False)
        #if max time is reached, end loop
        if loopClock.getTime() > max_time:
                continueRoutine = False
                trials.finished = True
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "choice"-------
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    choice_keyresp.keys = []
    choice_keyresp.rt = []
    #reset timeout
    timeout = 0
    
    # keep track of which components have finished
    choiceComponents = [choice_keyresp, choice_textshow]
    for thisComponent in choiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    choiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "choice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = choiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=choiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *choice_keyresp* updates
        waitOnFlip = False
        if choice_keyresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_keyresp.frameNStart = frameN  # exact frame index
            choice_keyresp.tStart = t  # local t and not account for scr refresh
            choice_keyresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_keyresp, 'tStartRefresh')  # time at next scr refresh
            choice_keyresp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(choice_keyresp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(choice_keyresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if choice_keyresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > choice_keyresp.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                choice_keyresp.tStop = t  # not accounting for scr refresh
                choice_keyresp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(choice_keyresp, 'tStopRefresh')  # time at next scr refresh
                choice_keyresp.status = FINISHED
        if choice_keyresp.status == STARTED and not waitOnFlip:
            theseKeys = choice_keyresp.getKeys(keyList=['s', 'l'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if choice_keyresp.keys == []:  # then this was the first keypress
                    choice_keyresp.keys = theseKeys.name  # just the first key pressed
                    choice_keyresp.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
        #if max time is reached, end loop
        if loopClock.getTime() > max_time:
                continueRoutine = False
                trials.finished = True
        
        # *choice_textshow* updates
        if choice_textshow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            choice_textshow.frameNStart = frameN  # exact frame index
            choice_textshow.tStart = t  # local t and not account for scr refresh
            choice_textshow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_textshow, 'tStartRefresh')  # time at next scr refresh
            choice_textshow.setAutoDraw(True)
        if choice_textshow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > choice_textshow.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                choice_textshow.tStop = t  # not accounting for scr refresh
                choice_textshow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(choice_textshow, 'tStopRefresh')  # time at next scr refresh
                choice_textshow.setAutoDraw(False)
        if choice_textshow.status == STARTED:  # only update if drawing
            choice_textshow.setPos((0,0), log=False)
            choice_textshow.setText(f'The easy task is worth: $1.00 \n\n The hard task is worth: ${str(reward)} \n\n The probability of winning is {str(prob)}%', log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "choice"-------
    for thisComponent in choiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if choice_keyresp.keys in ['', [], None]:  # No response was made
        choice_keyresp.keys = None
    trials.addData('choice_keyresp.keys',choice_keyresp.keys)
    if choice_keyresp.keys != None:  # we had a response
        trials.addData('choice_keyresp.rt', choice_keyresp.rt)
    #add choice and required key press info to datafile
    #coinflip for easy or hard if timeout
    trial_choice = choice_keyresp.keys
    choiceRT = choice_keyresp.rt
    if trial_choice == hard_handkeypress:
            choice = 'hard'
            required_key = 98
    if trial_choice == easy_handkeypress:
            choice = 'easy'
            required_key = 30
    if not trial_choice:
        timeout = 1
        coin_flip = round(random.random())
        if coin_flip == 1:
            choice = 'hard'
            required_key = 98
        if coin_flip == 0:
            choice = 'easy'
            required_key = 30
        
    thisExp.addData('timeout', timeout)
    thisExp.addData('choice', choice)
    thisExp.addData('required_presses', required_key)
    thisExp.addData('average_max_press', average_max_press)
    thisExp.addData('choiceRT',choiceRT)
    
    
    
    
    # ------Prepare to start Routine "easy"-------
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    #reset bar
    easy_fillbarshow.height = 0
    easy_fillbarshow.pos[1] = -200
    hard_fillbarshow.height = 0
    hard_fillbarshow.pos[1] = -200
    key_count = 0
    completed = 0
    easy_text.setText(easyhand)
    # keep track of which components have finished
    easyComponents = [easy_fillbar, easy_countdown, easy_text, easy_fillbarshow]
    for thisComponent in easyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    easyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "easy"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = easyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=easyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #if max time is reached, end loop
        if loopClock.getTime() > max_time:
                continueRoutine = False
                trials.finished = True
        
        #skip if hard trial
        if choice == 'hard':
                continueRoutine = False
        
        #move bar with key press
        key_press = kb.getKeys(easy_handkeypress)
        if key_press:
                key_count = key_count + 1
                if key_count < 31:
                    easy_fillbarshow.height += 400/30
                    easy_fillbarshow.pos[1] += (((400/30))/2)
        #determine if completed
                if key_count >= 30:
                    completed = 1
                    continueRoutine = False
        
        #add data
        thisExp.addData('actual_presses', key_count)
        thisExp.addData('completed', completed)
        
        #on-screen countdown
        countdown = round(7.0 - t, ndigits = 2)
        
        # *easy_fillbar* updates
        if easy_fillbar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            easy_fillbar.frameNStart = frameN  # exact frame index
            easy_fillbar.tStart = t  # local t and not account for scr refresh
            easy_fillbar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(easy_fillbar, 'tStartRefresh')  # time at next scr refresh
            easy_fillbar.setAutoDraw(True)
        if easy_fillbar.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > easy_fillbar.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                easy_fillbar.tStop = t  # not accounting for scr refresh
                easy_fillbar.frameNStop = frameN  # exact frame index
                win.timeOnFlip(easy_fillbar, 'tStopRefresh')  # time at next scr refresh
                easy_fillbar.setAutoDraw(False)
        
        # *easy_countdown* updates
        if easy_countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            easy_countdown.frameNStart = frameN  # exact frame index
            easy_countdown.tStart = t  # local t and not account for scr refresh
            easy_countdown.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(easy_countdown, 'tStartRefresh')  # time at next scr refresh
            easy_countdown.setAutoDraw(True)
        if easy_countdown.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > easy_countdown.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                easy_countdown.tStop = t  # not accounting for scr refresh
                easy_countdown.frameNStop = frameN  # exact frame index
                win.timeOnFlip(easy_countdown, 'tStopRefresh')  # time at next scr refresh
                easy_countdown.setAutoDraw(False)
        if easy_countdown.status == STARTED:  # only update if drawing
            easy_countdown.setText(f'Time left: {str(countdown)}', log=False)
        
        # *easy_text* updates
        if easy_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            easy_text.frameNStart = frameN  # exact frame index
            easy_text.tStart = t  # local t and not account for scr refresh
            easy_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(easy_text, 'tStartRefresh')  # time at next scr refresh
            easy_text.setAutoDraw(True)
        if easy_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > easy_text.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                easy_text.tStop = t  # not accounting for scr refresh
                easy_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(easy_text, 'tStopRefresh')  # time at next scr refresh
                easy_text.setAutoDraw(False)
        
        # *easy_fillbarshow* updates
        if easy_fillbarshow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            easy_fillbarshow.frameNStart = frameN  # exact frame index
            easy_fillbarshow.tStart = t  # local t and not account for scr refresh
            easy_fillbarshow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(easy_fillbarshow, 'tStartRefresh')  # time at next scr refresh
            easy_fillbarshow.setAutoDraw(True)
        if easy_fillbarshow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > easy_fillbarshow.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                easy_fillbarshow.tStop = t  # not accounting for scr refresh
                easy_fillbarshow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(easy_fillbarshow, 'tStopRefresh')  # time at next scr refresh
                easy_fillbarshow.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in easyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "easy"-------
    for thisComponent in easyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "hard"-------
    routineTimer.add(21.000000)
    # update component parameters for each repeat
    hard_text.setText(hardhand)
    # keep track of which components have finished
    hardComponents = [hard_fillbar, hard_text, hard_countdown, hard_fillbarshow]
    for thisComponent in hardComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    hardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "hard"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = hardClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=hardClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #if max time is reached, end loop
        if loopClock.getTime() > max_time:
                continueRoutine = False
                trials.finished = True
        
        #skip if easy trial
        if choice == 'easy':
            continueRoutine = False
        
        #move bar with key press
        key_press = kb.getKeys(hard_handkeypress)
        if key_press:
                key_count = key_count + 1
                if key_count < 99:
                    hard_fillbarshow.height += 400/98
                    hard_fillbarshow.pos[1] += ((400/98)/2)
                if key_count >= 98:
                    completed = 1
                    continueRoutine = False
        
        #add data
        thisExp.addData('actual_presses', key_count)
        thisExp.addData('completed', completed)
        
        #on-screen countdown
        countdown = round(21.0 - t, ndigits = 2)
        
        
        # *hard_fillbar* updates
        if hard_fillbar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hard_fillbar.frameNStart = frameN  # exact frame index
            hard_fillbar.tStart = t  # local t and not account for scr refresh
            hard_fillbar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hard_fillbar, 'tStartRefresh')  # time at next scr refresh
            hard_fillbar.setAutoDraw(True)
        if hard_fillbar.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hard_fillbar.tStartRefresh + 21-frameTolerance:
                # keep track of stop time/frame for later
                hard_fillbar.tStop = t  # not accounting for scr refresh
                hard_fillbar.frameNStop = frameN  # exact frame index
                win.timeOnFlip(hard_fillbar, 'tStopRefresh')  # time at next scr refresh
                hard_fillbar.setAutoDraw(False)
        
        # *hard_text* updates
        if hard_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hard_text.frameNStart = frameN  # exact frame index
            hard_text.tStart = t  # local t and not account for scr refresh
            hard_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hard_text, 'tStartRefresh')  # time at next scr refresh
            hard_text.setAutoDraw(True)
        if hard_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hard_text.tStartRefresh + 21-frameTolerance:
                # keep track of stop time/frame for later
                hard_text.tStop = t  # not accounting for scr refresh
                hard_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(hard_text, 'tStopRefresh')  # time at next scr refresh
                hard_text.setAutoDraw(False)
        
        # *hard_countdown* updates
        if hard_countdown.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hard_countdown.frameNStart = frameN  # exact frame index
            hard_countdown.tStart = t  # local t and not account for scr refresh
            hard_countdown.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hard_countdown, 'tStartRefresh')  # time at next scr refresh
            hard_countdown.setAutoDraw(True)
        if hard_countdown.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hard_countdown.tStartRefresh + 21-frameTolerance:
                # keep track of stop time/frame for later
                hard_countdown.tStop = t  # not accounting for scr refresh
                hard_countdown.frameNStop = frameN  # exact frame index
                win.timeOnFlip(hard_countdown, 'tStopRefresh')  # time at next scr refresh
                hard_countdown.setAutoDraw(False)
        if hard_countdown.status == STARTED:  # only update if drawing
            hard_countdown.setText(f'Time left: {str(countdown)}', log=False)
        
        # *hard_fillbarshow* updates
        if hard_fillbarshow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            hard_fillbarshow.frameNStart = frameN  # exact frame index
            hard_fillbarshow.tStart = t  # local t and not account for scr refresh
            hard_fillbarshow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(hard_fillbarshow, 'tStartRefresh')  # time at next scr refresh
            hard_fillbarshow.setAutoDraw(True)
        if hard_fillbarshow.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > hard_fillbarshow.tStartRefresh + 21-frameTolerance:
                # keep track of stop time/frame for later
                hard_fillbarshow.tStop = t  # not accounting for scr refresh
                hard_fillbarshow.frameNStop = frameN  # exact frame index
                win.timeOnFlip(hard_fillbarshow, 'tStopRefresh')  # time at next scr refresh
                hard_fillbarshow.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in hardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "hard"-------
    for thisComponent in hardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "feedback"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    #display feedback
    if completed == 1:
        feedback_text = 'You completed the task!'
    if completed == 0:
        feedback_text = 'You failed to complete the task.'
    feedback_text_show.setText(feedback_text)
    # keep track of which components have finished
    feedbackComponents = [feedback_text_show]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #if max time is reached, end loop
        if loopClock.getTime() > max_time:
                continueRoutine = False
                trials.finished = True
        
        # *feedback_text_show* updates
        if feedback_text_show.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text_show.frameNStart = frameN  # exact frame index
            feedback_text_show.tStart = t  # local t and not account for scr refresh
            feedback_text_show.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text_show, 'tStartRefresh')  # time at next scr refresh
            feedback_text_show.setAutoDraw(True)
        if feedback_text_show.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text_show.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text_show.tStop = t  # not accounting for scr refresh
                feedback_text_show.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_text_show, 'tStopRefresh')  # time at next scr refresh
                feedback_text_show.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # ------Prepare to start Routine "reward"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    #pick correct reward by winlose/choice
    if completed == 1:
        if winlose == 'w':
            if choice == 'hard':
                trial_reward = f'You won: ${reward}' %(reward)
                earnings = reward
            if choice == 'easy':
                trial_reward = 'You won: $1.00'
                earnings = 1.00
        if winlose == 'l':
            trial_reward = 'No money this trial'
            earnings = 0
    if completed == 0:
        earnings = 0
    
    thisExp.addData('earnings', earnings)
    
    # keep track of which components have finished
    rewardComponents = [reward_reward]
    for thisComponent in rewardComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rewardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "reward"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = rewardClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rewardClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #if max time is reached, end loop
        if loopClock.getTime() > max_time:
                continueRoutine = False
                trials.finished = True
        
        #skip if not reward
        if completed == 0:
            continueRoutine = False
        
        
        # *reward_reward* updates
        if reward_reward.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reward_reward.frameNStart = frameN  # exact frame index
            reward_reward.tStart = t  # local t and not account for scr refresh
            reward_reward.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reward_reward, 'tStartRefresh')  # time at next scr refresh
            reward_reward.setAutoDraw(True)
        if reward_reward.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > reward_reward.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                reward_reward.tStop = t  # not accounting for scr refresh
                reward_reward.frameNStop = frameN  # exact frame index
                win.timeOnFlip(reward_reward, 'tStopRefresh')  # time at next scr refresh
                reward_reward.setAutoDraw(False)
        if reward_reward.status == STARTED:  # only update if drawing
            reward_reward.setText(trial_reward, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rewardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "reward"-------
    for thisComponent in rewardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')


#payment calc
data = pd.read_csv(filename + '.csv')
complete_hard_wins = data.loc[(data.winlose == 'w') & (data.choice == 'hard') & (data.completed == 1)]
rewards = list(complete_hard_wins.reward)
if len(rewards) == 0:
    tot = 1
else:
    tot = random.choice(rewards) + random.choice(rewards)
with open(filename + '_reward.txt', "w") as text_file:
    text_file.write(str(tot))
    
#new dataFile
cleandata = data[['trial', 'choice', 'choiceRT', 'actual_presses', 'required_presses', 'completed', 'timeout', 'winlose', 'reward', 'prob', 'average_max_press', 'earnings']]
file = open(filename+'.csv',"r+")
file.truncate(0)
file.close()
cleandata.to_csv(filename+'.csv', index=False)
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
