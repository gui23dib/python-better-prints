from betterprint import BetterPrint as bp

config = bp()

config.toggleDebugMode(True)
config.toggleDetailedPrint(True)
config.toggleNamedInstances(True)

def debugprint(*objects, sep=' ', end='\n', flush=False):
    config.debug_print(*objects, sep=sep, end=end, flush=flush)

def styledprint(*objects, sep=' ', end='\n', flush=False, style=None):
    config.styledprint(*objects, sep=sep, end=end, flush=flush, style=style)

def betterprint(*objects, sep=' ', end='\n', flush=False):
    config.better_print(*objects, sep=sep, end=end, flush=flush)