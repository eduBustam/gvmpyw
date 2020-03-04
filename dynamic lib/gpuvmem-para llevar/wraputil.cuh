#ifndef WRAPUTIL_CUH
#define WRAPUTIL_CUH

#include "frprmn.cuh"
#include "directioncosines.cuh"
#include <time.h>

Synthesizer * wrapsynth();
Optimizator * wrapopti();
ObjectiveFunction * wrapOf();
Io * wrapIo();

#endif
