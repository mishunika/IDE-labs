# IDE Laboratory Work #1
###### student gr. FAF-111: Mihai Iachimovschi

## Part 1: Setting server environment. Version Control.
### Objectives:
  - Understanding and using CLI (basic level)
  - Administration of a remote linux machine using SSH
  - Ability to work with Version Control Systems (git || mercurial || svn)
  - Compile your C/C++/Java/Python programs through CLI using gcc/g++/javac/python compilers

### Intro:
From the start I've set up a Virtual Machine with ArchLinux on it, just for the sake of setting from scratch of a new machine.
IRL I used my existing mini-server, a Raspberry Pi device with GNU/Linux Raspbian (based on Debian).
The process of setting up a linux server is very simple, and you can do it just following the installation guide provided by distro's wiki pages ([Installation Guide](https://wiki.archlinux.org/index.php/Installation_Guide)).

### Setting up a VirtualBox instance:
The process of setup is classical one, and the only thing I needed to fix was the network interfaces.
By default there is a NAT network interface enabled, and it works pretty nice but gives no routing from the host machine.
So I've added a new interface, a Host-Only adapter that will make possible the access from the host machine.
The host-only interface can be configured in global settings.

### Connecting through SSH:
After configuring the [Network](https://wiki.archlinux.org/index.php/Network) and the [SSH](https://wiki.archlinux.org/index.php/Secure_Shell) daemon, you are ready to connect to the remote machine.
The connection is can be established by this command: `ssh [username@]host`.

### Now, let's go to the real RasPi server:
On my Raspberry Pi server I've set up a bare git repository that will be used as a origin for my local repository.
In order to deploy the application I created a **post-receive hook**.
This extremely simple hook will deploy the application and will execute the script from the second part of this laboratory work.
```bash
#!/bin/bash
GIT_WORK_TREE=/home/midps/deploy git checkout -f  # This will copy all working files to the deploy directory

cd /home/midps/deploy/lab\#1                      # This command will change the working directory
./compile.sh                                      # This will execute my script
```

### Basic GIT commands (The list was taken from Roman Roibu's repository and completed):
- Initialize a GIT repositoryenc:    `git init`
- Viewing the repo status:        `git status`
- View the staged files changes:  `git diff`
- View the commit log:            `git log`
- Add a change to staging:        `git add [filename]`
- Add just some chunks of code:   `git add -p [filename]`
- Commit staging changes:         `git commit -m "[commit message]"`
- Commit changed staged files:    `git commit -a`
- Clone a remote repository:      `git clone [remote repo]`
- Create a new branch:            `git branch [branch name]`
- Checkout into a branch:         `git checkout [branch name]`
- Merge a brange into current:    `git merge [branch name]`
- Add a remote:                   `git remote add [remote name] [remote repo]`
- Set a branch to track a remote: `git branch --track [remote repo/branch] [local branch]`
- Reset to previous commit:       `git reset [mode] [commit]`

## Part 2: Command Line Interface (CLI). Scripting.
### Objectives:
  - Understanding and using CLI (basic level)
  - Ability to work remotely (remote code editing)
  - Creating a script that will compile multiple projects (source codes) with resulting multiple programs

### Command line interface.
Well, I'm very familiar with CLI.
In my real life I use it every day, the most of the working time, so I can't tell to much about my learning experience at this laboratory work, but I'm very glad that such useful things are teached at the university.
It is really very good to know, I'm telling that from my experience.

### Scripting.
My approach to the script was a little bit different from your requirements, but still, covers all of them indirectly.
The main script was written in bash and it just checks syntax, compiles and executes the provided source code.
It is executed by the post-receive hook from the production server.
I've set up an array-like config and universalized the script, so now you can add just a new entry in the config array and the rest of the job will be done.
If the main script encounters some errors, It sends an SMS to my phone number, with a sample warning.
The errors from the compilation process are stored in special log files.

##### SMS:
The SMS is sent from the USB Dongle attached to the Raspberry Pi using [AT Commands](http://en.wikipedia.org/wiki/Hayes_command_set).
The workflow is very simple. Simple things rules the world.

## Conclusion
Even if I was already familiar to the CLI, I am very glad that I had this opportunity to apply and improve my knowledge at the University.
CLI is great, even now, I am writing this report in CLI using VIM editor.
Working with git is a great experience. Git hooks are great! I will use them more and more frequently.
Speaking about other Version Control Systems, I used SVN and at this laboratory work I had the opportunity to play with mercurial, also a very nice VCS.
Overall it was very interesting. I am looking forward to the next laboratory works.
