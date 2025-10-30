
### 7. Обновленный `main.py`

"""
Main Application Entry Point
ViolenceTracker Pro - Advanced Violence Detection System
"""

import sys
import os

# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from PyQt5.QtWidgets import QApplication
from src.gui_components import AdvancedViolenceDetectorApp

def main():
    """Main application entry point"""
    try:
        # Create application instance
        app = QApplication(sys.argv)
        app.setApplicationName("ViolenceTracker Pro")
        app.setApplicationVersion("1.0.0")
        
        # Create and show main window
        window = AdvancedViolenceDetectorApp()
        window.show()
        
        # Start event loop
        return app.exec_()
        
    except Exception as e:
        print(f"Application error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())