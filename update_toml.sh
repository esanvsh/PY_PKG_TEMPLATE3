
# The initial version
if [ -f .env ]
then
   eval "$(
   cat .env | awk '!/^\s*#/' | awk '!/^\s*$/' | while IFS='' read -r line; do
     key=$(echo "$line" | cut -d '=' -f 1);
     value=$(echo "$line" | cut -d '=' -f 2-);
     echo "export $key=\"$value\"";
   done)"
fi
#set -a && source .env && set +a
echo "$PROJECT_NAME"
echo "${GITHUB_USER_NAME}"
sed "s/GITHUB_USER_NAME/$GITHUB_USER_NAME/g" pyproject.toml > pyproject1.toml
echo "${REPO_NAME}"
sed "s/REPO_NAME/$REPO_NAME/g" pyproject1.toml > pyproject2.toml
echo "${AUTHOR_EMAIL}"
sed "s/AUTHOR_EMAIL/$AUTHOR_EMAIL/g" pyproject2.toml > pyproject3.toml
echo "${LICENSE_NAME}"
sed "s/LICENCSE_NAME/$LICENCSE_NAME/g" pyproject3.toml > pyproject4.toml


# read_env() {
#         local filename="${1:-.env}"
#         if [ ! -f "$filename" ]; then
#                 echo "missing ${filename} file"
#                 exit 1
#         fi
#         echo "Reading $filename"
#         while read -r LINE; do
#                 # Remove leading and trailing whitespaces, and carriage return
#                 CLEANED_LINE=$(echo "$LINE" | awk '{$1=$1};1' | tr -d '\r')
#                 if [[ $iCLEANED_LINE != '#'* ]] && [[ $CLEANED_LINE == *'='* ]]; then
#                         echo "$CLEANED_LINE"
#                         export "$CLEANED_LINE"
#                 fi
#         done < "$filename"
# }