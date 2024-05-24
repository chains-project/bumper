```java
import com.jcabi.aspects.Tv;

import java.util.ArrayList;
import java.util.List;

public class MkGithub {

    private final Tv tv = new Tv();
    private final List<String> issues = new ArrayList<>();

    public MkGithub() {
        tv.on();
    }

    public void addIssue(String issue) {
        issues.add(issue);
    }

    public void close() {
        tv.off();
    }

    public List<String> getIssues() {
        return issues;
    }
}
```