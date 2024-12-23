```java
import static org.junit.Assume.assumeTrue;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;

@RunWith(Parameterized.class)
public class PGS_MorphologyGroupShapeTests {

  private static final double DELTA = 1e-6;

  private final String name;
  private final String[] input;
  private final String[] result;

  public PGS_MorphologyGroupShapeTests(String name, String[] input, String[] result) {
    this.name = name;
    this.input = input;
    this.result = result;
  }

  @Parameters(name = "{index}: {0}")
  public static List<Object[]> data() {
    return Arrays.asList(
        new Object[][] {
          {
            "empty",
            new String[] {"empty"},
            new String[] {"empty"},
          },
          {
            "one",
            new String[] {"one"},
            new String[] {"one"},
          },
          {
            "two",
            new String[] {"one", "two"},
            new String[] {"one", "two"},
          },
          {
            "three",
            new String[] {"one", "two", "three"},
            new String[] {"one", "two", "three"},
          },
          {
            "four",
            new String[] {"one", "two", "three", "four"},
            new String[] {"one", "two", "three", "four"},
          },
          {
            "five",
            new String[] {"one", "two", "three", "four", "five"},
            new String[] {"one", "two", "three", "four", "five"},
          },
          {
            "six",
            new String[] {"one", "two", "three", "four", "five", "six"},
            new String[] {"one", "two", "three", "four", "five", "six"},
          },
          {
            "seven",
            new String[] {"one", "two", "three", "four", "five", "six", "seven"},
            new String[] {"one", "two", "three", "four", "five", "six", "seven"},
          },
          {
            "eight",
            new String[] {"one", "two", "three", "four", "five", "six", "seven", "eight"},
            new String[] {"one", "two", "three", "four", "five", "six", "seven", "eight"},
          },
          {
            "nine",
            new String[] {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"},
            new String[] {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"},
          },
          {
            "ten",
            new String[] {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"},
            new String[] {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"},
          },
        });
  }

  @Test
  public void testGroupShape() {
    assumeTrue(input.length > 1);
    List<String> actual =
        Arrays.stream(input)
            .map(
                s ->
                    s.replaceAll("\\s+", "")
                        .replaceAll("\\(", "")
                        .replaceAll("\\)", "")
                        .replaceAll(",", ""))
            .collect(Collectors.toList());
    Collections.sort(actual);
    List<String> expected =
        Arrays.stream(result)
            .map(
                s ->
                    s.replaceAll("\\s+", "")
                        .replaceAll("\\(", "")
                        .replaceAll("\\)", "")
                        .replaceAll(",", ""))
            .collect(Collectors.toList());
    Collections.sort(expected);
    assertEquals(expected, actual);
  }

  private void assertEquals(List<String> expected, List<String> actual) {
    assertEquals(expected.size(), actual.size());
    for (int i = 0; i < expected.size(); i++) {
      assertEquals(expected.get(i), actual.get(i));
    }
  }
}
```