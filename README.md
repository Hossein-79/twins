<div align="center">
    <a href="https://github.com/Hossein-79/twins">
        <img src="readme/shield.png" alt="Logo" width="101" height="121">
    </a>
    <h1 align="center">Twins</h1>
    <p align="center">
        A simple and intuitive web application built with Django that helps you verify a smart contract's validity on Algorand blockchain. 
        <br />
        <br />
        <a href="https://twins.bellman.top" target="_blank">View Demo</a>
    </p>
</div>

## âšī¸ About The Project
![Homepage Screen Shot](readme/cover-dark.png)
Twins allows you to easily compare an Algorand application with a source file on GitHub and make sure the same source has been deployed to the Algorand blockchain and get a badge to put in your Github readme. It will even know when there's a new commit and the new source file no longer reflects the deployed version, so the verified badge would get expired.

## đ¸ Screenshots
<div style="display:flex;flex-direction:row;justify-content:space-around;">
    <img src="readme/screenshot1.png" style="width:32%">
    <img src="readme/screenshot2.png" style="width:32%">
    <img src="readme/screenshot3.png" style="width:32%">
</div>


đ [Prototype UI design on figma](https://www.figma.com/file/oTgX20Xsb73qIbMKMbG2AT/Twins?node-id=5%3A2)

## đģ Technologies used
* [Django](https://www.djangoproject.com)
* [SQLite](https://www.sqlite.org/)
* [Tailwind](https://tailwindcss.com)
* [Feather icons](https://feathericons.com)

## đĸ Getting Started
To get a local copy up and running follow these simple example steps.

### Prerequisites
<!-- TODO: CHECK WITH HOSSEIN -->
* Python ([Download link](https://www.python.org/downloads/))
* NodeJS ([Download link](https://nodejs.org/en/download/))

### Installation
1. Clone the project's repository onto your device.
```
~ git clone https://github.com/Hossein-79/twins.git
```
2. Cd into the cloned folder.
```
~ cd twins
```
3. Install nodejs dependencies in order to be able to use tailwind.
```
~ npm install
```
4. Install the python dependencies.
```
~ pip install -r requrements.txt
```
5. Get a GitHub API key from [here](https://github.com/settings/tokens) and replace the following line inside `twins/github.py`:
```
g = Github("[YOUR_API_KEY]")
```
6. Run the following commands to create the database.
```
~ python3 manage.py makemigrations
~ python3 manage.py migrate
```
7. Start the local server on port 8000 and watch for changes.
```
~ python3 manage.py runserver
```
8. (Optional) Watch for CSS changes.
```
~ npx tailwindcss -i ./twins/static/style.src.css -o ./twins/static/style.css --watch
```

## đ¤ Contributing
Twins was developed for the [Algorand GreenHouse Hackathon](https://gitcoin.co/hackathon/greenhouse). If you wish to improve this project, please fork the repo and create a pull request.

1. Fork the Project
2. Create your Contrib Branch (`git checkout -b contrib/improvements`)
3. Commit your Changes (`git commit -m 'Add some improvements'`)
4. Push to the Branch (`git push origin contrib/improvements`)
5. Open a Pull Request

## đĒĒ License
Distributed under the MIT License. See [`LICENSE`](LICENSE) for more information.

## đ¤ Contact
If you have any questions or suggestions regarding this project feel free to reach either of us.

âī¸ amousavig@icloud.com

âī¸ ho.arabi79@gmail.com
