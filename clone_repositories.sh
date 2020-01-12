
while IFS=, read -r col1 col2
do
    echo "Started Cloning Repository  --  $col1"
    git clone https://github.com/$col1
    echo "Done Cloning Repository  --  $col1"
done < repository_mining_data.csv


