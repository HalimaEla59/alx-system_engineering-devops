0x0D. Web stack debugging #0
______________________________
*Background Context*

The Webstack debugging series will train you in the art of debugging. Computers and software rarely work the way we want (that’s the “fun” part of the job!).

Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to be a master of it.

In this debugging series, broken/bugged webstacks will be given to you, the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state. But before writing this Bash script, you should figure out what is going on and fix it manually.

Let’s start with a very simple example. My server must:

 - have a copy of the /etc/passwd file in /tmp
 - have a file named /tmp/isworking containing the string OK
 - Let’s pretend that without these 2 elements, my web application cannot work.
![image](https://github.com/HalimaEla59/alx-system_engineering-devops/assets/86242444/b04eeb61-cd7c-434c-b1fe-fa073ffd7d4d)
______________________________
Installing Docker

For this project you will be given a container which you can use to solve the task. If you would like to have Docker so that you can experiment with it and/or solve this problem locally, you can install it on your machine, your Ubuntu 14.04 VM, or your Ubuntu 16.04 VM if you upgraded.

 - Mac OS: https://docs.docker.com/desktop/install/mac-install/
 - Windows: https://docs.docker.com/desktop/install/windows-install/
 - Ubuntu 14.04 (Note that Docker for Ubuntu 14 is deprecated and you will have to make some adjustments to the instructions when installing): https://www.liquidweb.com/kb/how-to-install-docker-on-ubuntu-14-04-lts/
 - Ubuntu 16.04: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04
___________________________________
Resources

man or help:

curl
_______________________________
Tasks

0. Give me a page!

Be sure to read the Docker concept page

In this first debugging project, you will need to get Apache to run on the container and to return a page containing Hello Holberton when querying the root of it.
![image](https://github.com/HalimaEla59/alx-system_engineering-devops/assets/86242444/55990af8-3cc4-4d72-9858-c1a6b6707006)

