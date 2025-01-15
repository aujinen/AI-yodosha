# Neural Network Console Desktop
# version 0.2.0
# https://techhub.developer.sony.com/ja/neural-network-console#NNC%20D%20JA
# This model was convarted from AI-Yodosha-Chapter5's secand model (with dropouts) by H.Nishiyama
# https://github.com/aujinen/AI-yodosha/tree/main/Chapter5
# https://github.com/aujinen/AI-yodosha/tree/main/Chapter5/SonyNNC_Desktop

import nnabla as nn
import nnabla.functions as F
import nnabla.parametric_functions as PF

def network(x, y, test=False):
    # Input:x -> 1,1024,1024
    # Interpolate -> 1,64,64
    h = F.interpolate(x, (64,64))
    # Reshape -> 4096
    h = F.reshape(h, (h.shape[0],4096,))

    # Affine -> 512
    h = PF.affine(h, (512,), name='Affine')
    # ReLU
    h = F.relu(h, True)

    # Dropout
    if not test:
        h = F.dropout(h)

    # Affine_2 -> 256
    h = PF.affine(h, (256,), name='Affine_2')
    # ReLU_2
    h = F.relu(h, True)

    # Dropout_2
    if not test:
        h = F.dropout(h)

    # Affine_3 -> 128
    h = PF.affine(h, (128,), name='Affine_3')
    # ReLU_3
    h = F.relu(h, True)

    # Affine_4 -> 1
    h = PF.affine(h, (1,), name='Affine_4')
    # Sigmoid
    h = F.sigmoid(h)

    # BinaryCrossEntropy
    h = F.binary_cross_entropy(h, y)
    return h

