
import os
import sys

import saga.utils.benchmark as sb


# ------------------------------------------------------------------------------
#
def benchmark_pre (test_cfg, bench_cfg, session) :

    pass


# ------------------------------------------------------------------------------
#
def benchmark_core (args={}) :

    pass


# ------------------------------------------------------------------------------
#
def benchmark_post (args={}) :

    pass


# ------------------------------------------------------------------------------
#
# try:
if True :
    sb.benchmark_init ('benchmark.selftest', benchmark_pre, benchmark_core, benchmark_post)

# except Exception as e :
# 
#     print "Exception: %s" % e


