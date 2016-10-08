Audio steganography
===================

Examples:
-----------

> python encode.py 16 samples/song.wav samples/code.wav encoded16.wav
> python decode.py 16 encoded16.wav decoded16.wav
> 
> python encode.py 8 samples/song.wav samples/code.wav encoded8.wav
> python decode.py 8 encoded8.wav decoded8.wav
>
> python encode.py 4 samples/song.wav samples/code.wav encoded4.wav
> python decode.py 4 encoded4.wav decoded4.wav
>
> python encode.py 2 samples/song.wav samples/code.wav encoded2.wav
> python decode.py 2 encoded2.wav decoded2.wav
>
> python encode.py 1 samples/song.wav samples/code.wav encoded1.wav
> python decode.py 1 encoded1.wav decoded1.wav


TODO
-----------
Make encode and decode flexible with regards to sample-bits and number of channels. It currently only supports 16bit/stereo.
