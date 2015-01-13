#!/usr/bin/env python3

import sys
import logmein.main
try:
    sys.exit(logmein.main.main())
except KeyboardInterrupt:
    sys.exit(1)
