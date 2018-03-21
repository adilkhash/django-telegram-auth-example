import os
import sys

apps_root = os.path.join(os.path.dirname(__file__), '..', 'apps')
apps_root = os.path.normpath(os.path.abspath(apps_root))
if apps_root not in sys.path:
    sys.path.insert(0, apps_root)
