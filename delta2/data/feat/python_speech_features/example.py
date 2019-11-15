# Copyright (C) 2017 Beijing Didi Infinity Technology and Development Co.,Ltd.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

#!/usr/bin/env python3
''' Example for sigproc.py '''

# pylint: skip-file

import scipy.io.wavfile as wav

from base import mfcc
from base import delta
from base import logfbank

if __name__ == '__main__':
  (rate, sig) = wav.read("english.wav")
  mfcc_feat = mfcc(sig, rate)
  d_mfcc_feat = delta(mfcc_feat, 2)
  fbank_feat = logfbank(sig, rate)

  print(fbank_feat[1:3, :])
