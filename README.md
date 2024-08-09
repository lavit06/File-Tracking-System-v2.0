# File-Tracking-System-v2.0
# GMS - File Tracking System + Noting System

![Logo](https://github.com/algobasket/File-Tracking-System/blob/main/staticfiles/images/logo.png)

## Description

**GMS - File Tracking System** is a robust platform designed for organizations to manage file sharing, forwarding, approval, and access across different roles, including Admin, Dakghar (file uploader), GMS, GM (General Manager), CO, DO, HOS, and more. The system enables hierarchical file forwarding among these roles and is built using the Django framework.

**GMS - Noting System** complements the File Tracking System by allowing users to upload noting documents alongside Dak documents, apply digital signatures, and forward them through various user roles, ensuring secure and organized document management. This system is also developed using Django.

## Setup Instructions 

Clone the repository Or Download the latest release 
  ```shell
   > git clone https://github.com/algobasket/File-Tracking-System-v2.0.git 
   ```

### Latest Release 
https://github.com/algobasket/File-Tracking-System-v2.0/releases   

### 1. Put IP in .env file
### 2. Replace local domain in `nginx.config` and `.env` file
### 3. Change `ENV_TYPE` in `.env` file:
   - `local` if you want to run locally
   - `docker` or `production` for other environments


## Installation

### Windows Installation
1. Open PowerShell with administrative privileges.
2. Navigate to the project root.
    ```shell
    > cd File-Tracking-System-v2.0
    ```
3. Run the deployment script:
    ```shell
    File-Tracking-System-v2.0 >./deploy-docker-windows.ps1
    ```

### Linux Installation
1. On a Linux Ubuntu system, navigate to the project root.
    ```shell
    > cd File-Tracking-System-v2.0
    ```
2. Make the scripts executable:
    ```shell
    File-Tracking-System-v2.0 > chmod +x add-host-entry.sh
    File-Tracking-System-v2.0 > chmod +x deploy-docker-linux.sh
    ```
3. Run the deployment script:
    ```shell
    File-Tracking-System-v2.0 > ./deploy-docker-linux.sh
  

 ### Docker Installation
 1. Installing via Docker 
    ```
    File-Tracking-System-v2.0 > docker-compose up --build -d
    ```
 2. Rerun Docker after changes
    ```
    File-Tracking-System-v2.0 > docker-compose down
    File-Tracking-System-v2.0 > docker-compose up --build -d
    ```
## Accessing the Application

- The application will be running at: [http://efhz.lan/](http://efhz.lan/)
- PhpMyAdmin will be running at: [http://efhz.lan:8080/](http://efhz.lan:8080/)
- You can change efhz.lan in .env file
### LAN Access
- App: `http://LAN-IP.lan/` 
- PhpMyAdmin: `http://LAN-IP.lan:8080/`

## Conclusion
The GMS - File Tracking System offers a comprehensive solution for managing file sharing, approval, and access within an organization. With straightforward setup and installation instructions, the system can be deployed on both Windows and Linux platforms. Ensure proper configuration of your .env file for your specific environment, and experience seamless file management with GMS.

Feel free to fork the repository, star it, or contact us for any assistance. Consider supporting or sponsoring the project if you find it valuable.
