Here's a proposed patch to fix the error:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        );
    }
```

The error is caused by the fact that the `StringContains` constructor taking two parameters has been removed in the new library version. To fix the error, we can use the alternative constructor that takes a single `String` argument, like this:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            String.format("Status: Downloaded newer image for %s", image)
        );
    }
```
By using the alternative constructor, we can avoid the error caused by the removed constructor.