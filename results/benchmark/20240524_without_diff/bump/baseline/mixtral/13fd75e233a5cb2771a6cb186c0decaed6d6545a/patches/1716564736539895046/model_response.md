Here is a possible patch for the failing method:
```java
private static Matcher<String> imagePulled(final String image) {
    return new ContainsIgnoringCase(
        String.format("Status: Downloaded newer image for %s", image)
    );
}
```
This patch uses the `ContainsIgnoringCase` matcher from Hamcrest 2.2, which is a drop-in replacement for the deprecated `StringContains` matcher. This matcher has the same constructor signature as `StringContains`, so no other changes are needed.