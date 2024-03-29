from pathlib import Path
from toolbox import Toolbox
from argutils import print_args
import argparse

import sys
import traceback

def excepthook(exc_type, exc_value, exc_tb):
    traceback.print_exception(exc_type, exc_value, exc_tb)
    sys.exit(1)

if __name__ == '__main__':
    sys.excepthook = excepthook

    parser = argparse.ArgumentParser(
        description="Runs the toolbox",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    parser.add_argument("datasets_root", type=Path, help= \
        "Path to the directory containing your datasets. See toolbox/__init__.py for a list of "
        "supported datasets. You can add your own data by created a directory named UserAudio "
        "in your datasets root. Supported formats are mp3, flac, wav and m4a. Each speaker should "
        "be inside a directory, e.g. <datasets_root>/UserAudio/speaker_01/audio_01.wav.")
    parser.add_argument("-e", "--enc_models_dir", type=Path, default="encoder/saved_models", 
                        help="Directory containing saved encoder models")
    parser.add_argument("-s", "--syn_models_dir", type=Path, default="synthesizer/saved_models", 
                        help="Directory containing saved synthesizer models")
    parser.add_argument("-v", "--voc_models_dir", type=Path, default="vocoder/saved_models", 
                        help="Directory containing saved vocoder models")
    args = parser.parse_args()

    # Launch the toolbox
    print_args(args, parser)
    Toolbox(**vars(args))
    
