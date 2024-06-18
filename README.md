## Name
gcp-iam-reference

## Description
This is a simple Flask application that takes the Google Cloud Platform IAM predefined roles and presents them in an easier to search and copy/paste format. I'll set up automation to regularly update this shortly, but for now I'll manually run the CLI on a regular basis to pull in new roles. 

## Installation
Pretty straight-forward, I recommend the Dockerfile but as you can tell there are almost no dependencies. 

## Usage
See here: https://gcp-iam-reference.matduggan.com/
## Support
I'm glad to fix whatever. Either open an issue here or ping me on Mastodon: https://c.im/@matdevdug

## Roadmap
* add ability to compare two roles and highlight differences between them
* improve search to not just search for services but also roles inside of those services
* add CI/CD pipeline documented here running from Gitlab so people can see build status
* add conditions for search to exclude beta

## Contributing
PRs welcome.
 
## License
MIT License
