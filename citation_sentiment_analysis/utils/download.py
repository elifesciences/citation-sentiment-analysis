import os
from urllib.request import urlretrieve


def urlretrieve_with_progress(source_url, target_file):
    with tqdm(
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
        miniters=1,
        desc=os.path.basename(target_file),
        file=sys.stdout,
        leave=False
    ) as t:
        def reporthook(blockcount, blocksize, totalsize):
            if totalsize is not None:
                t.total = totalsize
            t.update(blockcount * blocksize - t.n)
        temp_file = target_file + '.part'
        urlretrieve(source_url, temp_file, reporthook=reporthook)
        if os.path.exists(target_file):
            os.remove(target_file)
        os.rename(temp_file, target_file)


def download_if_not_exists(source_url, target_file):
    if not os.path.exists(target_file):
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        urlretrieve_with_progress(source_url, target_file)
