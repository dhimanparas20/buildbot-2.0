#codes for build environment

sudo apt-get update -y
sudo su 
echo "============================INSTALLING=================================="
sudo apt install software-properties-common -y 
sudo add-apt-repository ppa:openjdk-r/ppa -y
sudo apt-get install rsync wget git nano screen python curl tmate -y
sudo apt-get install bison build-essential curl ccache flex lib32ncurses5-dev lib32z1-dev  libncurses5-dev libsdl1.2-dev libxml2 libxml2-utils lzop pngcrush schedtool squashfs-tools xsltproc zip zlib1g-dev git-core make gperf openjdk-8-jdk -y
sudo apt install bc g++-multilib gcc-multilib git gnupg gperf imagemagick lib32ncurses5-dev lib32readline-dev lib32z1-dev liblz4-tool libncurses5-dev libsdl1.2-dev libssl-dev  libxml2 libxml2-utils lzop pngcrush schedtool squashfs-tools xsltproc zip zlib1g-dev -y
exit
curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > repo
chmod a+x repo
sudo install repo /usr/local/bin
git clone https://github.com/akhilnarang/scripts.git scripts && cd scripts
bash setup/android_build_env.sh
cd && ls 
python3 vars.py
echo "============================DONE=================================="
./run.sh
