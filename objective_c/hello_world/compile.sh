#!/usr/bin/env bash

. /usr/share/GNUstep/Makefiles/GNUstep.sh
gcc `gnustep-config --objc-flags` -lobjc -lgnustep-base hello.m -o hello

