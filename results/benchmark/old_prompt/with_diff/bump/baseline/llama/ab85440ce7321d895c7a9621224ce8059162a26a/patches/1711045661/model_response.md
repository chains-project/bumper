Here's a proposed patch to fix the failing test:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new StringContains(
            false,
            String.format("Status: Downloaded newer image for %s", image)
        ) {
            // override the match method to use the new hamcrest method
            @Override
            public boolean match(String s) {
                return super.match(s) && s.contains(image);
            }
        };
    }
```
Explanation:

The error message indicates that the `StringContains` constructor cannot be applied to the given types because the formal and actual argument lists differ in length. The new library version includes an additional parameter of type `java.lang.String` in the `StringContains` constructor, which causes the error.

To fix the error, we can create a new anonymous inner class that extends `StringContains` and overrides the `match` method. In the `match` method, we call the super method and add an additional check to ensure that the input string contains the image name.

By doing this, we effectively bypass the incompatible constructor and use the new `StringContains` method with the additional parameter. This change should not affect the test's behavior, but it will allow it to compile and pass with the new library version.