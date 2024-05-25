Here is a possible patch for the failing code:

```java
private static Matcher<String> imagePulled(final String image) {
    return new containsString(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```

This patch uses the `containsString` method from the `org.hamcrest.CoreMatchers` class, which was added in JUnit 4.11. This method is a replacement for the deprecated `StringContains` constructor.

Note that you may need to import the `CoreMatchers` class at the beginning of your file if it is not already imported. You can do this by adding the following line at the beginning of your file:

```java
import static org.hamcrest.CoreMatchers.containsString;
```

I hope this helps! Let me know if you have any questions.