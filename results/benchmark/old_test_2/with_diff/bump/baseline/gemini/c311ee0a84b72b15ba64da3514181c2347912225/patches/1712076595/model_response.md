```java
  private static Matcher<String> imagePulled(final String image) {
        StringContains contains = new StringContains(false, String.format("Status: Downloaded newer image for %s", image));
        return contains;
    }
```