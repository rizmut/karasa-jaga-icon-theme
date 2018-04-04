#!/bin/sh

set -e

gh_repo="karasa-jaga-icon-theme"
gh_desc="Karasa Jaga icon themes"

cat <<- EOF

  $gh_desc
  https://github.com/rizmut/$gh_repo
  
  
EOF

temp_dir="$(mktemp -d)"

echo "=> Getting the latest version from GitHub ..."
curl -L "https://github.com/rizmut/$gh_repo/archive/master.tar.gz" -o "/tmp/$gh_repo.tar.gz"
echo "=> Unpacking archive ..."
tar -xzf "/tmp/$gh_repo.tar.gz" -C "$temp_dir"
echo "=> Deleting old $gh_desc ..."
sudo rm -f "/usr/share/icons/Karasa-Jaga"
echo "=> Installing ..."
sudo mkdir -p "/usr/share/icons/Karasa-Jaga"
cd "$temp_dir/$gh_repo-master/build/Karasa-Jaga" 
tar -cvzf ../../Karasa-Jaga.tar.gz *
cd "../../"
sudo tar -xvzf \
  "Karasa-Jaga.tar.gz" -C \
  "/usr/share/icons/Karasa-Jaga"
rm -f "Karasa-Jaga.tar.gz"
echo "=> Clearing cache ..."
rm -rf "/tmp/$gh_repo.tar.gz" "$temp_dir"
echo "=> Done!"
