#!/usr/bin/env bash

mkdir -p roles
rm -f roles/*
for i in $(gcloud iam roles list --filter='etag:AA==' --format json | jq -r '.[].name'); do
  gcloud iam roles describe "${i}" --format json > "${i}"
  echo "done."
done
