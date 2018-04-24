#!/bin/sh

set -e

gh_repo="karasa-jaga-icon-theme"
gh_desc="Karasa Jaga icon themes"

cat <<- EOF

  $gh_desc
  https://github.com/rizmut/$gh_repo
  
  
EOF

temp_dir="$(mktemp -d)"
cd "build/Karasa-Jaga"
tar -cvzf ../../Karasa-Jaga.tar.gz *
cd "../../"
echo "=> Deleting old $gh_desc ..."
sudo rm -Rf "/usr/share/icons/Karasa-Jaga"
echo "=> Installing ..."
sudo mkdir -p "/usr/share/icons/Karasa-Jaga"
sudo tar -xvzf \
  "Karasa-Jaga.tar.gz" -C \
  "/usr/share/icons/Karasa-Jaga"
rm -f "Karasa-Jaga.tar.gz"
#cd "$(dirname ${BASH_SOURCE[0]})"
echo "=> Pushing to git ..."
git add .
git commit -m "New build"
git push origin master
echo "=> Done!"
