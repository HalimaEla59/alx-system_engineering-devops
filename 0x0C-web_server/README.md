0x0C. Web server
_______________________
In this project, some of the tasks will be graded on 2 aspects:

Is your web-01 server configured according to requirements
Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)
For example, if I need to create a file /tmp/test containing the string hello world and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use emacs on my server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

But my answer file would contain:

sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu
As you can tell, I am not using emacs to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an SRE, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the root user, you do not need to use the sudo command.

A good Software Engineer is a lazy Software Engineer. 

Tips: to test your answer Bash script, feel free to reproduce the checker environment:

start a Ubuntu 16.04 sandbox
run your script on it
see how it behaves
___________________________________
General

 - What is the main role of a web server
 - What is a child process
 - Why web servers usually have a parent process and child processes
 - What are the main HTTP requests

DNS

 - What DNS stands for
 - What is DNS main role
 - DNS Record Types
    - A
    - CNAME
    - TXT
    - MX
____________________________
Tasks
______________________
0. Transfer a file to your server

Write a Bash script that transfers a file from our client to a server:

Requirements:

 - Accepts 4 parameters
 - The path to the file to be transferred
 - The IP of the server we want to transfer the file to
 - The username scp connects with
 - The path to the SSH private key that scp uses
 - Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
 - scp must transfer the file to the user home directory ~/
 - Strict host key checking must be disabled when using scp
   ![image](https://github.com/HalimaEla59/alx-system_engineering-devops/assets/86242444/64178110-646d-4888-be04-9969121ade4b)
____________________________________
1. Install nginx web server

Web servers are the piece of software generating and serving HTML pages, let’s install one!

Requirements:

 - Install nginx on your web-01
 - server
 - Nginx should be listening on port 80
 - When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
 - As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
 - You can’t use systemctl for restarting nginx
   ![image](https://github.com/HalimaEla59/alx-system_engineering-devops/assets/86242444/9c5fde66-6669-4949-8c34-6403da4f5592)
___________________________________________
2. Setup a domain name

.TECH Domains is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. We partnered with .TECH Domains so that you can learn about DNS.

.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your tools space. Feel free to drop a thank you tweet for .TECH Domains.

Provide the domain name in your answer file.

Requirement:

 - provide the domain name only (example: foobar.tech), no subdomain (example: www.foobar.tech)
 - configure your DNS records with an A entry so that your root domain points to your web-01 IP address Warning: the propagation of your records can take time (~1-2 hours)
 - go to your profile and enter your domain in the Project website url field

When your domain name is setup, please verify the Registrar here: https://whois.whoisxmlapi.com/ and you must see in the JSON response: "registrarName": "Dotserve Inc"
______________________________________
3. Redirection

 - Replace a line with multiple lines with sed
 - Configure your Nginx server so that /redirect_me is redirecting to another page.

Requirements:

 - The redirection must be a “301 Moved Permanently”
 - You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
 - Using what you did with 1-install_nginx_web_server, write 3-redirection so that it configures a brand new Ubuntu machine to the requirements asked in this task
   ![image](https://github.com/HalimaEla59/alx-system_engineering-devops/assets/86242444/80a8722e-f515-4163-b22a-c479b18732ed)
____________________________________
4. Not found page 404

Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.

Requirements:

 - The page must return an HTTP 404 error code
 - The page must contain the string Ceci n'est pas une page
 - Using what you did with 3-redirection, write 4-not_found_page_404 so that it configures a brand new Ubuntu machine to the requirements asked in this task
__________________________________
5. Install Nginx web server (w/ Puppet)
 (#advanced)

Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.

Requirements:

 - Nginx should be listening on port 80
 - When querying Nginx at its root / with a GET request (requesting a page) using curl, it must return a page that contains the string Hello World!
 - The redirection must be a “301 Moved Permanently”
 - Your answer file should be a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements
