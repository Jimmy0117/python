#! /usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import sys
import traceback


class CCMDError(Exception):

    def __ini__(self, msg=''):
        self.msg = msg


class CCmd(object):
    """
     远程执行命令类
    """

    def __init__(self, cmd_client):
        self.cmd_client = cmd_client
        self.cmd_list = ''
        self.cmd_result = ''

    def __exec_cmd(self, user_cmd):
        """
        Blocks until command succeeds
        A new Channel is opened and the requested command is executed.
        :param user_cmd:
        :return:
        """
        print('user input cmd:{}'.format(user_cmd))

        try:
            stdin, stdout, stderr = self.cmd_client.exec_command(user_cmd)
            self.cmd_result = stdout.read()
            exit_status = stdout.channel.recv_exit_status()
            if exit_status != 0:
                return False
        except paramiko.SSHException:
            raise CCMDError('raise exec command')

        return True

    def get_cmd_result(self):
        """
        返回命令执行结果
        :return:
        """

        return 'exec cmd result:{}'.format(self.cmd_result)

    def run_cmd(self, cmd_list):
        if len(cmd_list):
            if self.__exec_cmd(cmd_list):
                print('run cmd success')
            else:
                print('run cmd fail')
        else:
            pass

    def add_cmd(self, cmd_cell):
        """
        添加命令
        :param cmd_cell:
        :return:
        """
        self.cmd_list += cmd_cell
        # 多条命令分隔符
        self.cmd_list += ';'

    def run_multi_cmd(self):
        """
        同时执行多个命令
        :return:
        """
        # 不要最后一个分隔符;
        cmd_list = self.cmd_list[:-1]
        if len(cmd_list):
            self.run_cmd(cmd_list)


if __name__ == "__main__":

    # from base.ssh import ssh_client
    try:
        ip = ''
        usr = ''
        password = '.'
        client = ssh_client(ip, usr, password)
        cmd = CCmd(client)
        cmd.run_cmd('pwd')
        print(cmd.get_cmd_result())
    except Exception as e:
        print(traceback.format_exc())
        if isinstance(e, CCMDError):
            print(e.msg)
        else:
            print('get exception')
            sys.exit(1)
