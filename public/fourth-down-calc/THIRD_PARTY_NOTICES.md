# Model and source attribution

This calculator contains an inference-only JavaScript adaptation of decision
functions from nfl4th and nflfastR, and trained model assets exported from
nfl4th and fastrmodels. The models have not been retrained.

- nfl4th 1.0.7: https://github.com/nflverse/nfl4th
  Copyright (c) 2021 Ben Baldwin.
- nflfastR 5.2.0: https://github.com/nflverse/nflfastR
  Copyright (c) 2020 Sebastian Carl; Ben Baldwin.
- fastrmodels 2.1.0: https://github.com/nflverse/fastrmodels
  Copyright (c) 2021 Sebastian Carl, Ben Baldwin.

These packages are distributed under the MIT license:

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

XGBoost is used during export / validation under Apache License 2.0:
https://github.com/dmlc/xgboost/blob/master/LICENSE.
The browser tree evaluator is implemented in this repository; the XGBoost
runtime is not bundled.

The calculator is not affiliated with or endorsed by the NFL.
