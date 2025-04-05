# Inventory Insights – Preswald Data Dashboard

**Inventory Insights** is an interactive data dashboard built using [Preswald](https://app.preswald.com). It is designed to explore and analyze a sample inventory dataset through a clean user interface with real-time filtering, search, and visualization capabilities.

This application demonstrates how Preswald enables the creation of powerful, no-frontend dashboards using just Python and configuration files.

---

## Features

- Load and visualize inventory data from a CSV file
- Interactive sidebar that includes:
  - Dropdown menu to select an item
  - Checkbox to toggle between full dataset and filtered view
  - Sliders to control minimum price and quantity thresholds
  - Text input for searching items by name
- Scatter plot showing Quantity vs. Price for visual analysis
- User feedback through alert messages when no items match the selected filters
- Custom branding using a logo, favicon, and color theme (visible with sidebar)

---

## Dataset

The application uses a CSV file located at `data/items.csv`. The dataset contains inventory information with the following columns:

- **Item** – Name or identifier of the item
- **Quantity** – Units in stock
- **Price** – Unit price in dollars

Each row in the dataset represents a single inventory item.

---

## Getting Started

To run the application:

1. Log into [Preswald](https://app.preswald.com) using your GitHub account.
2. Create a new project.
3. Upload your dataset to the `data/` folder with the filename `items.csv`.
4. Replace the default `hello.py` and `preswald.toml` with the versions from this project.
5. Open the Preview tab to test the application.
6. Use the Share button to deploy the app and generate a public link.

---

## Configuration and Customization

Custom branding and data source settings are defined in `preswald.toml`. This includes:

- Application title
- Sidebar logo and browser favicon
- Primary and accent colors
- Dataset registration under `[data.my_dataset]`

To apply branding changes, ensure the `sidebar()` component is used in `hello.py`.

---

## License

This project is for demonstration and educational purposes. Feel free to use and adapt it for your own Preswald projects.

---

## Author

Created by Safiullah Saif.  
For questions or feedback, please reach out via GitHub or the project repository.
