```java
import org.apache.commons.lang3.StringUtils;
import org.jenkinsci.plugins.p4.client.ClientHelper;

public class CreateJFrogInstanceStep {
    public void someMethod() {
        ClientHelper clientHelper = new ClientHelper(null, null, null);
        boolean isBlank = StringUtils.isBlank(null);
    }
}
```