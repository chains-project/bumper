```java
import org.cactoos.list.ListOf;

public class RtTransaction {

    private final String id;
    private final ListOf<String> labels;
    private final Long timestamp;

    public RtTransaction(String id, ListOf<String> labels, Long timestamp) {
        this.id = id;
        this.labels = labels;
        this.timestamp = timestamp;
    }

    public String getId() {
        return id;
    }

    public ListOf<String> getLabels() {
        return labels;
    }

    public Long getTimestamp() {
        return timestamp;
    }
}
```