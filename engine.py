import threading
import queue
import chess.engine
from config import BLACK, WIDTH

# Initialize Stockfish engine (ensure the path is correct for your system)
engine = chess.engine.SimpleEngine.popen_uci(r"engine\stockfish-windows-x86-64-avx2\stockfish\stockfish-windows-x86-64-avx2.exe")

# Create a queue to send results from the engine thread to the main thread
result_queue = queue.Queue()

# This function runs the analysis in a separate thread
def engine_analysis_thread(board, time_limit=0.1, multipv=7):
    try:
        # Run the analysis in the background
        analysis = engine.analyse(board, chess.engine.Limit(time=time_limit), multipv=multipv)

        # Put the results into the queue so the main thread can access it
        result_queue.put(analysis)
    except Exception as e:
        result_queue.put(f"Error: {e}")

def draw_section(screen, board, font, y_offset):
    # Start the engine analysis in a separate thread
    analysis_thread = threading.Thread(target=engine_analysis_thread, args=(board,))
    analysis_thread.start()

    # While the analysis is running, you can draw a loading message or similar
    engine_lines = []
    for line in engine_lines:
        line_text = font.render(line, True, BLACK)
        screen.blit(line_text, (WIDTH + 20, y_offset))
        y_offset += 40

    # After starting the analysis, check for results in the queue
    analysis_thread.join()  # Wait for the analysis thread to finish

    # Get the result from the queue
    if not result_queue.empty():
        analysis = result_queue.get()

        if isinstance(analysis, str):
            # If there's an error message from the thread, display it
            engine_lines = [analysis]
        else:
            # Process the analysis results
            score = analysis[0]['score']
            engine_lines = []

            # Display the current evaluation of the position
            if score.is_mate():
                if score.relative.score() > 0:
                    engine_lines.append(f"M{score.relative.abstractmate()}")
                else:
                    engine_lines.append(f"M{score.relative.abstractmate()}")
            else:
                current_score = score.relative.score() / 100  # Convert centi-pawns to pawns
                engine_lines.append(f"Stockfish 17 Evaluation: {current_score * (2 * score.turn - 1):.2f}")

            # Display the suggested moves and their scores
            for idx, info in enumerate(analysis):
                moves = info['pv'][:5]  # The first move in the principal variation (best move)
                moves_str = ", ".join([str(move) for move in moves])  # Join first 5 moves
                move_score = info['score'].relative.score() / 100 * (2 * score.turn - 1) if info['score'] else None  # Convert to pawns
                engine_lines.append(f"{move_score:.2f} - {moves_str}" if move_score is not None else f"{moves_str}")

            # Display engine lines on the screen
            for line in engine_lines:
                line_text = font.render(line, True, BLACK)
                screen.blit(line_text, (WIDTH + 20, y_offset))
                y_offset += 40

# Don't forget to quit the engine when done
def quit_engine():
    engine.quit()