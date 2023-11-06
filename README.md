# Flatbuffers_Testing
Testing flatbuffers for usage

Given directory has files for encoding and decoding in CPP and Python working with same and cross languages.

For CPP, compilation step:
- g++ -std=c++20 -I flatbuffers/include/ fb_encoder.cpp -o fb_encoder
- g++ -std=c++20 -I flatbuffers/include/ fb_decoder.cpp -o fb_decoder

For Python, run step:
- python fb_encoder.py
- python fb_decoder.py
