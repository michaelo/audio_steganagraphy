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
    if len(sys.argv) != 5:
        print("Incorrect arguments.")
        print("python decode.py <bits> <inputfile1> <inputfile2> <outputfile>")

        exit(-1)

    bits = int(sys.argv[1])
    f_carrier = open(sys.argv[2])
    f_secret = open(sys.argv[3])
    out = create(sys.argv[4])

    frames = min(f_carrier.getnframes(), f_secret.getnframes())

#     num_frames = f1.getnframes()
#     samp_width_bytes = f1.getsampwidth()
#     bits = samp_width_bytes * 8

    samples = []
    # Read all samples from f1, then write to out

    for i in range(0, frames):
        frame1 = f_carrier.readframes(1) # 4 bytes, 2 bytes pr channel
        frame2 = f_secret.readframes(1) # 4 bytes, 2 bytes pr channel


        # Keep top byte from frame1, insert top byte from frame2 into low byte on frame1
        frame1_left = struct.unpack("<H", frame1[0:2])[0]
        frame1_right = struct.unpack("<H", frame1[2:])[0]

        frame2_left = struct.unpack("<H", frame2[0:2])[0]
        frame2_right = struct.unpack("<H", frame2[2:])[0]



        low_mask = 0xffff>>(16-bits)
        high_mask = 0xffff^low_mask

        # Shift secret to lower byte
        frame2_left = (frame2_left >> 16-bits) & low_mask
        frame2_right = (frame2_right >> 16-bits) & low_mask

        frame1_left = (frame1_left & high_mask) ^ frame2_left
        frame1_right = (frame1_right & high_mask) ^ frame2_right

        # val1 = (val1 << 8) & 0xff00
        # val2 = (val2 << 8) & 0xff00


        # Resulting samples
        samples.append(struct.pack('<H', frame1_left))
        samples.append(struct.pack('<H', frame1_right))


    out.writeframes("".join(samples))
    out.close()
