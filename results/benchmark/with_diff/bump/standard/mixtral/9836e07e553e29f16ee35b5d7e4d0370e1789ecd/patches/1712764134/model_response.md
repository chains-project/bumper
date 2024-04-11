Here is the proposed patch:

```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    return new org.hamcrest.core.StringContains(java.lang.String.format("Status: Downloaded newer image for %s", image));
}
```

Explanation:
The error message indicates that the `StringContains` constructor is now expecting only one argument, while the old version expected two arguments (a boolean and a string). The boolean argument was used to specify whether the match should be case-sensitive or not. In the new version, case-sensitivity is the default behavior, so the boolean argument is no longer needed. Therefore, we can simply remove the boolean argument from the constructor call.