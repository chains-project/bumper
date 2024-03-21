Here's a proposed patch to fix the error:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        );
    }
```

The error is caused by the fact that the `StringContains` constructor takes two parameters of type `java.lang.String`, whereas in the old version of the library, it took a single `java.lang.String` parameter.


To fix this, we can modify the `imagePulled` method to use the `StringContains` constructor that takes a single `java.lang.String` parameter, like this:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        );
    }
```

Alternatively, we can modify the `imagePulled` method to use the `StringContains` constructor that takes two `java.lang.String` parameters, like this:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            "Status: Downloaded newer image for ",
            image
        );
    }
```
Either of these modifications should fix the error and allow the code to compile.