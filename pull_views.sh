declare -a agents=('Abhinav' 'Abhisek' 'Anish' 'Nethaji' 'Nischal' 'Jithin' 'Phani' 'Kiran' 'Mahesh' 'Nataraj' 'Raveen' 'Prashanth')


for agent in "${agents[@]}"
do
  curl -u phani.valluri@accelerite.com:phani https://accelerite.zendesk.com/api/v2/views/search.json?query=${agent} > ${agent}.json 
done

python filter_views.py


