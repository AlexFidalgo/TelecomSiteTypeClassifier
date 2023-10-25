#!/bin/bash

extract_json_value() {
  local key="$1"
  local json="$2"
  echo "$json" | jq -r ".$key"
}

# Function to generate the form field and value
generate_field() {
  local field_name="$1"
  local field_value="$2"
  echo "-F \"$field_name=$field_value\""
}

# Function to extract JSON value by key
extract_json_value() {
  local key="$1"
  local json="$2"
  echo "$json" | jq -r ".$key"
}

# Array of form fields and values for the POST request
fields=(
  "fa_freq1=0"
  "fa_freq2=0"
  "fa_gsearch=1"
  "fa_lat=0"
  "fa_lon=0"
  "fa_dist="
  "fa_uf="
  "skip=0"
  "filter=1"
  "rpp=50"
)

# Add the "sort" fields with value "0"
for i in {0..39}; do
  fields+=("sort_$i=0")
done

# Add the "fc" fields with the exception of "fc_8"
for i in {0..7}; do
  fields+=("fc_$i=")
done

fields+=("fc_8=AC")

for i in {9..39}; do
  fields+=("fc_$i=")
done

fields+=("wfid=licencas")
fields+=("view=licenciamento")

curl_cmd="curl -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82' \
     -H 'Accept: */*' \
     -H 'Accept-Encoding: gzip, deflate, br' \
     -H 'Accept-Language: en-US,en;q=0.5' \
     -H 'Origin: https://sistemas.anatel.gov.br' \
     -H 'Host: sistemas.anatel.gov.br' \
     -H 'Referer: https://sistemas.anatel.gov.br/se/public/view/b/licenciamento.php?view=licenciamento' \
     -H 'Sec-Fetch-Dest: empty' \
     -H 'Sec-Fetch-Mode: cors' \
     -H 'Sec-Fetch-Site: same-origin' \
     -c cookies.txt \
     -b cookies.txt \
     -o response.html\
     https://sistemas.anatel.gov.br/se/public/view/b/licenciamento.php?view=licenciamento"

# Loop through the fields array and generate the field and value for the cURL command
for field in "${fields[@]}"; do
  field_and_value=($field)
  field_name="${field_and_value[0]}"
  field_value="${field_and_value[1]}"
  curl_cmd="$curl_cmd $(generate_field "$field_name" "$field_value")"
done

# Append the URL for the POST request
curl_cmd="$curl_cmd"

# Make the POST request to download the CSV file
response_json=$($curl_cmd)

# Extract the redirect URL from the JSON response
redirect_url=$(extract_json_value "redirectUrl" "$response_json")

# Construct the full URL for downloading the CSV file
download_url="https://sistemas.anatel.gov.br/se/public/view/b/export_licenciamento.php$redirect_url"

# Specify the output file name for the downloaded CSV
output_file="csv_licenciamento.csv"

# Download the CSV file using curl
curl -o "$output_file" "$download_url"

# Display a message when the download is complete
echo "CSV file downloaded: $output_file"
