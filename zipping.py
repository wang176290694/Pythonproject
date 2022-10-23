import threading
import time
import numpy as np
import pygame as pg
from moviepy.decorators import convert_masks_to_RGB, requires_duration
import moviepy.video.io.preview as vp
import ctypes
pg.init()
pg.display.set_caption('MoviePy')
def defe(event):
    pass
class BreakLoop(Exception):
    def __init__(self):
        self.value = 0
    def __str__(self):
        return repr(self.value)
def breakplay():
    raise BreakLoop
import inspect
import asyncio
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    try:
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            # pass
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")
    except Exception as err:
        print(err)
@requires_duration
@convert_masks_to_RGB
def preview(clip, fps=15, audio=True, audio_fps=22050, audio_buffersize=3000,
            audio_nbytes=2, fullscreen=False,eventa=defe):
    """ 
    Displays the clip in a window, at the given frames per second
    (of movie) rate. It will avoid that the clip be played faster
    than normal, but it cannot avoid the clip to be played slower
    than normal if the computations are complex. In this case, try
    reducing the ``fps``.
    
    Parameters
    ------------
    
    fps
      Number of frames per seconds in the displayed video.
        
    audio
      ``True`` (default) if you want the clip's audio be played during
      the preview.
        
    audio_fps
      The frames per second to use when generating the audio sound.
      
    fullscreen
      ``True`` if you want the preview to be displayed fullscreen.
      
    """
    if fullscreen:
        flags = pg.FULLSCREEN
    else:
        flags = 0
    
    # compute and splash the first image
    screen = pg.display.set_mode(clip.size, flags)
    
    audio = audio and (clip.audio is not None)
    
    if audio:
        # the sound will be played in parrallel. We are not
        # parralellizing it on different CPUs because it seems that
        # pygame and openCV already use several cpus it seems.
        
        # two synchro-flags to tell whether audio and video are ready
        videoFlag = threading.Event()
        audioFlag = threading.Event()
        # launch the thread
        audiothread = threading.Thread(target=clip.audio.preview,
                                       args=(audio_fps,
                                             audio_buffersize,
                                             audio_nbytes,
                                             audioFlag, videoFlag))
        audiothread.start()
    
    img = clip.get_frame(0)
    vp.imdisplay(img, screen)
    if audio:  # synchronize with audio
        videoFlag.set()  # say to the audio: video is ready
        audioFlag.wait()  # wait for the audio to be ready
    
    result = []
    
    t0 = time.time()
    for t in np.arange(1.0 / fps, clip.duration-.001, 1.0 / fps):
        
        img = clip.get_frame(t)
        try:
            for event in pg.event.get():
                eventa(event)
        except BreakLoop:
            _async_raise(audiothread.ident, SystemExit)
            break
        t1 = time.time()
        time.sleep(max(0, t - (t1-t0)))
        vp.imdisplay(img, screen)
