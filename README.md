# CrackThePUF
PUF (Physical unclonable function)  a promising way to provide "silicon fingerprints" based on the delays in signal propagation with respect to key. Since PUF are prone to ML Attacks, Crack the Multi level  PUF is a part Assignment of CS771  2024-2025-w course

## How to run

1. clone the repo

2. navigate to the directory

3. install the required packages using the following command
   ```
   pip install -r requirements.txt
   
   ```
4. use the ipython notebook to train the model and test the accuracy 
    

## How to submit

1. encrypt the submit folder using the following command
   ```
   zip -e file.zip file.py
   
   ```

2. check if are able unzip the file using the following command
   ```
   unzip -P "yourpassword" file.zip
   
   ```

3. connet to ssh server using the following command
   ```
   ssh -o KexAlgorithms=diffie-hellman-group-exchange-sha1 -o HostKeyAlgorithms=ssh-rsa ccid@webhome.cc.iitk.ac.in  
   
   ```

4. Navigate to the directory where encrypted submit.zip is in local storage and submit
   ```
    scp ./file.zip ccid@webhome.cc.iitk.ac.in:/www/ccid/www/directory_name
   
   ```
5.  check if can download the file from server

    ```
    wget http://home.iitk.ac.in/~ccid/directory_name/file.zip 

    ```
