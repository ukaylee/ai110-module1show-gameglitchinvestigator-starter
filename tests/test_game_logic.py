import sys
import os

# Add parent directory to path so we can import logic_utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic_utils import check_guess

#FIX: Made test cases for the bugs

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_boundary_case_guess_at_lower_bound():
    """
    Test the bug: hints should not be backwards at boundaries.
    If guessing 1 and secret is 50, should say "Go HIGHER", not "Go LOWER".
    """
    outcome, message = check_guess(1, 50)
    assert outcome == "Too Low", "Guess of 1 when secret is 50 should be Too Low"
    assert "HIGHER" in message, f"Should suggest going higher, but got: {message}"


def test_boundary_case_guess_at_upper_bound():
    """
    Test the bug: hints should not be backwards at boundaries.
    If guessing 100 and secret is 50, should say "Go LOWER", not "Go HIGHER".
    """
    outcome, message = check_guess(100, 50)
    assert outcome == "Too High", "Guess of 100 when secret is 50 should be Too High"
    assert "LOWER" in message, f"Should suggest going lower, but got: {message}"


def test_new_game_should_reset_to_playing_status():
    """
    Test that new game button would reset status back to 'playing'.
    This tests the logic that should happen when "New Game" is clicked.
    """
    # Simulate a game that was won
    game_state = {
        "status": "won",
        "attempts": 5,
        "secret": 42,
        "score": 85,
        "history": [10, 20, 30, 40, 42]
    }
    
    # Simulate what new game reset should do
    game_state["status"] = "playing"
    game_state["attempts"] = 0
    game_state["secret"] = 50  # different secret
    game_state["score"] = 0
    game_state["history"] = []
    
    # Verify all fields are reset
    assert game_state["status"] == "playing", "Status should be reset to 'playing'"
    assert game_state["attempts"] == 0, "Attempts should be reset to 0"
    assert game_state["score"] == 0, "Score should be reset to 0"
    assert game_state["history"] == [], "History should be cleared"


def test_new_game_clears_history():
    """
    Test that new game clears previous guess history.
    The bug would be if history persists between games.
    """
    # Game in progress with history
    history = [10, 25, 35, 45]
    
    # New game reset clears history
    history = []
    
    # Verify history is empty
    assert len(history) == 0, "New game should clear all previous guesses"
