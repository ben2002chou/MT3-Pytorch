from inference import InferenceHandler

handler = InferenceHandler("./pretrained")
handler.inference(
    "/home/chou150/depot/datasets/guitarset/audio/hex_pickup_original/00_BN1-129-Eb_comp_hex.wav",
    outpath="/home/chou150/code/mt3-pytorch/output.mid",
)
