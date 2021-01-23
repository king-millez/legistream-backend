import pytest
from legistream_backend.nz import Stream

def test_nz():
    nz_stream = Stream()
    print('\nHouse live status: ' + str(nz_stream.is_live))
    print('House stream URL: ' + nz_stream.stream_url)
    print(nz_stream.stream_urls)