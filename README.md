# AI E-commerce Product Catalog

A beauty products e-commerce catalog with intelligent filtering and search capabilities built as part of a technical assessment.

##  Overview

This project implements a product catalog viewer with AI-enhanced search functionality for beauty products including skincare, haircare, makeup, and perfume categories. The application provides an intuitive interface for browsing and filtering products with smart search capabilities.

## Features

### Core Features
- **Product Catalog Display**: Clean, responsive grid layout showcasing 12 beauty products
- **Advanced Filtering**: Filter by product name, description, category, and maximum price
- **Responsive Design**: Mobile-friendly interface with modern pink/beauty-themed styling
- **Interactive Elements**: Hover effects, product card interactions, and accessibility support

### AI Feature Implementation: Smart Product Search (Option A)
- **Natural Language Processing**: Enhanced search functionality that understands product attributes
- **Multi-field Search**: Searches across product names, descriptions, and categories simultaneously
- **Intelligent Filtering**: Combines text search with price-based filtering for refined results
- **Real-time Results**: Instant filtering without page reloads

## Technology Stack

- **Backend**: FastAPI (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **Templating**: Jinja2 templates
- **Styling**: Custom CSS with Google Fonts (Poppins)
- **Data**: JSON-based product storage
- **Server**: Uvicorn ASGI server

## Installation & Setup

### Prerequisites
- Python 3.7+
- Git

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai_ecommerce_test
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the application**
   Open your browser and navigate to: `http://127.0.0.1:8000`

## Project Structure

```
ai_ecommerce_test/
├── main.py              # FastAPI application and routing logic
├── products.json        # Product data (12 beauty products)
├── requirements.txt     # Project dependencies
├── templates/
│   └── index.html       # Main template with embedded CSS and JS
├── venv/               # Virtual environment (not tracked)
└── README.md           # This file
```

## AI Feature Choice: Recommendation System
Selected Option C - Recommendation System
Implementation Details

Rule-Based Logic: Implements intelligent filtering based on user preferences and constraints
Multi-Dimensional Filtering: Processes user inputs across product attributes (name, description, category, price)
Budget-Conscious Recommendations: Automatically filters products within specified price range
Category-Aware Suggestions: Groups and filters products by beauty categories
Real-time Processing: Server-side filtering with immediate response

Example User Scenarios

Budget-Conscious Shopper: Set max price to $20 → Shows affordable skincare and makeup options
Category Preference: Search "skincare" → Displays moisturizers, serums, and cleansers
Specific Product Hunt: Search "mascara" with $25 budget → Returns waterproof mascara recommendations
Brand/Ingredient Focus: Search "argan oil" → Suggests relevant haircare products

## Key Assumptions & Design Decisions

1. **Data Storage**: Used JSON file for rapid development instead of database connection
2. **AI Simplification**: Implemented rule-based search logic for quick execution within time constraints
3. **UI Focus**: Prioritized clean, intuitive interface over complex backend features
4. **Performance**: Optimized for small dataset; would require indexing for larger catalogs
5. **Accessibility**: Added keyboard navigation and ARIA labels for better user experience

## Design Highlights

- **Modern Aesthetics**: Beauty industry-appropriate pink gradient theme
- **Responsive Layout**: CSS Grid with mobile-first approach
- **Interactive Elements**: Smooth hover animations and transitions
- **Typography**: Professional Poppins font for enhanced readability
- **Visual Hierarchy**: Clear product information organization with rating system


##  Future Enhancements

- Integration with OpenAI API for advanced NLP capabilities
- Machine learning-based recommendation engine
- User authentication and personalized experiences
- Shopping cart and checkout functionality
- Product image support and gallery
- Advanced analytics and user behavior tracking
- Blockchain: Token-Gated Pricing: Implement loyalty tokens that provide exclusive discounts or early access to premium products, with smart contracts automatically applying benefits based on token holdings.

## Development Notes

This project was completed within the 1-hour time constraint, focusing on core functionality and clean implementation rather than production-level features. The emphasis was placed on demonstrating practical AI integration in an e-commerce context while maintaining code quality and user experience standards.

---

*Built for technical assessment - demonstrating full-stack development with AI integration capabilities.*
