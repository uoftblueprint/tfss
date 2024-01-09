# TFSS Email Processsing API

## Contributors
### Project Leads: 
Pierre-William Lessard, Youssef Soliman
### Senior Developers: 
Jeff Huang, Min Gi Kwon, Sarah Xu, Valerie Yip
### Junior Developers: 
Caesar Saleh, Sataphon Obra, York Hay Ng
</br></br>
# Project Setup Guide

This guide will walk you through the steps to set up and run the project.

## Clone the Repository

First, you need to clone the repository to your local machine. You can do this by running the following command in your terminal:

```sh
git clone https://github.com/uoftblueprint/tfss.git
```

After cloning the repository, navigate to the project directory:

```sh
cd tfss
```

Next, install the project dependencies. The dependencies are listed in the [`requirements.txt`](command:_github.copilot.openRelativePath?%5B%22requirements.txt%22%5D "requirements.txt") file. You can install them using `pip`:

```sh
pip install -r requirements.txt
```

## Setting Up the Environment

You need to set up your environment variables. An example of how to set them up is provided in the [`example.env`](command:_github.copilot.openRelativePath?%5B%22example.env%22%5D "example.env") file. 

Replace `YOUR_KEY_HERE` with your ChatGPT API key and `YOUR_PASSWORD` with a secure password. This password will be used to authorize requests to the Flask server.

## Running the Flask Server

The Flask server needs to be accessible over the internet for Power Automate to send HTTP requests. For production, regular deployment is recommended. However, for testing, you can use ngrok.

### Using ngrok

1. Download ngrok from [https://ngrok.com/](https://ngrok.com/).
2. Run the Flask server locally by executing the [`api.py`](command:_github.copilot.openRelativePath?%5B%22email_processing%2Fapi.py%22%5D "email_processing\api.py") script in the [`email_processing`](command:_github.copilot.openRelativePath?%5B%22email_processing%22%5D "email_processing") directory.
3. In a separate terminal, start ngrok on the same port as the Flask server (default is 5000):

```sh
ngrok http 5000
```

The output will include a "forwarding" URL in the format `<ngrok_url> -> http://localhost:5000`. The `<ngrok_url>` is the URL power automate will interact with.

## Setting Up Power Automate

To connect Power Automate to your server, you need to modify the "POST Process Email" HTTP block.

1. Set the `URI` field to the URL of your server followed by [`/email`](command:_github.copilot.openSymbolInFile?%5B%22email_processing%2Fapi.py%22%2C%22%2Femail%22%5D "email_processing/api.py"). If you're using ngrok, this would be `<ngrok_url>/email`.
2. Under the "headers" field, set the `Authorization` field to `Basic <base64credentials>`. Here, `<base64credentials>` is a Base64-encoded string of `tfss_user:<YOUR_PASSWORD>`. You can generate this string using a Base64 encoder like [https://www.base64encode.net/](https://www.base64encode.net/).

For example, if your password is `abc123`, input `tfss_user:abc123` into the encoder. The `Authorization` field would then be `Basic dGZzc191c2VyOmFiYzEyMw==`.

That's it! You've now set up the project and connected it to Power Automate.