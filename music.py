import winsound
import sys


def msc_intro():
    winsound.PlaySound("intro2.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )


def msc_intro2():
    winsound.PlaySound("intro1.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

def msc_boss1():
    winsound.PlaySound("music/boss1.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )

