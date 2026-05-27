#!/usr/bin/env python3
import argparse
import wave
import os
import sys

def get_params(path):
    with wave.open(path, "rb") as wf:
        return wf.getparams()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", default="cover.wav")
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print("QUALITY_FAIL")
        print("missing input")
        sys.exit(1)

    try:
        ref = get_params(args.reference)
        inp = get_params(args.input)
    except Exception as e:
        print("QUALITY_FAIL")
        print(f"error={e}")
        sys.exit(1)

    print(f"REFERENCE={args.reference}")
    print(f"INPUT={args.input}")
    print(f"REFERENCE_PARAMS={ref}")
    print(f"INPUT_PARAMS={inp}")

    if ref.nchannels == inp.nchannels and ref.sampwidth == inp.sampwidth and ref.framerate == inp.framerate and ref.nframes == inp.nframes:
        print("QUALITY_OK")
    else:
        print("QUALITY_FAIL")

if __name__ == "__main__":
    main()
