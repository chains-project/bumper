Here is a fixed version of the `imagePulled` method that should resolve the Hamcrest dependency issue:

```java
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.core.StringContains.containsString;

private static Matcher<String> imagePulled(final String image) {
    return containsString(String.format("Status: Downloaded newer image for %s", image));
}
```

This version of the method uses the `containsString` method from the `StringContains` class directly, instead of using the constructor. This should resolve the issue with the constructor not being found.