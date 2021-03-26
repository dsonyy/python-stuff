import os


def get_used_time(path):
    """Get the latest timestamp of file access, modification or creation"""
    return max(os.path.getatime(path),
               os.path.getctime(path),
               os.path.getmtime(path))
