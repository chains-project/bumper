```java
  import de.gwdg.metadataqa.api.json.JsonBranch;
  import java.util.Map;
  import java.util.stream.Collectors;
  import java.util.stream.Stream;

  public class MarcFactory {
    public static Map<String, JsonBranch> getBranches(String input) {
      Map<String, JsonBranch> branches =
          Stream.of(input.split(" "))
              .map(String::trim)
              .filter(s -> !s.isEmpty())
              .map(JsonBranch::new)
              .collect(Collectors.toMap(JsonBranch::getBranch, b -> b));
      return branches;
    }
  }
```