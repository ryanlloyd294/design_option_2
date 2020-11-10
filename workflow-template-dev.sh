export PROJECT=udemy-course-292015
export REGION=europe-west2
export ZONE=europe-west2-b
export TEMPLATE_ID=pyspark-test-1


gcloud dataproc workflow-templates create \
  $TEMPLATE_ID --region $REGION

gcloud dataproc workflow-templates set-managed-cluster \
  $TEMPLATE_ID \
  --region $REGION \
  --zone $ZONE \
  --cluster-name three-node-cluster \
  --master-machine-type n1-standard-4 \
  --master-boot-disk-size 500 \
  --worker-machine-type n1-standard-4 \
  --worker-boot-disk-size 500 \
  --num-workers 2 \
  --image-version 1.4-ubuntu \
  --metadata='PIP_PACKAGES=future==0.18.2
  gcloud==0.18.3 google==3.0.0
  google-api-core==1.22.3 google-api-python-client==1.12.3
  google-auth==1.22.0 google-auth-httplib2==0.0.4
  google-cloud==0.34.0 google-cloud-bigquery==2.0.0
  google-cloud-core==1.4.2 google-cloud-dataproc==2.0.2
  google-cloud-vision==2.0.0 google-crc32c==1.0.0
  google-resumable-media==1.0.0 googleapis-common-protos==1.52.0 six==1.13.0
  findspark' \
  --initialization-actions=gs://dataproc-initialization-actions/python/pip-install.sh,gs://envs-demo-rl/init-dev.sh \
  --properties "spark:spark.jars=gs://spark-lib/bigquery/spark-bigquery-latest.jar"


export STEP_ID=step-1

gcloud dataproc workflow-templates add-job pyspark \
  file:///design_option_2/main.py \
  --step-id $STEP_ID \
  --workflow-template $TEMPLATE_ID \
  --region $REGION

gcloud dataproc workflow-templates instantiate \
  $TEMPLATE_ID --region $REGION