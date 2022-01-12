import os
import argparse

from mido import MidiFile
import keyboard

import time

# define octave interval
octave_interval = 12

# pitch scoping
c3_pitch = 48
c5_pitch = 72
b5_pitch = 83

# setting note table
keytable = "z?x?cv?b?n?m" + "a?s?df?g?h?j" + "q?w?er?t?y?u"
notetable = "C?D?EF?G?A?B"

# define playing state
play_state = 'idle'


# convert pitch to notename
def note_name(pitch):
    # octave cycle
    pitch_index = pitch % octave_interval

    # out of range
    if pitch_index < 0:
        return '-'

    # get note from note table
    pre = notetable[pitch_index]

    # sharp note
    if pre == '?':
        pre = notetable[pitch_index - 1] + '#'

    # return note name
    return pre + str(pitch // octave_interval - 1)


# check note is playble
def midi_playable(event):
    if event.is_meta or event.type != 'note_on':
        return False
    return True


# find best shifting pitch
def find_best_shift(midi_data):
    # define counter
    note_counter = [0] * octave_interval
    octave_list = [0] * 11

    for event in midi_data:
        # skip unplayble event
        if not midi_playable(event):
            continue

        # loop for all octave
        for i in range(octave_interval):
            note_pitch = (event.note + i) % octave_interval
            # pitch in sharp
            if keytable[note_pitch] != '?':
                note_counter[i] += 1
                note_octave = (event.note + i) // octave_interval
                octave_list[note_octave] += 1

    max_note = max(range(len(note_counter)), key=note_counter.__getitem__)
    shifting = 0
    counter = 0
    # index = 0

    # calculate shifting by find max note cluster
    for i in range(len(octave_list) - 3):
        amount = sum(octave_list[i: i + 3])

        if amount > counter:
            counter = amount
            shifting = i

    return int(max_note + (4 - shifting) * octave_interval)


# play function
def play(midi, shifting):
    global play_state

    # set play state to playing
    play_state = 'playing'
    print('Start playing')

    for event in midi:
        # check playing state
        if play_state != 'playing':
            break

        # waiting
        time.sleep(event.time)

        # skip unplayable note
        if not midi_playable(event):
            continue

        # add shifting to note
        pitch = event.note + shifting

        # set original note
        original_pitch = pitch

        # pitch is lower than c3
        if pitch < c3_pitch:
            print(f"Pitch {note_name(pitch)} is lower than C3")

            # try to octave cycle pitch
            pitch = pitch % octave_interval + c3_pitch

        # pitch is higher than b5
        elif pitch > b5_pitch:
            print(f"Pitch {note_name(pitch)} is higher than B5")

            # try to octave cycle pitch
            pitch = pitch % octave_interval + c5_pitch

        # out of range -> skip
        if pitch < c3_pitch or pitch > b5_pitch:
            print('skip this note')
            continue

        key_press = keytable[pitch - c3_pitch]

        print(
            f"original key: {note_name(original_pitch)}({original_pitch}) Play key: {note_name(pitch)}({pitch}) Press: {key_press.upper()}\n")

        # keyboard press
        keyboard.send(key_press)


# keyboard control function
def control(*args):
    global play_state

    # pause
    if play_state == 'playing':
        play_state = 'pause'

    # play again
    elif play_state == 'idle':
        keyboard.call_later(play, args=args, delay=1)


# main function
if __name__ == '__main__':
    # get midi path from arg
    parser = argparse.ArgumentParser(
        description='MIDI file auto player with Lyre in Genshin Imapct')

    parser.add_argument('midi', nargs="?", type=str, help='path to midi file')

    args = parser.parse_args()

    midi = args.midi

    # default midi path
    if not midi:
        midi = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), 'files/endless_love.mid')

    # read midi file
    midi = MidiFile(midi)

    # get best shifting pitch
    shifting = find_best_shift(midi)

    # inform controller key
    print("Press '\\' to play/pause, and press 'backspace' to exit.\n")

    # define play/pause key
    keyboard.add_hotkey('\\', lambda: control(midi, shifting),
                        suppress=True, trigger_on_release=True)

    # define exit key
    keyboard.wait('backspace', suppress=True)
