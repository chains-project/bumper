```java
  import org.cactoos.iterable.LengthOf;

  import java.util.Collection;
  import java.util.Collections;
  import java.util.List;
  import java.util.stream.Collectors;

  import static io.zold.api.RtScore.RtScoreBuilder;
  import static io.zold.api.RtScore.RtScoreBuilder.rtScoreBuilder;
  import static java.util.Collections.singletonList;
  import static java.util.stream.Collectors.toList;

  public class RtScore {

    private final List<RtScoreItem> rtScoreItems;

    private RtScore(List<RtScoreItem> rtScoreItems) {
      this.rtScoreItems = Collections.unmodifiableList(rtScoreItems);
    }

    public static RtScoreBuilder rtScoreBuilder() {
      return new RtScoreBuilder();
    }

    public List<RtScoreItem> getRtScoreItems() {
      return rtScoreItems;
    }

    public static class RtScoreBuilder {

      private List<RtScoreItem> rtScoreItems = Collections.emptyList();

      public RtScoreBuilder() {
      }

      public RtScoreBuilder rtScoreItems(Collection<RtScoreItem> rtScoreItems) {
        this.rtScoreItems = new LengthOf<>(rtScoreItems).intValue() > 0
            ? rtScoreItems.stream().collect(toList())
            : singletonList(new RtScoreItem("No Data", 0));
        return this;
      }

      public RtScore build() {
        return new RtScore(rtScoreItems);
      }
    }
  }
```