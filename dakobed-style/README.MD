# Dakobed Neural Style Transfer

In this project I perform neural style transfer with the help of the Keras deep learning library.  The examples
were trained on an EC2 GPU instance.  I have also Dockerized this project, but as of yet have not been able to enable
GPU support.


### Example #1 using image of glacier peak as base & monet sunrise as style image

<img src="https://dakobed-style.s3-us-west-2.amazonaws.com/style_dir/gp_base.jpg" width="300" height="200">
<img src="https://dakobed-style.s3-us-west-2.amazonaws.com/sunrise.jpg" width="300" height="200">
<img src="https://dakobed-style.s3-us-west-2.amazonaws.com/result.png" width="300" height="200">

### Example #2 using image of mount baker as base & monet sunrise as style image

<img src="https://dakobed-style.s3-us-west-2.amazonaws.com/baker_base.jpg" width="300" height="200">
<img src="https://dakobed-style.s3-us-west-2.amazonaws.com/monet_style.jpg" width="300" height="200">
<img src="https://dakobed-style.s3-us-west-2.amazonaws.com/_at_iteration_9.png" width="300" height="200">


#### Steps for manual reproduct of Style Transfer

Launch GPU EC2 instance

bash launch.sh
bash scripts/sshEC2.sh replace-with-ec2-instance-ipv4-dns  (and edit to include path to your .pem file) 

