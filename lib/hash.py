from zlib import crc32


def compute_crc32(path: str) -> int:
    return crc32(path.encode()) & 0xFFFFFFFF
