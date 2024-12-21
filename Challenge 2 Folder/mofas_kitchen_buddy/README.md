# Mofa's Kitchen Buddy - API Documentation

## Overview
Mofa's Kitchen Buddy is a backend system for managing ingredients, storing recipes, and suggesting dishes based on available items and user preferences. This system integrates a chatbot powered by a Large Language Model (LLM) for personalized recipe recommendations.

---

## Endpoints

### 1. **Ingredients Management**

#### List Ingredients
- **Endpoint:** `GET /api/ingredients/`
- **Description:** Retrieves the list of all available ingredients.
- **Response:**
  ```json
  [
      {
          "id": 1,
          "name": "sugar",
          "quantity": 2,
          "unit": "cups"
      }
  ]
  ```

#### Add Ingredient
- **Endpoint:** `POST /api/ingredients/`
- **Description:** Adds a new ingredient.
- **Request Body:**
  ```json
  {
      "name": "flour",
      "quantity": 1,
      "unit": "kg"
  }
  ```
- **Response:**
  ```json
  {
      "id": 2,
      "name": "flour",
      "quantity": 1,
      "unit": "kg"
  }
  ```

#### Update Ingredient
- **Endpoint:** `PUT /api/ingredients/{id}/`
- **Description:** Updates an existing ingredient.
- **Request Body:**
  ```json
  {
      "quantity": 3
  }
  ```
- **Response:**
  ```json
  {
      "id": 1,
      "name": "sugar",
      "quantity": 3,
      "unit": "cups"
  }
  ```

#### Delete Ingredient
- **Endpoint:** `DELETE /api/ingredients/{id}/`
- **Description:** Deletes an ingredient.
- **Response:** `204 No Content`

---

### 2. **Recipe Management**

#### List Recipes
- **Endpoint:** `GET /api/recipes/`
- **Description:** Retrieves the list of all stored recipes.
- **Response:**
  ```json
  [
      {
          "id": 1,
          "title": "Chocolate Cake",
          "ingredients": [
              {"name": "flour", "quantity": 2, "unit": "cups"},
              {"name": "sugar", "quantity": 1, "unit": "cup"}
          ],
          "instructions": "Mix and bake.",
          "is_favorite": false,
          "image": "http://127.0.0.1:8000/media/recipes/chocolate_cake.jpg"
      }
  ]
  ```

#### Add Recipe
- **Endpoint:** `POST /api/recipes/`
- **Description:** Adds a new recipe.
- **Request Body (Form Data):**
  ```
  title: "Chocolate Cake"
  ingredients: [{"name": "sugar", "quantity": "1", "unit": "cup"}]
  instructions: "Mix and bake."
  image: (file upload)
  ```
- **Response:**
  ```json
  {
      "id": 1,
      "title": "Chocolate Cake",
      "ingredients": [
          {"name": "sugar", "quantity": "1", "unit": "cup"}
      ],
      "instructions": "Mix and bake.",
      "is_favorite": false,
      "image": "http://127.0.0.1:8000/media/recipes/chocolate_cake.jpg"
  }
  ```

#### Update Recipe
- **Endpoint:** `PUT /api/recipes/{id}/`
- **Description:** Updates an existing recipe.
- **Request Body:**
  ```json
  {
      "is_favorite": true
  }
  ```
- **Response:**
  ```json
  {
      "id": 1,
      "title": "Chocolate Cake",
      "ingredients": [
          {"name": "sugar", "quantity": "1", "unit": "cup"}
      ],
      "instructions": "Mix and bake.",
      "is_favorite": true,
      "image": "http://127.0.0.1:8000/media/recipes/chocolate_cake.jpg"
  }
  ```

#### Delete Recipe
- **Endpoint:** `DELETE /api/recipes/{id}/`
- **Description:** Deletes a recipe.
- **Response:** `204 No Content`

---

### 3. **Chatbot Integration**

#### Interact with Chatbot
- **Endpoint:** `POST /api/chatbot/`
- **Description:** Sends a user query to the chatbot and receives recipe suggestions.
- **Request Body:**
  ```json
  {
      "query": "I want something sweet."
  }
  ```
- **Response:**
  ```json
  {
      "suggestions": [
          "Chocolate Cake",
          "Brownie"
      ]
  }
  ```

---

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run migrations:
   ```bash
   python manage.py migrate
   ```
3. Start the server:
   ```bash
   python manage.py runserver
   ```
4. Access the API at `http://127.0.0.1:8000/api/`.

---

## Notes
- Media files (recipe images) are served from the `/media/` directory.
- Use `DRF`'s browsable API for easy interaction during development.

