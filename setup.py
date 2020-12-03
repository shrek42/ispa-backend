from setuptools import find_packages, setup


setup(
    name="app",
    long_description="longdesc",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "Flask-Migrate",
        "Flask-SQLAlchemy",
        "flask-jwt-extended",
        "PyMySQL",
        "pytest",
        "pytest-cov",
        "flake8",
        "pylint",
        "pylint-flask",
        "pylint-flask-sqlalchemy",
        "coverage",
    ],
)
