echo "Building docker image......"
read -p "Enter Version...." DOCKER_IMAGE_TAG
read -p "Enter name..." DOCKER_IMAGE_NAME

DOCKERFILE_REPO="./"

sudo docker build -t $DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG $DOCKERFILE_REPO


read -p "Enter Docker Hub Username: " USERNAME
read -s -p "Enter Docker Hub Password: " PASSWORD
echo ""

# gonna use the password-stdin to prevent password leak in the bash history
echo "$PASSWORD" | docker login --username "$USERNAME" --password-stdin

if [ $? -eq 0 ]; then
    echo "Successfully logged in to Docker Hub!"
else
    echo "Docker login failed. Check your credentials and try again."
fi

echo "Pushing docker image to dockerhub...."
sudo docker tag $DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG $USERNAME/$DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG
sudo docker push $USERNAME/$DOCKER_IMAGE_NAME:$DOCKER_IMAGE_TAG