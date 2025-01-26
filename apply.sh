[ -f ".env" ] && source .env
# Maximum number of retries
MAX_RETRIES=3
RETRY_COUNT=0


terraform fmt
terraform validate

# Function to run terraform apply
apply_terraform(){
    terraform apply --auto-approve
}

# Retry loop
while [[ $RETRY_COUNT -le $MAX_RETRIES ]]
do
    echo "Attempt #$((RETRY_COUNT + 1)) to apply Terraform, configuartion..."

    if apply_terraform; then
        echo "Terraform apply succeeded!"
        exit 0
    else
        echo "Terraform apply failed. Retrying..."
        RETRY_COUNT=$((RETRY_COUNT + 1))
    fi 

    if [[ $RETRY_COUNT -gt $MAX_RETRIES ]]; then
        echo "Terraform apply failed after $MAX_RETRIES retries."
        exit 1
    fi
done




