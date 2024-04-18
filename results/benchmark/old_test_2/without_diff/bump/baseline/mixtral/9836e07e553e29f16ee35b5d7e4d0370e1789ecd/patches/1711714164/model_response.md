Here's a possible patch for the given code:
```java
private static Matcher<String> imagePulled(final String image) {
    return new CoreMatchers.stringContains(
            String.format("Status: Downloaded newer image for %s", image)
    );
}
```
Explanation:
The error message suggests that the constructor `StringContains` is not applicable for the given argument. After checking the documentation for Hamcrest, I found that the class `StringContains` has been removed in newer versions. Instead, we should use `CoreMatchers.stringContains` which provides similar functionality.