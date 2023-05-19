# school-Interface
These instructions will guide you through the process of setting up and running the Django project from the GitHub repository.

| Project Stack | Version |
| -------- | -------- |
| Django   | 4.2   |
| Python   | 3.11   |
| React   | 18   |
| MySQL   | 8.0   |

### Set-up instructions
1. Fork the repository on GitHub <br>
2. Clone the repository (replace [your-username] with your GitHub username):<br>
```bash
git clone https://github.com/[your-username]/school-Interface.git
```
3. Create virtual environment<br>
```bash
cd school-Interface
python3 -m venv env
source env/bin/activate
```
4. Install Dependencies<br>
```bash
pip install -r requirements.txt
```
5. Configuration settings<br>
  - .env and config.py templates are provided in the root. Copy these to SchoolInterface/ directory. The .env and config.py files should be in the same directory level as the settings.py file.<br>
  - Modify database values and other settings as required in .env and config.py<br>
6. Migrate Database<br>
```bash
python manage.py migrate
```

