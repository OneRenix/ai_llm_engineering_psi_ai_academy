"""
Dice Rolling Tool for MCP Server

This module provides a comprehensive dice rolling utility that supports
standard tabletop RPG dice notation. It can handle various dice types,
multiple rolls, and keep/drop mechanics.

Supported notation formats:
- "1d20" - Roll one 20-sided die
- "2d6" - Roll two 6-sided dice and sum them
- "4d6k3" - Roll four 6-sided dice, keep the highest 3
- "1d100" - Roll one 100-sided die (percentile)

Features:
- Standard dice notation parsing
- Multiple roll support
- Keep/drop highest/lowest dice
- Formatted output for MCP integration

Author: AI Assistant
Date: 2024
"""

import random
import re


class DiceRoller:
    """
    A comprehensive dice rolling utility for tabletop RPGs and games.
    
    This class parses standard dice notation and provides methods for
    rolling dice with various configurations including keep/drop mechanics.
    
    Attributes:
        notation (str): Dice notation string (e.g., "2d6k1")
        num_rolls (int): Number of times to roll the dice
        dice_pattern (re.Pattern): Compiled regex pattern for parsing notation
    """
    
    def __init__(self, notation: str, num_rolls: int = 1):
        """
        Initialize the DiceRoller with notation and roll count.
        
        Args:
            notation (str): Dice notation in format "XdYkZ" where:
                X = number of dice to roll
                Y = number of sides on each die
                Z = number of dice to keep (optional)
            num_rolls (int, optional): Number of times to roll. Defaults to 1.
            
        Examples:
            >>> roller = DiceRoller("2d6", 3)
            >>> roller = DiceRoller("4d6k3")  # Roll 4d6, keep highest 3
        """
        self.notation = notation
        self.num_rolls = num_rolls
        
        # Compile regex pattern for parsing dice notation
        # Pattern matches: (\d+)d(\d+)(k(\d+))?
        # Groups: 1=num_dice, 2=dice_sides, 4=keep_count (optional)
        self.dice_pattern = re.compile(r"(\d+)d(\d+)(k(\d+))?")

    def roll_dice(self) -> tuple[list[int], list[int]]:
        """
        Roll dice according to the notation and return all rolls and kept rolls.
        
        This method parses the dice notation, generates random rolls,
        sorts them, and applies keep/drop mechanics.
        
        Returns:
            tuple[list[int], list[int]]: Tuple of (all_rolls, kept_rolls)
            
        Raises:
            ValueError: If the dice notation is invalid
            
        Example:
            >>> roller = DiceRoller("4d6k3")
            >>> all_rolls, kept_rolls = roller.roll_dice()
            >>> print(f"All: {all_rolls}, Kept: {kept_rolls}")
            All: [6, 4, 2, 1], Kept: [6, 4, 2]
        """
        # Parse the dice notation using regex
        match = self.dice_pattern.match(self.notation)
        if not match:
            raise ValueError(f"Invalid dice notation: {self.notation}. Use format 'XdY' or 'XdYkZ'")

        # Extract components from the regex match
        num_dice = int(match.group(1))      # Number of dice to roll
        dice_sides = int(match.group(2))    # Number of sides on each die
        keep = int(match.group(4)) if match.group(4) else num_dice  # How many to keep

        # Generate random rolls for each die
        rolls = [random.randint(1, dice_sides) for _ in range(num_dice)]
        
        # Sort rolls in descending order (highest first)
        rolls.sort(reverse=True)
        
        # Keep only the specified number of highest rolls
        kept_rolls = rolls[:keep]

        return rolls, kept_rolls

    def roll_multiple(self) -> list[dict]:
        """
        Roll the dice multiple times according to num_rolls.
        
        This method performs multiple rolls and returns detailed results
        for each roll including individual dice values and totals.
        
        Returns:
            list[dict]: List of dictionaries containing roll results:
                - rolls: List of all dice values
                - kept: List of kept dice values
                - total: Sum of kept dice values
                
        Example:
            >>> roller = DiceRoller("2d6", 3)
            >>> results = roller.roll_multiple()
            >>> for result in results:
            ...     print(f"Rolls: {result['rolls']}, Total: {result['total']}")
        """
        results = []
        for _ in range(self.num_rolls):
            # Roll the dice for this iteration
            rolls, kept_rolls = self.roll_dice()
            
            # Store the results
            results.append({
                "rolls": rolls,           # All dice values
                "kept": kept_rolls,       # Kept dice values
                "total": sum(kept_rolls)  # Sum of kept dice
            })
        return results

    def __str__(self) -> str:
        """
        Return a formatted string representation of the dice roll results.
        
        The format depends on the number of rolls:
        - Single roll: "ROLLS: X, Y -> RETURNS: Z"
        - Multiple rolls: "Roll 1: ROLLS: X, Y -> RETURNS: Z\nRoll 2: ..."
        
        Returns:
            str: Formatted string representation of the dice roll results
            
        Example:
            >>> roller = DiceRoller("2d6", 1)
            >>> print(roller)
            ROLLS: 6, 2 -> RETURNS: 8
            
            >>> roller = DiceRoller("1d20", 3)
            >>> print(roller)
            Roll 1: ROLLS: 15 -> RETURNS: 15
            Roll 2: ROLLS: 8 -> RETURNS: 8
            Roll 3: ROLLS: 19 -> RETURNS: 19
        """
        if self.num_rolls == 1:
            # Single roll - simple format
            rolls, kept_rolls = self.roll_dice()
            return f"ROLLS: {', '.join(map(str, rolls))} -> RETURNS: {sum(kept_rolls)}"
        else:
            # Multiple rolls - detailed format with roll numbers
            results = self.roll_multiple()
            result_strs = []
            
            for i, result in enumerate(results, 1):
                roll_str = f"Roll {i}: ROLLS: {', '.join(map(str, result['rolls']))} -> RETURNS: {result['total']}"
                result_strs.append(roll_str)
            
            return "\n".join(result_strs)


if __name__ == "__main__":
    """
    Command-line interface for testing the DiceRoller.
    
    When run directly, this script:
    1. Prompts for dice notation and number of rolls
    2. Creates a DiceRoller instance
    3. Displays the results
    
    Usage:
        python dice_roller.py
        
    Example interaction:
        Enter dice notation (e.g., 2d20k1): 4d6k3
        Number of rolls: 2
        Roll 1: ROLLS: 6, 5, 4, 2 -> RETURNS: 15
        Roll 2: ROLLS: 6, 6, 3, 1 -> RETURNS: 15
    """
    # Get user input for dice notation
    notation = input("Enter dice notation (e.g., 2d20k1): ")
    
    # Get user input for number of rolls
    num_rolls_input = input("Number of rolls: ") or "1"
    num_rolls = int(num_rolls_input)
    
    # Create and use the dice roller
    dice_roller = DiceRoller(notation, num_rolls)
    print(dice_roller) 