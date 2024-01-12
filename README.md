# Airbnb Console Project
## Project Overview

### Introduction
Welcome to the Airbnb Console Project! This project is the first step in a comprehensive series dedicated to cloning the Airbnb website. Our primary objective at this stage is to develop a console that facilitates the management of property listings.

### Project Purpose
The purpose of this project is to create a functional console that interacts with various classes representing essential components of the Airbnb platform. As part of a broader series, this console serves as the foundation for future developments, ultimately leading to the creation of a fully functional Airbnb clone. By focusing on listing management initially, we aim to lay the groundwork for handling user interactions and data persistence in the upcoming phases of the project.

### Key Features
- **Class Interaction:** The console allows users to interact with different classes representing crucial elements of the Airbnb ecosystem, such as users, states, cities, places, amenities, and reviews.
- **Listing Management:** With the ability to create, view, update, and delete listings, users can simulate the fundamental operations required for an online marketplace.

---

<!-- ubuntu --> <a href="https://ubuntu.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Ubuntu&color=E95420&logo=Ubuntu&logoColor=E95420&labelColor=2F333A" alt="Ubuntu"></a> <!-- fedora --> <a href="https://getfedora.org/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Fedora&color=294172&logo=Fedora&logoColor=294172&labelColor=2F333A" alt="Fedora"></a> <!-- bash --> <a href="https://www.gnu.org/software/bash/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GNU%20Bash&color=4EAA25&logo=GNU%20Bash&logoColor=4EAA25&labelColor=2F333A" alt="Bash"></a> <!-- python--> <a href="https://www.python.org" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Python&color=FFD43B&logo=python&logoColor=3776AB&labelColor=2F333A" alt="Python"></a> <!-- vim --> <a href="https://www.vim.org/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Vim&color=019733&logo=Vim&logoColor=019733&labelColor=2F333A" alt="NeoVim"></a> <!-- vs code --> <a href="https://code.visualstudio.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Visual%20Studio%20Code&color=5C2D91&logo=Visual%20Studio%20Code&logoColor=5C2D91&labelColor=2F333A" alt="VS Code"></a> <!-- git --> <a href="https://git-scm.com/" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=Git&color=F05032&logo=Git&logoColor=F05032&labelColor=2F333A" alt="Git"></a> <!-- github --> <a href="https://github.com" target="_blank"> <img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="GitHub"></a>

---

### Style Guidelines
* [pycodestyle (version 2.11.*)](https://pypi.org/project/pycodestyle/)
* [PEP8](https://pep8.org/)

### Development and Testing Environment
All development and testing were conducted on the following setup:
- **Operating System:** Ubuntu 20.04 LTS, Fedora (39)
- **Python Version:** +3.8
- **Editors Used:**
  - NVIM 0.9.*
  - Visual Studio Code 1.85.*
- **Version Control System:** Git 2.25.1

**Note:** This project was developed and tested on both Ubuntu 20.04 LTS and Fedora 39.


## Getting Started

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/airbnb-console.git
   ```

## Usage

### Running the Console
To run the Airbnb Console, open your terminal and navigate to the project directory. Then execute the following command:

```bash
python console.py
```

The console will start, and you'll see the prompt `(hbnb)`, indicating that you are now in the Airbnb Console environment.

### Console Commands
The Airbnb Console supports the following commands:

- **create:** Create a new instance.
- **show:** Display information about an instance.
- **destroy:** Delete an instance.
- **all:** Display information about all instances or all instances of a specific class.
- **update:** Update attributes of an instance.
- **quit or Ctrl+D:** Exit the console.

### Examples
Here are examples of how to use each command:

1. **create:**
   ```bash
   (hbnb) create User
   # or
   (hbnb) User.create()
   ```

   Expected Output:
   ```
   <new_user_id>
   ```

2. **show:**
   ```bash
   (hbnb) show User <user_id>
   # or
   (hbnb) User.show(<user_id>)
   ```

   Expected Output:
   ```
   [<string_representation_of_user_instance>]
   ```

3. **destroy:**
   ```bash
   (hbnb) destroy User <user_id>
   # or
   (hbnb) User.destroy(<user_id>)

   ```

   Expected Output:
   ```
   # Instance with <user_id> deleted
   ```

4. **all:**
   ```bash
   (hbnb) all
   ```

   Expected Output:
   ```
   [<string_representation_of_instance_1>, <string_representation_of_instance_2>, ...]
   ```
   ```bash
   (hbnb) all BaseModel
   # or
   (hbnb) User.all()
   ```

   Expected Output:
   ```
   [<string_representation_of_BaseModel_instance_1>, <string_representation_of_BaseModel_instance_2>, ...]
   ```

5. **update:**
   ```bash
   (hbnb) update User <user_id> name "John Doe"
   (hbnb) User.update(<user_id>, name, "John Doe")
   ```

   Expected Output:
   ```
   # Attribute 'name' of User <user_id> updated to "John Doe" create the attribute if doesn't exist.
   ```

6. **quit or Ctrl+D:**
   ```bash
   (hbnb) quit
   ```
## Data Storage and Data Persistence Explanation:

The data storage mechanism is designed to maintain data across different sessions of using the program. Here's a step-by-step explanation of how it works:

**Creation of Instances:**
When instances are created during a session using commands like create, update, etc., they are added to the __objects dictionary.

**Saving Data:**
The save method is then called to serialize the __objects dictionary and save it to the file.json file.

**Reload During Initialization:**
When the program is executed in a new session, the reload method is called during initialization.
This method reads the file.json file, deserializes the data, and populates the __objects dictionary with instances.

**Accessing Data:**
Throughout the session, any command that requires accessing instances utilizes the data in the __objects dictionary.

**Saving Changes:**
At the end of the session or when prompted by the user, the save method is called to update the file.json file with the latest data.

### Concatenate the file.json:
```bash
$ cat file.json
{"BaseModel.23fa9824-546d-4937-b92d-9e6a835abd07": {"id": "23fa9824-546d-4937-b92d-9e6a835abd07", "created_at": "2024-01-12T14:55:15.696065", "updated_at": "2024-01-12T14:55:15.696087", "__class__": "BaseModel"}, "BaseModel.ed51d529-1fea-4304-9e65-894cb73a13fb": {"id": "ed51d529-1fea-4304-9e65-894cb73a13fb", "created_at": "2024-01-12T15:45:11.046647", "updated_at": "2024-01-12T15:45:11.046666", "__class__": "BaseModel"}, "BaseModel.bcc9fcbc-92ca-4343-8bb6-728b6b993230": {"id": "bcc9fcbc-92ca-4343-8bb6-728b6b993230", "created_at": "2024-01-12T15:45:21.594380", "updated_at": "2024-01-12T15:45:21.594388", "__class__": "BaseModel"}, "User.47df44e6-4311-43b8-9dbd-092e2c2b305e": {"id": "47df44e6-4311-43b8-9dbd-092e2c2b305e", "created_at": "2024-01-12T16:00:24.893504", "updated_at": "2024-01-12T16:00:24.893523", "__class__": "User"}, "User.132a46a9-f679-41c8-ba48-830616fe1dbb": {"id": "132a46a9-f679-41c8-ba48-830616fe1dbb", "created_at": "2024-01-12T16:01:52.584668", "updated_at": "2024-01-12T16:01:52.584687", "__class__": "User"}, "BaseModel.cd82d497-4650-4ad2-a423-9ffabe365ad1": {"id": "cd82d497-4650-4ad2-a423-9ffabe365ad1", "created_at":"2024-01-12T16:03:09.347046", "updated_at": "2024-01-12T16:03:09.347068", "__class__": "BaseModel"}, "User.acbdb150-ff81-4c3a-9691-43d6d47b9945": {"id": "acbdb150-ff81-4c3a-9691-43d6d47b9945", "created_at": "2024-01-12T19:31:45.648973", "updated_at": "2024-01-12T19:31:45.648981", "__class__": "User"}}
```
## File Structure

### Project Structure:
```
./
├── models/
│   ├── engine/
│   │   ├── file_storage.py
│   │   └── __init__.py
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── __init__.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
├── tests/
│   └── test_console.py
├── AUTHORS
├── console.py
├── file.json
├── README.md
└── test_save_reload_base_model.py
```

### Explanation of Files:

- **`./models/` Directory:**
  - Contains modules for different data models used in the project.

  - **`./models/engine/` Directory:**
    - Houses the `file_storage.py` module that implements the data storage mechanism.

  - **Data Model Modules:**
    - `amenity.py`: Definition of the Amenity data model.
    - `base_model.py`: Definition of the BaseModel class, which is the base class for all other data models.
    - `city.py`: Definition of the City data model.
    - `place.py`: Definition of the Place data model.
    - `review.py`: Definition of the Review data model.
    - `state.py`: Definition of the State data model.
    - `user.py`: Definition of the User data model.

- **`./tests/` Directory:**
  - Contains test modules to ensure the functionality of the project, such as `test_console.py`.

- **`AUTHORS`:**
  - File containing the names of project authors.

- **`console.py`:**
  - The main Python file that initializes and runs the Airbnb Console.

- **`file.json`:**
  - JSON file where instances are serialized and stored using the `FileStorage` mechanism.

- **`README.md`:**
  - The main documentation file for the project.

- **`test_save_reload_base_model.py`:**
  - Test module to verify the functionality of saving and reloading instances using the `BaseModel` class.

