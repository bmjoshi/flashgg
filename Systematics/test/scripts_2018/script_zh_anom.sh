nEvents=-1
outdir=zh_anom
dumper=../WH_anom_dumper.py
queue=tomorrow
json=json/zh_anom.json

# fggRunJobs.py --load $json \
#               -d $outdir \
#               -n 100 \
#               -q $queue \
#               --no-use-tarball --no-copy-proxy -D -P \
#               -x cmsRun $dumper maxEvents=$nEvents #copyInputMicroAOD=True

fggRunJobs.py --load $json \
              -d $outdir \
              -n 10 \
              -q $queue \
              --no-copy-proxy -D -P \
              -x cmsRun $dumper maxEvents=$nEvents copyInputMicroAOD=True