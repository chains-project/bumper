Here's a proposed patch to fix the error:
```java
  private static Matcher<String> imagePulled(final String image) {
        return new AllOf(
            new StringContains(
                false,
                String.format("Status: Downloaded newer image for %s", image)
            ),
            new StringContains(
                false,
                "pullImage"
            )
        );
    }
```
The `StringContains` constructor takes two parameters, a `boolean` and a `String`. The error message indicates that the second parameter cannot be applied to the given types.

The issue is that the second parameter is a `String.format()` call, which returns a `String`. However, the `StringContains` constructor expects a `String` literal.

To fix this, we can use the `AllOf` class from the Hamcrest library, which allows combining multiple matchers. We create two matchers, one that matches the desired string format and another that matches the string "pullImage". The `AllOf` matcher will only match if both of its components match.

By doing this, we avoid the issue of passing a non-literal `String` to the `StringContains` constructor.