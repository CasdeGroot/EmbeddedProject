# Smart Tooling Embedded Project

For the project Smart Tooling we've created a project for a robotic crawler to inspect Oil Tanks.  
The robot can read sensors via serial connection and can be controlled with a xbox controller.  

## Getting Started

### Prerequisites

#### Install conda
* **Step 1** Go to https://conda.io/miniconda.html and select the operation system you are using.
* **Step 2** Download the installer for python 3.7. 
* **Step 3** Give the .sh file execute access with the command "chmod ug+x ./filename.sh".
* **Step 4** Run the installer with command "./filename.sh".
* **Step 5** Hold enter until it askes for 'yes or 'no', press yes.
* **Step 6** Press enter for default location path.
* **Step 7** Now wait for the installation to be finished.
* **Step 8** Add conda.sh to bashrc with command "echo ". /home/<username>/miniconda3/etc/profile.d/conda.sh" ~/.bashrc".
* **Step 9** Validate installation with the command "conda --version" on linux.

#### Install git
* **Step 1** Open terminal with Ctrl+Alt+t.
* **Step 2** Run command "sudo apt-get install git".
* **Step 3** Type in 'Y' to continue.
* **Step 4** Wait for git to install.
* **Step 5** Validate installation with the command "git --version" on linux.

#### *Optional* Install Gitkraken
* **Step 1** Go to https://www.gitkraken.com/download.
* **Step 2** Download the installer for working OS.
* **Step 3** Execute the installer and install Gitkraken.
* **Step 4** Visit https://support.gitkraken.com/start-here/guide for explanation of the software.

#### *Optional* Install PyCharm
* **Step 1** Open terminal with Ctrl+Alt+t.
* **Step 2** Run command "sudo snap install pycharm-community --classic".
* **Step 3** Wait for installation to be complete.
* **Step 4** Run PyCharm with the command "pycharm-community".

### Installing

#### Clone repository
* **Step 1** Open Gitkraken.
* **Step 2** Select the folder icon and click on "Clone".
* **Step 3** Add "https://github.com/CasdeGroot/EmbeddedProject.git" to the URL inputfield.
* **Step 4** Select clone location with the browse button.
* **Step 5** Select "Clone repo!".

#### Setup Environment
* **Step 1** Open terminal with Ctrl+Alt+t.
* **Step 2** Navigate to repo folder (folder with embeddedproject.yml file) "cd <path>" command.
* **Step 3** Create environment with command "conda env create -f embeddedproject.yml".
* **Step 4** Start environment with "conda activate embeddedproject".
* **Step 5** run command "conda list" and check if pyserial is in the printed list with version 3.4 to validate the install.

#### Setup IDE
* **Step 1** Open PyCharm with the command "sudo pycharm-community" while EmbeddedProject environment is activated.
* **Step 2** Select "Open" in the menu and open the project.
* **Step 3** Press Ctrl+Alt+S to open settings menu and select "Python Interpreter" in the dropdown menu.
* **Step 4** Press the gear icon and select 'Add'.
* **Step 5** Select "Existing Environment".
* **Step 6** In the "enterpreter field" type in "home/<username>/miniconda3/envs/EmbeddedProject/bin/python" or find the file with the file exporer.
* **Step 7** Select "OK".
* **Step 8** Validate the environment by checking all the listed packages with the embeddedproject.yml file.
* **Step 9** Select "OK" the IDE should now be set and code can be run.

#### Execute Code
To execute code to test if everything is set, right click on a python file and select "run <filename>".

## Authors

* **Cas de Groot** - https://github.com/casdegroot
