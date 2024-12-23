```java
  import org.cactoos.text.FormattedText;
  import org.cactoos.text.TextOf;

  import java.util.List;

  public class RtScore {

    /**
     * Calculate the Rt score for a given list of cases.
     *
     * @param cases the list of cases
     * @return the Rt score
     */
    public double calculate(List<Case> cases) {
      if (cases.isEmpty()) {
        return 0.0;
      }

      double sum = 0.0;
      for (Case aCase : cases) {
        sum += aCase.getRt();
      }

      return sum / cases.size();
    }

    /**
     * Calculate the Rt score for a given list of cases.
     *
     * @param cases the list of cases
     * @return the Rt score
     */
    public String calculateFormatted(List<Case> cases) {
      if (cases.isEmpty()) {
        return "0.0";
      }

      double sum = 0.0;
      for (Case aCase : cases) {
        sum += aCase.getRt();
      }

      return new FormattedText("%s", sum / cases.size()).asString();
    }

    public String calculateFormatted(List<Case> cases, String format) {
      if (cases.isEmpty()) {
        return "0.0";
      }

      double sum = 0.0;
      for (Case aCase : cases) {
        sum += aCase.getRt();
      }

      return new FormattedText(format, sum / cases.size()).asString();
    }
  }
```