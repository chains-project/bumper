```java
  import com.jcabi.aspects.Tv;
  import com.jcabi.github.mock.MkGithub;
  import java.util.Arrays;
  import java.util.List;
  import java.util.stream.Collectors;
  import org.kohsuke.github.GHIssue;

  public final class MkGithub {
    private static final List<String> LABELS =
        Arrays.stream(new String[] {"bug", "enhancement", "question", "wontfix"})
            .map(Tv::of)
            .collect(Collectors.toList());

    public static GHIssue createIssue(String project, String title, String body) {
      return null;
    }

    public static GHIssue createIssue(String project, String title, String body, List<String> labels) {
      return null;
    }

    public static GHIssue createIssue(String project, String title, String body, String... labels) {
      return null;
    }

    public static GHIssue createIssue(String project, String title, String body, Iterable<String> labels) {
      return null;
    }
  }
```