from betterprint import BetterPrint as bp

config = bp()

config.toggleDebugMode(True)
config.toggleDetailedPrint(True)

def dprint(*objects, sep=' ', end='\n', flush=False):
    config.debug_print(*objects, sep=sep, end=end, flush=flush)