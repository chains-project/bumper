```java
import org.junit.Assume;
import org.junit.Ignore;
import org.junit.Test;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class PGS_ProcessingGroupShapeTests {

    @Test
    public void testProcessingGroupShape() {
        // Given
        List<String> input = Arrays.asList("a", "b", "c");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithEmptyInput() {
        // Given
        List<String> input = Collections.emptyList();
        List<String> expectedOutput = Collections.emptyList();

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithNullInput() {
        // Given
        List<String> input = null;
        List<String> expectedOutput = Collections.emptyList();

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithLargeInput() {
        // Given
        List<String> input = Arrays.asList("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithDuplicateInput() {
        // Given
        List<String> input = Arrays.asList("a", "b", "c", "a", "b", "c");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithCaseInsensitiveInput() {
        // Given
        List<String> input = Arrays.asList("A", "B", "C");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithWhitespaceInput() {
        // Given
        List<String> input = Arrays.asList("  a  ", "  b  ", "  c  ");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithSpecialCharactersInput() {
        // Given
        List<String> input = Arrays.asList("a!", "b?", "c$");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithNumbersInput() {
        // Given
        List<String> input = Arrays.asList("1", "2", "3");
        List<String> expectedOutput = Collections.singletonList("1");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithNullElementInput() {
        // Given
        List<String> input = Arrays.asList("a", null, "c");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithEmptyElementInput() {
        // Given
        List<String> input = Arrays.asList("a", "", "c");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithWhitespaceElementInput() {
        // Given
        List<String> input = Arrays.asList("a", "  ", "c");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithSpecialCharactersElementInput() {
        // Given
        List<String> input = Arrays.asList("a", "!", "c");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithNumbersElementInput() {
        // Given
        List<String> input = Arrays.asList("a", "1", "c");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseInput() {
        // Given
        List<String> input = Arrays.asList("A", "b", "C");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndWhitespaceInput() {
        // Given
        List<String> input = Arrays.asList("  A  ", "  b  ", "  C  ");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndSpecialCharactersInput() {
        // Given
        List<String> input = Arrays.asList("A!", "b?", "C$");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndNumbersInput() {
        // Given
        List<String> input = Arrays.asList("A1", "b2", "C3");
        List<String> expectedOutput = Collections.singletonList("a1");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndNullElementInput() {
        // Given
        List<String> input = Arrays.asList("A", null, "C");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndEmptyElementInput() {
        // Given
        List<String> input = Arrays.asList("A", "", "C");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndWhitespaceElementInput() {
        // Given
        List<String> input = Arrays.asList("A", "  ", "C");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndSpecialCharactersElementInput() {
        // Given
        List<String> input = Arrays.asList("A", "!", "C");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndNumbersElementInput() {
        // Given
        List<String> input = Arrays.asList("A", "1", "C");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndNullAndEmptyElementInput() {
        // Given
        List<String> input = Arrays.asList("A", null, "", "C");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndWhitespaceAndSpecialCharactersElementInput() {
        // Given
        List<String> input = Arrays.asList("A", "  ", "!", "C");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndNumbersAndNullElementInput() {
        // Given
        List<String> input = Arrays.asList("A", "1", null, "C");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndEmptyAndWhitespaceElementInput() {
        // Given
        List<String> input = Arrays.asList("A", "", "  ", "C");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndWhitespaceAndSpecialCharactersAndNumbersElementInput() {
        // Given
        List<String> input = Arrays.asList("A", "  ", "!", "1", "C");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndNullAndEmptyAndWhitespaceElementInput() {
        // Given
        List<String> input = Arrays.asList("A", null, "", "  ", "C");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndWhitespaceAndSpecialCharactersAndNumbersAndNullElementInput() {
        // Given
        List<String> input = Arrays.asList("A", "  ", "!", "1", null, "C");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndEmptyAndWhitespaceAndSpecialCharactersAndNumbersAndNullElementInput() {
        // Given
        List<String> input = Arrays.asList("A", "", "  ", "!", "1", null, "C");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndWhitespaceAndSpecialCharactersAndNumbersAndNullAndEmptyElementInput() {
        // Given
        List<String> input = Arrays.asList("A", "  ", "!", "1", null, "", "C");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndAllElementTypesInput() {
        // Given
        List<String> input = Arrays.asList("A", "  ", "!", "1", null, "", "C");
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertEquals(expectedOutput, actualOutput);
    }

    @Test
    public void testProcessingGroupShapeWithPerformance() {
        // Given
        List<String> input = new ArrayList<>();
        for (int i = 0; i < 100000; i++) {
            input.add("a");
        }
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        long startTime = System.currentTimeMillis();
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);
        long endTime = System.currentTimeMillis();

        // Then
        assertEquals(expectedOutput, actualOutput);
        assertTrue(endTime - startTime < 1000);
    }

    @Test
    @Ignore("This test is too slow for Travis CI.")
    public void testProcessingGroupShapeWithVeryLargeInput() {
        // Given
        List<String> input = new ArrayList<>();
        for (int i = 0; i < 1000000; i++) {
            input.add("a");
        }
        List<String> expectedOutput = Collections.singletonList("a");

        // When
        long startTime = System.currentTimeMillis();
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);
        long endTime = System.currentTimeMillis();

        // Then
        assertEquals(expectedOutput, actualOutput);
        assertTrue(endTime - startTime < 10000);
    }

    @Test
    public void testProcessingGroupShapeWithNullOutput() {
        // Given
        List<String> input = Arrays.asList("a", "b", "c");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput == null);
    }

    @Test
    public void testProcessingGroupShapeWithEmptyOutput() {
        // Given
        List<String> input = Arrays.asList("a", "b", "c");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.isEmpty());
    }

    @Test
    public void testProcessingGroupShapeWithWhitespaceOutput() {
        // Given
        List<String> input = Arrays.asList("a", "b", "c");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).trim().isEmpty());
    }

    @Test
    public void testProcessingGroupShapeWithSpecialCharactersOutput() {
        // Given
        List<String> input = Arrays.asList("a", "b", "c");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[^a-zA-Z0-9\\s]"));
    }

    @Test
    public void testProcessingGroupShapeWithNumbersOutput() {
        // Given
        List<String> input = Arrays.asList("a", "b", "c");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[0-9]"));
    }

    @Test
    public void testProcessingGroupShapeWithNullElementOutput() {
        // Given
        List<String> input = Arrays.asList("a", null, "c");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0) == null);
    }

    @Test
    public void testProcessingGroupShapeWithEmptyElementOutput() {
        // Given
        List<String> input = Arrays.asList("a", "", "c");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).isEmpty());
    }

    @Test
    public void testProcessingGroupShapeWithWhitespaceElementOutput() {
        // Given
        List<String> input = Arrays.asList("a", "  ", "c");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).trim().isEmpty());
    }

    @Test
    public void testProcessingGroupShapeWithSpecialCharactersElementOutput() {
        // Given
        List<String> input = Arrays.asList("a", "!", "c");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[^a-zA-Z0-9\\s]"));
    }

    @Test
    public void testProcessingGroupShapeWithNumbersElementOutput() {
        // Given
        List<String> input = Arrays.asList("a", "1", "c");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[0-9]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseOutput() {
        // Given
        List<String> input = Arrays.asList("A", "b", "C");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndWhitespaceOutput() {
        // Given
        List<String> input = Arrays.asList("  A  ", "  b  ", "  C  ");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndSpecialCharactersOutput() {
        // Given
        List<String> input = Arrays.asList("A!", "b?", "C$");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndNumbersOutput() {
        // Given
        List<String> input = Arrays.asList("A1", "b2", "C3");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z0-9]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndNullElementOutput() {
        // Given
        List<String> input = Arrays.asList("A", null, "C");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndEmptyElementOutput() {
        // Given
        List<String> input = Arrays.asList("A", "", "C");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndWhitespaceElementOutput() {
        // Given
        List<String> input = Arrays.asList("A", "  ", "C");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndSpecialCharactersElementOutput() {
        // Given
        List<String> input = Arrays.asList("A", "!", "C");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndNumbersElementOutput() {
        // Given
        List<String> input = Arrays.asList("A", "1", "C");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z0-9]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndNullAndEmptyElementOutput() {
        // Given
        List<String> input = Arrays.asList("A", null, "", "C");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndWhitespaceAndSpecialCharactersElementOutput() {
        // Given
        List<String> input = Arrays.asList("A", "  ", "!", "C");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndNumbersAndNullElementOutput() {
        // Given
        List<String> input = Arrays.asList("A", "1", null, "C");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z0-9]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndEmptyAndWhitespaceElementOutput() {
        // Given
        List<String> input = Arrays.asList("A", "", "  ", "C");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndWhitespaceAndSpecialCharactersAndNumbersElementOutput() {
        // Given
        List<String> input = Arrays.asList("A", "  ", "!", "1", "C");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z0-9]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndNullAndEmptyAndWhitespaceElementOutput() {
        // Given
        List<String> input = Arrays.asList("A", null, "", "  ", "C");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndWhitespaceAndSpecialCharactersAndNumbersAndNullElementOutput() {
        // Given
        List<String> input = Arrays.asList("A", "  ", "!", "1", null, "C");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z0-9]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndEmptyAndWhitespaceAndSpecialCharactersAndNumbersAndNullElementOutput() {
        // Given
        List<String> input = Arrays.asList("A", "", "  ", "!", "1", null, "C");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z0-9]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndWhitespaceAndSpecialCharactersAndNumbersAndNullAndEmptyElementOutput() {
        // Given
        List<String> input = Arrays.asList("A", "  ", "!", "1", null, "", "C");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z0-9]"));
    }

    @Test
    public void testProcessingGroupShapeWithMixedCaseAndAllElementTypesOutput() {
        // Given
        List<String> input = Arrays.asList("A", "  ", "!", "1", null, "", "C");

        // When
        List<String> actualOutput = new PGS_ProcessingGroupShape().process(input);

        // Then
        assertTrue(actualOutput.get(0).matches("[a-zA-Z0-9]"));
    }
}
```