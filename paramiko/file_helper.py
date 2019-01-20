#! /usr/bin/env python
# *_* coding:utf-8 *_*


class CFileHelper(object):
    """
    文件上下创建帮助类
    """
    def __init__(self, client):
        self.client = client
        # return a new SFTPClient session object
        self.sftp = client.open_sftp()
        print('call init func')

    def __del__(self):
        """
        对象释放时自动关闭
        :return:
        """
        self.sftp.close()
        print('call del func')

    def upload(self, local_file, server_file):
        try:
            self.sftp.put(local_file, server_file)
        except Exception:
            print('upload file error')

    def mkdir(self, server_dir):
        try:
            self.sftp.mkdir(server_dir)
        except Exception :
            # dir already exist
            pass

    def down(self, server_file, local_file):
        try:
            self.sftp.get(server_file, local_file)
        except Exception:
            print('down file error')


if __name__ == "__main__":
    pass
