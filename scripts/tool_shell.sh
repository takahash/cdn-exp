split -b 2m -d --verbose noaa-12_256k.dat /var/www/html/files_2m/noaa-12_256k.dat-

num=1
for file in *; do
        mv $file $num
        num=$(expr $num + 1)
done