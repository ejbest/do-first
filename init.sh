[ -f ".env" ] && source .env
python insert.py DEVOPS-1234 TESTING3

terraform init -upgrade \
                -reconfigure \
                -backend-config="endpoint=$(vault kv get -field=S3_MINIO_ENDPOINT ejbest/terraform/s3_minio)" \
                -backend-config="bucket=$(vault kv get -field=S3_MINIO_BUCKET ejbest/terraform/s3_minio)" \
                -backend-config="access_key=$(vault kv get -field=S3_MINIO_ACCESS_KEY ejbest/terraform/s3_minio)" \
                -backend-config="secret_key=$(vault kv get -field=S3_MINIO_SECRET_KEY ejbest/terraform/s3_minio)" \
                -backend-config="region=$(vault kv get -field=S3_MINIO_REGION ejbest/terraform/s3_minio)" \
                -backend-config="key=gcp-install-2"
terraform fmt


