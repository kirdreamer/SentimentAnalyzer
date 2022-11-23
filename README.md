# Sentiment Analyzer

This is a simple sentiment analyzer using NLTK.

## Features

- Defines sentiment of the text
- Checks database for new data every minute
- Uses ORM, which provides fast communication between the database and the program.


## Usage
0. Perform a configuration in config.py and add properties "database.properties" in directory database.
Example of database.properties:
```
[db]
engine=postgresql
hostname=example.host.com
port=5432
password=
login=
name=
table=comment
```
1. Run "init_module.py".
2. Check results in your database.
3. Press Ctrl+C to interrupt the program. 
## Contributing

Contributions are always welcome!

If you have a suggestion that would make this better, please fork the repo and create a pull request.\
You can also simply open an issue with the tag "enhancement".\
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Feedback

If you have any feedback, please reach out to me via GitHub.

