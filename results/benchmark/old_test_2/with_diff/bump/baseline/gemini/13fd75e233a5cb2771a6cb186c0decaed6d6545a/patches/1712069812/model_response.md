```java
  private static Matcher<String> imagePulled(final String image) {
        boolean negated = false;
        String message = String.format("Status: Downloaded newer image for %s", image);
        return new StringContains(negated, message);
    }
```