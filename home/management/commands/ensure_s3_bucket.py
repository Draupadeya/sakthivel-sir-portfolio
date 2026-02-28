from django.core.management.base import BaseCommand
from django.conf import settings
import boto3


class Command(BaseCommand):
    help = 'Ensure Supabase Storage portfolio bucket exists'

    def handle(self, *args, **options):
        """Create the portfolio bucket if it doesn't exist"""
        
        # Only run if S3 storage is configured
        if not hasattr(settings, 'AWS_S3_ENDPOINT_URL'):
            self.stdout.write(
                self.style.WARNING('S3 storage not configured, skipping bucket creation')
            )
            return

        try:
            s3_client = boto3.client(
                's3',
                endpoint_url=settings.AWS_S3_ENDPOINT_URL,
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                region_name=settings.AWS_S3_REGION_NAME or 'auto'
            )

            bucket_name = settings.AWS_STORAGE_BUCKET_NAME
            
            # Try to create the bucket
            try:
                s3_client.create_bucket(Bucket=bucket_name)
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created bucket: {bucket_name}')
                )
            except s3_client.exceptions.BucketAlreadyExists:
                self.stdout.write(
                    self.style.SUCCESS(f'Bucket already exists: {bucket_name}')
                )
            except s3_client.exceptions.BucketAlreadyOwnedByYou:
                self.stdout.write(
                    self.style.SUCCESS(f'Bucket already owned by you: {bucket_name}')
                )
            except Exception as e:
                if 'BucketAlreadyExists' in str(e) or 'already exists' in str(e):
                    self.stdout.write(
                        self.style.SUCCESS(f'Bucket already exists: {bucket_name}')
                    )
                else:
                    raise

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error ensuring bucket exists: {e}')
            )
            raise
