# Personal Habit-Tracker with Pixela API

## Overview 🌟

Welcome to your Personal Habit-Tracker powered by the Pixela API! This project is designed to empower you to track and visualize your daily habits with ease. By leveraging Pixela, you can effortlessly create custom graphs, log your daily activities, update your progress dynamically, and manage your data flexibly through intuitive API interactions.

## Key Features 🚀

- **Graph Customization:** Tailor graphs to monitor diverse habit metrics.
- **Daily Activity Logging:** Log activities with precision and detail.
- **Real-time Progress Updates:** Easily update and monitor your ongoing progress.
- **Effortless Data Management:** Delete entries as needed for accurate habit tracking.

## Technologies Utilized 🛠️

- **Python:** Core language for backend logic and API interactions.
- **Requests Library:** Facilitates seamless HTTP requests to interact with the Pixela API.
- **Datetime Handling:** Ensures accurate timestamp management for habit logging.
- **Secure Environment Variables:** Safely manages sensitive data such as API tokens.

## Setup and Usage 📋

1. **Environment Setup:**
   - Obtain your Pixela `USERNAME`, `TOKEN`, and `GRAPHID`.
   - Set these variables securely as environment variables.

2. **Installation:**
   - Clone the repository:
     ```bash
     git clone https://github.com/flack74/habit-tracker.git
     cd habit-tracker
     ```
   - Install necessary dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Getting Started:**
   - Customize the Python script (`habit_tracker.py`) to suit your specific habit tracking needs.
   - Execute the script:
     ```bash
     python habit_tracker.py
     ```
   - Follow prompts to log, update, or delete habits as required.

4. **API Interaction Guide:**
   - Uncomment relevant sections in `habit_tracker.py` to create graphs, log activities, update progress, or delete entries.
   - Handle Pixela API responses to ensure smooth and effective data management.

## Example Interaction 📝

```plaintext
How much time did you spend coding today: 3 hours
Successfully updated your coding session for today: 20240717
```

## Contributing 🤝

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Implement your changes and commit them:
   ```bash
   git commit -m "Add your meaningful commit message"
   ```
4. Push changes to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request to merge your changes.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments 🙏

- Special thanks to Pixela for providing a robust API platform that enhances personal habit tracking.
- Inspired by the transformative impact of habit-tracking tools on personal productivity and well-being.

---
