```java
import org.cactoos.iterable.LengthOf;

public class RtScore {
    public RtScore(String rtScore) {
        // Initialize the score
        this.rtScore = rtScore;
    }

    // Get the score
    public String getScore() {
        return rtScore;
    }

    // Calculate the score
    public int calculateScore() {
        // Check if the score is valid
        if (rtScore == null || rtScore.isEmpty()) {
            return 0;
        }

        // Split the score into tokens
        String[] tokens = rtScore.split("-");

        // Check if the score has the correct format
        if (tokens.length != 2) {
            return 0;
        }

        // Get the first and second tokens
        String firstToken = tokens[0];
        String secondToken = tokens[1];

        // Check if the first token is a number
        try {
            Integer.parseInt(firstToken);
        } catch (NumberFormatException e) {
            return 0;
        }

        // Check if the second token is a number
        try {
            Integer.parseInt(secondToken);
        } catch (NumberFormatException e) {
            return 0;
        }

        // Calculate the score
        int score = Integer.parseInt(firstToken) * 10 + Integer.parseInt(secondToken);

        // Return the score
        return score;
    }

    // Check if the score is valid
    public boolean isValidScore() {
        // Check if the score is valid
        return calculateScore() > 0;
    }

    // Get the length of the score
    public int getLength() {
        return new LengthOf<>(rtScore).intValue();
    }

    // Get the first token of the score
    public String getFirstToken() {
        // Split the score into tokens
        String[] tokens = rtScore.split("-");

        // Return the first token
        return tokens[0];
    }

    // Get the second token of the score
    public String getSecondToken() {
        // Split the score into tokens
        String[] tokens = rtScore.split("-");

        // Return the second token
        return tokens[1];
    }

    // Get the score as a string
    public String toString() {
        return rtScore;
    }

    // Private fields
    private final String rtScore;
}
```