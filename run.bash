cd $(dirname $0)
python3 -m venv .env
source .env/bin/activate
python3 -m pip install pytest

if [ $1 = "ut" ]
then
    pytest test/
elif [ $1 = "run" ]
then
    python3 src/main.py $2
else
    echo "Invalid argument !!!"
fi