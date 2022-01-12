## About Genshin Lyre Player

_Genshin Lyre Player_ - a project for auto playing MIDI song with Windsong Lyre in Genshin Impact.

## Youtube

For more information can be seen in my [video](https://youtu.be/f0EuECyRqF0) on YouTube.

[![new_thumb](https://github.com/TitorPs360/midi-genshin-lyre-player-python/blob/main/fig/cover.png?raw=true)](https://youtu.be/f0EuECyRqF0)

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

   ![alt text](https://github.com/TitorPs360/midi-genshin-lyre-player-python/blob/main/fig/step1.png?raw=true)

2. Equipt and use Windsong Lyre

   ![alt text](https://github.com/TitorPs360/midi-genshin-lyre-player-python/blob/main/fig/step2.png?raw=true)

3. Open CMD as administrator

   ![alt text](https://github.com/TitorPs360/midi-genshin-lyre-player-python/blob/main/fig/step3.png?raw=true)

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
