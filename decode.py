import sys
import wave
import struct

def create(path):
    f = wave.open(path, 'w')
    f.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))
    return f


def open(path):
    print "open: {}".format(path)
    data = wave.open(path, "r")
    print data.getparams()
    return data

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Incorrect arguments.")
        print("python decode.py <bits> <inputfile> <outputfile>")

        exit(-1)

    bits = int(sys.argv[1])
    encoded = open(sys.argv[2])
    decoded = create(sys.argv[3])

    frames = encoded.getnframes()

    samples = []

    for i in range(0, frames):
        low_mask = 0xffff>>(16-bits)
        frame1 = encoded.readframes(1) # 4 bytes, 2 bytes pr channel

        frame1_left = struct.unpack("<H", frame1[0:2])[0]
        frame1_right = struct.unpack("<H", frame1[2:])[0]

        frame1_left = (frame1_left & low_mask) << (16-bits)
        frame1_right = (frame1_right & low_mask) << (16-bits)

        # Resulting samples
        samples.append(struct.pack('<H', frame1_left))
        samples.append(struct.pack('<H', frame1_right))

    decoded.writeframes("".join(samples))
    decoded.close()
