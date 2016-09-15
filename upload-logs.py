#!/usr/bin/env python
import os
import subprocess
import sys
import tempfile

# Compresses the contents of a folder and upload the result to Box.
# Run this script as:
#
# $ upload-logs.py LOG_DIR DEST_NAME
#
# e.g.:
#
# $ upload-logs.py /tmp/wsklogs /openwhisk-travis/logs-5512.tar.gz

def upload_file(username, password, local_file, remote_file):
    if remote_file[0] == '/':
        remote_file = remote_file[1:]

    subprocess.call([ "curl", "-s", "-T", local_file, "ftps://ftp.box.com/%s" % remote_file, "--user", "%s:%s" % (username, password) ])

def tar_gz_dir(dir_path):
    _, dst = tempfile.mkstemp(suffix = ".tar.gz")
    subprocess.call([ "tar", "-czf", dst, dir_path ])
    return dst

if __name__ == "__main__":
    box_username = os.environ.get("BOX_USERNAME", None)
    box_password = os.environ.get("BOX_PASSWORD", None)

    if not box_username or not box_password:
        sys.stderr.write("Couldn't retrieve Box credentials.\n")
        sys.exit(1)

    dir_path = sys.argv[1]
    dst_path = sys.argv[2]

    print "Compressing logs dir..."
    tar = tar_gz_dir(dir_path)
    print "Uploading to Box..."
    upload_file(box_username, box_password, tar, dst_path)

