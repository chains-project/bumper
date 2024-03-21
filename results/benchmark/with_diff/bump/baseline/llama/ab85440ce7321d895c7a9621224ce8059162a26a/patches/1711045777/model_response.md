Here's a proposed patch to fix the error:
```java
  private static Matcher<String> imagePulled(final String image) {
        String pulledImage = "Pulled image: " + image;
        return new StringContains(
            false,
            pulledImage
        );
    }
```
The patch creates a new variable `pulledImage` that concatenates the string "Pulled image: " with the input `image`. The `StringContains` constructor is then called with `false` and the newly created `pulledImage` string.

The error is caused by the fact that the `StringContains` constructor expects a single `String` argument, but the old library version passed a `boolean` and a `String` as separate arguments. The new library version expects the `String` argument to be passed as a single argument. The patch fixes this by creating a new `String` that contains the concatenation of "Pulled image: " and the input `image`, and passing that as a single argument to the `StringContains` constructor.