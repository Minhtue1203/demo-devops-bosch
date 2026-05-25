#!/bin/bash
set -e

echo "=== Update apt ==="
apt update

echo "=== Install basic tools ==="
apt install -y python3 python3-pip python3-venv git wget unzip curl

echo "=== Install Sonar Scanner ==="
cd /tmp

if [ ! -f sonar-scanner-cli-5.0.1.3006-linux.zip ]; then
  wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
fi

unzip -o sonar-scanner-cli-5.0.1.3006-linux.zip

rm -rf /opt/sonar-scanner
mv sonar-scanner-5.0.1.3006-linux /opt/sonar-scanner

ln -sf /opt/sonar-scanner/bin/sonar-scanner /usr/local/bin/sonar-scanner

echo "=== Versions ==="
python3 --version
pip3 --version
git --version
sonar-scanner --version

echo "=== Jenkins tools setup completed ==="
