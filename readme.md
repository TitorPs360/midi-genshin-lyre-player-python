## About Genshin Lyre Player

_Genshin Lyre Player_ - a project for auto playing MIDI song with Windsong Lyre in Genshin Impact.

## Requirements

- Genshin Impact on Windows
- Anaconda with Python 3
- Git

## Install

```
git clone https://github.com/TitorPs360/midi-genshin-lyre-player-python.git
cd midi-genshin-lyre-player-python
conda create --name <env> --file requirements.txt
```

## Usage

1. Open Genshin Impact
2. Equipt and use Windsong Lyre
3. Open CMD as administrator
4. Activate anaconda environment
   ```
   conda activate <env>
   ```
5. Run script

   - Show how to use this script

   ```
   python main.py --help
   ```

   - Or play default song

   ```
   python main.py
   ```

   - Or play MIDI song

   ```
   python main.py [path to midi file]
   ```

6. Switch back to Genshin Impact window, press "\\" to play/pause
7. Press "backspace" to exit
