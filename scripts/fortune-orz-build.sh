set -e
cat << EOF | ./configure


fortune
/opt/fortune-orz/bin
/opt/fortune-orz/bin
/opt/fortune-orz/man/man6
/opt/fortune-orz/man/man8
/opt/fortune-orz/share
/opt/fortune-orz/var/games
y































EOF
make && sudo make install && sudo rm -rf /opt/fortune-orz/share/fortune
[ ! -d fortune-orz ] && git clone https://github.com/Icenowy/fortune-orz
sudo mkdir -p /opt/fortune-orz/share/fortune/
sudo cp fortune-orz/* /opt/fortune-orz/share/fortune/
sudo rm -f /opt/fortune-orz/share/fortune/README.md
sudo rm -f /opt/fortune-orz/share/fortune/fortune-orz-build.sh
for i in /opt/fortune-orz/share/fortune/*
do
sudo /opt/fortune-orz/bin/strfile $i
done
