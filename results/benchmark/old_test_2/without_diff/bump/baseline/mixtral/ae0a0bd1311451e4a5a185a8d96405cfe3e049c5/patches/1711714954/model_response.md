Here is a fixed version of the method using a `contains` method from Apache Commons Lang, which is a library that should be compatible with the one you are currently using:

```java
import org.apache.commons.lang3.StringUtils;

private static Matcher<String> imagePulled(final String image) {
    return new StringContains(
        false,
        String.format("Downloaded newer image for %s", image),
        StringUtils::contains
    );
}
```

This version of the method uses the `contains` method from Apache Commons Lang to check if the string contains the expected substring. This method should be compatible with the one you are currently using.

Note: The `StringUtils::contains` method reference is used as the matcher function for the `StringContains` class. This function reference simply calls the `contains` method from Apache Commons Lang.

I hope this helps! Let me know if you have any questions.