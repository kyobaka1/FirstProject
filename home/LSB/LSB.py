#!/usr/bin/env python
# coding:UTF-8
from .StegAudio import AudioLSB,makeNewAudioFile


def Encode(urlout,file_in):
    in_audio = AudioLSB(file_in)
    file_out = urlout
    message = "COPYRIGHT Doan Ngoc Vuong - Steganography Final Project"
    data = in_audio.hideMes(message)
    makeNewAudioFile(file_out,in_audio.params,data)
def Decode(file_in):
    in_audio = AudioLSB(file_in)
    message = in_audio.getMes()
    return message