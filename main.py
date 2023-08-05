import requests
import minecraft_launcher_lib
import subprocess
import os
import shutil
import urllib
class MineLaunch():
    class forge():
        def install_authlib(self,minecraft_dir,authlib_download_link:None):
            if authlib_download_link == None:
                authlib_download_link = "https://www.udrop.com/file/KrBu/authlib-2.1.28.jar"
            self.minecraft_dir = minecraft_dir
            link = authlib_download_link
            filename = "authlib-2.1.28.jar"
            extract_path = os.path.normpath(minecraft_dir+"/libraries/com/mojang/authlib/2.1.28")
            try:
                shutil.rmtree(extract_path, ignore_errors=True)
                os.makedirs(extract_path)
            except:
                os.makedirs(extract_path)
            fullfilename = os.path.join(extract_path, filename)
            urllib.request.urlretrieve(link, fullfilename)
        def install(self,minecraft_dir,forge_version,username):
            self.minecraft_dir = minecraft_dir
            self.forge_version = forge_version
            self.options = {
            "username": username,
            }
            minecraft_launcher_lib.forge.install_forge_version(self.forge_version,self.minecraft_dir)
        def run(self,only_command:False,server_ip:None,server_port:None):
            minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.forge_version[0:self.forge_version.find("-")]+"-forge-"+self.forge_version[self.forge_version.find("-")+1:len(self.forge_version)], self.minecraft_dir, self.options)
            if server_ip != None:
                if server_port != None:
                    minecraft_command.append("--server")
                    minecraft_command.append(server_ip)
                    minecraft_command.append("--port")
                    minecraft_command.append(int(server_port))
            if only_command == False:
                subprocess.call(minecraft_command)
            else:
                return minecraft_command
    class minecraft():
        def install_authlib(self,minecraft_dir,authlib_download_link:None):
            if authlib_download_link == None:
                authlib_download_link = "https://www.udrop.com/file/KrBu/authlib-2.1.28.jar"
            self.minecraft_dir = minecraft_dir
            link = authlib_download_link
            filename = "authlib-2.1.28.jar"
            extract_path = os.path.normpath(minecraft_dir+"/libraries/com/mojang/authlib/2.1.28")
            try:
                shutil.rmtree(extract_path, ignore_errors=True)
                os.makedirs(extract_path)
            except:
                os.makedirs(extract_path)
            fullfilename = os.path.join(extract_path, filename)
            urllib.request.urlretrieve(link, fullfilename)
        def install(self,minecraft_dir,version,username):
            self.minecraft_dir = minecraft_dir
            self.version = version
            self.options = {
            "username": username,
            }
            minecraft_launcher_lib.install.install_minecraft_version(self.version,self.minecraft_dir)
            def install(self,minecraft_dir,forge_version,username):
                self.minecraft_dir = minecraft_dir
                self.forge_version = forge_version
                self.options = {
                "username": username,
                }
                minecraft_launcher_lib.forge.install_forge_version(self.forge_version,self.minecraft_dir)
        def run(self,only_command:False,server_ip:None,server_port:None):
            minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.forge_version[0:self.forge_version.find("-")]+"-forge-"+self.forge_version[self.forge_version.find("-")+1:len(self.forge_version)], self.minecraft_dir, self.options)
            if server_ip != None:
                if server_port != None:
                    minecraft_command.append("--server")
                    minecraft_command.append(server_ip)
                    minecraft_command.append("--port")
                    minecraft_command.append(int(server_port))
            if only_command == False:
                subprocess.call(minecraft_command)
            else:
                return minecraft_command
