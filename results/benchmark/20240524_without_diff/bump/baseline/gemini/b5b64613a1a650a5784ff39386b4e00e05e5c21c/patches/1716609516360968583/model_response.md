```java
import static org.apache.commons.lang3.StringUtils.isAllBlank;
import static org.apache.commons.lang3.StringUtils.isNotBlank;

public class CreateJFrogInstanceStep {

    public void createJFrogInstance(String url, String username, String password) {
        if (isNotBlank(url) && isNotBlank(username) && isNotBlank(password)) {
            // Create JFrog instance
        } else {
            throw new IllegalArgumentException("URL, username, and password must be provided.");
        }
    }
}
```